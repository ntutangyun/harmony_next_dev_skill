# 401 参数检查失败的可能原因和解决办法

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-20_

问题现象

调用接口报错401 参数检查失败。

可能原因

必选参数没有传入。

参数类型错误 (Type Error)。

参数数量错误 (Argument Count Error)。

空参数错误 (Null Argument Error)。

参数格式错误 (Format Error)。

参数值范围错误 (Value Range Error)。

client_id配置错误。

应用运行的HarmonyOS系统版本为HarmonyOS 6.0.0(20)以下时，使用自动签名方式配置签名，未使用手动签名。

解决措施

请检查必选参数是否传入，传入的参数类型是否错误，以及传入的参数是否符合规格约束。

检查module type为entry的模块下module.json5中的client_id配置的值是否正确，请参考配置Client ID。

应用运行的HarmonyOS系统版本为HarmonyOS 6.0.0(20)以下时，请使用手动签名方式配置签名。详情请参考配置签名和指纹。
