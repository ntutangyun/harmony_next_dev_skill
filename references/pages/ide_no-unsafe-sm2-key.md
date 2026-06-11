# @security/no-unsafe-sm2-key

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-sm2-key_

此规则禁止不安全的非对称密钥类型SM2算法。推荐使用SM2_256|SHA256算法和RSA算法，算法详情参见：非对称加解密算法和非对称密钥加解密算法规格。

规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm2-key": "warn"
  }
}

选项

该规则无需配置额外选项。

正例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('SM2_256|SHA256')

反例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('SM2|SHA256')

规则集

plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm2-key": "warn"
  }
}
```

### Code block 2

```
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('SM2_256|SHA256')
```

### Code block 3

```
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('SM2|SHA256')
```

### Code block 4

```
plugin:@security/all
```
