# 操作日志

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-operation-log_

操作日志界面显示用户通过ohpm-repo管理界面进行的所有操作，以及通过ohpm命令行工具执行publish，unpublish和dist-tags等相关命令所记录的日志。操作日志界面分为两个部分：第一部分为筛选条件，第二部分是展示符合筛选条件的数据。

注意

操作日志的数据每隔一天会定时清除，默认保留100天内的操作日志数据，数据保留时间可通过config.yaml中配置项operation_log_retention设定。

一级事件类型	二级事件类型	三级事件类型
用户管理	新增用户	-
删除用户	-
修改用户角色	-
重置用户密码	-
仓库管理	管理仓库	新增仓库
删除仓库
更新代码仓
上架资源包
下架资源包
批量下架资源包
uplink	更新Uplink代理
添加Uplink
修改Uplink
删除Uplink
tag	增加Tag
更新Tag
删除Tag
权限管理	编辑包可见性
新增包白名单用户
删除包白名单用户
包权限管理	新增包所有者	-
删除包所有者	-
转移包所有者	-
新增包维护者	-
删除包维护者	-
认证管理	证书认证	添加发布公钥
删除发布公钥
Access Token	生成Access Token
删除Access Token
组织管理	组织	添加分组
修改分组
删除分组
组织成员	添加组成员
删除组成员
组织管理员	添加组管理员
删除组管理员
系统设置	更新oh-package.json5检查规则	-
重置系统密钥	-
更新系统安全配置	-
