# @correctness/listen

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_listen-default-network-change_

// With the ohos.permission.GET_NETWORK_INFO permission configured
import connection from '@ohos.net.connection';
export function test() {
  const defaultNet = connection.getDefaultNetSync();
  const netCapabilities = connection.getNetCapabilitiesSync(defaultNet);
  let bearerTypes = netCapabilities.bearerTypes;
  const netConnection = connection.createNetConnection();
  netConnection.on('netCapabilitiesChange', (netCap: connection.NetCapabilityInfo) => {
    const newBearTypes = netCap.netCap.bearerTypes;
    if (newBearTypes !== bearerTypes) {
      bearerTypes = newBearTypes;
    }
  });
}
反例
// With the ohos.permission.GET_NETWORK_INFO permission configured
// import connection from '@ohos.net.connection';
// The `on(type: 'netCapabilitiesChange', callback: Callback<connection.NetCapabilityInfo>)`, `getDefaultNet`/`getDefaultNetSync` and `getNetCapabilities`/`getNetCapabilitiesSync` functions are not called.
规则集
plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@correctness/image-interpolation-check
@correctness/listen-multi-network-concurrent
