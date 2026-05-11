# Session间缓存共享

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-cache-shared_

创建ResponseCache实例。其中，pathToFolder即缓存记录文件路径，'/path/dir'请根据实际情况替换为想要存储HTTP缓存的沙箱路径。

const responseCache = new rcp.ResponseCache({
  persistent: {
    kind: 'file-system',
    pathToFolder: '/path/dir' // 请根据自身业务选择合适的路径
  }
});

创建SessionA和SessionB。配置responseCache实例到SessionA和SessionB中。

const sessionA: rcp.Session = rcp.createSession({
  requestConfiguration: {
    cache: responseCache
  }
});
const sessionB: rcp.Session = rcp.createSession({
  requestConfiguration: {
    cache: responseCache
  }
});

由SessionA发起第一次请求。'https://www.example.com'请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会从网络服务器获取数据，此时可查看缓存状态信息，此时缓存条数应当为1。

const responseA = await sessionA.get('https://www.example.com');
console.info(`Request succeeded, message is ${JSON.stringify(responseA)}`);
let cacheState = await responseCache.getState();
console.info(`The current number of cache entries is: ${cacheState.count}`);

由SessionB发起第二次请求。'https://www.example.com'请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会直接从缓存中获取响应，此时可查看缓存状态信息，此时缓存命中数应当为1。

const responseB = await sessionB.get('https://www.example.com');
console.info(`Request succeeded, message is ${JSON.stringify(responseB)}`);
cacheState = await responseCache.getState();
console.info(`The current cache hit count is: ${cacheState.hitCount}`);
配置相同缓存存储路径

创建不同的ResponseCache实例，但对应缓存存储路径相同，将ResponseCache实例配置到不同Session中，可以在Session间共享缓存数据。

导入模块。

import { rcp } from '@kit.RemoteCommunicationKit';

创建ResponseCacheA和ResponseCacheB实例，两者对应缓存存储路径相同。其中，pathToFolder即HTTP缓存响应记录文件路径，'/path/dir'请根据实际情况替换为想要存储HTTP缓存的沙箱路径。

const responseCacheA = new rcp.ResponseCache({
  persistent: {
    kind: 'file-system',
    pathToFolder: '/path/dir' // 请根据自身业务选择合适的路径
  }
});
const responseCacheB = new rcp.ResponseCache({
  persistent: {
    kind: 'file-system',
    pathToFolder: '/path/dir' // 请根据自身业务选择合适的路径
  }
});

创建SessionA和SessionB。配置responseCacheA实例到SessionA，配置responseCacheB实例到SessionB中。

const sessionA: rcp.Session = rcp.createSession({
  requestConfiguration: {
    cache: responseCacheA
  }
});
const sessionB: rcp.Session = rcp.createSession({
  requestConfiguration: {
    cache: responseCacheB
  }
});

由SessionA发起第一次请求。'https://www.example.com'请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会从网络服务器获取数据，此时可查看responseCacheA的缓存状态信息，此时缓存条数应当为1。

const responseA = await sessionA.get('https://www.example.com');
console.info(`Request succeeded, message is ${JSON.stringify(responseA)}`);
let cacheState = await responseCacheA.getState();
console.info(`The current number of cache entries is: ${cacheState.count}`);

由SessionB发起第二次请求。'https://www.example.com'请根据实际情况替换为支持HTTP缓存协议的URL。本次请求将会直接从缓存中获取响应，此时可查看responseCacheB的缓存状态信息，此时缓存条数和缓存命中数均应当为1。

const responseB = await sessionB.get('https://www.example.com');
console.info(`Request succeeded, message is ${JSON.stringify(responseB)}`);
cacheState = await responseCacheB.getState();
console.info(`The current number of cache entries is: ${cacheState.count}`);
console.info(`The current cache hit count is: ${cacheState.hitCount}`);
HTTP缓存基本功能
自定义缓存拦截器
