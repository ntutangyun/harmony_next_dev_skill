# 通过华为账号一键登录获取用户风险等级

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-get-risklevel-byquicklogin_

通过华为账号一键登录获取用户风险等级能力支持Phone、Tablet、PC/2in1设备。并且从5.1.1(19)版本开始，新增支持TV设备。

业务流程

图1 华为账号一键登录（用户首次登录应用）获取华为账号风险等级流程图

参考华为账号一键登录业务流程，确保系统账号已登录，匿名手机号获取成功，且用户首次使用华为账号登录应用。（如用户非首次使用华为账号登录，可通过华为账号其他方式登录获取用户风险等级来查询华为账号的风险等级）

调用LoginWithHuaweiIDButton组件，在LoginWithHuaweiIDButtonParams参数中设置风险等级字段标识riskLevel，拉起应用登录页。

用户同意协议后，点击华为账号一键登录按钮，应用可以通过HuaweiIDCredential获取到Authorization Code等数据。

将获取的Authorization Code数据传给应用服务端，应用服务端通过调用获取用户风险等级接口查询当前登录用户的华为账号风险等级。

应用基于用户风险等级判断继续登录流程或者返回对应风控措施。

接口说明

一键登录接口遵循华为账号一键登录接口说明，当应用需要获取用户风险等级时，在LoginWithHuaweiIDButton组件参数LoginWithHuaweiIDButtonParams中传入riskLevel字段，通过一键登录返回Authorization Code查询用户的风险等级。

接口名	描述
LoginWithHuaweiIDButtonParams	LoginWithHuaweiIDButton组件参数，支持传入riskLevel字段（可选），标识一键登录后可查询用户风险等级。
开发前提

在进行代码开发前，请确认已完成一键登录开发前提工作。

应用在使用获取风险等级能力之前，需要完成对应的scope权限申请。

scope权限申请审批未完成或未通过，将报错1001502014 应用未申请scopes或permissions权限。当前可通过发送邮件至accountkit@huawei.com进行申请。

请提供如下信息进行申请，我们会在1-2个工作日内回复申请结果，请您留意邮箱消息。

邮件主题：【获取风险等级】权限申请

邮件正文：（请在正文中描述下具体希望申请的权限）

企业名称：***

应用名称：***

应用包名：com.***.***

APP ID：1****12

Client ID：1****14

背景介绍： （请提供应用简单介绍，便于快速了解）

使用场景：（请提供相关使用场景的文字描述、交互流程图或参考交互视频等，可提供类似应用的使用场景进行说明）

使用该权限的必要性： （请提供应用需要该权限和信息的必要性）

客户端开发

一键登录前置流程（获取系统账号登录状态，获取系统账号匿名手机号）请参考一键登录开发流程中的导入模块及获取匿名手机号，确保系统账号已登录，匿名手机号获取成功，且用户首次通过华为账号登录该应用。

参考一键登录开发流程中展示一键登录页面并获取Authorization Code的示例代码，在LoginWithHuaweiIDButton组件参数params中设置riskLevel标识为true，其余示例代码保持不变，拉起应用登录页。

LoginWithHuaweiIDButton({
  params: {
    // LoginWithHuaweiIDButton支持的样式
    style: loginComponentManager.Style.BUTTON_RED,
    // 账号登录按钮在登录过程中展示加载态
    extraStyle: {
      buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
        show: true
      })
    },
    // LoginWithHuaweiIDButton的边框圆角半径
    borderRadius: 24,
    // LoginWithHuaweiIDButton支持的登录类型
    loginType: loginComponentManager.LoginType.QUICK_LOGIN,
    // LoginWithHuaweiIDButton支持按钮的样式跟随系统深浅色模式切换
    supportDarkMode: true,
    // verifyPhoneNumber：如果华为账号用户在过去90天内未进行短信验证，是否拉起Account Kit提供的短信验证码页面
    verifyPhoneNumber: true,
    // riskLevel：标识应用期望在登录后获取华为账号的风险等级
    riskLevel: true,
  },
  controller: this.controller
})

用户同意协议并点击一键登录按钮后，可获取到Authorization Code，将该值传给应用服务端用于获取用户风险等级。

服务端开发

应用服务端使用Client ID、Client Secret、Authorization Code调用获取用户级凭证接口向华为账号服务器请求获取Access Token、Refresh Token。

使用Access Token调用获取用户风险等级接口获取用户的风险等级。

Access Token过期处理

由于Access Token的有效期仅为60分钟，当Access Token失效或者即将失效时（可通过REST API错误码判断），可以使用Refresh Token（有效期180天）通过刷新用户级凭证接口向华为账号服务器请求获取新的Access Token。

说明

当Access Token失效时，若应用不使用Refresh Token向华为账号服务器请求获取新的Access Token，账号的授权信息将会失效，导致使用Access Token的功能都会失败。

当Access Token非正常失效（如修改密码、退出账号、删除设备）时，应用可重新登录授权获取Authorization Code，向华为账号服务器请求获取新的Access Token。

Refresh Token过期处理

由于Refresh Token的有效期为180天，当Refresh Token失效后（可通过REST API错误码判断），应用服务端需要通知客户端，重新调用授权接口，请求用户重新授权。

应用基于风险等级判别用户风险程度，决定是否需要对用户进行额外验证或拦截用户行为。

概述
华为账号其他方式登录获取用户风险等级
