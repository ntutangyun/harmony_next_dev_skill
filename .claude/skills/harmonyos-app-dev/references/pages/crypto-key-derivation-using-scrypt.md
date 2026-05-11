# 使用SCRYPT进行密钥派生(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-scrypt_

如果使用string类型，需要直接传入用于密钥派生的数据，而不是HexString、base64等字符串类型。同时需要确保该字符串为utf-8编码，否则派生结果会有差异。

salt：盐值。

n：迭代次数，需要为正整数。

p：并行化参数，需要为正整数。

r：块大小参数，需要为正整数。

maxMemory：最大内存限制参数，需要为正整数。

keySize：目标密钥的字节长度，需要为正整数。

调用cryptoFramework.createKdf，指定字符串参数'SCRYPT'，创建密钥派生算法为SCRYPT的密钥派生函数对象（Kdf）。

输入SCRYPT对象，调用Kdf.generateSecret进行密钥派生。

Kdf.generateSecret的多种调用形式如表所示。

接口名	返回方式
generateSecret(params: KdfSpec, callback: AsyncCallback<DataBlob>): void	callback异步生成。
generateSecret(params: KdfSpec): Promise<DataBlob>	Promise异步生成。
generateSecretSync(params: KdfSpec): DataBlob	同步生成。

通过await返回结果：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';


async function scryptAwait() {
  try {
    let spec: cryptoFramework.ScryptSpec = {
      algName: 'SCRYPT',
      salt: new Uint8Array(16),
      passphrase: 'password',
      n:1024,
      p:16,
      r:8,
      maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
      keySize: 64
    };
    let kdf = cryptoFramework.createKdf('SCRYPT');
    let secret = await kdf.generateSecret(spec);
    console.info('key derivation output: ' + secret.data);
  } catch(error) {
    let e: BusinessError = error as BusinessError;
    console.error('key derivation failed, errCode: ' + e.code + ', errMsg: ' + e.message);
  }
}
Await.ets

通过Promise返回结果：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';


function scryptPromise() {
  let spec: cryptoFramework.ScryptSpec = {
    algName: 'SCRYPT',
    passphrase: '123456',
    salt: new Uint8Array(16),
    n:1024,
    p:16,
    r:8,
    maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
    keySize: 64
  };
  let kdf = cryptoFramework.createKdf('SCRYPT');
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
import { BusinessError } from '@kit.BasicServicesKit';
import { buffer } from '@kit.ArkTS';


function kdfSync() {
  try {
    let spec: cryptoFramework.ScryptSpec = {
      algName: 'SCRYPT',
      passphrase: '123456',
      salt: new Uint8Array(16),
      n:1024,
      p:16,
      r:8,
      maxMemory:1024 * 16 * 8 * 10, //n * p * r * 10
      keySize: 64
    };
    let kdf = cryptoFramework.createKdf('SCRYPT');
    let secret = kdf.generateSecretSync(spec);
    console.info('[Sync]key derivation output: ' + secret.data);
  } catch(error) {
    let e: BusinessError = error as BusinessError;
    console.error('key derivation failed, errCode: ' + e.code + ', errMsg: ' + e.message);
  }
}
Sync.ets
使用HKDF进行密钥派生(C/C++)
使用SCRYPT进行密钥派生(C/C++)
