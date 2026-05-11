# 打开应用功能跳转第三方应用失败

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-2_

startAbility failed, code is 16000018, message is The application is not allow jumping to other applications when api version is above 11.

解决措施

需要执行命令手动开启限制开关。

hdc shell param set persist.sys.abilityms.support.start_other_app true
单击快速验证手机号按钮，无法拉起页面
剪贴板粘贴框遮挡智能填充选择框
