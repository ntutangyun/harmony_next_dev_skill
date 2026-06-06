# 验证签名

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-taas-verifysignature_

--BEGIN CERTIFICATE-----');
const thirdCert = '-----BEGIN CERTIFICATE-----' + certList[1];
// 获取公钥
const textEncoder = new util.TextEncoder();
const encodingBlob: cert.EncodingBlob = {
  data: textEncoder.encodeInto(thirdCert),
  encodingFormat: cert.EncodingFormat.FORMAT_PEM
};
const x509Cert = await cert.createX509Cert(encodingBlob);
const asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('ECC256');
const keyPair = asyKeyGenerator.convertKeySync(x509Cert.getPublicKey().getEncoded(), null);
const pubKey = keyPair.pubKey; // 证书中的公钥需要转换成cryptoFramework能够接收的格式

创建非对称密钥类型为ECC256、摘要算法为SHA256的verify实例，并使用步骤1中获取到的公钥进行初始化。

const verifier = cryptoFramework.createVerify('ECC256|SHA256');
verifier.initSync(pubKey);

使用原始数据和签名结果进行验证签名。

const originData = ...; // 请使用获取到的安全图像原始数据
const signatureData = ...; // 请使用获取到的签名结果
const inputData: cryptoFramework.DataBlob = {
  data: new Uint8Array(originData)
};
const signature: cryptoFramework.DataBlob = {
  data: new Uint8Array(signatureData)
};
// 验证签名结果
const result = verifier.verifySync(inputData, signature);
验证匿名证书链
数字盾服务
