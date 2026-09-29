# Enterprise Space Kit常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-faq_

编译失败，该如何解决

问题现象

编译不通过，签名证书缺少所需权限，报错：install failed due to grant request permissions failed.

解决措施

参考访问控制概述，检查应用签名是否正常配置权限。

如还未解决，请通过在线提单提交问题，华为支持人员会及时处理。

切换空间时，后台空间的应用无法启动或被终止

问题现象

切换空间时后台空间的应用被系统冻结，导致应用无法启动或被终止。

可能原因

为防止企业数据泄漏，空间切换时，后台空间的应用不可访问前台空间数据。

解决措施

调用setLockdownExemptionApps接口将应用加入豁免应用列表，确保应用可在后台空间正常运行，不会被冻结。
