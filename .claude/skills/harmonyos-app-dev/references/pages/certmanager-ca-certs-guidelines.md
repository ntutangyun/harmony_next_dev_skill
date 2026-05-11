# CA证书开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certmanager-ca-certs-guidelines_

--BEGIN CERTIFICATE-----\n' +
    'MIIDSTCCAjECFFRZKkiBuiZ+zqfjJOg05yeTePM9MA0GCSqGSIb3DQEBCwUAMGEx\n' +
    'CzAJBgNVBAYTAmNuMQ0wCwYDVQQIDARvaG9zMQswCQYDVQQHDAJjbTEhMB8GA1UE\n' +
    'CgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMRMwEQYDVQQDDApUZXN0Um9vdENB\n' +
    'MB4XDTI1MTAxNTA3MzE0MloXDTI2MTAxNTA3MzE0MlowYTELMAkGA1UEBhMCY24x\n' +
    'DTALBgNVBAgMBG9ob3MxCzAJBgNVBAcMAmNtMSEwHwYDVQQKDBhJbnRlcm5ldCBX\n' +
    'aWRnaXRzIFB0eSBMdGQxEzARBgNVBAMMClRlc3RSb290Q0EwggEiMA0GCSqGSIb3\n' +
    'DQEBAQUAA4IBDwAwggEKAoIBAQC5p4eoQJyTBvn01M8SwEi8dguTIPGmD3a8SGIj\n' +
    'KXaB6ltv742H5EBjgk+zC8+Gis0ehEqwk3pVnnmByeYvrERxsUqDt69/FndlfTxI\n' +
    'C2/2MxWVk97g/6TpJ5Lt2mTrH+rSOgUDyU27aPn12ZnDF1mLsT+U+CBmfj4+J4tW\n' +
    'yzdFNj7kcKMQQok+L1dtFlDNMNpMA1UqADzoC3XgFl49CpDtoFId9DVsgUPkPfX1\n' +
    '89cCunomgJe1b17FzxfNu2yhbl5cnUEjeHGbmBgBIB7uG8tjGstnDPx7fl3Xrj+Q\n' +
    'fRrwCpVKD9RxoyUBFbHttixxY5bHFUdvHRB251sxD+JfxxxLAgMBAAEwDQYJKoZI\n' +
    'hvcNAQELBQADggEBAEGbNqcMU7C/lrIytI/OTtzYbkWDsfnRSPxlCUoZ2Xh3S83A\n' +
    'SNQ9Ze5tDwWdW9Hlde9May6hzvuQSYeMLLnyM8WGResXCs7UbnSQe7fGfUu+xDGb\n' +
    'h4tamnRFtZydxCCgDT9lIdHeutlPwOuxlR4HXpeowGeGJX0iFrdo6D0iXAY34hic\n' +
    'yLQzuBqE/1s3PLA83Fi4EOOOV7P/ahmOLtBFlHbySHV68i9PNeNr9SDykH9/RgI9\n' +
    '5G8ZTZj8oSmbTGGtfNuVXybMyJMRlz6BkxG++kYcg7STRBqHGX7RrWHiupguNreO\n' +
    '4sJBdSpWBq172ZEyOvTqC4xX9lLYqwwBQ++TFoo=\n' +
    '-----END CERTIFICATE-----');


  let certUri: string = '';
  let certScope = certificateManager.CertScope.CURRENT_USER;
  try {
    /* 在当前用户下，安装用户CA证书。 */
    let result = certificateManager.installUserTrustedCertificateSync(userCAData, certScope);
    certUri = (result.uri != undefined) ? result.uri : '';
    console.info(`Succeeded in install user ca cert, certUri is ${certUri}`);
  } catch (err) {
    console.error(`Failed to install user ca cert. Code: ${err.code}, message: ${err.message}`);
  }


  try {
    /* 获取用户CA证书详情。 */
    let result = await certificateManager.getUserTrustedCertificate(certUri);
    if (result === undefined || result.certInfo == undefined) {
      console.error('The result of getting user ca cert is undefined.');
    } else {
      let certInfo = result.certInfo;
      console.info('Succeeded in getting user ca cert.');
    }
  } catch (err) {
    console.error(`Failed to get user ca certificate. Code: ${err.code}, message: ${err.message}`);
  }


  try {
    /* 获取当前用户下的用户CA证书列表。 */
    let result = await certificateManager.getAllUserTrustedCertificates(certScope);
    if (result == undefined) { /* 用户根CA证书个数为0时，返回result为undefined。 */
      console.info('the count of the user trusted certificates is 0');
    } else if (result.certList == undefined) {
      console.error('The result of getting current user trusted certificates is undefined.');
    } else {
      let list = result.certList;
      console.info('Succeeded in getting user ca cert list.');
    }
  } catch (err) {
    console.error(`Failed to get user ca certificate. Code: ${err.code}, message: ${err.message}`);
  }


  try {
    /* 删除安装的用户CA证书。 */
    certificateManager.uninstallUserTrustedCertificateSync(certUri);
  } catch (err) {
    console.error(`Failed to uninstall user ca certificate. Code: ${err.code}, message: ${err.message}`);
  }
}
CertManagerUserCASample.ets

获取系统CA证书路径、用户CA证书路径。应用可以直接通过该路径访问CA证书。

import { certificateManager } from '@kit.DeviceCertificateKit';


function getUserCaPathSample() {
  try {
    /* 获取系统CA的存储位置。 */
    let property1: certificateManager.CertStoreProperty = {
      certType: certificateManager.CertType.CA_CERT_SYSTEM,
    }
    let systemCAPath = certificateManager.getCertificateStorePath(property1);
    console.info(`Success to get system ca path: ${systemCAPath}`);


    /* 获取当前用户的用户CA存储位置。 */
    let property2: certificateManager.CertStoreProperty = {
      certType: certificateManager.CertType.CA_CERT_USER,
      certScope: certificateManager.CertScope.CURRENT_USER,
    }
    let userCACurrentPath = certificateManager.getCertificateStorePath(property2);
    console.info(`Success to get current user's user ca path: ${userCACurrentPath}`);


    /* 获取设备公共的用户CA存储位置。 */
    let property3: certificateManager.CertStoreProperty = {
      certType: certificateManager.CertType.CA_CERT_USER,
      certScope: certificateManager.CertScope.GLOBAL_USER,
    }
    let globalCACurrentPath = certificateManager.getCertificateStorePath(property3);
    console.info(`Success to get global user's user ca path: ${globalCACurrentPath}`);
  } catch (error) {
    console.error(`Failed to get store path. Code: ${error.code}, message: ${error.message}`);
  }
}
CertManagerGetCAPathSample.ets
应用证书凭据开发指导
证书管理对话框开发指导
