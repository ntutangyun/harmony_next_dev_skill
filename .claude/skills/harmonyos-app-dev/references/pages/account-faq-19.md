# 不同开发者的应用之间如何实现用户数据互通

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-19_

不同开发者的应用，可以使用GroupUnionID关联用户数据来实现数据互通。GroupUnionID是华为账号用户在关联主体账号组内的唯一标识。不同开发者账号加入同一关联主体账号组后，其组内所有开发者的应用获取到用户的GroupUnionID相同。应用获取GroupUnionID流程如下：

开发者账号加入同一关联主体账号组。

通过创建账号组创建关联主体账号组，在关联主体账号组中添加账号组成员。

获取GroupUnionID。

针对新用户，在登录时可以直接获取GroupUnionID，具体指导请参考：通过Authorization Code获取GroupUnionID。

针对已获取OpenID或UnionID的用户，可以批量获取GroupUnionID，具体指导请参考：通过OpenID或UnionID获取GroupUnionID。

注意

GroupUnionID是一个大小写敏感的字符串，最大长度为64字符，在存储、查询、比较GroupUnionID时，请务必保留其原始大小写。

三方开发框架接入华为账号一键登录
401 参数检查失败的可能原因和解决办法
