# @security/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-dsa_

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('DSA3072|SHA256');
cryptoFramework.createVerify('DSA3072|SHA256');
反例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('DSA1024|SHA256');
cryptoFramework.createVerify('DSA1024|SHA256');
规则集
plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@security/no-unsafe-dh
@security/no-unsafe-dh-key
