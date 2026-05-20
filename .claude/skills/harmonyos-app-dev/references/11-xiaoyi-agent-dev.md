# Xiaoyi (小艺) Agent Development — HarmonyOS NEXT

_Source authority: `https://developer.huawei.com/consumer/cn/doc/service/*` (小艺开放平台 / Xiaoyi Open Platform)_

## What the Xiaoyi Open Platform is

Xiaoyi Open Platform is Huawei's **intelligent agent (智能体) development and distribution platform** for HarmonyOS NEXT. It provides end-to-end tooling to build, debug, and publish AI agents that users access through Xiaoyi (the system-level AI assistant), system navigation bar, Xiaoyi Search, Xiaoyi Suggestions, and in-app entry points.

Agents are published to the **Agent Market (智能体市场)** and distributed across devices (phone, tablet, car, PC, watch).

## Four development modes

| Mode | Description | Best for |
|---|---|---|
| **LLM mode (单Agent)** | LLM-driven: pick a model, write prompts, add plugins/workflows. Model handles intent routing dynamically. | Simple Q&A, knowledge retrieval, content generation |
| **Workflow mode (工作流模式)** | Rule-based: compose ordered steps (data fetch → process → act) by dragging nodes on a canvas. | Complex multi-step business logic with deterministic flows |
| **A2A mode** | Bring your own agent: connect an existing third-party agent via the HarmonyOS Agent-to-Agent protocol (JSON-RPC 2.0). Requires both a HarmonyOS app (for the client side) and a cloud agent server. | Enterprise developers with existing cloud agents + HarmonyOS apps |
| **OpenClaw mode** | OpenClaw工具-based: install `@ynhcj/xiaoyi` plugin on an OpenClaw server for rapid personal agent creation. One per account, dev-only publishing. | Personal assistants, automation, quick prototypes |

### Mode capability matrix (key differences)

| Capability | LLM | Workflow | A2A | OpenClaw |
|---|---|---|---|---|
| Model selection & prompt | ✓ | — | — | — |
| Plugins | ✓ | — | ✓ | — |
| Workflows | ✓ | ✓ | — | — |
| Knowledge base | ✓ | — | — | — |
| Account binding | — | ✓ | ✓ | — |
| Paid agent | — | ✓ | ✓ | — |
| Variables & long-term memory | ✓ | ✓ | ✓ | — |
| Quick commands | ✓ | ✓ | ✓ | — |
| Trigger | ✓ | ✓ | ✓ | — |
| Associated app (AgentKit) | ✓ | ✓ | ✓ | — |

## Agent lifecycle

```
Create → Configure → Debug & Preview → Publish (review 1-3 days) → Live in Agent Market
```

- **Create**: Workspace → Intelligent Agents → + Create, pick a mode
- **Configure**: Fill basic info, privacy, compliance, and orchestration
- **Debug**: Web debug panel + publish to device test (真机测试) for white-listed testers
- **Publish** (上架): Submit for review. Review takes 1-3 business days. Team admin only.
- **Upgrade**: Submit new version; if rejected, the previous approved version stays live.
- **Take-down** (下架): Removes agent from market. Can re-edit and re-submit.

Version history is tracked; you can view and roll back to any historical version.

## Configuration areas

### 1. Basic info (基础信息)
- **Icon**: 1:1 PNG/JPEG, <5 MB, no transparency
- **Name**: Required, unique per account
- **One-line description**: Shown on agent detail page
- **Category**: Choose from platform classification
- **Supported devices**: Multi-select — Phone (HarmonyOS NEXT / HarmonyOS), Tablet, PC, Watch, Car
  - HarmonyOS NEXT = ROM 5.x+; HarmonyOS = ROM 4.x
- **Aliases**: Multiple, for distribution accuracy
- **AgentCard**: Auto-generated "business card" of agent capabilities. Syncs from plugins/workflows. Editable fields: function name, description, dependencies.

### 2. Privacy policy (隐私协议服务)
- **Custom privacy URL**: If you already have a privacy policy page, paste the URL directly.
- **Platform-hosted privacy**: If no custom URL, the platform provides a template-based builder covering:
  - Introduction & version changes
  - How we collect/use personal info (default: conversation data; add custom data types)
  - Personalized recommendations (optional)
  - Minor protection (optional)
  - Third-party sharing (optional) — per-company and per-MCP-server declarations
  - Personal info management (fixed content)
  - Storage location & duration (storage: China servers only; duration: fixed or "minimum necessary")
  - Developer custom section (optional)
  - Contact methods (phone, email, address)
  - Effective date
- Each agent can have multiple privacy policies, but only ONE is linked at publish time.
- Auto-detection: if agent capabilities reference data not declared in the linked policy, the platform flags a warning.

### 3. Content compliance (内容合规)
Mandatory per Chinese AI regulations:
- **AI-generated content labeling**: Declare whether outputs contain AI-generated text/images/audio/video. If yes, fill in label metadata (Label 1/2/3, ContentProducer, ProducerID, ReservedCode1, ContentPropagator, PropagatorID, ReservedCode2).
- **LLM filing numbers**: If using third-party (non-platform) LLMs, provide the CAC filing number and algorithm filing number.

## Orchestration (编排)

### Model selection & prompt (LLM mode)
- Choose from available platform models
- **Multi-model comparison**: Test different models side-by-side
- **Hyperparameters** (model-dependent): Context rounds 0-20, Top-K 1-256, Top-P 0-1, Temperature 0-1
- **Prompt comparison**: Test prompts side-by-side, pick the best
- **Prompt optimization**:
  1. Dataset-based optimization: defines an optimization task with evaluation model, strategy, rounds (max 20), sample count (max 10). Two evaluation methods: model self-evaluation (for creative tasks) or exact text matching (for classification/precise outputs).
  2. Full-text auto-optimize / optimize from debug results

### Dialog settings (Workflow mode)
- Context window: 0-20 rounds (for the LLM node within the workflow)

### Capability extensions (能力拓展) — 19 sub-areas:

**A2A basic config** (A2A mode only):
- API URL: endpoint that speaks the HarmonyOS Agent-to-Agent protocol
- Session: server-assigned, stateless communication (carry auth credentials each request)
- Auth: AK/SK, OAuth 2.0 (Client mode), Header-based, or Query-based

**A2A output settings**: Bind cards to output parameters. Max 20 outputs. Each output needs cardName, cardDescription, and a `cardData` Object parameter.

**OpenClaw basic config**: (1) Create credentials in Workspace → Credentials → copy Key + Secret Key. (2) Configure server channel with AK/SK. One OpenClaw agent per account. Publish dev-test only (no public market listing).

**Opening dialog & preset questions**: Markdown welcome message + up to 3 one-tap preset questions.

**Input file settings**: Toggle photo upload (JPEG/PNG/BMP/WEBP), camera capture, file upload (PDF/DOC/DOCX/TXT/PPT/PPTX/XLSX/XLS). Photo/file max 6 at a time in "pending area" mode.

**Quick commands** (快捷指令): Up to 10 static + 1 dynamic.
- **Static types**:
  - Jump-type: DeepLink to app (config: app name, package name, DeepLink, min version)
  - Send-type: Document, Image, Text, Camera (lens selectable), Choice panel (upload objects, image templates, grid selectors, dropdown selectors)
  - State-type: Toggle associated with a variable (e.g., enable/disable a feature)
- **Dynamic**: Workflow-driven. Event triggers (HalfScreen/FullScreen) pass `EVENT_INPUT` to workflow; workflow outputs `dynamicDirective[]` (content + query) + `eventInfo`.

**Background image**: Chat background for the agent.

**Character voice**: Select default timbre from available voices. User-side voice switching can be enabled/disabled per agent.

**Plugins**: Tool sets (one plugin = one or more tools/APIs). Types: MCP, Cloud, End-side. Bind cards to plugin outputs. Supports mock sets for testing.

**Workflow config**: Bind main workflow for the agent. Supports text+card mixed output, UI jump config.

**Trigger**: Auto-execute agent on events — supports generic events and Webhook events.

**Associated app** (关联应用): Link agent to HarmonyOS apps via AppGallery Connect. The app must integrate **AgentKit** (Function component). When user taps the component in-app, the agent opens in half-screen mode. Prerequisites: ROM 6.0.0+ / API SDK 20+, Xiaoyi app 11.3.8.300+.

**Account binding** (A2A/Workflow only): Huawei account one-tap auth.
- A2A mode: Toggle switch + APP ID (Client ID from AGC). Requests are sent to the A2A-configured API URL.
- Workflow mode: APP ID + auth service URL + auth method. Auto-attaches system variable `agent_login_session_id` to workflows.
- Flow: User taps superlink → authorization → `agentLoginSessionId` returned → persisted on device → carried in subsequent sessions.
- superlink format: `superlink://vassistant?hwIdAuth=phone&appId={{APP_ID}}&agentId={{agentId}}`
- Only enterprise developers can apply for phone number permission. Requires AGC project + web app creation + sensitive permission application.

**Paid agent** (enterprise only, beta): Digital goods (virtual cards, game items, membership). Requires contacting Xiaoyi commercialization team first.

**Knowledge base**: RAG for agent. Settings: relevance threshold (0-1), max recall segments (0-20), max recall tokens (0-999999), query rewriting (on by default), no-hit reply (default or custom).

**Variables**: User variables (persistent per-user, editable in workflows/plugins) + System variables (read-only: device identifier, language, etc.).

**Long-term memory**: Extracts and stores key info across conversations. Triggers after context window is exhausted. Auto-appended to prompt (can disable for workflow-only use). Viewable/resettable per user.

## Debugging & preview

| Feature | LLM | Workflow | A2A | OpenClaw |
|---|---|---|---|---|
| Device publish test | ✓ | ✓ | ✓ | ✓ |
| Web debug | ✓ | ✓ | ✓ | ✓ |
| Trigger debug | ✓ | — | ✓ | — |
| Memory viewer | ✓ | ✓ | — | — |
| TTS playback | ✓ | ✓ | ✓ | ✓ |

**Device test** (真机测试): Publish to a white-listed device. The agent appears in Xiaoyi app with a "开发中" (in-development) badge. White-listed devices see the dev version even after public publish — remove the whitelist or cancel dev publish to fix.

## Agent Communication Protocol (A2A)

The A2A protocol uses **JSON-RPC 2.0** over HTTP between Agent Client (Xiaoyi app on device) and Agent Server (your cloud backend).

### Message structure
- `kind: "data"` — structured data exchange
- `header.namespace` + `header.name` — message routing
  - `Common / Action` — invoke an action (intent framework, location, etc.)
  - `Command / Deeplink` — navigate to app page
  - `Common / UploadExeResult` — report action execution result back to server
- `method: "authorize"` / `method: "deauthorize"` — account binding (JSON-RPC)

### Key message patterns

**Action command** (server → client, invoke intent framework on device):
```json
{
  "header": { "namespace": "Common", "name": "Action" },
  "payload": {
    "executeParam": {
      "executeMode": "background", // or "foreground"
      "intentName": "SearchNote",
      "intentParam": { "query": "yesterday's" },
      "bundleName": "com.huawei.hmos.notepad",
      "actionResponse": true,
      "actionResponseConfig": { "type": "WHITE", "resultPath": ["result.items.entityId"] }
    },
    "response": [
      { "code": "0", "commandUserInteractionDisplayText": "Found {number} notes." },
      { "code": "1", "commandUserInteractionDisplayText": "No notes found." }
    ]
  }
}
```
Constraint: the intentName and bundleName must match an intent-framework plugin registered in the platform, or the cloud side blocks the request.

**DeepLink command** (server → client, open app page):
```json
{
  "header": { "namespace": "Command", "name": "Deeplink" },
  "payload": {
    "url": "the-deeplink-url",
    "appName": "App name (shows market page if not installed)",
    "packageName": "optional.package.name",
    "appType": "OpenHarmony"
  }
}
```

**Location request** (server → client, get GPS coordinates):
Server issues `Common/Action` with `intentName: "GetCurrentLocation"` and `bundleName: "com.huawei.hmos.aidispatchservice"`. Client reports back via `Common/UploadExeResult` with `latitude` and `longitude` in WGS84.

### Context variables available to Agent Server
When configured in the platform (variable settings toggled on):
- `app_ver` — Xiaoyi app version
- `foreground_apps` — list of foreground apps

### Response data structures (server → client)

**Top-level data**:
| Field | Type | Description |
|---|---|---|
| `kind` | string | Always `"data"` |
| `data.text` | string | Display text (plain or Markdown) |
| `data.commands` | CommandObject[] | Device-side tool invocation commands |
| `data.cardsInfo` | CardDataObject[] | Card template data |
| `data.chipsInfo` | ChipDataObject | Follow-up question chips (max 64 chars per chip) |
| `data.reference` | ReferenceDataObject | Citation/reference cards |

**CardDataObject**: `cardName` (must match A2A output config), `cardData` (array → `items[*]`, object → direct), `displayType` (`EmbedMarkdown` or `DisplayFaCard`).

**ChipDataObject**: Questions in superlink format: `superlink://vassistant?text={{question}}&startmode=recognize`.

**ReferenceDataObject**: Items with `name`, `source`, `card` (type: `leftPictureRightText`, title, subtitle, link with `startMode` 0=in-Xiaoyi / 1=browser).

### Quick command reporting (client → server)
When user taps an agent's bottom quick command:
```json
"userInputInfo": {
  "statusInfo": [{
    "isSelected": true,
    "statusKey": "platform-defined key",
    "statusValue": "platform-defined value"
  }]
}
```

### Authorization flow
1. Client POSTs to agent server with JSON-RPC method `authorize`, carrying `authCode` (obtained from Huawei Account SDK).
2. Server responds with `agentLoginSessionId`.
3. Client persists `agentLoginSessionId` locally and includes it in subsequent requests.
4. Deauthorization: JSON-RPC method `deauthorize` with `agentLoginSessionId` + `cpUserId`.

## Workflow development

Visual canvas with drag-and-drop nodes. Node types:
- **Start** (with system parameter `EVENT_INPUT`)
- **LLM** — invoke a model
- **Plugin** — call a plugin tool
- **Workflow** — nest another workflow (sub-workflow)
- **Code** — execute custom code (JS/Python)
- **Selector** — conditional branching
- **Intent Classification** — route based on intent
- **Output** — format response
- **Loop** / **Batch Processing**
- **Knowledge Base** — RAG retrieval
- **Variable** — read/write variables
- **Long-term Memory**
- **Text Processing**
- **Questioner** — ask user for input mid-flow

Workflow lifecycle: Create → Add nodes → Configure I/O → Test Run (green border on success) → Publish. Exported as JSON (with optional sub-workflow inclusion). Version management: publish archive, system auto-archive, manual archive.

## Plugin development

### MCP plugins
- **Standard registration**: Manual entry of info, tool list auto-fetched from MCP server. Developer self-auth or Huawei unified auth.
- **External platform import**: Import from ModelScope via API key.
- **Publishing channels**: Agent (no review), Xiaoyi Dialog (Huawei review), Plugin Marketplace (Huawei review).
- **Auth**: Self-authenticated plugins expose auth key in plugin description.

### Cloud plugins
- One plugin = multiple tools (APIs). Each tool has input/output parameter schemas.
- **Batch processing**: Request → wait → complete.
- **Stream processing** (WebSocket/SSE): Uses `streamInfo` with frame types `start`, `partial`, `final`.
- **Mock sets**: Return preset data without calling real API. Random single mode or full return mode.

### End-side plugins
- Bridge to HarmonyOS device apps. Must be published on AppGallery Connect first (package name linked).
- **Execution modes**: Foreground (Standard/Applink/Deeplink), Background (returns data for card binding), Card (renders app card).
- **Device-side implementation**: Create `insight_intent.json` in project root defining intents (name, version, srcEntry, execution mode: `uiAbility`/`form`/`uiExtension`/`serviceExtension`). Implement intent handlers in ArkTS.
- **Permission control**: Must declare permission usage descriptions before publishing.

## Card development

Visual drag-and-drop card editor. Two types: Official Cards (platform preset) and My Cards (custom).

- **Create**: Standard (from scratch) or AI-generated (from example image, 10x10~1024x1024 JPG/PNG <5MB)
- **Editor**: Three-panel — components, canvas (with component tree), property config
- **Variables**: String, Number, Array, Object, Object(Aggregated Link), Boolean — bind components to variables
- **Reply templates**: Query plugin/workflow output params, configure card templates
- **Card upgrade**: When a new card version is created, bound configs show "pending update" — parameters are cleared after upgrade
- Component types: text, image, button, list, choice group, multi-tab, map, H5, audio/video

## Knowledge base development

- **Import methods**: Document, Image (with smart annotation), Data Source (API config), Web Crawler (auto-crawl on schedule)
- **Publishing**: Document-type knowledge needs data validation first. If "authorize for knowledge QA" is checked, review takes 1-3 days.
- **Agent binding**: Add knowledge base in agent's orchestration settings

## Interface development (开发界面)

Build custom full-screen or half-screen popup UIs for agents. Drag-and-drop editor similar to cards. Variables: interface input params (optional, with defaults) + custom variables. Interface Skill Association: whitelist plugins/workflows for event calls.

## Timbre development (开发音色)

Enterprise only, max 5 timbres per account. Clone from local recording or uploaded audio (must follow platform-provided script). Used in agent's character voice settings.

## Xiaoyi Compass (小艺罗盘)

One-stop evaluation + monitoring platform:
- **Evaluation (评测)**: Structured evaluation sets (CSV import or manual entry), customizable evaluator prompts with 0.0-1.0 scoring, automated evaluation tasks
- **Observation (观测)**: Operations dashboard with usage metrics

## OpenClaw integration

1. Install OpenClaw on server (not a personal computer).
2. Create OpenClaw-mode agent in platform, get credentials.
3. Run: `openclaw plugins install @ynhcj/xiaoyi@latest`
4. Add Xiaoyi channel config in `/root/.openclaw/openclaw.json`:
   ```json
   { "ak": "your-key", "sk": "your-secret-key", "agentId": "your-agent-id" }
   ```
5. Restart: `openclaw gateway restart`
6. Check: `openclaw logs --follow`

## Digital product payment (enterprise, beta)

For selling digital goods through agents:
- **Product types**: Consumable, Non-consumable, Non-renewing subscription
- **Pricing**: RMB only, China mainland
- **Integration flow**: Enable merchant service → integrate Huawei account login → configure payment triggers (superlink or end-plugin) → configure order notification & rights query APIs → publish products → dev test with mock payment toggle → publish paid agent
- **Order notification API** (IF1): HTTPS POST, RSA3072 signature. Notifies developer to grant/revoke rights.
- **Rights query API** (IF2): HTTPS POST, AK/SK or OAuth 2.0. Returns `privilegeList` with status, expiration.

## AgentKit — in-app agent launcher

HarmonyOS apps can embed a "component icon" that launches an associated agent in half-screen mode:
- **Prerequisites**: App published on AGC with manual signing, agent configured with "Associated App" pointing to that app, app integrated with AgentKit (Function component)
- **Common issues**:
  - "Agent not authorized for this app" → check agent-app association in platform, verify app name/package/appId match, ensure manual signing (not auto-sign)
  - No component icon → AgentKit not integrated, or ROM < 6.0.0 / API SDK < 20
  - Dev agent still showing after publish → remove device from white-list or cancel dev publish

## Publishing & audit

### Pre-publish checklist
- Private cloud/MCP plugins: currently NOT supported for personal developer agent publishing (debug only)
- All checklist items must pass validation

### Audit specifications (11 categories)
1. **Agent info**: Name must be clear/functional (Chinese only, no special chars, no superlatives). Avatar must be copyright-owned, no watermarks/QR codes. Description ≤50 chars.
2. **Agent security**: No viruses, trojans, data theft, crypto mining, ad fraud.
3. **Agent function**: Must have practical value. No pure redirects, no forced downloads.
4. **Agent content**: No illegal/pornographic/violent/gambling content. AI-generated content must be labeled. **No anthropomorphic agents** (per national regulations).
5. **User privacy**: Privacy policy required. Data minimization. Sensitive data (calls, SMS, biometrics, health, location) cannot be used for ads.
6. **Minor protection**: Content suitable for minors. No addiction features.
7. **Intellectual property**: Must own all content rights. No Huawei impersonation.
8. **Agent qualifications**: Generative AI service filing number required if using LLM. 3-month grace period.
9. **Developer behavior**: Truthful registration. Government agents need official authorization.
10. **AI labeling & LLM filing FAQ**: How to obtain CAC filing numbers.
11. **Appendix**: Business-specific qualifications (securities, banking, medical, news, ride-hailing, legal, recruitment, etc.).

### Audit process
- Submit via agent editor [上架] button or Workspace → Agent list → operations
- Review cycle: 1-3 business days
- Team accounts: only team admin can publish/take-down
- Rejection reason visible in version history or status tag hover

## Key URLs

- Xiaoyi Open Platform: `https://developer.huawei.com/consumer/cn/doc/service/`
- Agent protocol details: `https://developer.huawei.com/consumer/cn/doc/service/agent2agent-0000002498656261`
- Intent framework: `https://developer.huawei.com/consumer/cn/doc/service/intents-kit-0000001677103865`
- Intelligent agent white paper: `https://developer.huawei.com/consumer/cn/doc/service/intelligent-agent-white-paper-0000002508129114`
- AI terminal white paper: `https://developer.huawei.com/consumer/cn/doc/service/ai-terminal-white-paper-0000001929691644`
- Terms of service: `https://developer.huawei.com/consumer/cn/doc/service/terms_conditions-0000001193795972`
