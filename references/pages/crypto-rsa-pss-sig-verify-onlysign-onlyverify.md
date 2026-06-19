# 使用RSA密钥对（PSS模式）签名验签（OnlySign和OnlyVerify模式）(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-pss-sig-verify-onlysign-onlyverify_

从API版本26.0.0开始，签名验签支持OnlySign/OnlyVerify模式。对应的算法规格请查看签名验签算法规格：RSA。

签名

调用cryptoFramework.createMd，指定摘要算法SHA256，生成摘要实例（Md）。

调用Md.update，传入自定义消息，进行摘要更新计算。单次update长度没有限制。

调用Md.digest，获取摘要计算结果。

调用cryptoFramework.createAsyKeyGenerator、AsyKeyGenerator.generateKeyPair，生成密钥算法为RSA、密钥长度为1024位、素数个数为2的非对称密钥对象（KeyPair），包括公钥（PubKey）和私钥（PriKey）。

如何生成RSA非对称密钥，开发者可参考下文示例，并结合非对称密钥生成和转换规格：RSA和随机生成非对称密钥对理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

调用cryptoFramework.createSign，指定字符串参数'RSA|PSS|SHA256|MGF1_SHA256|OnlySign'，创建非对称密钥类型为不带长度的RSA、填充模式为PSS、摘要算法为SHA256、掩码算法为MGF1_SHA256，签名模式为OnlySign的Sign实例，用于完成签名操作。

调用Sign.init，使用私钥（PriKey）初始化Sign实例。

调用Sign.sign，生成摘要数据签名。

验签

调用cryptoFramework.createVerify，指定字符串参数'RSA|PSS|SHA256|MGF1_SHA256|OnlyVerify'，创建非对称密钥类型为RSA、填充模式为PSS、摘要算法为SHA256、掩码算法为MGF1_SHA256，验签模式为OnlyVerify的Verify实例，用于完成验签操作。

调用Verify.init，使用公钥（PubKey）初始化Verify实例。

调用Verify.verify，对摘要数据进行验签。

异步方法示例：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function signMessagePromise(priKey: cryptoFramework.PriKey, digestBlob: cryptoFramework.DataBlob) {
  let signAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlySign';
  let signer = cryptoFramework.createSign(signAlg);
  await signer.init(priKey);
  let signData = await signer.sign(digestBlob);
  return signData;
}

async function verifyMessagePromise(digestBlob: cryptoFramework.DataBlob, signMessageBlob: cryptoFramework.DataBlob,
  pubKey: cryptoFramework.PubKey) {
  let verifyAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlyVerify';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  await verifier.init(pubKey);
  let res = await verifier.verify(digestBlob, signMessageBlob);
  console.info('verify result: ' + res);
  return res;
}

async function main() {
  let messageData: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is rsa onlySign test', 'utf-8').buffer) };
  // 先使用 Md 计算 SHA256 摘要（32字节）
  let md = cryptoFramework.createMd('SHA256');
  await md.update(messageData);
  let digestBlob = await md.digest();
  let keyGenAlg = 'RSA1024';
  let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  let keyPair = await generator.generateKeyPair();
  let signData = await signMessagePromise(keyPair.priKey, digestBlob);
  let verifyResult = await verifyMessagePromise(digestBlob, signData, keyPair.pubKey);
  if (verifyResult === true) {
    console.info('verify result: success.');
  } else {
    console.error('verify result: failed.');
  }
}

同步方法示例：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function signMessagePromise(priKey: cryptoFramework.PriKey, digestBlob: cryptoFramework.DataBlob) {
  let signAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlySign';
  let signer = cryptoFramework.createSign(signAlg);
  signer.initSync(priKey);
  let signData = signer.signSync(digestBlob);
  return signData;
}

function verifyMessagePromise(digestBlob: cryptoFramework.DataBlob, signMessageBlob: cryptoFramework.DataBlob,
  pubKey: cryptoFramework.PubKey) {
  let verifyAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlyVerify';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  verifier.initSync(pubKey);
  let res = verifier.verifySync(digestBlob, signMessageBlob);
  console.info('verify result: ' + res);
  return res;
}

function main() {
  let messageData: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is rsa onlySign test', 'utf-8').buffer) };
  // 先使用 Md 计算 SHA256 摘要（32字节）
  let md = cryptoFramework.createMd('SHA256');
  md.updateSync(messageData);
  let digestBlob = md.digestSync();
  let keyGenAlg = 'RSA1024';
  let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  let keyPair = generator.generateKeyPairSync();
  let signData = signMessagePromise(keyPair.priKey, digestBlob);
  let verifyResult = verifyMessagePromise(digestBlob, signData, keyPair.pubKey);
  if (verifyResult === true) {
    console.info('verify result: success.');
  } else {
    console.error('verify result: failed.');
  }
}

## Code blocks

### Code block 1

```
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

async function signMessagePromise(priKey: cryptoFramework.PriKey, digestBlob: cryptoFramework.DataBlob) {
  let signAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlySign';
  let signer = cryptoFramework.createSign(signAlg);
  await signer.init(priKey);
  let signData = await signer.sign(digestBlob);
  return signData;
}

async function verifyMessagePromise(digestBlob: cryptoFramework.DataBlob, signMessageBlob: cryptoFramework.DataBlob,
  pubKey: cryptoFramework.PubKey) {
  let verifyAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlyVerify';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  await verifier.init(pubKey);
  let res = await verifier.verify(digestBlob, signMessageBlob);
  console.info('verify result: ' + res);
  return res;
}

async function main() {
  let messageData: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is rsa onlySign test', 'utf-8').buffer) };
  // 先使用 Md 计算 SHA256 摘要（32字节）
  let md = cryptoFramework.createMd('SHA256');
  await md.update(messageData);
  let digestBlob = await md.digest();
  let keyGenAlg = 'RSA1024';
  let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  let keyPair = await generator.generateKeyPair();
  let signData = await signMessagePromise(keyPair.priKey, digestBlob);
  let verifyResult = await verifyMessagePromise(digestBlob, signData, keyPair.pubKey);
  if (verifyResult === true) {
    console.info('verify result: success.');
  } else {
    console.error('verify result: failed.');
  }
}
```

### Code block 2

```
import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';

function signMessagePromise(priKey: cryptoFramework.PriKey, digestBlob: cryptoFramework.DataBlob) {
  let signAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlySign';
  let signer = cryptoFramework.createSign(signAlg);
  signer.initSync(priKey);
  let signData = signer.signSync(digestBlob);
  return signData;
}

function verifyMessagePromise(digestBlob: cryptoFramework.DataBlob, signMessageBlob: cryptoFramework.DataBlob,
  pubKey: cryptoFramework.PubKey) {
  let verifyAlg = 'RSA|PSS|SHA256|MGF1_SHA256|OnlyVerify';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  verifier.initSync(pubKey);
  let res = verifier.verifySync(digestBlob, signMessageBlob);
  console.info('verify result: ' + res);
  return res;
}

function main() {
  let messageData: cryptoFramework.DataBlob =
    { data: new Uint8Array(buffer.from('This is rsa onlySign test', 'utf-8').buffer) };
  // 先使用 Md 计算 SHA256 摘要（32字节）
  let md = cryptoFramework.createMd('SHA256');
  md.updateSync(messageData);
  let digestBlob = md.digestSync();
  let keyGenAlg = 'RSA1024';
  let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  let keyPair = generator.generateKeyPairSync();
  let signData = signMessagePromise(keyPair.priKey, digestBlob);
  let verifyResult = verifyMessagePromise(digestBlob, signData, keyPair.pubKey);
  if (verifyResult === true) {
    console.info('verify result: success.');
  } else {
    console.error('verify result: failed.');
  }
}
```
