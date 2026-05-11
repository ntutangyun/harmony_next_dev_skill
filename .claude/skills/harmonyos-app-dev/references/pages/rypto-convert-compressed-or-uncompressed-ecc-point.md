# 使用ECC压缩/非压缩点格式转换(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rypto-convert-compressed-or-uncompressed-ecc-point_

通过传入字符串参数format，可指定需要获取的点数据格式。如果需要获取压缩格式，则指定format为："COMPRESSED"；需要获取非压缩格式，则指定format为："UNCOMPRESSED"。

指定非压缩点数据转换为压缩点数据

指定Uint8Array类型的ECC非压缩点数据，调用ECCKeyUtil.convertPoint，构造Point对象，用于生成点数据。

调用ECCKeyUtil.getEncodedPoint，获取压缩点数据。

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


function eccPointUncompressedToCompressed() {
  let pkData =
    new Uint8Array([4, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195,
      157, 111, 40, 217, 215, 148, 120, 224, 205, 82, 83, 92, 185, 21, 211, 184, 5, 19, 114, 33, 86, 85, 228, 123, 242,
      206, 200, 98, 178, 184, 130, 35, 232, 45, 5, 202, 189, 11, 46, 163, 156, 152]);
  let returnPoint = cryptoFramework.ECCKeyUtil.convertPoint('NID_brainpoolP256r1', pkData);
  console.info('convertPoint result: success.');
  let returnData = cryptoFramework.ECCKeyUtil.getEncodedPoint('NID_brainpoolP256r1', returnPoint, 'COMPRESSED');
  console.info('returnData: ' + returnData);
}
CompressedPointData.ets
指定压缩点数据获取密钥对象
指定Uint8Array类型的ECC压缩点数据，调用ECCKeyUtil.convertPoint，得到Point对象，用于密钥对象生成。
调用ECCKeyUtil.genECCCommonParamsSpec，指定曲线名'NID_brainpoolP256r1'，生成ECC的非对称公共密钥参数。
构造ECCPubKeySpec对象，用于指定ECC算法中公钥包含的参数。ECCPubKeySpec是AsyKeySpec的子类。需要通过参数algName指定算法'ECC'；指定密钥参数类型AsyKeySpecType.PUBLIC_KEY_SPEC，参数pk指定为得到的point对象。
通过得到的公钥参数，调用createAsyKeyGeneratorBySpec，创建非对称密钥生成器（AsyKeyGeneratorBySpec）。
调用AsyKeyGeneratorBySpec.generatePubKey，得到指定的公钥。
调用ECCKeyUtil.getEncodedPoint，得到非压缩点数据。
调用PubKey.getAsyKeySpec，获取ECC算法中公钥pk的x坐标。
import { cryptoFramework } from '@kit.CryptoArchitectureKit';


async function eccPointCompressedToPoint() {
  let pkData =
    new Uint8Array([2, 143, 39, 57, 249, 145, 50, 63, 222, 35, 70, 178, 121, 202, 154, 21, 146, 129, 75, 76, 63, 8, 195,
      157, 111, 40, 217, 215, 148, 120, 224, 205, 82]);
  let returnPoint = cryptoFramework.ECCKeyUtil.convertPoint('NID_brainpoolP256r1', pkData);
  console.info('convertPoint result: success.');
  let eccCommonParamsSpec = cryptoFramework.ECCKeyUtil.genECCCommonParamsSpec('NID_brainpoolP256r1');
  let eccPubKeySpec: cryptoFramework.ECCPubKeySpec = {
    algName: 'ECC',
    specType: cryptoFramework.AsyKeySpecType.PUBLIC_KEY_SPEC,
    params: eccCommonParamsSpec,
    pk: returnPoint
  };
  let generatorBySpec = cryptoFramework.createAsyKeyGeneratorBySpec(eccPubKeySpec);
  let pubKey = await generatorBySpec.generatePubKey();
  let returnData = cryptoFramework.ECCKeyUtil.getEncodedPoint('NID_brainpoolP256r1', returnPoint, 'UNCOMPRESSED');
  console.info('returnData: ' + returnData);
  let eccPkX = pubKey.getAsyKeySpec(cryptoFramework.AsyKeySpecItem.ECC_PK_X_BN);
  console.info('returnPoint x data: ' + returnPoint.x);
  console.info('ECC_PK_X_BN: ' + eccPkX);
}
GetKeyObject.ets
使用ECC压缩/非压缩公钥格式转换(C/C++)
使用ECC压缩/非压缩点格式转换(C/C++)
