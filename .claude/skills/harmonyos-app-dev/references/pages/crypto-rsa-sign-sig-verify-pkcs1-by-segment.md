# 使用RSA密钥对分段签名验签（PKCS1模式）(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-sign-sig-verify-pkcs1-by-segment_

调用cryptoFramework.createAsyKeyGenerator、AsyKeyGenerator.generateKeyPair，生成密钥算法为RSA、密钥长度为1024位、素数个数为2的非对称密钥对象（KeyPair），包括公钥（PubKey）和私钥（PriKey）。

如何生成RSA非对称密钥，开发者可参考下文示例，并结合非对称密钥生成和转换规格：RSA和随机生成非对称密钥对理解，参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

调用cryptoFramework.createSign，指定字符串参数'RSA1024|PKCS1|SHA256'，创建非对称密钥类型为RSA1024、填充模式为PKCS1、摘要算法为SHA256的Sign实例，用于完成签名操作。

调用Sign.init，使用私钥（PriKey）初始化Sign实例。

将一次传入数据量设置为64字节，多次调用Sign.update，传入待签名的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

调用Sign.sign，生成数据签名。

验签

调用cryptoFramework.createVerify，指定字符串参数'RSA1024|PKCS1|SHA256'，与签名的Sign实例保持一致。创建Verify实例，用于完成验签操作。

调用Verify.init，使用公钥（PubKey）初始化Verify实例。

调用Verify.update，传入待验证的数据。当前单次update长度没有限制，开发者可以根据数据量判断如何调用update。

调用Verify.verify，对数据进行验签。

异步方法示例：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';


async function signMessageBySegment(priKey: cryptoFramework.PriKey, plainText: Uint8Array) {
  let signAlg = 'RSA1024|PKCS1|SHA256';
  let signer = cryptoFramework.createSign(signAlg);
  await signer.init(priKey);
  let textSplitLen = 64; // 自定义的数据拆分长度，此处取64
  for (let i = 0; i < plainText.length; i += textSplitLen) {
    let updateMessage = plainText.subarray(i, i + textSplitLen);
    let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
    // 分段update
    await signer.update(updateMessageBlob);
  }
  // 已通过分段传入所有明文，故此处sign传入null
  let signData = await signer.sign(null);
  return signData;
}


async function verifyMessageBySegment(pubKey: cryptoFramework.PubKey, plainText: Uint8Array,
  signMessageBlob: cryptoFramework.DataBlob) {
  let verifyAlg = 'RSA1024|PKCS1|SHA256';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  await verifier.init(pubKey);
  let textSplitLen = 64; // 自定义的数据拆分长度，此处取64
  for (let i = 0; i < plainText.length; i += textSplitLen) {
    let updateMessage = plainText.subarray(i, i + textSplitLen);
    let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
    // 分段update
    await verifier.update(updateMessageBlob);
  }
  // 已通过分段传入所有明文，故此处verify第一个参数传入null
  let res = await verifier.verify(null, signMessageBlob);
  console.info('verify result: ' + res);
  return res;
}


async function rsaSignatureBySegment() {
  let message = 'This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!';
  let keyGenAlg = 'RSA1024';
  let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  let keyPair = await generator.generateKeyPair();
  let messageData = new Uint8Array(buffer.from(message, 'utf-8').buffer);
  let signData = await signMessageBySegment(keyPair.priKey, messageData);
  let verifyResult = await verifyMessageBySegment(keyPair.pubKey, messageData, signData);
  if (verifyResult === true) {
    console.info('verify result: success.');
  } else {
    console.error('verify result: failed.');
  }
}
rsa_pkcs1_segment_signature_asynchronous.ets

同步方法示例：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';


function signMessageBySegment(priKey: cryptoFramework.PriKey, plainText: Uint8Array) {
  let signAlg = 'RSA1024|PKCS1|SHA256';
  let signer = cryptoFramework.createSign(signAlg);
  signer.initSync(priKey);
  let textSplitLen = 64; // 自定义的数据拆分长度，此处取64
  for (let i = 0; i < plainText.length; i += textSplitLen) {
    let updateMessage = plainText.subarray(i, i + textSplitLen);
    let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
    // 分段update
    signer.updateSync(updateMessageBlob);
  }
  // 已通过分段传入所有明文，故此处sign传入null
  let signData = signer.signSync(null);
  return signData;
}


function verifyMessageBySegment(pubKey: cryptoFramework.PubKey, plainText: Uint8Array,
  signMessageBlob: cryptoFramework.DataBlob) {
  let verifyAlg = 'RSA1024|PKCS1|SHA256';
  let verifier = cryptoFramework.createVerify(verifyAlg);
  verifier.initSync(pubKey);
  let textSplitLen = 64; // 自定义的数据拆分长度，此处取64
  for (let i = 0; i < plainText.length; i += textSplitLen) {
    let updateMessage = plainText.subarray(i, i + textSplitLen);
    let updateMessageBlob: cryptoFramework.DataBlob = { data: updateMessage };
    // 分段update
    verifier.updateSync(updateMessageBlob);
  }
  // 已通过分段传入所有明文，故此处verify第一个参数传入null
  let res = verifier.verifySync(null, signMessageBlob);
  console.info('verify result: ' + res);
  return res;
}


function rsaSignatureBySegment() {
  let message = 'This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!' +
    'This is a long plainText! This is a long plainText! This is a long plainText! This is a long plainText!';
  let keyGenAlg = 'RSA1024';
  let generator = cryptoFramework.createAsyKeyGenerator(keyGenAlg);
  let keyPair = generator.generateKeyPairSync();
  let messageData = new Uint8Array(buffer.from(message, 'utf-8').buffer);
  let signData = signMessageBySegment(keyPair.priKey, messageData);
  let verifyResult = verifyMessageBySegment(keyPair.pubKey, messageData, signData);
  if (verifyResult === true) {
    console.info('verify result: success.');
  } else {
    console.error('verify result: failed.');
  }
}
rsa_pkcs1_segment_signature_synchronous.ets
使用RSA密钥对（PKCS1模式）签名恢复(C/C++)
使用RSA密钥对分段签名验签 (PKCS1模式)(C/C++)
