# @security/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-rsa-key_

该规则禁止使用不安全的RSA密钥，如RSA模数长度小于2048bit。推荐使用Petal Aegis SDK中的安全RSA签名接口，详情参见：RSA密钥。

规则配置
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-rsa-key": "error"
  }
}
选项

该规则无需配置额外选项。

正例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('RSA3072|PRIMES_2');
反例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createAsyKeyGenerator('RSA512|PRIMES_2');
规则集
plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@security/no-unsafe-rsa-encrypt
@security/no-unsafe-rsa-sign
