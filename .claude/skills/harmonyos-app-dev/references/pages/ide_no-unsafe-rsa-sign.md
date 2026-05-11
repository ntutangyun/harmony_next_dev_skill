# @security/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-rsa-sign_

该规则禁止不安全的RSA签名算法，如RSA模数长度小于2048bit、摘要或掩码摘要中使用不安全的MD5或SHA1哈希算法。推荐使用Petal Aegis SDK中的安全RSA签名接口，详情参见： RSA加解密。

规则配置
// code-linter.json5
{
  "rules": {
    "@security/no-unsafe-rsa-sign": "error"
  }
}
选项

该规则无需配置额外选项。

正例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('RSA3072|PSS|SHA256|MGF1_SHA256');
cryptoFramework.createVerify('RSA3072|PSS|SHA256|MGF1_SHA256');
反例
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createSign('RSA512|PKCS1|MD5');
cryptoFramework.createVerify('RSA512|PKCS1|MD5');
规则集
plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@security/no-unsafe-rsa-key
@security/no-unsafe-3des
