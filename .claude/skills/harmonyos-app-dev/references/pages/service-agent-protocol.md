# 鸿蒙Agent通信协议接入方案

_Source: https://developer.huawei.com/consumer/cn/doc/service/agent2agent-0000002498656261_

鸿蒙Agent通信协议基于JSON-RPC 2.0，用于Agent Client（小艺APP）和Agent Server（三方智能体后台）之间的通信。

## 消息结构

### 顶层data字段说明

| 字段名称 | 类型 | 是否必填 | 字段描述 |
|---|---|---|---|
| kind | string | 是 | 字段类型，此处固定为"data" |
| data | object | 是 | 数据类型为data类型的结构体定义 |
| data.commands | array[CommandObject] | 否 | 服务器侧响应客户端调用时，需要调用端侧工具时下发的调用指令 |
| data.cardsInfo | array[CardDataObject] | 否 | 服务器侧响应客户端调用时，返回的卡片模板填充数据 |
| data.chipsInfo | ChipDataObject | 否 | 服务器侧响应客户端调用时，返回的接续追问气泡数据 |
| data.reference | ReferenceDataObject | 否 | 服务器侧响应客户端调用时，返回的循证引用数据 |

### CommandObject参数说明

| 字段名称 | 类型 | 是否必填 | 字段描述 |
|---|---|---|---|
| header.namespace | String | 是 | 按具体业务场景填充 |
| header.name | String | 是 | 按具体业务场景填充 |
| payload | Object | - | 按具体业务场景填充 |

## 关键指令类型

### 1. Common-Action指令（调用三方APP意图框架）
Agent Server返回该指令时，必须先在小艺开放平台注册意图框架插件，且插件bundleName和intentName与返回指令中的值一致。

报文样例：
```json
{
    "payload":{
       "actionResponseConfig": {
           "type": "WHITE",
           "resultPath":["result.items.entityId"]
       },
      "response":[{
         "commandUserInteractionDisplayText":"找到{number}个备忘。",
         "code":"0",
         "commandUserInteractionSpeak":"找到{number}个备忘。"
      }],
        "executeParam":{
            "executeMode":"background",
            "intentName":"SearchNote",
            "intentParam":{
                "query":"昨天的"
            },
            "actionResponse": "true",
            "bundleName":"com.huawei.hmos.notepad"
        }
    },
    "header":{
        "namespace":"Common",
        "name":"Action"
    }
}
```

### 2. Command-DeepLink指令
小艺APP收到DeepLink指令，通过DeepLink方式打开应用的指定路径。

报文样例：
```json
{
  "header": {
      "namespace": "Command",
      "name": "Deeplink"
  },
  "payload": {
      "url": "{{STRING}}",
      "appName": "{{STRING}}",
      "packageName": "{{STRING}}",
      "appType": "{{STRING}}"
  }
}
```

| 字段名称 | 类型 | 是否必填 | 字段描述 |
|---|---|---|---|
| url | string | 是 | 要跳转到的应用页面url |
| appName | string | 是 | 要打开的应用名，当本地没有安装，会引导到应用市场安装 |
| packageName | string | 否 | 应用包名 |
| appType | string | 否 | DeepLink：访问的应用的类型；OpenHarmony：鸿蒙单框应用 |

### 3. 获取位置信息指令
AgentServer下行Command指令获取位置信息。需先在智能体中添加获取经纬度插件-定位服务。

下行Command报文（注意：下发定位服务指令时，响应报文中的final不要填true）：
```json
{
    "header": {
        "namespace": "Common",
        "name": "Action"
    },
    "payload": {
        "cardParam": {},
        "executeParam": {
            "achieveType": "INTENT",
            "actionResponse": true,
            "bundleName": "com.huawei.hmos.aidispatchservice",
            "executeMode": "background",
            "intentName": "GetCurrentLocation",
            "intentParam": {},
            "needUnlock": true,
            "permissionId": [],
            "timeOut": 5
        },
        "needUploadResult": true,
        "pageControlRelated": false,
        "responses": [{
            "displayText": "",
            "resultCode": "",
            "ttsText": ""
        }]
    }
}
```

上报位置信息指令（使用WGS84坐标系）：
```json
{
    "header": {
        "name": "UploadExeResult",
        "namespace": "Common"
    },
    "payload": {
        "intentName": "GetCurrentLocation",
        "outputs": {
            "latitude": 31.980,
            "longitude": 118.762
        }
    }
}
```

## 设备上下文参数

Agent Server端可获取的受控系统上下文信息，需先在小艺开放平台变量配置项中打开对应配置项。

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

## 授权登录/解授权

### 发送授权码
```bash
curl 'https://xxx/agent/message' \
-H 'Content-Type: application/json' \
-H 'agent-session-id:8f01f3d172cd4396a0e535ae8aec6687' \
-d '{
    "jsonrpc": "2.0",
    "id": "消息序列号",
    "method": "authorize",
    "params": {
        "message": {
            "role": "user",
            "parts": [{
                "kind": "data",
                "data": {
                    "authCode": "从华为账号获取用户授权后的授权码"
                }
            }]
        }
    }
}'
```

### 授权响应
```json
{
    "jsonrpc": "2.0",
    "id": "消息序列号",
    "result": {
        "version": "1.0",
        "agentLoginSessionId": "用户登录凭证唯一ID"
    },
    "error": {
        "code": "0表示成功",
        "message": "错误描述"
    }
}
```

### 解除授权
使用JSON-RPC方法`deauthorize`，携带`agentLoginSessionId`和`cpUserId`。

## 快捷指令上报

Agent Client请求Agent Server侧的data数据结构：
```json
"userInputInfo": {
    "statusInfo": [{
        "isSelected": true,
        "statusKey": "Agent开发平台定义的快捷指令的Key",
        "statusValue": "Agent开发平台定义的快捷指令的Value"
    }]
}
```

## CardDataObject卡片数据

| 字段名称 | 类型 | 是否必填 | 字段描述 |
|---|---|---|---|
| cardsInfo | Object | 是 | 业务卡片结构化数据 |
| cardName | String | 是 | 业务卡片名称，与A2A输出配置中的卡片名称一致 |
| cardData | Object | 是 | 多条记录建议放在items[*].[JSONObject]里面 |
| displayType | String | 否 | EmbedMarkdown（嵌入MD显示）/ DisplayFaCard（独立出卡），默认独立显示 |

## ChipDataObject追问气泡

| 字段名称 | 类型 | 是否必填 | 字段描述 |
|---|---|---|---|
| content | String | 是 | superlink格式，长度不超过64字符 |
| domain | String | 是 | documentSummary文档摘要 / AIGC LLM生成 |
| icon | String | 否 | 气泡图标URL |
