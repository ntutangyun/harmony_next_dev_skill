# @security/no-unsafe-dh

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-dh_

该规则禁止使用不安全的DH密钥协商算法，如DH模数长度小于2048bit。

规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dh": "error"
  }
}

选项

该规则无需配置额外选项。

正例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp3072');

反例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp1536');

规则集

plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-dh": "error"
  }
}
```

### Code block 2

```
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp3072');
```

### Code block 3

```
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKeyAgreement('DH_modp1536');
```

### Code block 4

```
plugin:@security/recommended
plugin:@security/all
```
