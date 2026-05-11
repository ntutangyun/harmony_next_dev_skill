# @security/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-sm2-cipher_

此规则禁止在SM2算法中使用不安全的消息摘要算法MD5和SHA1。推荐使用SM2_256|SHA256算法和RSA算法，算法详情参见：非对称加解密算法和非对称密钥加解密算法规格。

规则配置
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-sm2-cipher": "warn"
  }
}
选项

该规则无需配置额外选项。

正例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM2_256|SHA256')
反例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createCipher('SM2_256|SHA1')
cryptoFramework.createCipher('SM2_256|MD5')
规则集
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@security/no-unsafe-sm2-key
@security/no-unsafe-ecdh
