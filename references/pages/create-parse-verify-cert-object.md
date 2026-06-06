# 证书对象的创建、解析和校验

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-parse-verify-cert-object_

--BEGIN CERTIFICATE-----\n' +
  'MIIBLzCB1QIUO/QDVJwZLIpeJyPjyTvE43xvE5cwCgYIKoZIzj0EAwIwGjEYMBYG\n' +
  'A1UEAwwPRXhhbXBsZSBSb290IENBMB4XDTIzMDkwNDExMjAxOVoXDTI2MDUzMDEx\n' +
  'MjAxOVowGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYI\n' +
  'KoZIzj0DAQcDQgAEHjG74yMIueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTa\n' +
  'tUsU0i/sePnrKglj2H8Abbx9PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEA\n' +
  '0ce/fvA4tckNZeB865aOApKXKlBjiRlaiuq5mEEqvNACIQDPD9WyC21MXqPBuRUf\n' +
  'BetUokslUfjT6+s/X4ByaxycAA==\n' +
  '-----END CERTIFICATE-----\n';


// 证书示例
function certSample(): void {
  let textEncoder = new util.TextEncoder();
  let encodingBlob: cert.EncodingBlob = {
    // 将证书数据从string类型转换成Uint8Array。
    data: textEncoder.encodeInto(certData),
    // 证书格式，仅支持PEM和DER。在此示例中，证书为PEM格式。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };


  // 创建X509Cert实例。
  cert.createX509Cert(encodingBlob, (err, x509Cert) => {
    if (err != null) {
      // 创建X509Cert实例失败。
      console.error(`createX509Cert failed, errCode:${err.code}, errMsg:${err.message}`);
      return;
    }
    // X509Cert实例创建成功。
    console.info('createX509Cert result: success.');


    // 获取证书版本。
    let version = x509Cert.getVersion();
    // 获取证书序列号。
    let serial = x509Cert.getCertSerialNumber();
    console.info(`X509 version: ${version} , X509 serial:${serial}`);


    // 获取证书颁发者名称。
    let issuerName = x509Cert.getIssuerName(cert.EncodingType.ENCODING_UTF8);
    console.info(`X509 issuerName: ${issuerName}`);


    // 获取证书主体名称。
    let subjectNameBin = x509Cert.getSubjectName(cert.EncodingType.ENCODING_UTF8);
    let encoder = util.TextDecoder.create();
    let subjectName = encoder.decodeToString(subjectNameBin.data);
    console.info(`X509 subjectName: ${subjectName}`);


    // 获取证书对象的字符串类型数据。
    let certString = x509Cert.toString(cert.EncodingType.ENCODING_UTF8);
    console.info(`X509 certString: ${certString}`);


    // 使用上级证书对象的getPublicKey()方法或本（自签名）证书对象获取公钥对象。
    try {
      let pubKey = x509Cert.getPublicKey();
      // 验证证书签名。
      x509Cert.verify(pubKey, (err, data) => {
        if (err == null) {
          // 签名验证成功。
          console.info('verify result: success.');
        } else {
          // 签名验证失败。
          console.error(`verify failed, errCode: ${err.code} , errMsg:${err.message}`);
        }
      });
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`getPublicKey failed, errCode: ${e.code} , errMsg:${e.message}`);
    }


    // 用一个字符串代表时间。
    let date = '20230930000001Z';


    // 验证证书的有效期。
    try {
      x509Cert.checkValidityWithDate(date);
    } catch (error) {
      let e: BusinessError = error as BusinessError;
      console.error(`checkValidityWithDate failed, errCode: ${e.code}, errMsg:${e.message}`);
    }
  });
}
CreateParseVerifyCertObject.ets
证书算法库框架概述
证书扩展信息对象的创建、解析和校验
