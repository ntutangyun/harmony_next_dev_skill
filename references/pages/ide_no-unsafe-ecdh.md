# @security/no-unsafe-ecdh

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-ecdh_

此规则禁止使用不安全的非对称密钥类型ECC。推荐使用ECC256算法，详情参见：密钥生成算法。

规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-ecdh": "warn"
  }
}

选项

该规则无需配置额外选项。

正例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC256');

反例

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC');

规则集

plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-ecdh": "warn"
  }
}
```

### Code block 2

```
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC256');
```

### Code block 3

```
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('ECC');
```

### Code block 4

```
plugin:@security/all
```
