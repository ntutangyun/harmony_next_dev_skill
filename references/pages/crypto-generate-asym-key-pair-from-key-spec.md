# 指定密钥参数生成非对称密钥对(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-from-key-spec_

p', p); // length is 224, hex : ffffffffffffffffffffffffffffffff000000000000000000000001
    let a = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_A_BN);
    showBigIntInfo('--- a', a); // length is 224, hex : fffffffffffffffffffffffffffffffefffffffffffffffffffffffe
    let b = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_B_BN);
    showBigIntInfo('--- b', b); // length is 224, hex : b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4
    let gX = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_G_X_BN);
    showBigIntInfo('--- gX', gX); // length is 224, hex : b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21
    let gY = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_G_Y_BN);
    showBigIntInfo('--- gY', gY); // length is 224, hex : bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34
    let n = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_N_BN);
    showBigIntInfo('--- n', n); // length is 224, hex : ffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d
    let h = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_H_NUM);
    console.warn('--- h: ' + h); // key h: 1
    let fieldType = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FIELD_TYPE_STR);
    console.warn('--- field type: ' + fieldType); // key field type: Fp
    let fieldSize = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FIELD_SIZE_NUM);
    console.warn('--- field size: ' + fieldSize); // key field size: 224
    let curveName = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_CURVE_NAME_STR);
    console.warn('--- curve name: ' + curveName); // key curve name: NID_secp224r1
    if (keyType == 'priKey') {
      let sk = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_SK_BN);
      showBigIntInfo('--- sk', sk);
    } else if (keyType == 'pubKey') {
      let pkX = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
      showBigIntInfo('--- pkX', pkX);
      let pkY = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
      showBigIntInfo('--- pkY', pkY);
    }
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(`getAsyKeySpec failed: errCode: ${e.code}, message: ${e.message}`);
  }
}


// 根据EccCommonSpec实例生成ECC密钥对，获取密钥规格
function testEccUseCommKeySpecGet() {
  try {
    let commKeySpec = genEccCommonSpec(); // 使用参数属性，构造ECC公私钥公共密钥参数对象
    let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // 使用密钥参数对象创建生成器
    let keyPairPromise = generatorBySpec.generateKeyPair(); // Generate an ECC key pair.
    keyPairPromise.then(keyPair => { // 使用生成器创建ECC密钥对
      showEccSpecDetailInfo(keyPair.priKey, 'priKey'); // 对私钥获取相关密钥参数属性
      showEccSpecDetailInfo(keyPair.pubKey, 'pubKey'); // 对公钥获取相关密钥参数属性
    }).catch((error: BusinessError) => {
      // 逻辑错误等异步异常在此捕获
      console.error(`generateComm failed: errCode: ${error.code}, message: ${error.message}`);
    })
  } catch (error) {
    // 参数错误等同步异常在此捕获
    let e: BusinessError = error as BusinessError;
    console.error(`ecc comm spec failed: errCode: ${e.code}, message: ${e.message}`);
  }
}
Promise.ets

同步返回结果（调用方法generateKeyPairSync）：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


function showBigIntInfo(bnName: string, bnValue: bigint | string | number) {
  if (typeof bnValue === 'string') {
    console.error('type: string');
    return;
  }
  if (typeof bnValue === 'number') {
    console.error('type: number');
    return;
  }
  console.info(bnName + ':');
  console.info('. Decimal: ' + bnValue.toString());
  console.info('. Hexadecimal: ' + bnValue.toString(16));
  console.info('. Length (bits): ' + bnValue.toString(2).length);
}


// 根据密钥规格构造ECCCommonParamsSpec结构体。ECCCommonParamsSpec结构体定义了ECC私钥和公钥的公共参数
function genEccCommonSpec(): cryptoFramework.ECCCommonParamsSpec {
  let fieldFp: cryptoFramework.ECFieldFp = {
    fieldType: 'Fp',
    p: BigInt('0xffffffffffffffffffffffffffffffff000000000000000000000001')
  }
  let G: cryptoFramework.Point = {
    x: BigInt('0xb70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21'),
    y: BigInt('0xbd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34')
  }
  let eccCommonSpec: cryptoFramework.ECCCommonParamsSpec = {
    algName: 'ECC',
    specType: cryptoFramework.AsyKeySpecType.COMMON_PARAMS_SPEC,
    field: fieldFp,
    a: BigInt('0xfffffffffffffffffffffffffffffffefffffffffffffffffffffffe'),
    b: BigInt('0xb4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4'),
    g: G,
    n: BigInt('0xffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d'),
    h: 1
  }
  return eccCommonSpec;
}


// 打印ECC密钥规格
function showEccSpecDetailInfo(key: cryptoFramework.PubKey | cryptoFramework.PriKey, keyType: string) {
  console.info('show detail of ' + keyType + ':');
  try {
    let p = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FP_P_BN);
    showBigIntInfo('--- p', p); // length is 224, hex : ffffffffffffffffffffffffffffffff000000000000000000000001
    let a = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_A_BN);
    showBigIntInfo('--- a', a); // length is 224, hex : fffffffffffffffffffffffffffffffefffffffffffffffffffffffe
    let b = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_B_BN);
    showBigIntInfo('--- b', b); // length is 224, hex : b4050a850c04b3abf54132565044b0b7d7bfd8ba270b39432355ffb4
    let gX = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_G_X_BN);
    showBigIntInfo('--- gX', gX); // length is 224, hex : b70e0cbd6bb4bf7f321390b94a03c1d356c21122343280d6115c1d21
    let gY = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_G_Y_BN);
    showBigIntInfo('--- gY', gY); // length is 224, hex : bd376388b5f723fb4c22dfe6cd4375a05a07476444d5819985007e34
    let n = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_N_BN);
    showBigIntInfo('--- n', n); // length is 224, hex : ffffffffffffffffffffffffffff16a2e0b8f03e13dd29455c5c2a3d
    let h = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_H_NUM);
    console.warn('--- h: ' + h); // key h: 1
    let fieldType = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FIELD_TYPE_STR);
    console.warn('--- field type: ' + fieldType); // key field type: Fp
    let fieldSize = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_FIELD_SIZE_NUM);
    console.warn('--- field size: ' + fieldSize); // key field size: 224
    let curveName = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_CURVE_NAME_STR);
    console.warn('--- curve name: ' + curveName); // key curve name: NID_secp224r1
    if (keyType == 'priKey') {
      let sk = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_SK_BN);
      showBigIntInfo('--- sk', sk);
    } else if (keyType == 'pubKey') {
      let pkX = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
      showBigIntInfo('--- pkX', pkX);
      let pkY = key.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_Y_BN);
      showBigIntInfo('--- pkY', pkY);
    }
  } catch (e) {
    console.error(`getAsyKeySpec failed: errCode: ${e.code}, message: ${e.message}`);
  }
}


// 根据EccCommonSpec实例生成ECC密钥对，获取密钥规格
function testEccUseCommKeySpecGetSync() {
  try {
    let commKeySpec = genEccCommonSpec(); // 使用参数属性，构造ECC公私钥公共密钥参数对象
    let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(commKeySpec); // 使用密钥参数对象创建生成器
    let keyPair = generatorBySpec.generateKeyPairSync(); // Generate an ECC key pair.
    if (keyPair != null) {
      showEccSpecDetailInfo(keyPair.priKey, 'priKey'); // 对私钥获取相关密钥参数属性
      showEccSpecDetailInfo(keyPair.pubKey, 'pubKey'); // 对公钥获取相关密钥参数属性
    } else {
      console.error('get key pair result: fail!');
    }
  } catch (e) {
    // 逻辑错误等异常在此捕获
    console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  }
}
Sync.ets
根据椭圆曲线名生成SM2密钥对

对应的算法规格请查看非对称密钥生成和转换规格：SM2。

构造ECCCommonParamsSpec对象，用于指定非对称公共密钥参数。根据genECCCommonParamsSpec接口传入相应的NID字符串名称生成相应的非对称公共密钥参数。

使用密钥参数生成密钥时，bigint类型参数需采用大端字节序输入，且值应为正数以满足数学运算要求。

创建ECCKeyPairSpec对象，并且algName设置为SM2，用于指定SM2算法中密钥对包含的参数。

调用cryptoFramework.createAsyKeyGeneratorBySpec，将ECCKeyPairSpec对象传入，创建非对称密钥生成器。

调用AsyKeyGeneratorBySpec.generateKeyPair，得到各项数据与密钥参数一致的密钥对（KeyPair）。

调用PriKey.getAsyKeySpec，获取SM2算法中椭圆曲线参数。

以使用Promise方式根据椭圆曲线名生成SM2密钥为例：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


function genSM2KeyPairSpec() {
  let sm2CommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2');
  let sm2KeyPairSpec: cryptoFramework.ECCKeyPairSpec = {
    algName: 'SM2',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: sm2CommonParamsSpec,
    sk: BigInt('0x6330B599ECD23ABDC74B9A5B7B5E00E553005F72743101C5FAB83AEB579B7074'),
    pk: {
      x: BigInt('0x67F3B850BDC0BA5D3A29D8A0883C4B17612AB84F87F18E28F77D824A115C02C4'),
      y: BigInt('0xD48966CE754BBBEDD6501A1385E1B205C186E926ADED44287145E8897D4B2071')
    },
  };
  return sm2KeyPairSpec;
}


async function sm2Test() {
  let sm2KeyPairSpec = genSM2KeyPairSpec();
  let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(sm2KeyPairSpec);
  let keyPair = await generatorBySpec.generateKeyPair();
  let sm2CurveName = keyPair.priKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_CURVE_NAME_STR);
  console.info('ECC_CURVE_NAME_STR: ' + sm2CurveName); // NID_sm2
}
Promise.ets

同步返回结果（调用方法generateKeyPairSync）：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


function genSM2KeyPairSpec() {
  let sm2CommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_sm2');
  let sm2KeyPairSpec: cryptoFramework.ECCKeyPairSpec = {
    algName: 'SM2',
    specType: cryptoFramework.AsyKeySpecType.KEY_PAIR_SPEC,
    params: sm2CommonParamsSpec,
    sk: BigInt('0x6330B599ECD23ABDC74B9A5B7B5E00E553005F72743101C5FAB83AEB579B7074'),
    pk: {
      x: BigInt('0x67F3B850BDC0BA5D3A29D8A0883C4B17612AB84F87F18E28F77D824A115C02C4'),
      y: BigInt('0xD48966CE754BBBEDD6501A1385E1B205C186E926ADED44287145E8897D4B2071')
    },
  };
  return sm2KeyPairSpec;
}


function sm2TestSync() {
  let sm2KeyPairSpec = genSM2KeyPairSpec();
  let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(sm2KeyPairSpec);
  try {
    let keyPair = generatorBySpec.generateKeyPairSync();
    if (keyPair != null) {
      let sm2CurveName = keyPair.priKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_CURVE_NAME_STR);
      console.info('ECC_CURVE_NAME_STR: ' + sm2CurveName); // NID_sm2
    } else {
      console.error('get key pair result: fail!');
    }
  } catch (e) {
    console.error(`get key pair failed: errCode: ${e.code}, message: ${e.message}`);
  }
}
Sync.ets
指定二进制数据转换非对称密钥对(C/C++)
指定密钥参数生成非对称密钥对(C/C++)
