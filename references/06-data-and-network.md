# Data persistence & networking

Source pages:
- app-file-overview, app-file-access
- data-persistence-by-preferences, data-persistence-by-kv-store, data-persistence-by-rdb-store
- http-request, net-connection-manager, websocket-connection

## App file sandbox

Each app runs in a sandboxed file space. Use `Context` (UIAbility's `this.context`) to access directories:

| Path | Backed by |
|---|---|
| `ctx.filesDir` | App-private data, retained across uninstalls only if EL1+backup |
| `ctx.cacheDir` | Cacheable — system may purge under pressure |
| `ctx.tempDir` | Process-lifetime tmp files |
| `ctx.bundleCodeDir` | The HAP install dir (read-only) |
| `ctx.preferencesDir` | Backing dir for `Preferences` API |
| `ctx.databaseDir` | Backing dir for relational/KV stores |
| `ctx.distributedFilesDir` | Cross-device file area (Distributed File Manager) |
| `ctx.resourceDir` | Module's resource dir |
| `ctx.area` | `EL1` (always available) / `EL2` (after unlock, default for user data) |

## File IO with `@kit.CoreFileKit`

```typescript
import { fileIo, fs } from '@kit.CoreFileKit';

// Sync open & write
const path = `${this.context.filesDir}/log.txt`;
const file = fileIo.openSync(path, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
fileIo.writeSync(file.fd, 'hello\n');
fileIo.closeSync(file);

// Async API mirrors with `.open`, `.read`, `.write`, `.close` returning Promises.

// Stat / listing / mkdir / rm
const meta = fileIo.statSync(path);
fileIo.mkdirSync(`${this.context.filesDir}/sub`);
const entries = fileIo.listFileSync(this.context.filesDir);
fileIo.unlinkSync(path);
```

For copying / moving / streaming: `fs.copyFile`, `fs.moveFile`, `streamSync`, `Stream.read/write`. Watcher: `fs.createWatcher(path, events, cb)`.

For accessing user-selected files (Documents, Downloads, etc.) outside the sandbox, use `FilePicker` from `@kit.CoreFileKit`:

```typescript
import { picker } from '@kit.CoreFileKit';
const docPicker = new picker.DocumentViewPicker();
const uris = await docPicker.select({ maxSelectNumber: 1 });
```

## Preferences (lightweight KV)

`@kit.ArkData` provides `preferences` — small, synchronous, in-process key/value cache backed by disk:

```typescript
import { preferences } from '@kit.ArkData';

const store: preferences.Preferences = await preferences.getPreferences(this.context, 'settings');
await store.put('userId', 'abc');
const userId: preferences.ValueType = await store.get('userId', '');
await store.flush();   // persist
```

Keys are strings, values are primitives / arrays / `Uint8Array`. Single-process only — for cross-process use KV store.

## KV store

Distributed-capable key/value DB. Use when:
- You want data shared between devices (same Huawei account, Trusted Device list).
- Cross-process within the app.

```typescript
import { distributedKVStore } from '@kit.ArkData';

const mgr = distributedKVStore.createKVManager({ context: this.context, bundleName: 'com.example.myapp' });
const options: distributedKVStore.Options = {
  createIfMissing: true,
  encrypt: false,
  backup: false,
  autoSync: true,                                     // sync across user's devices
  kvStoreType: distributedKVStore.KVStoreType.SINGLE_VERSION,
  securityLevel: distributedKVStore.SecurityLevel.S1
};
const kv = await mgr.getKVStore<distributedKVStore.SingleKVStore>('appKv', options);

await kv.put('lastSeen', Date.now());
const value = await kv.get('lastSeen');
```

Listen for sync updates: `kv.on('dataChange', SubscribeType.SUBSCRIBE_TYPE_REMOTE, cb)`.

## Relational DB (RDB)

SQL-backed structured store via `@kit.ArkData`:

```typescript
import { relationalStore } from '@kit.ArkData';

const config: relationalStore.StoreConfig = {
  name: 'mydata.db',
  securityLevel: relationalStore.SecurityLevel.S1,
  encrypt: false
};

const store: relationalStore.RdbStore = await relationalStore.getRdbStore(this.context, config);

await store.executeSql(`CREATE TABLE IF NOT EXISTS items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  created INTEGER NOT NULL
)`);

await store.insert('items', { title: 'Buy milk', created: Date.now() });

const predicates = new relationalStore.RdbPredicates('items');
predicates.equalTo('title', 'Buy milk');
const rs: relationalStore.ResultSet = await store.query(predicates, ['id', 'title']);
while (rs.goToNextRow()) {
  const row = { id: rs.getLong(0), title: rs.getString(1) };
}
rs.close();
```

Migrations: pass `version` in StoreConfig and use `relationalStore.RdbOpenCallback` (older API) or set up scripts. Distributed table API exists too: `setDistributedTables`, then `sync`.

## HTTP

```typescript
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

const req: http.HttpRequest = http.createHttp();
try {
  const res = await req.request('https://api.example.com/items', {
    method: http.RequestMethod.GET,
    header: { 'content-type': 'application/json' },
    expectDataType: http.HttpDataType.STRING,
    readTimeout: 60_000,
    connectTimeout: 60_000
  });
  console.log(`status=${res.responseCode}`);
  console.log(String(res.result));
} catch (e) {
  const err = e as BusinessError;
  console.error(`http err ${err.code} ${err.message}`);
} finally {
  req.destroy();
}
```

- One `HttpRequest` = one in-flight call. Don't reuse.
- For streaming downloads / progress: `req.on('headersReceive', cb)`, `req.on('dataReceive', cb)`, `req.on('dataEnd', cb)`.
- Built-in cookie/cache support: `http.HttpRequestOptions.usingCache`, `caPath`.
- Interceptor API (`http.HttpInterceptorChain`, `http.HttpInterceptor`) for cross-cutting logic.
- For server certificate pinning: `network-security-config` JSON in `resources/base/profile/`, then point `module.json5` to it.

Permission: declare `ohos.permission.INTERNET` in `module.json5.requestPermissions` (system_grant — always granted but required).

For large file upload/download with progress, prefer `@kit.BasicServicesKit` → `request.uploadFile` / `request.downloadFile` (built on the system's BackgroundTransfer service).

## WebSocket

```typescript
import { webSocket } from '@kit.NetworkKit';

const ws = webSocket.createWebSocket();
ws.on('open', () => { ws.send('hello'); });
ws.on('message', (err, msg) => { console.log(String(msg)); });
ws.on('close', (err, info) => {});
ws.on('error', (err) => {});
await ws.connect('wss://echo.example.com');
// ws.send('payload') — string or ArrayBuffer
// ws.close({ code: 1000, reason: 'bye' })
```

## Network connection state

Use `@kit.NetworkKit` `connection`:

```typescript
import { connection } from '@kit.NetworkKit';

const netState = await connection.getDefaultNet();
const cap = await connection.getNetCapabilities(netState);
// listen
const handle = connection.createNetConnection();
handle.on('netAvailable', (net) => {});
handle.on('netCapabilitiesChange', ({ net, netCap }) => {});
handle.on('netLost', (net) => {});
handle.register();
// later: handle.unregister();
```

For DNS resolution: `connection.getAddressesByName(host)`. For binding to a specific network (cellular vs Wi-Fi): `connection.setAppNet(net)`.

### Network acceleration (多网并发 / Network Boost Kit)

For network quality awareness, prediction, and multi-network concurrency (网络加速), use `@kit.NetworkBoostKit` (`netQuality`). Apps can report QoE (`netQuality` / appReportQoE) and react to handover callbacks for smoother switches between networks. See `pages/networkboost-introduction.md`, `pages/networkboost-appreportqoe.md`, `pages/networkboost-nethandoverguide.md`.

## What this doesn't cover

- Cloud-side storage / CloudDB sync — see Cloud Foundation Kit overview in `references/10-kits-catalog.md`.
- File sharing across apps (URI permissions) — see `app-file-access` source page.
- Bluetooth / NFC IO — see `@kit.ConnectivityKit` (visit canonical docs).
