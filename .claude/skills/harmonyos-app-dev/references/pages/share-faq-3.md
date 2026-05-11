# 分享时提示“您选择的文件不支持分享”

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-faq-3_

排查分享过程中，文件是否真实存在并且拥有文件的访问权限，可使用fs.stat尝试访问文件，并通过比较文件创建时间和分享发起时间确认文件存在。

分享数据类型不支持
Wallet Kit（钱包服务）
