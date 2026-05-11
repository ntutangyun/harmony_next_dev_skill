# @security/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-ecdh_

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC256');
反例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC');
规则集
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@security/no-unsafe-sm2-cipher
@security/no-unsafe-huks
