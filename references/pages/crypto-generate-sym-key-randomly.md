# 随机生成对称密钥(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-sym-key-randomly_

调用cryptoFramework.createSymKeyGenerator，指定字符串参数'AES256'，创建密钥算法为AES、密钥长度为256位的对称密钥生成器（SymKeyGenerator）。

调用SymKeyGenerator.generateSymKey，随机生成对称密钥对象（SymKey）。

调用SymKey.getEncoded，获取密钥对象的二进制数据。

以使用Promise方式随机生成AES密钥为例：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


function testGenerateAesKey() {
  // 创建SymKeyGenerator实例
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  // 使用密钥生成器随机生成对称密钥
  let promiseSymKey = symKeyGenerator.generateSymKey();
  promiseSymKey.then(key => {
    // 获取对称密钥的二进制数据，输出256位密钥。长度为32字节
    let encodedKey = key.getEncoded();
    console.info('key hex: ' + encodedKey.data);
  });
}
Promise.ets

同步方法（调用方法generateSymKeySync）：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


function testSyncGenerateAesKey() {
  // 创建SymKeyGenerator实例
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('AES256');
  // 使用密钥生成器随机生成对称密钥
  let promiseSymKey = symKeyGenerator.generateSymKeySync();
  // 获取对称密钥的二进制数据，输出256位密钥。长度为32字节
  let encodedKey = promiseSymKey.getEncoded();
  console.info('key hex: ' + encodedKey.data);
}
Sync.ets
随机生成SM4密钥

对应的算法规格请查看对称密钥生成和转换规格：SM4。

调用cryptoFramework.createSymKeyGenerator，指定字符串参数'SM4_128'，创建密钥算法为SM4、密钥长度为128位的对称密钥生成器（SymKeyGenerator）。

如果开发者需要使用其他算法，请注意修改此处入参的字符串参数。

调用SymKeyGenerator.generateSymKey，随机生成对称密钥对象（SymKey）。

调用SymKey.getEncoded，获取密钥对象的二进制数据。

以使用Promise方式随机生成SM4密钥为例：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


function testGenerateSM4Key() {
  // 创建SymKeyGenerator实例
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
  // 使用密钥生成器随机生成对称密钥
  let promiseSymKey = symKeyGenerator.generateSymKey();
  promiseSymKey.then(key => {
    // 获取对称密钥的二进制数据，输出128位字节流。长度为16字节
    let encodedKey = key.getEncoded();
    console.info('key hex: ' + encodedKey.data);
  });
}
Promise.ets

同步方法（调用方法generateSymKeySync）：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


function testSyncGenerateSm4Key() {
  // 创建SymKeyGenerator实例
  let symKeyGenerator = cryptoFramework.createSymKeyGenerator('SM4_128');
  // 使用密钥生成器随机生成对称密钥
  let promiseSymKey = symKeyGenerator.generateSymKeySync();
  // 获取对称密钥的二进制数据，输出128位字节流。长度为16字节
  let encodedKey = promiseSymKey.getEncoded();
  console.info('key hex: ' + encodedKey.data);
}
Sync.ets
密钥生成和转换开发指导
随机生成对称密钥(C/C++)
