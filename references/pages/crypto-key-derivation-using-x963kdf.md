# 使用X963KDF进行密钥派生(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf_

如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。

info：可选的上下文与应用相关信息，可为空，用于拓展短密钥。

keySize：目标密钥的字节长度，需要为正整数。

调用cryptoFramework.createKdf，指定字符串参数'X963KDF|SHA256'，创建密钥派生算法为X963KDF、HMAC函数摘要算法为SHA256的密钥派生函数对象（Kdf）。

输入X963KdfSpec对象，调用Kdf.generateSecret进行密钥派生。

Kdf.generateSecret的多种调用形式如表所示。

接口名	返回方式
generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void	callback异步生成。
generateSecret(params: KdfSpec): Promise<DataBlob>	Promise异步生成。
generateSecretSync(params: KdfSpec): DataBlob	同步生成。

通过await返回结果：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';


async function kdfAwait() {
  let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
  let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
  let spec: cryptoFramework.X963KdfSpec = {
    algName: 'X963KDF',
    key: keyData,
    info: infoData,
    keySize: 32
  };
  let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
  let secret = await kdf.generateSecret(spec);
  console.info('key derivation output: ' + secret.data);
}
Await.ets

通过Promise返回结果：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';


function kdfPromise() {
  let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
  let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
  let spec: cryptoFramework.X963KdfSpec = {
    algName: 'X963KDF',
    key: keyData,
    info: infoData,
    keySize: 32
  };
  let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
  let kdfPromise = kdf.generateSecret(spec);
  kdfPromise.then((secret) => {
    console.info('key derivation output: ' + secret.data);
  }).catch((error: BusinessError) => {
    console.error(`key derivation failed: errCode: ${error.code}, message: ${error.message}`);
  });
}
Promise.ets

通过同步方式返回结果：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { buffer } from '@kit.ArkTS';


function kdfSync() {
  let keyData = new Uint8Array(buffer.from('012345678901234567890123456789', 'utf-8').buffer);
  let infoData = new Uint8Array(buffer.from('infostring', 'utf-8').buffer);
  let spec: cryptoFramework.X963KdfSpec = {
    algName: 'X963KDF',
    key: keyData,
    info: infoData,
    keySize: 32
  };
  let kdf = cryptoFramework.createKdf('X963KDF|SHA256');
  let secret = kdf.generateSecretSync(spec);
  console.info('[Sync]key derivation output: ' + secret.data);
}
Sync.ets
使用SCRYPT进行密钥派生(C/C++)
使用X963KDF进行密钥派生(C/C++)
