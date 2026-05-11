# 证书集合及证书吊销列表集合对象的创建和获取

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-get-cert-crl-object_

--BEGIN X509 CRL-----\n' +
    'MIHzMF4CAQMwDQYJKoZIhvcNAQEEBQAwFTETMBEGA1UEAxMKQ1JMIGlzc3VlchcN\n' +
    'MTcwODA3MTExOTU1WhcNMzIxMjE0MDA1MzIwWjAVMBMCAgPoFw0zMjEyMTQwMDUz\n' +
    'MjBaMA0GCSqGSIb3DQEBBAUAA4GBACEPHhlaCTWA42ykeaOyR0SGQIHIOUR3gcDH\n' +
    'J1LaNwiL+gDxI9rMQmlhsUGJmPIPdRs9uYyI+f854lsWYisD2PUEpn3DbEvzwYeQ\n' +
    '5SqQoPDoM+YfZZa23hoTLsu52toXobP74sf/9K501p/+8hm4ROMLBoRT86GQKY6g\n' +
    'eavsH0Q3\n' +
    '-----END X509 CRL-----\n';


  // 证书吊销列表二进制数据，需业务自行赋值。
  let textEncoder = new util.TextEncoder();
  let encodingBlob: cert.EncodingBlob = {
    data: textEncoder.encodeInto(crlData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };
  let x509CRL: cert.X509CRL = {} as cert.X509CRL;
  try {
    x509CRL = await cert.createX509CRL(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509CRL failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509CRL;
}


async function createX509Cert(): Promise<cert.X509Cert> {
  let certData = '-----BEGIN CERTIFICATE-----\n' +
    'MIIBHTCBwwICA+gwCgYIKoZIzj0EAwIwGjEYMBYGA1UEAwwPRXhhbXBsZSBSb290\n' +
    'IENBMB4XDTIzMDkwNTAyNDgyMloXDTI2MDUzMTAyNDgyMlowGjEYMBYGA1UEAwwP\n' +
    'RXhhbXBsZSBSb290IENBMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEHjG74yMI\n' +
    'ueO7z3T+dyuEIrhxTg2fqgeNB3SGfsIXlsiUfLTatUsU0i/sePnrKglj2H8Abbx9\n' +
    'PK0tsW/VgqwDIDAKBggqhkjOPQQDAgNJADBGAiEApVZno/Z7WyDc/muRN1y57uaY\n' +
    'Mjrgnvp/AMdE8qmFiDwCIQCrIYdHVO1awaPgcdALZY+uLQi6mEs/oMJLUcmaag3E\n' +
    'Qw==\n' +
    '-----END CERTIFICATE-----\n';


  let textEncoder = new util.TextEncoder();
  let encodingBlob: cert.EncodingBlob = {
    data: textEncoder.encodeInto(certData),
    // 根据encodingData的格式进行赋值，支持FORMAT_PEM和FORMAT_DER。
    encodingFormat: cert.EncodingFormat.FORMAT_PEM
  };


  let x509Cert: cert.X509Cert = {} as cert.X509Cert;
  try {
    x509Cert = await cert.createX509Cert(encodingBlob);
  } catch (err) {
    let e: BusinessError = err as BusinessError;
    console.error(`createX509Cert failed, errCode: ${e.code}, errMsg: ${e.message}`);
  }
  return x509Cert;
}


async function sample() {
  const x509Cert = await createX509Cert();
  const x509CRL = await createX509CRL();
  let collection: cert.CertCRLCollection = {} as cert.CertCRLCollection;
  try {
    collection = cert.createCertCRLCollection([x509Cert], [x509CRL]);
    console.info('createCertCRLCollection result: success.');
  } catch (err) {
    console.error(`createCertCRLCollection failed: errCode: ${err.code}, message: ${err.message}`);
  }


  const certParam: cert.X509CertMatchParameters = {
    validDate: '231128000000Z'
  }
  try {
    let certs: cert.X509Cert[] = await collection.selectCerts(certParam);
  } catch (err) {
    console.error(`selectCerts failed: errCode: ${err.code}, message: ${err.message}`);
  }


  const crlParam: cert.X509CRLMatchParameters = {
    x509Cert: x509Cert
  }
  try {
    let crls: cert.X509CRL[] = await collection.selectCRLs(crlParam);
    console.info('selectCRLs result: success.');
  } catch (err) {
    console.error(`selectCRLs failed: errCode: ${err.code}, message: ${err.message}`);
  }
}
CreateGetCertCrlObject.ets
证书链校验器对象的创建和校验
证书链对象的创建和校验
