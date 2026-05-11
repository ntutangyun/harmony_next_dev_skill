# 一键登录场景下无法获取到匿名手机号如何解决

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-3_

当开发者开启了代码混淆时，为了防止quickLoginAnonymousPhone（匿名手机号）属性在release包中被混淆，请在调用“获取匿名手机号”方法所在工程模块的混淆文件obfuscation-rules.txt中添加如下配置：

# 开发者开启属性混淆需要配置quickLoginAnonymousPhone属性白名单防止其被混淆
-enable-property-obfuscation
-keep-property-name
quickLoginAnonymousPhone

Wearable、TV（非5.1.1版本）设备无法获取到手机号，会报1001500003 不支持该scopes或permissions。

华为账号未绑定手机号，该异常场景应用需要展示其他登录方式。

使用华为账号一键登录服务的账号必须是中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）华为账号。

确认是否在AGC的开发与服务中申请华为账号一键登录权限。图示为未申请状态，未申请将报错1001502014 应用未申请scopes或permissions权限。

申请的华为账号一键登录权限待审批或待生效，权限申请后需要24小时后生效或将调试设备的系统时间向后调整24小时后重试。

权限申请成功后，确认scope参数是否传入的是quickLoginAnonymousPhone，详情可参考一键登录客户端开发。

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 获取匿名手机号需传quickLoginAnonymousPhone这个scope，传参之前需要先申请“华为账号一键登录”权限，否则会返回1001502014错误码
authRequest.scopes = ['quickLoginAnonymousPhone'];
1001502014 应用未申请scopes或permissions权限的可能原因和解决方法
一键登录场景下无法获取到明文手机号如何解决
