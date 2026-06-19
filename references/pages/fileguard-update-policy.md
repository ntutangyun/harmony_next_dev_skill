# 更新安全管控策略

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-update-policy_

场景介绍

Enterprise Data Guard Kit为应用提供下发管控策略的能力，相关策略会被分发到HarmonyOS系统中执行。

接口说明

详细接口说明可参考接口文档。

接口名	描述
updatePolicy(policy: string, callback: AsyncCallback<void>): void	使用Callback方式更新安全管控策略。
updatePolicy(policy: string): Promise<void>	使用Promise方式更新安全管控策略。
getPolicy(): Promise<string | null>	使用Promise方式获取当前设备生效的管控策略内容。

开发步骤

导入模块。

import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';

初始化FileGuard对象guard，调用接口updatePolicy，更新安全管控策略。

通过回调函数方式，更新安全管控策略。

function updatePolicyCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: string = '{' +
    '"net_intercept_toggle":1,' +
    '"default_policy":1,' +
    '"net_reject_cache_time":30,' +
    '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '"netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '"netsegment_blocklist":["172.16.0.0-172.31.255.255","192.168.0.0-192.168.255.255"],' +
    '"netsegment_update_type": 0,' +
    '"usb_intercept_toggle":1,' +
    '"smb_client_intercept_toggle":1,' +
    '"smb_server_intercept_toggle":1,' +
    '"new_file_audit_toggle":1,' +
    '"kia_variant_toggle":1,' +
    '"audit_filter_toggle":1,' +
    '"print_intercept_toggle":0,' +
    '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '"bluetooth_intercept_time":30,' +
    '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '"nearlink_intercept_time":30,' +
    '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
    '"kia_file_access_toggle":0,' +
    '"Tag1":{' +
    '   "tag":"sensitive",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["192.168.0.0-192.168.255.255"]' +
    '  }' +
    '}';
  guard.updatePolicy(policy, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
    } else {
      console.info(`Succeeded in updating policy.`);
    }
  });
}

通过Promise方式，更新安全管控策略。

function updatePolicyPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: string = '{' +
    '"net_intercept_toggle":1,' +
    '"default_policy":1,' +
    '"net_reject_cache_time":30,' +
    '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '"netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '"netsegment_blocklist":["172.16.0.0-172.31.255.255","192.168.0.0-192.168.255.255"],' +
    '"netsegment_update_type": 0,' +
    '"usb_intercept_toggle":1,' +
    '"smb_client_intercept_toggle":1,' +
    '"smb_server_intercept_toggle":1,' +
    '"new_file_audit_toggle":1,' +
    '"kia_variant_toggle":1,' +
    '"audit_filter_toggle":1,' +
    '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '"bluetooth_intercept_time":30,' +
    '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '"nearlink_intercept_time":30,' +
    '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
    '"Tag1":{' +
    '   "tag":"sensitive",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["192.168.0.0-192.168.255.255"]' +
    '  }' +
    '}';
  guard.updatePolicy(policy).then(() => {
    console.info(`Succeeded in updating policy.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
  });
}

初始化FileGuard对象guard，调用接口getPolicy，获取当前设备生效的管控策略内容。

function getPolicyPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  guard.getPolicy().then((policy: string | null) => {
    if (policy === null) {
      console.info(`The obtained policy is null.`);
      return;
    }
    console.info(`Succeeded in getting policy. policy length: ${policy.length}`);
    // 返回字符串较长，分次打印
    let len: number = 2000; // 每次打印2000字符
    let totalLen: number = policy.length;
    for (let i: number = 0; i < totalLen; i += len) {
      let end: number = Math.min(i + len, totalLen);
      let item: string = policy.substring(i, end);
      console.info(`policy: ${item}`);
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get policy. Code: ${err.code}, message: ${err.message}.`);
  });
}

## Code blocks

### Code block 1

```
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
function updatePolicyCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: string = '{' +
    '"net_intercept_toggle":1,' +
    '"default_policy":1,' +
    '"net_reject_cache_time":30,' +
    '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '"netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '"netsegment_blocklist":["172.16.0.0-172.31.255.255","192.168.0.0-192.168.255.255"],' +
    '"netsegment_update_type": 0,' +
    '"usb_intercept_toggle":1,' +
    '"smb_client_intercept_toggle":1,' +
    '"smb_server_intercept_toggle":1,' +
    '"new_file_audit_toggle":1,' +
    '"kia_variant_toggle":1,' +
    '"audit_filter_toggle":1,' +
    '"print_intercept_toggle":0,' +
    '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '"bluetooth_intercept_time":30,' +
    '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '"nearlink_intercept_time":30,' +
    '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
    '"kia_file_access_toggle":0,' +
    '"Tag1":{' +
    '   "tag":"sensitive",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["192.168.0.0-192.168.255.255"]' +
    '  }' +
    '}';
  guard.updatePolicy(policy, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
    } else {
      console.info(`Succeeded in updating policy.`);
    }
  });
}
```

### Code block 3

```
function updatePolicyPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: string = '{' +
    '"net_intercept_toggle":1,' +
    '"default_policy":1,' +
    '"net_reject_cache_time":30,' +
    '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '"netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '"netsegment_blocklist":["172.16.0.0-172.31.255.255","192.168.0.0-192.168.255.255"],' +
    '"netsegment_update_type": 0,' +
    '"usb_intercept_toggle":1,' +
    '"smb_client_intercept_toggle":1,' +
    '"smb_server_intercept_toggle":1,' +
    '"new_file_audit_toggle":1,' +
    '"kia_variant_toggle":1,' +
    '"audit_filter_toggle":1,' +
    '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '"bluetooth_intercept_time":30,' +
    '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '"nearlink_intercept_time":30,' +
    '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
    '"Tag1":{' +
    '   "tag":"sensitive",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_trustlist":["10.0.0.0-10.255.255.255"],' +
    '   "netsegment_blocklist":["192.168.0.0-192.168.255.255"]' +
    '  }' +
    '}';
  guard.updatePolicy(policy).then(() => {
    console.info(`Succeeded in updating policy.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### Code block 4

```
function getPolicyPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  guard.getPolicy().then((policy: string | null) => {
    if (policy === null) {
      console.info(`The obtained policy is null.`);
      return;
    }
    console.info(`Succeeded in getting policy. policy length: ${policy.length}`);
    // 返回字符串较长，分次打印
    let len: number = 2000; // 每次打印2000字符
    let totalLen: number = policy.length;
    for (let i: number = 0; i < totalLen; i += len) {
      let end: number = Math.min(i + len, totalLen);
      let item: string = policy.substring(i, end);
      console.info(`policy: ${item}`);
    }
  }).catch((err: BusinessError) => {
    console.error(`Failed to get policy. Code: ${err.code}, message: ${err.message}.`);
  });
}
```
