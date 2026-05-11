# @security/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-dh_

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp3072');
反例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp1536');
规则集
plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@security/no-unsafe-aes
@security/no-unsafe-dsa
