# @security/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-sm4_

此规则禁止不安全的SM4算法，如加密模式ECB。推荐使用SM4_CBC_PKCS5Padding等不同算法，详情参见：对称加解密算法。

规则配置
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm4": "warn"
  }
}
选项

该规则无需配置额外选项。

正例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createKdf('SM4_128|CBC|PKCS7')
反例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM4_128|ECB|PKCS7')
规则集
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@security/no-unsafe-kdf
@security/no-unsafe-sm2-key
