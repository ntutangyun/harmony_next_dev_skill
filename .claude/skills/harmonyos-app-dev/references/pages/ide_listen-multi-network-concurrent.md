# @correctness/listen

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_listen-multi-network-concurrent_

"@correctness/listen-multi-network-concurrent": "suggestion"
  }
}
选项

该规则无需配置额外选项。

正例
// With the ohos.permission.GET_NETWORK_INFO permission configured
import { netHandover } from '@kit.NetworkBoostKit';
import { BusinessError } from '@kit.BasicServicesKit';
try {
  netHandover.on('handoverChange', (info: netHandover.HandoverInfo) => {
    if (info.handoverStart) {
      console.info('handover start');
    } else if (info.handoverComplete) {
      console.info('handover complete');
    }
  });
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
try {
  netHandover.off('handoverChange');
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
反例
// With the ohos.permission.GET_NETWORK_INFO permission configured
// The `on(type: 'handoverChange', callback: Callback<HandoverInfo>)` function is not called.
规则集
plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@correctness/listen-default-network-change
@correctness/multimedia-use-stride-in-image-receiver
