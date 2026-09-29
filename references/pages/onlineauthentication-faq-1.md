# IFAA常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-faq-1_

开通IFAA免密认证失败

问题现象

开通IFAA免密认证失败。

可能原因

移动端设备没有联网。

解决措施

移动端设备连接Wi-Fi或热点，再次尝试。

IFAA认证超时失败

问题现象

IFAA认证报错The service is abnormal。

可能原因

IFAA进程是非常驻进程，拉起后有时间限制。只有preAuth接口拉起IFAA进程时有1分钟的保活时间，其余接口拉起IFAA进程的保活时间均为10秒。如果在preAuth和auth之间调用了getAnonymousId等其他接口，会将保活时间刷新为10秒，导致preAuth和auth之间的时间间隔超出10秒后IFAA进程退出，auth调用超时失败。

解决措施

确保preAuth和auth连续调用，在preAuth和auth之间不要调用其他IFAA接口，如getAnonymousId，避免保活时间被刷新为10秒导致超时。

可通过hilog日志辅助排查：

查看日志中“ifaa delay unload time is”确认当前IFAA进程的保活时间。

若日志中出现“Service unloaded successfully.”，表示IFAA进程已退出，后续调用auth接口会失败。
