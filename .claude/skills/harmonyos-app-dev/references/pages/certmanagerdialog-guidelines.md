# 证书管理对话框开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/certmanagerdialog-guidelines_

--BEGIN CERTIFICATE-----
MIIDSTCCAjECFFRZKkiBuiZ+zqfjJOg05yeTePM9MA0GCSqGSIb3DQEBCwUAMGEx
CzAJBgNVBAYTAmNuMQ0wCwYDVQQIDARvaG9zMQswCQYDVQQHDAJjbTEhMB8GA1UE
CgwYSW50ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMRMwEQYDVQQDDApUZXN0Um9vdENB
MB4XDTI1MTAxNTA3MzE0MloXDTI2MTAxNTA3MzE0MlowYTELMAkGA1UEBhMCY24x
DTALBgNVBAgMBG9ob3MxCzAJBgNVBAcMAmNtMSEwHwYDVQQKDBhJbnRlcm5ldCBX
aWRnaXRzIFB0eSBMdGQxEzARBgNVBAMMClRlc3RSb290Q0EwggEiMA0GCSqGSIb3
DQEBAQUAA4IBDwAwggEKAoIBAQC5p4eoQJyTBvn01M8SwEi8dguTIPGmD3a8SGIj
KXaB6ltv742H5EBjgk+zC8+Gis0ehEqwk3pVnnmByeYvrERxsUqDt69/FndlfTxI
C2/2MxWVk97g/6TpJ5Lt2mTrH+rSOgUDyU27aPn12ZnDF1mLsT+U+CBmfj4+J4tW
yzdFNj7kcKMQQok+L1dtFlDNMNpMA1UqADzoC3XgFl49CpDtoFId9DVsgUPkPfX1
89cCunomgJe1b17FzxfNu2yhbl5cnUEjeHGbmBgBIB7uG8tjGstnDPx7fl3Xrj+Q
fRrwCpVKD9RxoyUBFbHttixxY5bHFUdvHRB251sxD+JfxxxLAgMBAAEwDQYJKoZI
hvcNAQELBQADggEBAEGbNqcMU7C/lrIytI/OTtzYbkWDsfnRSPxlCUoZ2Xh3S83A
SNQ9Ze5tDwWdW9Hlde9May6hzvuQSYeMLLnyM8WGResXCs7UbnSQe7fGfUu+xDGb
h4tamnRFtZydxCCgDT9lIdHeutlPwOuxlR4HXpeowGeGJX0iFrdo6D0iXAY34hic
yLQzuBqE/1s3PLA83Fi4EOOOV7P/ahmOLtBFlHbySHV68i9PNeNr9SDykH9/RgI9
5G8ZTZj8oSmbTGGtfNuVXybMyJMRlz6BkxG++kYcg7STRBqHGX7RrWHiupguNreO
4sJBdSpWBq172ZEyOvTqC4xX9lLYqwwBQ++TFoo=
-----END CERTIFICATE-----`);


async function installUserCADialogSample() {
  /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
  let context: common.Context = new UIContext().getHostContext() as common.Context;
  let certScope = certificateManagerDialog.CertificateScope.CURRENT_USER; /* 安装在当前用户下。 */
  try {
    /* 安装证书。 */
    certificateManagerDialog.openInstallCertificateDialog(context, certType, certScope, cert).then((result) => {
      console.info('Succeeded in opening install ca dialog.');
      certUri = result;
    }).catch((err: BusinessError) => {
      console.error(`Failed to open install ca dialog. Code: ${err.code}, message: ${err.message}`);
    })
  } catch (error) {
    console.error(`Failed to open install ca dialog. Code: ${error.code}, message: ${error.message}`);
  }
}


async function uninstallUserCADialogSample() {
  /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
  let context: common.Context = new UIContext().getHostContext() as common.Context;
  try {
    /* 删除证书。 */
    certificateManagerDialog.openUninstallCertificateDialog(context, certType, certUri).then(() => {
      console.info('Succeeded in opening uninstall ca dialog.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to open uninstall ca dialog. Code: ${err.code}, message: ${err.message}`);
    })
  } catch (error) {
    console.error(`Failed to open uninstall ca dialog. Code: ${error.code}, message: ${error.message}`);
  }
}


async function certDetailDialogSample() {
  /* context为应用的上下文信息，由调用方自行获取，此处仅为示例。 */
  let context: common.Context = new UIContext().getHostContext() as common.Context;
  try {
    let property: certificateManagerDialog.CertificateDialogProperty = {
      showInstallButton: false    /* 不显示安装按钮。 */
    };
    /* 显示证书详情。 */
    certificateManagerDialog.openCertificateDetailDialog(context, cert, property).then(() => {
      console.info('Succeeded in opening show ca detail dialog.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to open show ca detail dialog. Code: ${err.code}, message: ${err.message}`);
    })
  } catch (error) {
    console.error(`Failed to open show ca detail dialog. Code: ${error.code}, message: ${error.message}`);
  }
}
CertManagerCaDialogSample.ets
CA证书开发指导
Device Security Kit（设备安全服务）
