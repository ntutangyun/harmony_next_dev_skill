# 手动签名

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing-manual_

功能介绍

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请调试证书和调试Profile文件前，需要通过DevEco Studio生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。

密钥：格式为.p12，包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，公钥和私钥用于数字签名和验证。

证书请求文件：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和通用名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。

数字证书：格式为.cer，由华为AppGallery Connect颁发。

Profile文件：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

生成密钥和证书请求文件

DevEco Studio 6.1.0 Beta2及以上版本

在主菜单栏单击Build > Generate Key and CSR。

Keystore Name：填写p12文件名称，仅允许包含字母、数字、下划线（_）、中划线（-）、句号（.）。

Select file save path：设置密钥库文件存储路径。

Key store password：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。

Confirm password：再次输入密钥库密码。

Alias：密钥别名。请记住该别名，后续签名配置需要使用。

Validity(years)：选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。

First and last name：选填，通用名称，可填写应用名称或开发者姓名等。

Organizational unit：选填，组织单位，可填写部门名称或个人开发等。

Organization：选填，组织名称，可填写公司全称或开发者姓名等。

City or locality：选填，城市或地区。

State or province：选填，州或省。

Country code(XX)：选填，国家码。

说明

First and last name、Organizational unit、Organization、City or locality、State or province填写要求小于64个字符，不可使用双引号（"）、斜杠（\）、反引号（`）。

CSR File Name：填写CSR文件名称，仅允许包含字母、数字、下划线（_）、中划线（-）、句号（.）。

Select file save path：设置CSR文件存储路径。

DevEco Studio 6.1.0 Beta2以下版本

说明

如果本地已有对应的密钥，无需新生成密钥，可以在Generate Key界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。

Key store file：设置密钥库文件存储路径，并填写p12文件名。

Password：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。

Confirm password：再次输入密钥库密码。

Alias：必填，别名，用于标识密钥名称。请记住该别名，后续签名配置需要使用。

Password：必填，密码，与密钥库密码保持一致，无需手动输入。

Validity(years)：选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。

First and last name：选填，通用名称，可填写应用名称或开发者姓名等。

Organizational unit：选填，组织单位，可填写部门名称或个人开发等。

Organization：选填，组织名称，可填写公司全称或开发者姓名等。

City or locality：选填，城市或地区。

State or province：选填，州或省。

Country code(XX)：选填，国家码。

说明

First and last name、Organizational unit、Organization、City or locality、State or province要求：字符长度为（0，64），且不可使用双引号（"）、斜杠（\）、反引号（`）。

申请调试证书

说明

如您未在AGC中注册该应用，申请前需要在AGC中注册，具体请参考创建HarmonyOS应用。

申请调试Profile文件和添加权限信息

说明

若应用因特殊场景要求使用受限开放权限，请务必在此步骤进行申请，否则应用将在审核时被驳回。受限开放权限可申请的特殊场景请参考受限开放权限。

确保应用申请受限开放权限时提供的场景和功能信息准确。如果应用内使用的受限开放权限超出您申请的范围，或申请权限后使用的功能和场景超出可使用的范围，将影响应用上架。

{
  "module": {
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
  }
}

使用上述生成的调试证书，在AGC中申请和下载Profile，将生成的Profile保存至本地，供配置签名使用，具体请参考申请调试Profile。

配置签名信息

Store file：选择密钥库文件，文件后缀为.p12，该文件为生成密钥和证书请求文件中生成的.p12文件。

Store password：输入密钥库密码，该密码与生成密钥和证书请求文件中填写的密钥库密码保持一致。

Key alias：输入密钥的别名信息，与生成密钥和证书请求文件中填写的别名保持一致。

Key password：输入密钥的密码，与生成密钥和证书请求文件中填写的Store Password保持一致。

Sign alg：签名算法，固定为SHA256withECDSA。

Profile file：选择申请调试Profile和添加权限信息中生成的Profile文件，文件后缀为.p7b。

Certpath file：选择申请调试证书中生成的数字证书文件，文件后缀为.cer。

说明

Store file、Profile file、Certpath file三个字段支持配置相对路径，以项目根目录为起点，配置文件所在位置的路径名称。

密钥库文件、密钥库密码、密钥别名、密钥密码、Profile文件、数字证书文件必须配套使用，否则会导致签名失败。若失败请根据报错信息进行修改，再进行签名。

配置完成后，将鼠标悬停在Provisioning Profile: DevEco Manage Profile后，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息；或者进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。

配置完成后，将鼠标悬停在Provisioning Profile: DevEco Manage Profile后，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息；或者进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。

点击右上角的“Run”按钮运行应用/元服务。

## Code blocks

### Code block 1

```
{
  "module": {
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
  }
}
```
