# 仅MDM应用可用权限

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-mdm-apps_

以下权限仅对MDM（Mobile Device Management）设备管理应用开放。

企业MDM应用：

企业MDM应用定义：

企业MDM（Mobile Device Management）应用从移动端设备管控应用延伸而来，在HarmonyOS中表示对1+8设备提供高级管控能力的应用，包括对设备、应用、外设等的管理，如设置禁止连接WiFi、禁止使用USB设备等限制。

企业MDM应用仅支持在企业场景下使用，设备需在华为HEM平台进行注册管理或者为搭载鸿蒙电脑专业版、企业版的PC设备。

企业MDM应用发布开发指导：

申请企业MDM应用发布证书、申请企业MDM应用发布Profile。

企业MDM应用支持格式：

支持.hap，.app，需要为单个应用包体。

如果包含多个hap、hsp文件，需打包为.app格式，且需要在工程级build-profile.json5文件中，将packOptions的appWithSignedPkg属性配置为true，保证APP里的HAP/HSP包均被签名。

企业MDM应用安装方式：

设备注册纳管到华为HEM平台，在首次开机时通过HEM平台批量部署。

在搭载鸿蒙电脑专业版、企业版的PC设备上，开启离线应用安装开关后本地直接安装。

通过上架企业私有应用商店（企业MDM应用）在企业内部进行统一分发安装。

企业MDM应用无法上架华为应用市场进行公开、非公开发布。

说明

HarmonyOS系统以应用包名作为应用的唯一标识，不同的发布证书代表不同的应用版本，需创建不同的应用包名。

ohos.permission.ENTERPRISE_GET_DEVICE_INFO

允许应用激活设备管理应用。

包括读取设备ID、读取设备硬盘序列号，读取OS版本、读取机器名。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_GET_NETWORK_INFO

允许设备管理应用查询网络信息。

包括查询网卡设置、IP地址、MAC地址，网卡启用状态。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_INSTALL_BUNDLE

允许设备管理应用安装和卸载包。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_core

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_MANAGE_SET_APP_RUNNING_POLICY

允许设备管理应用设置应用运行管理策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_RESET_DEVICE

允许设备管理应用恢复设备出厂设置。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_SET_ACCOUNT_POLICY

允许设备管理应用设置账户管理策略。

比如新增账号。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_SET_BUNDLE_INSTALL_POLICY

允许设备管理应用设置包安装管理策略。

比如设置包安装白名单。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_SET_DATETIME

允许设备管理应用设置系统时间。

包括设置系统时间值，禁止用户修改系统时间策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：9

ohos.permission.ENTERPRISE_SET_NETWORK

允许设备管理应用设置网络信息。

包括禁用、开启网卡。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_SET_WIFI

允许设备管理应用设置和查询WiFi信息。

可设置和查询WiFi禁用，设置WiFi连接。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT

允许设备管理应用订阅管理事件。

比如应用安装事件、应用卸载事件和系统更新事件等。订阅成功后，事件触发时会通知设备管理应用。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：9

ohos.permission.ENTERPRISE_RESTRICT_POLICY

允许设备管理员下发和获取限制类策略。

比如禁用HDC，禁用直连打印服务等。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_SET_SCREENOFF_TIME

允许设备管理员设置系统休眠时间。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_MANAGE_USB

允许设备管理员管理USB。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_MANAGE_NETWORK

允许设备管理员管理网络。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_MANAGE_CERTIFICATE

允许设备管理员管理证书。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_GET_SETTINGS

允许设备管理员查询“设置”应用数据。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.ENTERPRISE_SET_BROWSER_POLICY

允许设备设置/取消浏览器策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：10

ohos.permission.SET_ENTERPRISE_INFO

允许设备管理应用设置企业信息。

企业设备管理器激活后可设置企业组织信息，包括企业名称和描述信息，用于system UI展示设备被所属管理信息。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：9

ohos.permission.ENTERPRISE_MANAGE_SECURITY

允许设备设置安全管理策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

允许设备管理应用设置和查询蓝牙信息。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_MANAGE_SYSTEM

允许设备管理系统设置参数策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_MANAGE_WIFI

允许设备管理应用设置和查询WIFI信息。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

允许设备管理应用管理限制策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_MANAGE_APPLICATION

允许设备管理应用管理应用策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_MANAGE_LOCATION

允许设备管理应用设置和查询位置信息。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_REBOOT

允许设备管理应用进行关机重启操作。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_LOCK_DEVICE

允许设备管理应用锁定设备。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_MANAGE_SETTINGS

允许设备管理应用管理设置。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：11

ohos.permission.ENTERPRISE_OPERATE_DEVICE

允许设备管理应用操作设备。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

起始版本：12

ohos.permission.ENTERPRISE_ADMIN_MANAGE

允许应用管理设备管理应用。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：12

ohos.permission.ENTERPRISE_RECOVERY_KEY

允许设备管理应用管理企业级恢复密钥。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_core

授权方式：系统授权（system_grant）

起始版本：13

ohos.permission.ENTERPRISE_MANAGE_DELEGATED_POLICY

允许设备管理应用委托其他应用设置设备管控策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：14

ohos.permission.ENTERPRISE_GET_ALL_BUNDLE_INFO

允许设备管理应用获取设备所有应用信息。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：20

ohos.permission.ENTERPRISE_SET_USER_RESTRICTION

允许设备管理应用限制用户修改系统设置。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：20

ohos.permission.ENTERPRISE_MANAGE_APN

允许设备管理应用管理设备APN策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：20

ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

允许设备管理应用管理设备通话策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：20

ohos.permission.ENTERPRISE_SET_KIOSK

允许设备管理应用设置Kiosk模式。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：20

ohos.permission.ENTERPRISE_MANAGE_LOCAL_PUBLICSPACES

允许企业应用启用、创建、删除工作空间。

获取此权限后，应用可以设置空间切换免密登录时间、用户照片、不允许删除的空间列表等。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：PC/2in1

起始版本：20

ohos.permission.ENTERPRISE_FILE_TRANSFER_AUDIT_POLICY_MANAGEMENT

允许设备管理应用管理文件传输的策略和审计信息。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：PC/2in1

起始版本：20

ohos.permission.ENTERPRISE_SET_WALLPAPER

允许设备管理应用设置壁纸。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：20

ohos.permission.MANAGE_PREINSTALLED_ANTIVIRUS

允许设备管理应用管理系统预装的防病毒软件。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：PC/2in1

起始版本：20

ohos.permission.ENTERPRISE_MANAGE_USER_GRANT_PERMISSION

允许设备管理应用设置user_grant类权限策略。

获取该权限后，设备管理应用可设置被管理应用user_grant类权限策略，策略支持静默授予、拒绝授予以及默认（即不影响应用申请）。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：20

ohos.permission.ENTERPRISE_DATA_IDENTIFY_FILE

允许设备管理应用识别文件敏感内容。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_core

授权方式：系统授权（system_grant）

支持设备：PC/2in1

起始版本：21

ohos.permission.ENTERPRISE_ACCESS_DLP_FILE

允许设备管理应用生成、解密DLP文件，查询DLP文件策略。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_core

授权方式：系统授权（system_grant）

支持设备：PC/2in1

起始版本：20

变更信息：在API20，该权限面向系统应用开放；从API 21开始，面向MDM应用开放。

ohos.permission.ENTERPRISE_MANAGE_DEVICE_ADMIN

允许应用管理其他设备管理应用。

获取该权限后，超级设备管理应用可管理其他设备管理应用。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：23

ohos.permission.ENTERPRISE_START_ABILITIES

允许设备管理应用访问其他组件。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：23

ohos.permission.ENTERPRISE_READ_LOG

允许设备管理应用收集系统日志。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：23

ohos.permission.ENTERPRISE_DEACTIVATE_DEVICE_ADMIN

允许已激活的设备管理应用解除自身的激活状态。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：23

ohos.permission.ENTERPRISE_ACTIVATE_DEVICE_ADMIN

允许企业设备管理应用自行完成激活操作。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | PC/2in1 | Tablet

起始版本：24

ohos.permission.ENTERPRISE_MANAGE_LOCAL_ACCOUNTS

允许企业设备管理应用管理本地账号。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：Phone | Tablet

起始版本：26.0.0

ohos.permission.ENTERPRISE_INTERACT_ACROSS_LOCAL_ACCOUNTS

允许企业设备管理应用进行多用户操作。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_core

授权方式：系统授权（system_grant）

支持设备：Phone | Tablet

起始版本：26.0.0

ohos.permission.ENTERPRISE_VPN

允许设备管理应用默认拥有VPN接入权限。

获取此权限后，应用无需经过用户确认，默认可接入VPN。

申请后AGC的审核时长： 预计3个工作日内反馈审核结果。

权限级别：system_basic

授权方式：系统授权（system_grant）

支持设备：PC/2in1

起始版本：26.0.0
