# Xiaoyi (小艺) Agent Development — HarmonyOS NEXT

_Source authority: `https://developer.huawei.com/consumer/cn/doc/service/*` (小艺开放平台 / Xiaoyi Open Platform)_

## What the Xiaoyi Open Platform is

Xiaoyi Open Platform is Huawei's **unified Agent + Skill development and distribution platform** for HarmonyOS NEXT. It provides end-to-end tooling to build, debug, evaluate, publish, and operate AI agents that users access through Xiaoyi (the system-level AI assistant) and in-app entry points. The platform's core ecosystem is a 2×2 matrix — **Agent vs Skill × cloud-side vs device-side** — compatible with device, cloud, MCP, and intent-framework tools ("Skill化" of all of them). Skills are executed by **小艺Claw**, the Xiaoyi agent runtime.

Agents are published to the **Agent Market (智能体市场)** and distributed across devices (phone, tablet, PC, watch, car). The platform also runs a **Plugin Marketplace** (system plugins, system-app plugins, third-party app plugins, MCP tools) plus private custom cloud/device plugins.

Doc tree top levels: 小艺开放平台 (平台概览与核心概念 / 平台特性与能力体系 / 动态与公告), Agent (Agent编排模式 / 开发Agent / A2A协议接入方案 / Agent上架审核规范 …), Skill, 资源库 (工作流 / 插件 / 知识库 / 卡片 / 界面 / 音色 / 意图框架), 小艺罗盘 (now top-level), 最佳实践, 合作协议与补充接口文档.

## Six development modes

| Mode | Description | Best for |
|---|---|---|
| **Device A2A mode (端A2A模式)** | In-app agent on the device talks to the on-device Xiaoyi client agent over the device A2A protocol — lightweight end-to-end integration using on-device compute and system APIs; low latency, high privacy. | Developers who already ship a HarmonyOS app and want an on-device agent |
| **Cloud A2A mode (云A2A模式)** | Bring your own agent: connect an existing third-party cloud agent via the cloud A2A protocol (StreamableHTTP + JSON-RPC 2.0). | Enterprise developers with existing cloud agents + HarmonyOS apps |
| **Cloud workflow mode (云工作流模式)** | Rule-based: compose ordered steps (data fetch → process → act) by connecting plugins, LLM nodes, branches, code blocks on a canvas. | Complex multi-step business logic with deterministic flows |
| **OpenClaw mode** | Connect an OpenClaw server via the `@ynhcj/xiaoyi` plugin for rapid personal agent creation. One per account, device-test publishing only. | Personal assistants, automation, quick prototypes |
| **LLM mode (单Agent)** | LLM-driven: pick a model, write prompts, add plugins/workflows. Model handles intent routing dynamically. | Simple Q&A, knowledge retrieval, content generation |
| **Multi-agent mode (多Agents模式)** | Split a complex task into sub-tasks, each handled by a sub-agent with its own role prompt, plugins, and workflows; the LLM acts as the task planner that routes to sub-agents based on user need + role prompts + sub-agent descriptions. | Complex, business-diverse scenarios needing multiple specialists |

### Mode capability matrix (key differences)

Columns: 端A2A / 云A2A / 云工作流 / OpenClaw / LLM / 多Agents.

| Capability | 端A2A | 云A2A | 云工作流 | OpenClaw | LLM | 多Agents |
|---|---|---|---|---|---|---|
| Model selection & settings | — | — | — | — | ✓ | ✓ |
| Dialog settings (对话设置) | — | — | ✓ | — | — | — |
| Opening dialog (开场对话) | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Input file settings | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| User question suggestions | — | — | ✓ | — | ✓ | ✓ |
| Quick commands | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| Background image, character voice | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Plugins | — | ✓ | — | — | ✓ | ✓ |
| Workflows | ✓ | — | ✓ | — | ✓ | ✓ |
| Trigger | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Associated app (AgentKit) | — | ✓ | ✓ | — | ✓ | ✓ |
| Sub-agents (智能体) | — | — | — | — | — | ✓ |
| Knowledge base | — | — | — | — | ✓ | ✓ |
| Variables | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Long-term memory | — | — | ✓ | — | ✓ | ✓ |
| A2A basic config / output settings | — | ✓ | — | — | — | — |
| Account binding | — | ✓ | ✓ | — | — | — |
| OpenClaw basic config | — | — | — | ✓ | — | — |

## Agent lifecycle

```
Create → Configure → Debug & Preview → Publish (review 1-3 business days) → Live in Agent Market
```

- **Create**: Workspace → 智能体 → + Create, pick a mode; fill name/avatar/description/category/devices.
- **Configure**: Basic info, privacy, compliance, orchestration (编排).
- **Debug**: Web debug panel + device test (真机测试) for white-listed testers.
- **Publish** (上架): Submit for review; pre-publish checklist must pass platform validation. Team accounts: admin only.
- **Upgrade**: If a new version fails review, the previous approved version stays live.
- **Take-down** (下架): Removes agent from market; can re-edit and re-submit.
- **Version management**: View version records (incl. publish/take-down/withdraw versions); roll back overwrites the draft. Rollback rules: linked resources (plugin/workflow/card/knowledge base) auto-relink to latest version, or the link is dropped if the resource was removed; everything else restores fully.

## Configuration areas

### 1. Basic info (基础信息)
- **Icon**: 1:1, <5 MB, png/jpeg/jpg, opaque background
- **Name**: Required
- **One-line description**: Shown on agent detail page
- **Category**, **Aliases** (multiple, improve distribution accuracy)
- **File storage type (文件存储类型)**
- **Creator nickname (创建者昵称)**: defaults to account nickname; enterprise devs can pick an approved one
- **Supported devices**: Phone/Tablet/PC/Watch — HarmonyOS NEXT (ROM 5.x+); Phone/Tablet — HarmonyOS (ROM 4.x); Car — HarmonyOS
- **AgentCard**: auto-generated capability "business card" used for Xiaoyi main-dialog distribution. Syncs from basic info + plugins/workflows. Editable: function name, description, dependencies (device-plugin deps). Read-only: name, ID, version, description, input types (from input-file settings), output type (string, reserved).

### 2. Privacy policy (隐私协议服务)
- **Custom privacy URL** or **platform-hosted builder** with template sections: intro & version changes; how personal info is collected/used (conversation data by default + custom data items); personalized recommendation (optional); minor protection (optional); third-party sharing and third-party MCP Server declarations (optional, per company/server); personal info management (fixed); storage location (China servers only) & duration (fixed or "minimum necessary"); developer custom section; contact methods (phone/email/address); effective date.
- Multiple policies per agent, but only ONE linked at publish. Must click 【生成协议】 ("completed" state) before linking; re-generate after edits.
- The platform auto-detects mismatches between agent capabilities and the linked policy and flags them.

### 3. Content compliance (内容合规)
Mandatory per Chinese AI regulations (生成式AI管理暂行办法, 深度合成规定, AI生成合成内容标识办法):
- **AI-generated content labeling**: declare whether outputs contain AI-generated text/images/audio/video/virtual scenes. If yes: Label (1=is, 2=may be, 3=suspected AI-generated), ContentProducer, ProducerID, ReservedCode1, ContentPropagator, PropagatorID, ReservedCode2. Self-verify implicit labels via the AI标识服务检测平台.
- **LLM filing numbers**: required when using third-party (non-platform) LLMs — CAC generative-AI service filing number + algorithm filing number (comma-separated if multiple).

## Orchestration (编排)

### Model selection & prompt (LLM mode)
- Model picker with **multi-model comparison debugging**
- **Hyperparameters**: context rounds 0-20; some models also Top-K 1-256 (step 1), Top-P 0-1 (step 0.01), Temperature 0-1 (step 0.01)
- **Prompt comparison** debugging
- **Prompt optimization**: (1) dataset-based multi-round optimization — optimizer model + evaluation model, evaluation via model self-evaluation (creative tasks) or exact text matching (classification/precise output), max 10 examples, max 20 rounds; (2) full-text auto-optimize / optimize from debug results
- Heads-up: the platform retires models — e.g. DeepSeek-V3 / DeepSeek-R1 go offline 2026-05-30 (migrate to DeepSeek-V3.2). Configure a developer contact email (通用设置 → 开发者信息) for retirement reminders.

### Dialog settings (Workflow mode)
- Context window: 0-20 rounds

### Capability extensions (能力拓展)

**A2A basic config** (A2A mode, mandatory before publish): API URL (speaks the HarmonyOS Agent protocol); session mode (server-assigned session, or stateless with credentials per request); auth: AK/SK, OAuth 2.0 (Client mode only), Header, or Query (discouraged).

**A2A output settings**: bind cards to outputs; max 20 entries; each has cardName, cardDescription, and an output parameter that must be named `cardData` (Object, with sub-items).

**OpenClaw basic config**: one OpenClaw agent per account; devices default to Phone NEXT + Phone HarmonyOS. (1) Create credentials in Workspace → 凭证 (secret key visible only at creation). (2) Configure the xiaoyi channel on the OpenClaw server with ak/sk (other channel fields must not be changed). Publishing = device test only, for white-listed users; dev-test state is long-lived.

**Opening dialog & preset questions**: two variants.
- *Preset (static)*: Markdown welcome message + up to 3 one-tap preset questions, same on every launch.
- *Dynamic (动态开场对话)*: opening line + preset questions refreshed on each launch via a bound workflow or the A2A service. Workflow mode: bind two end-node variables — opening line must be String, preset guides must be Array\<Object\> whose items have a String `content` field. A2A mode: clicking 动态开场对话 saves the config and fires an init event to the A2A URL — `events[]` with `header` namespace `Common` / name `Trigger` and `payload.eventName: "AgentInit"`; the server replies with an artifact-update whose data part carries `openingText: { openingText, openingQuestions: [{content}] }`.

**Input file settings**: photo upload (JPEG/JPG/PNG/BMP/WEBP) + camera capture (device-only, no web preview); file upload (pdf/doc/docx/txt/ppt/pptx/xlsx/xls). Send modes: direct, or "pending area" (text+attachments together, max 6 photos/files per message). Optional photo/file quick-command presets.

**User question suggestions** (LLM/Workflow): off by default; after each reply suggests follow-up questions via system prompt or custom prompt.

**Quick commands** (快捷指令): up to 30 static + 1 dynamic; the dynamic one is pinned first (position not adjustable); static order is drag-adjustable. Commands can be restricted to specific Xiaoyi app versions or device types.
- **Static types**:
  - Jump-type: DeepLink to app (app name, package, DeepLink, min app version, optional Action name). No web preview.
  - Send-type: Document / Image / Text / Camera (front/rear lens, optional crop) / Choice panel (components: 1 upload object, 1 image template, up to 2 tiled selectors, up to 2 dropdown selectors; query auto-assembled from text + component values)
  - State-type: toggleable feature bound to exactly one variable (variable must have a non-empty default; state value must differ from the default); when selected, the state value rides along with user queries
- **Dynamic**: workflow-driven. `HalfScreen`/`FullScreen` events pass `EVENT_INPUT` (with `header.name` = event) to the workflow; the workflow outputs `dynamicDirective[]` (`content` + `query`) and `eventInfo` (`directiveName: "QuickChips"`, `eventName`). Workflow mode must bind the agent's main workflow (use a selector node to share it with dialog logic).

**Background image**: chat background in the Xiaoyi app.

**Character voice**: pick a default timbre; "user can switch voice" toggle on by default. Custom (cloned) timbres are usable **only when the user-switch toggle is off**.

**Plugins** (in-agent config): parameter settings (async-task Push notification toggle for cloud/MCP plugins; foreground/background execution + immediate-execution/interrupt-broadcast for device plugins; input defaults + LLM-visibility toggle; output 融合生成 toggle for LLM fusion), card binding (multiple cards, text/card ordering, batch vs stream first/last-frame rules, conditional card output via String/Array[String] flag match), debugging (cloud plugins show name/tool/params/result in web debug; device plugins need a real device), upgrade (cloud auto-updates draft agents, device plugins re-add manually), mock sets (web debug only; real devices always call the real API).

**Workflow config**: bind workflows; execution settings (async-task Push notification when app is backgrounded); card binding on output/end nodes (stream nodes can mix card+text; non-stream output nodes are card-only; thinking-mode output nodes can't bind cards); **text-card mixed output (文卡混排)** — requires a stream cloud plugin emitting `items.displayType: "EmbedMarkdown"`, bind variable must be named `items`, stream toggle on, plugin directly wired to the answering output/end node; **UI jump config (界面跳转)** — bind a published Interface, map interface input params to node outputs (no web debug, device test only).

**Trigger**: auto-execute on events.
- *Generic events* (通用事件): fire on half-screen/full-screen entry; LLM and A2A modes only; one trigger per event. Task types (LLM): agent prompt / plugin / workflow (each with "save to conversation context" toggle). A2A mode: no task config — the event + params are forwarded to the A2A API URL. Triggered workflows get no `USER_INPUT`; define custom start-node params. Re-bind manually after plugin/workflow upgrades.
- *Webhook events*: async long tasks. Developer POSTs to `https://hag.cloud.huawei.com/open-ability-agent/v1/agent-webhook` with headers `x-hag-trace-id`, `X-Access-Key`, `X-Sign` = Base64(HMAC-SHA256(secretKey, ts)), `X-Ts`; JSON-RPC body with `apiId`, `pushId` (system var push_id), optional `agentLoginSessionId`, `pushText` (≤84 EN chars / 57 CN chars, 3 lines), `kind: "task"`, `artifacts[].parts` with `text` (shown directly) **or** `data` (runs the configured plugin/workflow, or is forwarded via A2A); text wins if both sent. User gets a push notification; tapping it opens the agent with the result.

**Associated app** (关联应用): link agent to HarmonyOS apps (AGC-published, same account). The app integrates **AgentKit** (Function component) to launch the agent half-screen. Requires **manual signing** (auto-sign randomizes appid → auth failure), ROM 6.0.0+ / API SDK 20+, Xiaoyi app 11.3.8.300+. White-listed devices keep launching the "开发中" dev agent after public release — remove the whitelist or cancel dev publish.

**Account binding** (A2A/Workflow only): Huawei account one-tap auth.
- A2A mode: toggle + APP ID (Client ID of an AGC web app), then internal review with Huawei support. Auth requests go to the A2A API URL.
- Workflow mode: APP ID + auth service API URL + auth method (AK/SK, Header, Query). Auto-creates system variable `agent_login_session_id` (the `agentLoginSessionId` from the authorize response) for downstream nodes.
- Binding UX: superlink in replies — `superlink://vassistant?hwIdAuth=phone&appId={{APP_ID}}&agentId={{agentId}}` — or the bind-phone row on the agent detail page.
- Phone-number permission: **enterprise developers only**; apply in Developer Alliance 管理中心 → 授权管理 → 华为帐号服务 with use-case materials. APP ID's product name/icon must match the agent's.

**Paid agent** (付费智能体): for paid digital goods/services; **beta, enterprise developers only** — request enablement from the Xiaoyi commercialization team via business contact or Developer Alliance ticket. Requires account binding first. See payment service section below.

**Knowledge base** (LLM mode): relevance threshold 0-1, max recall segments 0-20, max recall tokens 0-999999, query rewriting (on by default), no-hit reply (default "抱歉，这个问题不在知识范围内" or custom).

**Variables**: user variables (per-user persistent; usable in prompt and workflows; context-based auto-extraction in LLM mode only — and disabled when an executed workflow contains a variable component) + system variables (read-only, off by default: device identifier, device language, etc.) + **counter variables (计数变量)** — atomic counters for throttling/metering agent-feature usage, counted per user (uid) or per device (odid). Max 10 per agent; name, dimension, and reset period (fixed: natural month/week/day/hour) are immutable after save; initial value must be an integer; **not supported in 云A2A mode**; usable only in the query-counter-variable and quota-management workflow nodes; not viewable/resettable in the memory viewer. Inspect/reset other variables via 【记忆】→【变量】.

**Long-term memory** (LLM/Workflow): extracts key info after the context window is exhausted (e.g. 20-round window → extraction from round 21). Auto-appended to prompt by default ("支持在Prompt中调用"); uncheck to restrict to workflow use. Viewable/resettable via 【记忆】→【长期记忆】.

## Debugging & preview

| Feature | LLM | Workflow | A2A | OpenClaw |
|---|---|---|---|---|
| Device test (真机测试) | ✓ | ✓ | ✓ | ✓ |
| Trigger debug | ✓ | — | ✓ | — |
| Memory viewer | ✓ | ✓ | — | — |
| TTS playback (朗读) | ✓ | ✓ | ✓ | ✓ |
| Web debug | ✓ | ✓ | ✓ | ✓ |

- **Device test**: configure white-list user groups (max 100 groups/team, 100 users/group, by phone number or email/UID; batch import supported), then 【发布真机测试】. The agent appears in Xiaoyi with a "开发中" badge. **Dev state is valid for 15 days per publish**; cancel via 【取消发布】.
- **Debug console (调试台)**: full-link tracing per request — session overview (latency, token usage, status, first-token latency), a visual call tree with per-node I/O and timing, and a flame graph. Web-debug sessionId for support tickets: browser devtools → network → "run" request → first message's sessionId/interactionId.

## Cloud A2A protocol (云A2A协议)

Docs are split into a **technical spec overview** (`agent2agent-comments-0000002500412353`) and **message/command definitions** (`agent2agent-define-0000002467293060`). Single endpoint, POST only, **StreamableHTTP + JSON-RPC 2.0** between Agent Client (Xiaoyi) and Agent Server (your backend); no long-lived connections, reconnect supported; compatible with Google A2A `message/stream` / `tasks/cancel`.

**Session modes**: (1) recommended — server-assigned `agent-session-id` header (like MCP's session id); server must implement `initialize` + `notifications/initialized` and keep ≥5 concurrent session ids valid per credential; (2) stateless — credentials in headers per request, no initialize needed.

### RPC methods
| Method | Purpose |
|---|---|
| `initialize` | Get `agentSessionId` (+ `agentSessionTtl`, suggest 7 days) |
| `notifications/initialized` | Client signals init complete (HTTP 200, no body) |
| `message/stream` | User dialog; server may upgrade to SSE (`Content-Type: text/event-stream`) |
| `tasks/cancel` | Cancel current task → state `canceled|failed|unknown` |
| `clearContext` | Clear multi-turn context → state `cleared|failed|unknown` |
| `authorize` / `deauthorize` | Account binding (authCode → `agentLoginSessionId`; deauth carries `agentLoginSessionId` + `cpUserId`) |
| `push` | **Server→Client** push notification for async long tasks (via the hag webhook endpoint, HMAC-SHA256-signed headers) |

### message/stream essentials
- Request params: task `id`, `sessionId` (client-assigned context key; changes when user clears context), optional `agentLoginSessionId`, `message.parts[]` with `kind: text | file | data` (file = name/mimeType + `uri`; the earlier `bytes` alternative was removed).
- SSE responses are **TaskStatusUpdateEvent** (`kind: "status-update"`; status.message text shown in the status bar; `state: submitted|working|input-required|completed|canceled|failed|unknown`) or **TaskArtifactUpdateEvent** (`kind: "artifact-update"`; `artifact.parts[]` with `reasoningText` (deep-think stream), `text` (markdown body), `data` (cards/commands/chips/references); `append` = incremental, `lastChunk` ends one stream burst).
- `final: true` ends the SSE task channel (server can't push afterwards) — mandatory at task end; **don't set final=true when issuing a location command**.
- Error codes: 0 success, 99911114 content non-compliant, 99911113 throttled.

### Data structures
- **Request data (client→server)**: `kind:"data"` + `data.{authCode, agentLoginSessionId, events[] (header.namespace/name + payload), userInputInfo (quick-command taps: statusInfo[].isSelected/statusKey/statusValue), variables}`.
- **Response data (server→client)**: `data.text` (markdown ok) plus `commands[]` (CommandObject), `cardsInfo[]` (CardDataObject: `cardName` must match A2A output config, `cardData` — arrays in `items[*]`, `displayType: EmbedMarkdown | DisplayFaCard` default standalone), `chipsInfo` (chips ≤64 chars, `superlink://vassistant?text={{q}}&startmode=recognize`, domain `documentSummary|AIGC`), `reference` (citation cards, type `leftPictureRightText`, weblink `startMode` 0=in-Xiaoyi / 1=browser).

### Device-side commands
- **`Common/Action`** — invoke intent framework in your app: `executeParam` (executeMode background/foreground, intentName, intentParam, bundleName, actionResponse) + optional `actionResponseConfig` (WHITE/BLACK resultPath filter) + per-code `response` texts. The intent plugin must be registered on the platform with matching bundleName/intentName, or the cloud blocks it (whitelisting required for all device-call commands except Deeplink). Results return via event `Common/UploadExeResult` (toolName, resultCode, responseDataList).
- **`Command/Deeplink`** — open app page (url, appName — store fallback if not installed, packageName, appType `DeepLink|OpenHarmony`).
- **Location**: `Common/Action` with `intentName: "GetCurrentLocation"`, `bundleName: "com.huawei.hmos.aidispatchservice"` (requires the 定位服务 plugin added to the agent); client reports WGS84 `latitude`/`longitude` via UploadExeResult.
- **Device context variables** (toggle on in platform variable config): `variables.systemVariables` — `app_ver`, `foreground_apps`; plus `clientVariables`, `memoryVariables`.

## Device A2A protocol (端A2A协议)

Spec for **in-app agents talking to the on-device Xiaoyi** (端A2A协议技术规范, doc version V0.6). JSON-RPC 2.0 messages exchanged over an in-device Extension Ability connection — the dialog method is **`MessageStream`** (capitalized, NOT the cloud protocol's `message/stream`).

### Core concepts
- **Context**: logical session container, `contextId` assigned by the agent in its first response frame; Xiaoyi carries it on subsequent requests; a request without contextId resets the session.
- **Task**: one unit of work with its own lifecycle; `taskId` assigned by the agent; states `TASK_STATE_SUBMITTED | WORKING | INPUT_REQUIRED | COMPLETED | CANCELLED | FAILED`; terminated tasks cannot be restarted.
- **Artifact**: output unit of a task (`artifactId`); contents of one artifact are rendered/processed together (e.g. reasoning + body + card), independent items get separate artifacts.
- **Part**: content shards of an artifact — text, cards, long-task commands, etc.

### Supported scenarios
1. **Dialog interaction**: LUI chat — single/multi-turn replies, clarification, file exchange, AgentUIExtension cards.
2. **Long-task accompaniment**: agent returns `uiSession` `action: "CREATE"`; after Xiaoyi's UI is ready it sends `uiSession` `action: "READY"` (uiSessionState WORKING) and the agent moves to TASK_STATE_WORKING. Progress is surfaced via dialog capsules (对话胶囊), status capsules (状态胶囊), and the dialog panel; the user can intervene. Either side closes via `uiSessionState: "CLOSING"`, then TASK_STATE_COMPLETED.
3. **UI-control accompaniment**: like long tasks but with a UI-control overlay/mask and streaming-light effect while the agent drives the UI.
4. **Native control**: on recognizing specific intents the agent operates its own app natively (different paths depending on foreground/background) while keeping the dialog experience.
5. **Chips (topic) recommendation**: Xiaoyi passes app/device context; the agent returns chips suggestions best fitting the scene.
6. **Dynamic opening lines**: Xiaoyi calls method `GetOpening` (params carry message contextId + metadata traceId/agentId/appVersion); the agent creates a task, streams an artifact-update whose data part is `openingTexts: { openingText, openingQuestions: [] }`, then a status-update TASK_STATE_COMPLETED.

### Implementation (in the HarmonyOS app)
- **AgentExtensionAbility** — mandatory core component; created in DevEco Studio via New → Extension Ability → Agent, which generates `module.json5` (registers the ability, `metadata` points to `agent_config.json`), `agent_config.json` (the AgentCard), and the ability class. Lifecycle: `onCreate` → `onConnect(want, proxy)` (save the `AgentHostProxy`) → optional `onAuth` (key negotiation, reply via `proxy.authorize`) → `onData(proxy, data)` (handle each A2A message, reply via `proxy.sendData`) → `onDisconnect` → `onDestroy`.
- **AgentUIExtensionAbility** — optional, for custom UI cards; `type: agentUI`, `exported: true`; load the ArkTS page in `onSessionCreate(want, session)`; the `payload` of a `uiExtensionCard` command arrives in `want.parameters['ability.want.params.payload']`.

### AgentCard (agent_config.json)
`agentCards[]` entries; key fields:
- **Required**: `name` (≤64), `description` (≤512 — drives Xiaoyi's intent matching and skill routing), `agentId` (unique within the bundle; must match the `connectAgentExtensionAbility` agentId), `version`, `iconUrl`, `defaultInputModes`/`defaultOutputModes` (MIME types), `skills[]` (each with required `id`/`name`/`description`/`tags`, optional `examples`, per-skill input/outputModes), `appInfo`.
- **Optional**: `capabilities` (`streaming`, `pushNotifications`, `extendedAgentCard`), `provider` (organization + url), `documentationUrl`, `extension` — a JSON string per **ExtInfo**: `introduction` (opening line, required), `securityInfo`, `supportedInterfaces[]` (ordered, first = preferred; url + `protocolBinding: JSONRPC` + protocolVersion), `developmentType` (`NATIVE` default / `PROCODE` / `LOWCODE`), `reqMetaRequired`.
- **appInfo**: `bundleName`, `moduleName`, `abilityName`, `minAppVersion`, `deviceTypes`.

### Error codes
JSON-RPC: `-32700` parse error, `-32600` invalid request, `-32602` invalid params, `-32603` internal error. Agent→Xiaoyi: `-32001` TaskNotFound, `-32002` TaskNotCancelable, `-32004` UnsupportedOperation. HarmonyOS extensions: `99911113` flow control, `99911114` risk control, `99911200` task invalid, `99911222` contextId invalid.

### Platform-side setup (端A2A-mode agent)
Create a 端A2A-mode agent → associate an app/元服务 (fill app name / 元服务 module + service name) → import the AgentCard (per the AgentCard spec) → configure the rest (input files, quick commands, …).

## Workflow development

Canvas editor; new workflows start with Start + End nodes. Node types: **Start, End, LLM, Plugin, Workflow (sub-workflow), Code, Selector, Intent Classification, Output, Loop, Batch Processing, Knowledge Base, Variable, Long-term Memory, Text Processing, Questioner, Query Counter Variable (查询计数变量), Quota Management (配额管理)**.

- **Query Counter Variable node**: read-only fetch of a counter variable's current value; outputs `isSuccess`, `counterVariable`, `errorMessage`.
- **Quota Management node**: atomic increment/decrement of a counter variable (设置值 = step, may be negative) with a quota threshold (限额); outputs `counterVariable` (new value), `errorMessage`, and `resultStatus` ∈ `success` (assigned) | `quotas` (over quota, value unchanged) | `error` (execution error, value unchanged).

- Lifecycle: create → add/connect nodes → configure I/O → 试运行 (green border on success, inspect node I/O + trace tree) → 上架 (required before use in agents).
- **Import/export**: export to JSON (optionally including sub-workflows) and import into any workspace (cross-account). Account-bound resources (plugins, KBs, workflows) may break — replace manually; import sub-workflows first, publish, then re-link in the main workflow.
- **Version management**: publish archives, system auto-archive ("当前" test version after edits), manual archives; preview (read-only, can test-run) and roll back (overwrites draft).

## Plugin development

Three plugin classes: **MCP** (MCP-protocol servers), **Cloud** (your HTTP service), **Device/端** (bridges to HarmonyOS apps).

### MCP plugins
- **Standard registration**: enter server info; the tool list is auto-fetched on save (may lag a few minutes). Market listing additionally requires usage description (Markdown incl. apikey acquisition), AI-generated-content declaration, personal-info collection statement, and LLM filing info.
- **External platform import**: from ModelScope (魔搭) via API key/access token; only long-lived self-deployed MCP servers under that account; auto-creates + publishes to the Agent channel; duplicates (same config URL) are skipped.
- **Publishing channels**: Agent (no manual review), Xiaoyi Dialog (Huawei review), Plugin Marketplace (Huawei review). 
- **Auth**: developer self-auth (auth-key link in plugin description; consumers configure their own key) or Huawei unified auth.

### Cloud plugins
- One plugin = multiple tools (APIs); tool name/description/params drive function-calling quality.
- **Protocols**: Restful (must respond within **2.2 s** or it times out), SSE, WebSocket. Auth: AK/SK (accessKey + ts + sign = Base64(HMAC-SHA256(secretKey, ts)); validate ts within ~15 min), OAuth (Client mode), Header, Query.
- **Batch vs stream**: stream tools (WebSocket/SSE) return `reply.streamInfo` — `streamContent` (cumulative full text), `streamingTextId`, `streamType: start|partial|final`, `textType: plainText|markdown` — plus optional `items[]` for card binding (`displayType: "EmbedMarkdown"` required for text-card mixing; otherwise only the final frame's items count).
- **Mock sets**: created per tool after publish. Batch tools: random-single mode only. Stream tools: random-single or full-sequence return; mock data must contain exactly one `start` and one `final` frame.

### Device (端) plugins
- Package name must be an AGC-published app under the same account.
- **Execution modes**: foreground (standard implementation / Applink / Deeplink), background (data return, card-bindable), card (app renders a card).
- **Device-side implementation**: create `entry/src/main/resources/base/profile/insight_intent.json` declaring intents (intentName/intentVersion must match the platform tool name/version; srcEntry; executor binding via `uiAbility` (foreground/background executeMode), `form`, `uiExtension`, or `serviceExtension`). Implement handlers in ArkTS; outputs must include `code` and `result`.
- **Permission control**: device plugins that need permissions add entries to the agent's permission config — usage descriptions are mandatory before publish (per MIIT rules, state the concrete purpose, e.g. "推荐附近门店"); users authorize on device.
- Mock sets supported for device tools as well.

## Card development

Visual drag-and-drop card editor; Official Cards (platform preset) vs My Cards (custom). Only the latest published version shows in pickers; published versions are view-only; linked cards can't be deleted.

- **Create**: standard (from scratch) or **AI-generated** from an example image (10x10–1024x1024 px, JPG/PNG, <5 MB; takes ~1-3 min; result may need touch-up)
- **Editor**: components / canvas (component tree) / property panel; variables (String, Number, Array, Object, aggregated-link Object, Boolean) bind to components; event actions include jumps, sending messages to Xiaoyi/agent, setting variables, modifying component props, page switch, app-install check, plugin invocation, clipboard, image preview, list-item deletion, operating Xiaoyi
- Component guides: audio/video, choice group, multi-tab, map, H5 card
- **Reply templates** (回复模板配置): map plugin/workflow output params into card templates
- **Card upgrade**: bound configs show "pending update"; parameters are cleared after upgrading the binding

## Interface development (开发界面)

Full-screen/half-screen popup GUIs (vs inline cards). Built in Workspace → 界面 with the same editor paradigm as cards. Variables: interface input params (optional, defaults apply if not passed by the workflow) + custom variables. **关联技能 (associated skills)**: whitelist of plugins/workflows callable from component events (auto-populated from event actions; H5 components may only whitelist device plugins). Publish before binding from workflows (工作流界面跳转配置) or generic-event triggers. No web debug — verify on device.

## Timbre development (开发音色)

Enterprise developers only, max 5 timbres per account (Workspace → 音色). Clone from a local recording or uploaded audio reading the platform-provided script, then synthesize to audition. Used in the agent's 角色声音 — only when the user voice-switch toggle is off.

## Knowledge base development

- Create in Workspace → 知识库; pick knowledge type per entry; crawler import supports a crawl URL + schedule.
- If you check "授权知识库用于知识问答" (allow Xiaoyi dialog to use it), publish review takes 1-3 business days.
- Document-type knowledge requires data validation before it can be published.
- Bind to agents in orchestration → 知识库 (LLM mode).

## Skill development

Skills (now a top-level doc tree section next to Agent) are **standardized capability units callable by AI agents** — executed by 小艺Claw. The platform covers the full lifecycle: create (Vibe Coding or import), device test, publish to the resource library.

- **Vibe Coding creation**: Workspace → Skill → 新建Skill → Vibe Coding. Fill name/description/trigger intents in a chat box; attach extension abilities via the **@** button; generation runs with clarification questions and a Todos progress list; the platform auto-validates SKILL.md compliance; optionally auto-generates test cases, executes tool calls, and produces a **Canvas evaluation report**; finally write the Skill description (for semantic matching by agents) and the Skill is auto-packaged. A **Skill检索** option searches 小艺Claw's built-in skills for similar published skills to use as a generation template (visual "Skill graph" of results; one template at a time).
- **Import**: 新建Skill → 导入Skill, upload a Skill package for the platform to parse.
- **Extension abilities (attach via @)**: 插件 (plugins from the marketplace / your own / partners; cloud, device, or MCP types), **Agent** (embed an agent of any of the six modes — your own or a partner's), 生态Skill (reference an existing Skill as capability base), 系统CLI (public or private CLI tools; a CLI tool project ships `config.json` descriptor + `BUILD.gn` + src/docs), 附件 (attachments: max 10 per Skill, 1 MB each; `.md` / `.py` / `.txt` / `.zip`), Skill检索.

### Skill format (HarmonyOS Skill development standard, V6)
A Skill is a **directory** with mandatory `SKILL.md` + `module.json`, optional `scripts/`, `references/`, `assets/`.
- **SKILL.md** = YAML frontmatter + Markdown body. Frontmatter: `name` (required, 1-64 chars `[a-z0-9-]`, must equal the directory name), `description` (required; hard limit 512 chars Chinese / 1024 English, ~300-token soft budget; state capability + trigger cases, no marketing words), optional `license`, `compatibility`, `metadata`, `allowed-tools`. Body: hard limit 500 lines (~5000 tokens soft); write only what the model can't do reliably, organized as 领域知识 → 工具定义 → 经验攻略 / SOP / 安全红线 → 与人协作; overflow goes to `references/`.
- **module.json**: `version` (Semver, required), `availableOn` (phone/tablet/pc/wearable/car/tv/cloud/cloudSandbox/localSandbox), `toolDependencies` (platform-registered tools only; must match the body's tool definitions), `abilityName`, `visibility` (`private`/`system` default/`public`), `srcEntries` (ETS scripts, 0-100, under `scripts/`), `permissions`, `requestPermissions`, auto-generated `minAPIVersion`/`targetAPIVersion`.
- **Tools**: system-preset (`exec`, `invoke`, `read`, `write`, `web_search`, `web_fetch`, `load_skill` — never declared), platform-registered vs Skill-private Function tools (`invoke`) and CLI tools (`exec`), and private scripts under `scripts/` invoked via `exec` of **`ohos-arktsScript --skillName … --scriptPath … --functionName … --args …`** (ArkTS runs on device; Python/Node are delegated to PC/cloud via subAgent). Validate with `skills-ref validate ./my-skill`; pre-publish security scanning (dangerous commands, hardcoded credentials, path traversal) + LLM semantic audit (prompt injection, false claims).

### Skill test, publish, account binding
- **Device test**: pick whitelist user groups (max 100 groups/team, 100 users/group), max 10 groups per publish; each device-test publish is **valid 15 days**; re-publish or cancel anytime.
- **Publish (上架)**: one-stop listing page; upgrades keep the previous approved version live; separate **Skill review standard** (信息安全 & 上架审核) applies — intent transparency ("who is it and what does it want"), description must list all core actions and match actual behavior, no hidden logic, an explicit catalog of forbidden prompt-injection patterns (file theft, context exfiltration, code/command injection, DoS/token bombs, task hijacking, preference manipulation, behavior concealment, destructive-op laundering, tool override), permission minimization (only the isolated work directory).
- **Huawei-account binding**: for Skills needing a logged-in apiKey. Configure 账号鉴权 (clientId from an AGC web app + auth API URL + domains using the token). At runtime the Skill reads **`loginToken` from environment variables** (the `.xiaoyienv` file); if missing/expired it calls the `huawei_id_tool` tool once (params clientId + skillName) to refresh. Server implements JSON-RPC callbacks `authorize` (authCode → loginToken, 7-day validity, + loginRefreshToken, ~6 months), `refreshToken`, and `deauthorize` (AK/SK — accessKey + ts + `sign` = Base64(HMAC-SHA256(secretKey, ts)) — Header, or Query auth). Business requests carry `login-token` in the header. Phone-number permission: enterprise developers only.

## Xiaoyi Compass (小艺罗盘)

One-stop evaluation + observability platform:
- **Evaluation (评测)**:
  - **评测集 (evaluation sets)**: structured input + reference_output columns (customizable); local file import (append or full overwrite) or manual entry (max 200 rows); versioned on every save.
  - **评估器 (evaluators)**: model + scoring prompt (templates available; declare input/output/expected-output variables) producing 0.0-1.0 scores with reasons; debuggable before save.
  - **评测任务 (evaluation tasks)**: pick agent + evaluation set + optional evaluator (with field mapping); without an evaluator it's a batch run with I/O inspection. **Weekly quota on evaluation runs.** Results viewable/downloadable.
- **Observation (观测)**: 运营看板 operations dashboard with per-agent usage metrics.

## OpenClaw integration

1. Install OpenClaw on a server (or PC — but the OpenClaw community advises against your primary personal machine for data-safety reasons).
2. Create an OpenClaw-mode agent on the platform; get credentials (ak/sk) and agentId.
3. `openclaw plugins install @ynhcj/xiaoyi@latest`
4. Add the channel in `/root/.openclaw/openclaw.json` (channels sits at the same level as models/agents):
   ```json
   "channels": { "xiaoyi": { "enabled": true, "ak": "…", "sk": "…", "agentId": "…" } }
   ```
5. `openclaw gateway restart`, then `openclaw logs --follow` — "info sent claw_bot_init message" confirms the connection.

## Digital product payment (enterprise, beta)

For selling digital goods (consumable / non-consumable / non-renewing subscription) through A2A or Workflow agents. RMB pricing, China mainland only.

- **Flow**: enable merchant service → integrate Huawei account binding (server must return `cpUserId`) → add paywall touchpoints (superlink `superlink://vassistant?startmode=cashierpage&parameters={"agentid":"…","transBuffer":"…"}` — agentid from system var `agent_instance_id` since dev-test and live agents have different instance ids; or a device plugin that opens the product page) → implement & register the two callback APIs (配置→商品管理→订单服务对接配置, Huawei-reviewed) → configure products (ID immutable, name, intro <128 chars, real price/original price, perks ≤8, fee agreements ≤3; product review ~2-3 business days; admins/ops only) → device-side display ordering → mock-payment device test (模拟付费验证功能 whitelist toggle; `purchaseTest: true` flag) → publish the paid agent (include fee-trigger descriptions for reviewers). Transaction details kept up to 7 years, manual re-issue (补发) for failed grants; revenue settlement via 管理中心.
- **Order notification API** (Huawei → developer, HTTPS POST): signed with `signature` header — SHA256WithRSA/PSS, RSA-3072 (download public key, Huawei holds private). Body: traceId, status PAID/REVOKE, agentOrderId, skuId, ts, userIdType CP_USER_ID, userId, transBuffer, amount (fen), currency CNY, purchaseTest, deviceType (0 phone / 2 tablet / 4 watch / 5 car / 11 PC). Respond `code: "success"` + `cpOrderId`.
- **Rights query API** (Huawei → developer, HTTPS POST): AK/SK (accessKey + sign + ts) or OAuth 2.0 (Client). Returns `privilegeList[]`: privilegeName, privilegeId, privilegeStatus Active/Inactive, expireTime (yyyyMMddHHmmssSSS), privilegeDetail[].

## AgentKit — in-app agent launcher

HarmonyOS apps embed a Function-component icon that launches the associated agent half-screen.
- **Prerequisites**: AGC-published app with **manual signing**, agent's 关联应用 pointing at it, AgentKit integrated; device ROM 6.0.0+ / API SDK 20+, Xiaoyi app 11.3.8.300+.
- **Common issues**: "智能体未授权给该应用" → missing association / mismatched name-package-appid / auto-signing; no icon → AgentKit not integrated or ROM/SDK too old; dev agent still launching after release → remove device from whitelist or cancel dev publish.

## Publishing & audit

### Pre-publish checklist
- Personal-developer agents containing **private cloud plugins or private MCP plugins cannot be published** (debug only).
- All platform checklist items must pass before 上架 can be initiated.

### Audit specifications (上架审核规范 chapters)
1. **Agent info**: name must directly convey function; Simplified Chinese or Chinese-English mix only, no special characters/traditional characters, no marketing/superlative/test words, no broad generic terms, trademark check required. Creator name must not claim "官方". Avatar: original/copyrighted, clear, no pure-color images, no watermarks/QR codes/contact info, no ranking claims. Description ≤50 chars, ends with punctuation, consistent 你/您.
2. **Agent security**: no viruses, trojans, data theft, mining, ad fraud.
3. **Agent function**: real practical value; no pure redirects or forced downloads.
4. **Agent content**: no illegal/pornographic/violent/gambling/terror/discriminatory content; AI-generated content must be labeled; **anthropomorphic (拟人化) agents are currently not allowed** per 《人工智能拟人化互动服务管理暂行办法》; Huawei may run content-safety testing during review.
5. **Agent payment (智能体付费)**: honest pricing, auto-renewal rules (explicit consent, single-purchase option, second confirmation, reminder ≥5 days before renewal, easy standalone unsubscribe), loot-box probability disclosure.
6. **Agent advertising (智能体广告)**: ads must be labeled "广告", truthful, in-agent only, non-intrusive (no popups on system keys/exit), one-tap genuine close button.
7. **User privacy**: privacy policy required; data minimization; sensitive data (calls, SMS, biometrics, health, location) not for ads.
8. **Minor protection**: age-appropriate content, no addiction mechanics.
9. **Intellectual property**: own all rights; no Huawei impersonation.
10. **Agent qualifications**: LLM-backed agents need the generative-AI service filing + algorithm filing; may submit without and complete filing within 3 months.
11. **Developer behavior**: truthful registration; government agents need official authorization.
12. **FAQs**: AI-labeling & LLM-filing FAQ (how to fill/verify labels, where to query filing numbers); permission-usage-description FAQ (state a clear, accurate purpose when requesting location/calendar etc., or the agent can't pass review).
13. **Appendix**: business-specific qualifications (securities, banking, medical, news, ride-hailing, legal, recruitment, etc.).
14. **Non-admitted types (不收录类型)**: a dedicated chapter enumerates agent categories the market will not list — e.g. forged documents/certificates, weapons, protected-wildlife trade, surrogacy, e-cigarettes, SMS bombing, "网络水军" (fake engagement) services, virtual-currency trading and other illegal finance, gambling-style red-packet/betting mechanics, fortune-telling targeted at minors, anthropomorphic agents, 饭圈 (fan-circle) content, and more.
15. **Violation handling (智能体开发者违规处置措施)**: tiered measures — account freezing, inclusion in a risk-agent list with security controls, take-down/invisibility, deadline-bound rectification, and escalating penalties for repeat offenses; regulator orders override; appeals/re-listing after rectification unless permanently removed.

### Audit process
- Submit via the editor's 【上架】/【升级】 button or Workspace → 智能体 list operations (上架/下架/升级/撤回).
- Review cycle 1-3 business days; team admin only.
- Rejection reasons: version history (版本记录) or hover on the status tag in the agent list.

## Best practices (最佳实践, added 2026-07-27)

Three worked cases under 最佳实践 → 实践案例; use them as reference architectures.

- **云A2A智能体协同 — 京东Agent** (`cloud-a2a-jingdong-0000002640047776`): the reference cloud-A2A integration. Your Remote Agent must expose a `message/stream` RPC that handles tasks asynchronously, pushes progress over SSE, can ask clarifying questions, streams the first token ASAP, returns a complete final message, and caches per-user context keyed by the platform-issued `sessionId`. Two session-keeping styles: server-side session allocation (requires implementing the session-init message) vs **stateless per-request auth (recommended** — every request carries auth headers, no init interface, horizontally scalable). Auth options: **AK/SK (recommended)**, OAuth 2.0 client-credentials (token URL, client id/secret, scope), or API key (header preferred; query is discouraged). Opening dialog + at most **3 preset guide questions**; up to **20 preset cards** in the A2A output config, selected by card ID in responses; extended commands for session termination, context clearing, offline push. Account binding: register the Huawei-account Client ID on the platform, return an `agentLoginSessionId` on (silent or interactive) authorization; the client persists it and re-authorizes automatically when it expires.
- **Vibe Coding 端云协同 — 种草打卡Skill** (`vibe-coding-skill-0000002670207675`): a Skill that chains device plugins (相机-TakePhoto → 定位服务-GetCurrentLocation → 备忘录-CreateNote) with cloud plugins (联网问答-ComplexSearchOnline for store-specific copy, 图像生成-TextToImage for retouching/creative images). Flow: Skill → 新建Skill → Vibe Coding mode → describe name/function/trigger intent/scenes → answer the auto-generated clarification questions → automatic packaging.
- **Vibe Coding 场景化编排 — 同程程心Skill** (`vibe-coding-tcchengxin-0000002639887830`): an API-wrapping travel Skill. Design principles: intent-driven routing (one intent → one query script), structured fields + a free-text `--extra` passthrough, and **verbatim output of the backend response** (the LLM must not summarize/rewrite). Scripts are Node.js (`node scripts/<domain>-query.js … --channel … --surface …`, HTTPS POST, 15 s timeout). Mandatory credential flow before every query: read `/home/sandbox/.openclaw/.xiaoyienv` (`<clientId>_login_token` / `_expire_time`) → if missing/expired call the `huawei_id_tool` (clientId, skillName) → fall back to an env-var API key; auth via `apikey` header. Includes explicit fallback strategies (e.g. air-rail intermodal when no flights).

## System-agent GUI operation status (added 2026-08-14)

HarmonyOS lets apps detect when a **Huawei system agent** (系统智能体) is driving their UI (GUI operation) and identify it by Agent DID (合作协议与补充接口文档 → 系统智能体GUI操作状态查询说明, `agent-gui-0000002680521240`). During such an operation the system writes the state + Agent DID into the Settings DB key **`AI_Operation_Mode`** (`settings.domainName.USER_PROPERTY`). Read it with `settings.getValue(context, 'AI_Operation_Mode', '', settings.domainName.USER_PROPERTY)` when coming to the foreground and watch it with `settings.registerKeyObserver(context, 'AI_Operation_Mode', cb)`: empty ⇒ not in a system-agent GUI operation; valid "on" ⇒ operation in progress; valid "off"/empty again ⇒ finished. Apps that do not want system agents operating their UI apply by email to `hagservice@huawei.com` (subject 【系统智能体操控拒绝申请】<app name>, with bundle name, developer contact, reason).

## Markdown output rendering

The platform publishes an official **markdown syntax spec** for agent output (合作协议与补充接口文档 → markdown语法规范, `markdown-grammar-0000002553963585`): `#`-style headings 1-6 (Setext `=`/`-` headings are NOT supported in the single-box Xiaoyi renderer), ordered/unordered lists (no tables/code blocks/quotes nested inside list items), plus the other standard constructs. Check it when formatting agent replies.

## Key URLs

- Xiaoyi Open Platform docs root: `https://developer.huawei.com/consumer/cn/doc/service/`
- 鸿蒙智能体 guide: `https://developer.huawei.com/consumer/cn/doc/service/developer-guide-0000002469667881`
- Agent protocol hub: `https://developer.huawei.com/consumer/cn/doc/service/agent2agent-0000002498656261`
  - Spec overview: `https://developer.huawei.com/consumer/cn/doc/service/agent2agent-comments-0000002500412353`
  - Message/command definitions: `https://developer.huawei.com/consumer/cn/doc/service/agent2agent-define-0000002467293060`
- OpenClaw integration: `https://developer.huawei.com/consumer/cn/doc/service/openclaw-0000002518410344`
- Digital product payment: `https://developer.huawei.com/consumer/cn/doc/service/digital-product-payment-0000002537601305`
- Xiaoyi Compass: `https://developer.huawei.com/consumer/cn/doc/service/commissioning-space-0000002512393840`
- Intent framework: `https://developer.huawei.com/consumer/cn/doc/service/intents-kit-0000001677103865`
- Intelligent agent white paper: `https://developer.huawei.com/consumer/cn/doc/service/intelligent-agent-white-paper-0000002508129114`
- AI terminal white paper: `https://developer.huawei.com/consumer/cn/doc/service/ai-terminal-white-paper-0000001929691644`
- Terms of service: `https://developer.huawei.com/consumer/cn/doc/service/terms_conditions-0000001193795972`
