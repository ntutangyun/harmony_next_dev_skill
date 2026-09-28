# 版本说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-releasenote_

ohpm-repo 6.0.1

[h2]新增特性

支持编辑个人的邮箱和手机号。具体请参考个人中心主页。

支持编辑用户的邮箱和手机号。具体请参考用户管理。

支持批量上传三方包。具体请参考仓库管理和配置文件

支持配置自定义登录验证插件。具体请参考自定义登录验证插件和配置文件。

私仓访问外部公仓时，支持进行https认证证书校验。具体请参考配置文件、ohpm-repo export_pkginfo、ohpm-repo batch_download和uplinks。

ohpm-repo 6.0.0

[h2]新增特性

在编辑仓库时，支持分别设置标准版本发布策略和先行版本发布策略。具体请参考仓库管理。

ohpm-repo 5.5.1

[h2]新增特性

支持返回固定版本的元数据。具体请参考ohpm仓库接口协议。

[h2]变更特性

ohpm-repo不再依赖node-fetch三方库

ohpm-repo依赖的node-fetch三方库由于长时间未更新维护。从ohpm-repo 5.5.1版本开始，不再依赖node-fetch三方库。

变更影响

基于ohpm-repo开发的插件，若使用了ohpm-repo依赖的node-fetch三方库，在升级到ohpm-repo 5.5.1版本后，使用该插件会有报错提示（找不到node-fetch库）。

适配指导

方案一：将该插件中的node-fetch替换成其他三方库。

方案二：在ohpm-repo安装包中执行“npm install node-fetch@2.7.0”，自行安装上node-fetch三方库。

ohpm-repo 5.4.5 Beta

[h2]新增特性

新增CheckUpdate API，支持查询当前引入的三方库是否有更新。具体请参考CheckUpdate。

ohpm-repo 5.4.3 Beta

[h2]新增特性

ohpm-repo支持基于dockerfile进行私仓服务搭建。具体请参考基于Dockerfile部署ohpm-repo私仓。

ohpm-repo拉取元数据时支持拉取精简版本的元数据。具体请参考ohpm仓库接口协议。

ohpm-repo 5.4.0

[h2]新增特性

ohpm-repo支持导出和导入包权限数据。具体请参考ohpm-repo export_pkgPermission和ohpm-repo import_pkgPermission。

ohpm-repo 5.3.0

[h2]新增特性

支持配置多个仓库，并能够为每个仓库设置可读策略，可写策略和发布策略。具体请参考仓库管理。

支持为每个包配置管理权限，支持配置包的查看者，维护者和所有者。具体请参考包权限管理。

ohpm-repo 5.2.0

[h2]新增特性

ohpm-repo支持三方库字节码文件的OHMUrl版本一致性校验。具体请参考content_check_plugin。

说明

更多历史版本请参考版本说明。
