# 1001502003 输入参数值无效的可能原因和解决办法

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-22_

一键登录场景，传入的匿名手机号不正确，或是未调用授权API（AuthorizationWithHuaweiIDRequest）获取匿名手机号。

接口传参异常，如调用授权API（AuthorizationWithHuaweiIDRequest）时scopes和permissions属性均为空。

解决措施

在 AppGallery Connect（简称AGC）的开发与服务中，选择对应的项目和对应的应用，在“常规 > 应用 ”下，找到应用的Client ID和APP ID。

若Client ID和APP ID不同：请检查module type为entry的模块下module.json5中的client_id是否配置或配置的值是否正确，参考配置Client ID。

若Client ID和APP ID相同：可无需配置Client ID。

请在AppGallery Connect中重新申请Profile文件并重新进行签名。在调试阶段，请参考申请调试Profile，完成Profile申请并重新手动签名；在发布阶段，请参考申请发布Profile，完成Profile申请并重新手动签名。

需要通过授权API（AuthorizationWithHuaweiIDRequest）获取到匿名手机号，将其作为参数调用一键登录接口。

检查authentication相关接口参数。

60180007 服务端通过Authorization Code无法获取到华为账号一键登录手机号如何解决
个人数据处理说明
