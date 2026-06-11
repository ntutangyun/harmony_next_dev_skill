# 鸿蒙Agent通信协议（A2A）

_Source: https://developer.huawei.com/consumer/cn/doc/service/agent2agent-0000002498656261_

接入方案文档现为两部分：技术规范总览（`agent2agent-comments-0000002500412353`）与消息指令定义（`agent2agent-define-0000002467293060`，含消息指令定义、消息参数说明、端侧插件工具指令、底部快捷指令、设备上下文参数等子页）。

## 技术规范总览

鸿蒙Agent通信协议用于Agent Client（小艺APP/小艺云侧）和Agent Server（三方智能体后台）之间的通信：

- 统一一个Endpoint，仅POST方法，采用 **StreamableHTTP + JSON-RPC 2.0** 协议；服务器侧不用维护长链接，支持断线重连。
- 兼容谷歌A2A协议的 `message/stream`、`tasks/cancel` 等RPC方法。
- 小艺Client Agent使用 `message/stream` 请求三方Remote Agent；Remote Agent异步处理任务，通过 **SSE** 返回：任务处理进展状态、（可选）向用户追问澄清、首Token后流式输出响应内容、任务完成后返回完整响应报文。要求三方Remote Agent基于用户sessionId缓存对话上下文。

### 两种会话模式

| 模式 | 说明 |
|---|---|
| 模式1（推荐）：基于session维护状态 | 服务器侧分配`agent-session-id`（类似MCP的mcp-session-id），客户端每次请求时放在header中。服务器需实现`initialize`、`notifications/initialized`方法，且需保证对同一AK/SK、APIKey、OAuth客户端可同时分配多个agent-session-id（建议不低于5个同时有效），防止凭证吊销间隙问题 |
| 模式2（简化）：无状态 | 客户端每次请求都在header中携带认证凭据（AK/SK、APIKey等），服务器不需要实现`initialize`/`notifications/initialized` |

### RPC方法一览

| RPC方法 | 调用方式 | 功能定义 |
|---|---|---|
| `initialize` | Request/Response阻塞式 | Client发起Server初始化，获取sessionId（服务器-服务器接口初始化） |
| `notifications/initialized` | Request/Response阻塞式 | Client通知Server初始化完成 |
| `message/stream` | 非阻塞式，Server可用`Content-Type: text/event-stream`升级为SSE流式响应 | 用户发起对话时请求Server处理，接收流式输出（markdown文本、图片、数据、任务进展状态、追问报文等） |
| `tasks/cancel` | Request/Response阻塞式 | Client请求终止Server当前任务输出 |
| `clearContext` | Request/Response阻塞式 | Client请求清理Server本次多轮对话上下文 |
| `authorize` | Request/Response阻塞式 | Client向Server发送宿主APP代智能体获取的用户授权信息 |
| `deauthorize` | Request/Response阻塞式 | Client向Server发送用户取消当前授权登录消息 |
| `push` | Request/Response阻塞式 | **Server向Client**推送PUSH通知（适用于异步长耗时任务，如音、视频、文件生成） |

## 初始化/初始化完成（initialize / notifications/initialized）

请求（header携带`Authorization: Bearer <your-api-key>`）：

```json
{
    "jsonrpc": "2.0",
    "id": "全局唯一消息序列号（字符串）",
    "method": "initialize"
}
```

响应：

```json
{
    "jsonrpc": "2.0",
    "id": "从请求中取出该字段返回",
    "result": {
        "version": "1.0",
        "agentSessionId": "认证通过后返回的唯一会话标识符，后续请求放在header的agent-session-id字段",
        "agentSessionTtl": "有效期，单位秒，一般建议7天"
    },
    "error": { "code": "0表示成功（字符串或整形）", "message": "错误描述" }
}
```

`notifications/initialized`：Client携带`agent-session-id` header发送`method: "notifications/initialized"`，Server返回HTTP 200即可，无响应体。

## 发起会话（message/stream）

请求（header携带`agent-session-id`）：

```json
{
    "jsonrpc": "2.0",
    "id": "全局唯一消息序列号",
    "method": "message/stream",
    "params": {
        "id": "请求任务唯一ID，一次流式交互中保持不变",
        "sessionId": "Agent Client侧分配的会话唯一标识符，用于存储上下文；用户清理上下文后会更新该值",
        "agentLoginSessionId": "账号绑定后每次请求可携带的用户登录凭证（可选）",
        "message": {
            "role": "user",
            "parts": [
                { "kind": "text", "text": "用户输入Query或子任务Query" },
                { "kind": "file", "file": { "name": "文件名", "mimeType": "MIME类型", "bytes": "字节码（与uri互斥）", "uri": "URI地址（与bytes互斥）" } },
                { "kind": "data", "data": "结构化数据JSONObject，如用户参数、端插件执行结果等" }
            ]
        }
    }
}
```

响应为SSE流，`result`为`TaskStatusUpdateEvent`（中间状态）或`TaskArtifactUpdateEvent`（中间/最终输出）二者之一。

**TaskStatusUpdateEvent（状态推送）**：

```json
{
    "jsonrpc": "2.0",
    "id": "从请求中取出返回",
    "result": {
        "taskId": "使用请求中的任务ID返回",
        "kind": "status-update",
        "final": false,
        "status": {
            "message": {
                "role": "agent",
                "parts": [{ "kind": "text", "text": "简短的任务过程状态描述（状态栏展示），如思考中、分析中" }]
            },
            "state": "submitted|working|input-required|completed|canceled|failed|unknown"
        }
    },
    "error": { "code": "0成功；99911114内容不合规；99911113流控", "message": "错误描述" }
}
```

注意：若有Artifact输出，则不用`completed`状态消息收尾。

**TaskArtifactUpdateEvent（结果推送）**：

```json
{
    "jsonrpc": "2.0",
    "id": "从请求中取出返回",
    "result": {
        "taskId": "使用请求中的任务ID返回",
        "kind": "artifact-update",
        "append": false,
        "lastChunk": true,
        "final": false,
        "artifact": {
            "artifactId": "本条Artifact的唯一ID",
            "parts": [
                { "kind": "reasoningText", "reasoningText": "深度思考的流式输出内容，支持markdown" },
                { "kind": "text", "text": "正文流式输出内容，支持markdown" },
                { "kind": "data", "data": "结构化数据：卡片数据、端指令、推荐问题、循证引用等" }
            ]
        }
    }
}
```

关键字段语义：

| 字段 | 说明 |
|---|---|
| `append` | 输出内容是否追加到前序片段，布尔，默认false；增量输出时为true |
| `lastChunk` | 是否流式输出的最后一个片段，默认true。一次会话请求（以final=true结束）允许若干次流式输出，每次流式输出以lastChunk=true结束 |
| `final` | 标识本任务SSE流是否结束，默认false。**设置为true后会断开端云任务通道，云侧不能再往端侧推送消息**；任务结束必须设置为true |

## 终止会话（tasks/cancel）

请求：`method: "tasks/cancel"`，携带`sessionId`。响应：

```json
{
    "jsonrpc": "2.0",
    "id": "从请求中取出返回",
    "result": {
        "id": "使用请求中的该字段返回",
        "status": { "state": "canceled|failed|unknown" }
    },
    "error": { "code": "0表示成功", "message": "错误描述" }
}
```

## 清理上下文（clearContext）

请求：`method: "clearContext"`，携带`sessionId`。响应`result.status.state`取值为`cleared|failed|unknown`。

## 授权登录/解授权（authorize / deauthorize）

账号一键授权登录方案要点：

1. 开发者在华为开发者联盟账号服务获取appId，并在小艺开放平台智能体开发页面注册保存。
2. 小艺APP加载三方智能体页面时从平台获取智能体的appId。
3. 用户在智能体内点击账号授权：已授权过则静默发起授权到三方服务器返回新的`agentLoginSessionId`；未授权则弹框获取用户授权，三方服务器基于华为账号授权码获取用户手机号后返回`agentLoginSessionId`。
4. 小艺APP保存该`agentLoginSessionId`，后续给该智能体发消息时携带。APP客户端侧需持久化到本地。
5. `agentLoginSessionId`超期失效或不存在时，小艺APP重新发起授权流程。

**authorize请求**：

```json
{
    "jsonrpc": "2.0",
    "id": "全局唯一消息序列号",
    "method": "authorize",
    "params": {
        "message": {
            "role": "user",
            "parts": [{ "kind": "data", "data": { "authCode": "宿主APP代智能体从华为账号获取的授权码" } }]
        }
    }
}
```

响应：`result: { "version": "1.0", "agentLoginSessionId": "用户登录凭证唯一ID" }`。

**deauthorize请求**：`method: "deauthorize"`，data中携带`agentLoginSessionId`和`cpUserId`（支付场景下标识CP侧用户的唯一ID）。响应仅返回`result.version`。

正文中需要提示账号登录时，可在markdown中使用超链接：
`superlink://vassistant?hwIdAuth=phone&appId={{账号绑定中配置的APP ID}}&agentId={{智能体的agentId}}`

## PUSH通知（push）

Agent Server → Agent Client，POST到 `https://hag.cloud.huawei.com/open-ability-agent/v1/agent-webhook`，请求头：

| Header | 说明 |
|---|---|
| `x-hag-trace-id` | 客户端使用随机数生成 |
| `X-Access-Key` | 小艺开放平台触发器Webhook事件分配的appKey |
| `X-Sign` | `Base64(HMAC-SHA256(secretKey, ts))`，secretKey为平台配置的接入密钥 |
| `X-Ts` | 毫秒时间戳；服务端应校验与当前时间差值（如绝对值小于15分钟）以防重放 |

请求体关键字段：`result.apiId`（创建API时生成的API ID）、`result.pushId`（平台系统变量push_id）、`result.agentLoginSessionId`、`result.pushText`（Push通知展示内容）、`result.kind`（固定`task`）、`result.artifacts[]`（artifactId用于去重；parts含text/data）、`result.status.state`（`completed|canceled|failed`）。

响应：`{ "id": "对应请求体id", "resultId": "对应请求体result.id", "result": { "code", "message" } }`。

## 请求data数据结构（Client → Server）

文本query放在`text`，文件/图片放在`file`，端侧事件放在`data.events`。

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `kind` | string | 是 | 固定为`"data"` |
| `data` | object | 是 | data类型结构体 |
| `data.authCode` | string | 否 | 仅authorize方法时必选 |
| `data.agentLoginSessionId` | string | 否 | 仅deauthorize方法时必选 |
| `data.events` | array[EventObject] | 否 | 客户端上报事件时必选；EventObject含`header.namespace`、`header.name`、`payload` |
| `data.userInputInfo` | JSONObject | 否 | 底部快捷指令点击产生的用户输入信息 |
| `data.variables` | JSONObject | 否 | 平台开放的用户变量、系统变量和客户端变量，开关打开后才传递给CP Server |

## 响应data数据结构（Server → Client）

文本放在`text`（纯文本或markdown），其它结构化数据放在`data`。

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `kind` | string | 是 | 固定为`"data"` |
| `data.commands` | array[CommandObject] | 否 | 需要调用端侧工具时下发的调用指令（header.namespace + header.name + payload） |
| `data.cardsInfo` | array[CardDataObject] | 否 | 卡片模板填充数据 |
| `data.chipsInfo` | ChipDataObject | 否 | 接续追问气泡数据 |
| `data.reference` | ReferenceDataObject | 否 | 循证引用数据 |

端侧调用指令（Deeplink跳转指令除外）需在小艺开放平台注册端调用插件并加白名单后才能生效。APP上报数据给Agent Server：在Server下发意图框架调用指令后，APP按意图输出参数放在EventObject带回。

**CardDataObject**：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `cardName` | String | 是 | 业务卡片名称，与平台A2A输出配置中的卡片名称一致 |
| `cardData` | Object | 是 | 多条记录建议放在`items.[*].[JSONObject]`；非数组用JSONObject |
| `displayType` | String | 否 | `EmbedMarkdown`（嵌入MD显示）/ `DisplayFaCard`（独立出卡）；默认独立显示（卡片展示在文字下方） |

**ChipDataObject**（`chipsInfo.displayChips.chipsList[]`）：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `content` | String | 是 | superlink格式：`superlink://vassistant?text={{推荐问题内容}}&startmode=recognize`，长度不超过64字符 |
| `domain` | String | 是 | 问题所属垂域：`documentSummary`文档摘要 / `AIGC` LLM生成 |
| `icon` | String | 否 | 气泡图标URL |

**ReferenceDataObject**（`reference.items[]`）：每项含`params`（打点参数：`name`站点名称、`source`站点来源类型）和`card`（参考来源卡片：`type`固定`leftPictureRightText`；`params`含`title`网页标题、`subTitle`站点名称、`link.webLink`（`startMode` 0=小艺内部拉起/1=浏览器，默认0；`url`网页链接）、`imageInfo.small.url`标题logo）。

## 端侧插件工具指令

### Common-Action指令（调用三方APP意图框架）

约束：Agent Server返回该指令时，必须先在小艺开放平台注册意图框架插件，且插件的bundleName和intentName与指令中的值一致，否则云侧会拦截。

```json
{
    "header": { "namespace": "Common", "name": "Action" },
    "payload": {
        "actionResponseConfig": { "type": "WHITE", "resultPath": ["result.items.entityId"] },
        "response": [
            { "code": "0", "commandUserInteractionDisplayText": "找到{number}个备忘。", "commandUserInteractionSpeak": "找到{number}个备忘。" },
            { "code": "1", "commandUserInteractionDisplayText": "没有找到相关的备忘录…", "commandUserInteractionSpeak": "没有找到相关的备忘录…" }
        ],
        "executeParam": {
            "executeMode": "background",
            "intentName": "SearchNote",
            "intentParam": { "query": "昨天的" },
            "actionResponse": "true",
            "bundleName": "com.huawei.hmos.notepad"
        }
    }
}
```

ExecuteParam参数：

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `actionResponse` | boolean | 是 | 意图框架执行结果是否需要上报云侧 |
| `actionResponseConfig` | object | 否 | 上报参数配置；为空表示全部上报。`type`：`BLACK`黑名单/`WHITE`白名单；`resultPath`为意图框架返回结果里的参数路径 |
| `executeMode` | string | 是 | `background` / `foreground` |
| `intentName` | string | 是 | 意图名称，由意图框架定义 |
| `intentParam` | object | 是 | 意图执行参数 |
| `bundleName` | string | 是 | 被调用方包名 |

执行结果通过上行Event指令（`Common / UploadExeResult`）带回：payload含`toolName`（意图名）、`resultCode`、`responseText`、`responseDataList`（工具调用结果）。

### Command-Deeplink指令

```json
{
    "header": { "namespace": "Command", "name": "Deeplink" },
    "payload": { "url": "...", "appName": "...", "packageName": "...", "appType": "..." }
}
```

| 字段 | 必填 | 说明 |
|---|---|---|
| `url` | 是 | 要跳转到的应用页面url |
| `appName` | 是 | 应用名；本地未安装时引导到应用市场安装 |
| `packageName` | 否 | 应用包名，不为空则指定包名调用 |
| `appType` | 否 | `DeepLink`：访问的应用类型；`OpenHarmony`：鸿蒙单框应用 |

### 获取经纬度指令（定位服务）

需先在智能体中添加获取经纬度插件-定位服务。下发`Common/Action`，`executeParam`含`achieveType: "INTENT"`、`bundleName: "com.huawei.hmos.aidispatchservice"`、`intentName: "GetCurrentLocation"`、`executeMode: "background"`、`needUnlock: true`、`timeOut: 5`，外层`needUploadResult: true`。**注意：下发定位服务指令时，响应报文中的final不要填true。**

小艺APP上报位置信息（放在请求`data.events`中）：

```json
{
    "header": { "namespace": "Common", "name": "UploadExeResult" },
    "payload": {
        "intentName": "GetCurrentLocation",
        "outputs": { "latitude": 31.980, "longitude": 118.762 }
    }
}
```

经纬度使用WGS84坐标系。

## 底部快捷指令上报

需先在平台智能体内配置对应快捷指令。用户点击时，Client在请求data中携带：

```json
"userInputInfo": {
    "statusInfo": [{
        "isSelected": true,
        "statusKey": "Agent开发平台定义的快捷指令的Key",
        "statusValue": "Agent开发平台定义的快捷指令的Value，如联网搜索"
    }]
}
```

## 设备上下文参数

Agent Server可获取的受控系统上下文信息，需先在小艺开放平台变量配置项中打开对应开关：

```json
{
    "variables": {
        "clientVariables": [{}],
        "systemVariables": [{
            "app_ver": "小艺APP的版本号",
            "foreground_apps": "智能体运行的前台应用列表"
        }],
        "memoryVariables": [{}]
    }
}
```

| 字段 | 说明 |
|---|---|
| `clientVariables` | 应用变量 |
| `systemVariables` | 系统变量（如`app_ver`、`foreground_apps`） |
| `memoryVariables` | 用户变量 |

## 子页面URL索引

- 技术规范总览：`https://developer.huawei.com/consumer/cn/doc/service/agent2agent-comments-0000002500412353`
- 消息指令定义（目录）：`https://developer.huawei.com/consumer/cn/doc/service/agent2agent-definition-0000002500439093`
- 初始化/初始化完成：`.../initialize-initialized-0000002537681161`
- 发起会话：`.../message-stream-0000002505761434`
- 终止会话：`.../tasks-cancel-0000002537561193`
- 清理上下文：`.../clear-context-0000002537681163`
- 授权登录/解授权：`.../authorize-deauthorize-0000002505921274`
- PUSH通知：`.../pushmessage-0000002505761436`
- 请求data数据结构：`.../query-data-0000002537691281`
- 响应data数据结构：`.../response-data-0000002505931382`
- 端侧插件工具指令：`.../agent2agent-action-0000002467539682`
- 底部快捷指令：`.../agent2agent-command-0000002467900460`
- 设备上下文参数：`.../agent2agent-context-0000002501019701`
