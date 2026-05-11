# 证书CMS解封装

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-cms-decapsulation-object_

--BEGIN CERTIFICATE-----\n' +
    'MIICGDCCAb6gAwIBAgIGAXKnJjrAMAoGCCqGSM49BAMCMFcxCzAJBgNVBAYTAkNO\n' +
    'MQ8wDQYDVQQIDAbpmZXopb8xDzANBgNVBAcMBuilv+WuiTEPMA0GA1UECgwG5rWL\n' +
    '6K+VMRUwEwYDVQQDDAzkuK3mlofmtYvor5UwHhcNMjUwOTE2MDY0MTMwWhcNMzUw\n' +
    'OTE0MDY0MTMwWjBXMQswCQYDVQQGEwJDTjEPMA0GA1UECAwG6ZmV6KW/MQ8wDQYD\n' +
    'VQQHDAbopb/lrokxDzANBgNVBAoMBua1i+ivlTEVMBMGA1UEAwwM5Lit5paH5rWL\n' +
    '6K+VMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEB06h4SzOryi3d7PW9yN2wACC\n' +
    'VxlduBQjVLWZlDKhFKkdZjve8mUyytSSbBj/rrzR2XmzUzofuNkUbAtje3DDJqN2\n' +
    'MHQwHQYDVR0OBBYEFNtUldgBESf31bwTnYtApIctaSdtMB8GA1UdIwQYMBaAFNtU\n' +
    'ldgBESf31bwTnYtApIctaSdtMAsGA1UdDwQEAwIBBjAJBgNVHREEAjAAMAkGA1Ud\n' +
    'EgQCMAAwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNIADBFAiEAzxzaG2vR\n' +
    'zUnFFL3X3lRQ0IOJrb6cvkSZuaFd4bW2lgUCIHW6QGGnECDFMbDNz7Og9kjkt+3k\n' +
    'FmEJWqEMYudBH3Ul\n' +
    '-----END CERTIFICATE-----';
let ECC_256_PRIVATE: string =
  '-----BEGIN PRIVATE KEY-----\n' +
    'MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgOYwEyIw3ZNIAL4xO\n' +
    'pP6eVcQYcrL2sfnt6vB0z9tKmMmhRANCAAQHTqHhLM6vKLd3s9b3I3bAAIJXGV24\n' +
    'FCNUtZmUMqEUqR1mO97yZTLK1JJsGP+uvNHZebNTOh+42RRsC2N7cMMm\n' +
    '-----END PRIVATE KEY-----';


// string转Uint8Array。
function stringToUint8Array(str: string): Uint8Array {
  let arr: number[] = [];
  for (let i = 0, j = str.length; i < j; i++) {
    arr.push(str.charCodeAt(i));
  };
  return new Uint8Array(arr);
}


async function createX509Cert(inStream: string): Promise<cert.X509Cert> {
  let encodingBlob: cert.EncodingBlob = {
    data: stringToUint8Array(inStream),
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509Cert: cert.X509Cert = await cert.createX509Cert(encodingBlob);
  return x509Cert;
}


async function testCmsDecryptTest() {
  try {
    let plainText: Uint8Array = new Uint8Array([0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07]);
    let x509CertEc: cert.X509Cert = await createX509Cert(ECC_256_PUBKEY);
    let cms: cert.CmsGenerator = cert.createCmsGenerator(cert.CmsContentType.ENVELOPED_DATA);
    let option: cert.CmsGeneratorOptions = {
      outFormat: cert.CmsFormat.PEM
    };
    cms.setRecipientEncryptionAlgorithm(cert.CmsRecipientEncryptionAlgorithm.AES_128_GCM);
    let recipientInfo: cert.CmsRecipientInfo = {
      keyAgreeInfo: {
        cert: x509CertEc,
        digestAlgorithm: cert.CmsKeyAgreeRecipientDigestAlgorithm.SHA256
      }
    };
    await cms.addRecipientInfo(recipientInfo);
    console.info('add recipient result: success, digestAlgorithm = ' + recipientInfo.keyAgreeInfo?.digestAlgorithm);
    let envelopeData = await cms.doFinal(plainText, option);
    console.info('doFinal result: success, envelopeData = ' + envelopeData);
    let cipherText = await cms.getEncryptedContentData();
    console.info('getEncryptedContentData result: success, cipherText = ' + cipherText);
    let config: cert.CmsEnvelopedDecryptionConfig = {
      keyInfo: {
        key: ECC_256_PRIVATE
      },
    };
    let cmsDecrypt: cert.CmsParser = cert.createCmsParser();
    await cmsDecrypt.setRawData(envelopeData, cert.CmsFormat.PEM);
    let decPlainText: Uint8Array = await cmsDecrypt.decryptEnvelopedData(config);
    console.info('[XTS] decryptEnvelopedData result: success, decPlainText = ' + decPlainText);
    console.info('decryptEnvelopedData result: success.');
  } catch (error) {
    console.error(`verifySignedData failed: errCode: ${error.code}, message: ${error.message}`);
  }
}
CreateCmsDecapsulationObject.ets
证书CMS验签
证书PKCS12的创建和解析
