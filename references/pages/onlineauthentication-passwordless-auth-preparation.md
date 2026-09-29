# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-passwordless-auth-preparation_

FIDO开发准备

开发者的业务需要接入符合FIDO UAF标准的协议，并部署符合FIDO UAF标准协议的FIDO服务端。FIDO网址：FIDO官方网站 （见网站链接免责声明）。

IFAA开发准备

开发者的业务需要接入IIFAA联盟，并接入IIFAA中心服务器。IIFAA网址：IIFAA官方网站 （见网站链接免责声明）。

SOTER开发准备

开发者的业务需要接入SOTER服务器。SOTER github：SOTER开源项目（见网站链接免责声明）。

通行密钥开发准备

仅当开发者使用FIDO2 C API开发时，需要申请如下通行密钥服务权限。在申请权限前，请保证符合权限使用的基本原则。申请方式请参考：申请受限权限。

应用能力	需要权限
通行密钥	ohos.permission.ACCESS_FIDO2_ONLINEAUTH

FIDO2协议基于应用的网址域名开通应用的通行密钥，开发者的应用需要关联网址域名，才可使用通行密钥服务。接入需完成四步：开通App Linking服务 > 建立域名与应用关联关系 > 在AGC为应用创建关联的网址域名 > 在module.json5中配置关联的网址域名。

DID数字身份开发准备

开发者需要部署符合W3C DID协议的服务器。

开发者基于数字身份服务开发时，需要申请如下数字身份权限。在申请权限前，请保证符合权限使用的基本原则。申请方式请参考：申请受限权限。

应用能力	需要权限
数字身份	ohos.permission.ACCESS_DIGITAL_IDENTITY
