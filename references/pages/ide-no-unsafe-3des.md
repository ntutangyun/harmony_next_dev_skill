# @security/no-unsafe-3des

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-no-unsafe-3des_

该规则禁止使用不安全的3DES加密模式，例如3DES|ECB。建议使用安全的3DES加密模式，例如3DES|CBC。详情参考3DES加密模式。

规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-3des": "error"
  }
}

选项

该规则无需配置额外选项。

正例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('3DES|CBC');

反例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('3DES|ECB');

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
    "@security/no-unsafe-3des": "error"
  }
}
```

### Code block 2

```
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('3DES|CBC');
```

### Code block 3

```
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('3DES|ECB');
```

### Code block 4

```
plugin:@security/recommended
plugin:@security/all
```
