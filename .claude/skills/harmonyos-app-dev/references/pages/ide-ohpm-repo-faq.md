# 常见问题FAQ

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-faq_

使用证书认证在git-bash终端下执行ohpm publish XX.har发包到ohpm-repo中报错：The content of private key in the key_path error
使用AccessToken认证，执行publish/unpublish/dist-tags等命令失败
应用内hsp包如何发布到ohpm-repo
执行ohpm-repo命令报错
在执行ohpm-repo install或者ohpm-repo start的时候报错：server install failed: YAMLException: bad indentation of a mapping entry
执行命令ohpm-repo <command>，报错ohpm-repo不存在或者<command>命令不存在。
ohpm-repo成功启动后，根据配置文件中的listen值访问ohpm-repo私仓管理界面，界面不显示信息或者无法打开页面
机器A部署ohpm-repo私仓服务，在机器B上通过A的域名+端口访问已部署的ohpm-repo私仓服务，打开包的描述页出错
执行ohpm-repo install时报错：fail to initialize encryption component: Error: invalid crypto component.
执行ohpm publish XX.har发包到ohpm-repo私仓中报错
报错：connect ECONNREFUSED ::1:8089
报错：The content of private key in the key_path error.
报错：HttpCode 400 Group does not exist!
报错：HttpCode 400 You are not a developer of the group!
报错：ohpm ERROR: HttpCode 404 Not Found
报错：Same ohpm package is exists!
报错：Request Entity Too Large
报错：The packageType is no equals the exists packageType!
执行ohpm install XX.har从ohpm-repo私仓中下载包报错
ohpm-repo配置uplink后，执行install命令下载uplink所配置仓库中的包失败
访问ohpm-repo私仓管理界面报错
访问ohpm-repo私仓管理界面中页面功能，报错：非法请求
访问ohpm-repo私仓管理页面，报错“加密组件无效”。
访问ohpm-repo私仓管理界面，报错：“系统配置错误，请联系管理员”
配置ohpm-repo私仓工具环境变量
Windows环境
Linux和macOS环境
展开章节
ohpm-repo私仓工具获取与升级
从下载中心上获取最新ohpm-repo工具包。

ohpm-repo升级指导：在升级之前请务必进行好数据的备份，具体的升级指导文档见：ohpm-repo版本升级。
现象：报错信息如下：

原因分析：在ohpm-repo私仓部署根目录deploy_root中，加密组件meta文件受到损坏，处于失效状态。ohpm-repo私仓中，uplink的代理地址信息和证书认证的公钥信息均通过meta加密组件进行加密存储。
解决方法：
如果是版本升级导致的问题，请找回上一个版本中meta文件，替换当前版本的meta文件。
其他原因导致meta文件损坏，需要执行如下步骤：
清空数据库中表publickey和uplinkproxy中的内容（操作数据库前请提前备份，避免误删数据影响开发）。
删除受损的meta文件。
重新执行ohpm-repo install命令，生成新的meta文件。
在ohpm-repo管理界面的仓库管理处，重新配置uplink的代理信息。
在ohpm-repo管理界面的认证管理处，重新配置证书认证的公钥数据。
解决方法：有一些三方包包含组织名，只有发布包的用户在该组织下才具有发包的能力。报错信息表明已经有管理员账户添加了该包组织，但是当前账户没有在该组织的成员里面。在ohpm中包的命名格式为@<group>/<package_name>，其中<group>为组织名，找到创建<group>组织的负责人账户，然后负责人账户登录ohpm-repo管理界面，进入组织的详情里，添加需要发包的账户为组织的成员，成员即可发布具有对应组织名的包。

现象：访问ohpm-repo私仓管理界面的页面功能，报错“非法请求”。

原因分析：在ohpm-repo私仓5.0.2版本中，新增接口防重放攻击机制，该机制将校验ohpm-repo私仓所有涉及修改数据请求中的时间戳。若请求携带的时间戳与服务器当前时间相差超过1分钟（超前或滞后），系统将拒绝该请求，并返回“非法请求”错误。
解决方法：为确保系统正常运行，请保持服务器与客户端浏览器时间同步。
现象：打开ohpm-repo私仓管理界面，访问仓库管理页面中uplink代理配置页面，或访问认证管理页面中证书认证配置页面，报错“加密组件无效”，且已经配置的信息被清空。

原因：uplink代理的地址信息和证书认证的公钥信息存储均需要加密，加密组件为ohpm-repo私仓部署根目录deploy_root中的meta文件。如果加密时的meta文件和解密时的meta文件不一致，会导致解密数据失败。
解决方法：
如果是版本升级导致的问题，请找回上一个版本中meta文件，替换当前版本的meta文件，保证加密组件的一致性。
其他原因导致使用meta文件解密失败，需要执行如下步骤：
清空数据库中表publickey和uplinkproxy中的内容（操作数据库前请提前备份，避免误删数据影响开发）。
删除解密失败的meta文件。
重新执行ohpm-repo install命令，生成新的meta文件。
在ohpm-repo管理界面的仓库管理处，重新配置uplink的代理信息。
在ohpm-repo管理界面的认证管理处，重新配置证书认证的公钥数据。
现象：访问ohpm-repo私仓管理界面，在ohpm-repo管理界面报错“非法请求”，在ohpm-repo运行日志报错：“verify reverse proxy usage: set "use_reverse_proxy" to false in config.yaml if not used, or refresh "x-forwarded-for" in Nginx if it is.”。

原因分析：在ohpm-repo私仓5.0.7版本中，配置文件新增配置项use_reverse_proxy，用于判断是否已使用反向代理。如果配置use_reverse_proxy值为true，但未使用反向代理或者在配置反向代理时未刷新x-forwarded-for值，将导致从请求头获取到x-forwarded-for值为空，报此错误。
解决方法：只有已使用反向代理，才能够将配置项use_reverse_proxy置为true，且需要在反向代理配置时刷新x-forwarded-for值（如果存在多级代理，只需要在最外层代理配置），配置命令为：“proxy_set_header x-forwarded-for $remote_addr”。
安全配置指南
附录
