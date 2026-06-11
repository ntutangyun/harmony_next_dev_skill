# Xiaoyi (小艺) Agent Development — HarmonyOS NEXT

_Source authority: `https://developer.huawei.com/consumer/cn/doc/service/*` (小艺开放平台 / Xiaoyi Open Platform)_

## What the Xiaoyi Open Platform is

Xiaoyi Open Platform is Huawei's **intelligent agent (智能体) development and distribution platform** for HarmonyOS NEXT. It provides end-to-end tooling to build, debug, and publish AI agents that users access through Xiaoyi (the system-level AI assistant) and in-app entry points.

Agents are published to the **Agent Market (智能体市场)** and distributed across devices (phone, tablet, PC, watch, car). The platform also runs a **Plugin Marketplace** (system plugins, system-app plugins, third-party app plugins, MCP tools) plus private custom cloud/device plugins.

Doc tree top levels: 业务介绍, 鸿蒙智能体 (快速创建智能体 / 开发智能体 / 开发知识库 / 开发工作流 / 开发插件 / 开发卡片 / 开发界面 / 开发音色 / 小艺罗盘 / 上架审核规范), 鸿蒙Agent通信协议接入方案, 智能体数字商品支付服务, OpenClaw接入, 意图框架, white papers, terms.

## Four development modes

| Mode | Description | Best for |
|---|---|---|
| **LLM mode (单Agent)** | LLM-driven: pick a model, write prompts, add plugins/workflows. Model handles intent routing dynamically. | Simple Q&A, knowledge retrieval, content generation |
| **Workflow mode (工作流模式)** | Rule-based: compose ordered steps (data fetch → process → act) by connecting nodes on a canvas. | Complex multi-step business logic with deterministic flows |
| **A2A mode** | Bring your own agent: connect an existing third-party agent via the HarmonyOS Agent-to-Agent protocol (StreamableHTTP + JSON-RPC 2.0). | Enterprise developers with existing cloud agents + HarmonyOS apps |
| **OpenClaw mode** | Connect an OpenClaw server via the `@ynhcj/xiaoyi` plugin for rapid personal agent creation. One per account, device-test publishing only. | Personal assistants, automation, quick prototypes |

### Mode capability matrix (key differences)

| Capability | LLM | Workflow | A2A | OpenClaw |
|---|---|---|---|---|
| Model selection & settings / prompt | ✓ | — (对话设置 only) | — | — |
| A2A basic config / output settings | — | — | ✓ | — |
| OpenClaw basic config | — | — | — | ✓ |
| Opening dialog & preset questions, input files, background image, character voice | ✓ | ✓ | ✓ | ✓ |
| User question suggestions | ✓ | ✓ | — | — |
| Quick commands | ✓ | ✓ | ✓ | — |
| Plugins | ✓ | — | ✓ | — |
| Workflows | ✓ | ✓ | — | — |
| Trigger | ✓ | ✓ | ✓ | — |
| Associated app (AgentKit) | ✓ | ✓ | ✓ | — |
| Account binding | — | ✓ | ✓ | — |
| Paid agent | — | ✓ | ✓ | — |
| Knowledge base | ✓ | — | — | — |
| Variables | ✓ | ✓ | ✓ | — |
| Long-term memory | ✓ | ✓ | — | — |

"语音通话" (voice call) appears in the orchestration list but is marked **暂不支持** (not yet supported).

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

**Opening dialog & preset questions**: Markdown welcome message + up to 3 one-tap preset questions.

**Input file settings**: photo upload (JPEG/JPG/PNG/BMP/WEBP) + camera capture (device-only, no web preview); file upload (pdf/doc/docx/txt/ppt/pptx/xlsx/xls). Send modes: direct, or "pending area" (text+attachments together, max 6 photos/files per message). Optional photo/file quick-command presets.

**User question suggestions** (LLM/Workflow): off by default; after each reply suggests follow-up questions via system prompt or custom prompt.

**Quick commands** (快捷指令): up to 10 static + 1 dynamic; dynamic ones are pinned first (if dynamic yields <5, static ones fill in).
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

**Variables**: user variables (per-user persistent; usable in prompt and workflows; context-based auto-extraction in LLM mode only — and disabled when an executed workflow contains a variable component) + system variables (read-only, off by default: device identifier, device language, etc.). Inspect/reset via 【记忆】→【变量】.

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

## Agent Communication Protocol (A2A)

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
- Request params: task `id`, `sessionId` (client-assigned context key; changes when user clears context), optional `agentLoginSessionId`, `message.parts[]` with `kind: text | file | data` (file = name/mimeType + bytes XOR uri).
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

## Workflow development

Canvas editor; new workflows start with Start + End nodes. Node types: **Start, End, LLM, Plugin, Workflow (sub-workflow), Code, Selector, Intent Classification, Output, Loop, Batch Processing, Knowledge Base, Variable, Long-term Memory, Text Processing, Questioner**.

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

### Audit process
- Submit via the editor's 【上架】/【升级】 button or Workspace → 智能体 list operations (上架/下架/升级/撤回).
- Review cycle 1-3 business days; team admin only.
- Rejection reasons: version history (版本记录) or hover on the status tag in the agent list.

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
