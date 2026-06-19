# 配置调试签名

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing_

针对开发调试场景，DevEco Studio为开发者提供了自动签名方案，帮助开发者高效进行调试。此外，也可以选择手动签名方式生成调试签名。

使用场景说明

当需要进行跨设备调试、跨应用交互调试、断网情况下调试或者多用户共同开发且需要共享密钥时，必须使用手动签名。

使用部分不支持自动签名的受限开放权限时，必须使用手动签名。支持自动签名的ACL权限清单请参见自动签名支持的ACL权限。

需要华为业务方审核的权限时（例如华为账号一键登录等），必须使用手动签名。

若kit需要配置指纹，建议使用手动签名。

发布场景必须使用手动签名。

自动签名

DevEco Studio 6.0.0 Beta3及之前版本，自动签名未关联注册的应用。

从DevEco Studio 6.0.0 Beta5版本开始，自动签名新增关联注册应用的方式，签名操作界面新增“Associate with registered application”选项。

关联注册应用的自动签名：与应用市场（AppGallery Connect，简称AGC）的应用绑定，可在DevEco Studio开通开放能力。

未关联注册应用的自动签名：未与应用市场的应用绑定，不支持在DevEco Studio开通开放能力。

[h2]约束与限制

从DevEco Studio 6.1.1 Beta1版本开始，关联注册应用的自动签名支持在所有国家/地区使用。

使用自动签名前，请确保本地系统时间与北京时间（UTC/GMT+08:00）保持一致。如果不一致，将导致签名失败。

[h2]关联注册应用

操作步骤

说明

如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。

说明

点击Team下拉框，可以切换团队账号。

开始签名后，DevEco Studio根据Bundle name查询该团队在AGC上同包名的应用。若在AGC查询到应用，则进行自动签名；若在AGC未查询到应用或应用冲突，请根据提示信息修改后重新自动签名，具体修改请参考常见问题。

默认开启：默认勾选该开放能力，包括Account Kit、Location Kit、Intents Kit。

直接开启：点击开放能力名称，在界面右侧查看功能简介，勾选后可直接开启。

申请开启：点击开放能力名称，在界面右侧查看功能简介，填写申请理由（Application Reason）和上传附件（Upload Attachment）。申请后在AGC的互动中心页面可看到已提交的申请消息，具体请参考管理接入的华为开放能力。

说明

Push Kit（推送服务）开放能力接入后不可取消。

{
  "module": {
    ...
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
    ...
  }
}

26.0.0 Beta1及以上版本

Enable ACL Permissions +下会显示配置文件中添加的ACL权限，点击Enable ACL Permissions +，在ACL Permission Configuration窗口会显示未申请的ACL权限，填写申请理由（Request reason）和附件（Attachment）等，点击OK。在AGC中查看权限申请进度，具体请参考申请ACL权限。

26.0.0 Beta1以下版本

修改配置文件后，在签名界面点击OK，若应用已在AGC申请该权限则签名成功；若应用未申请该权限，会导致签名失败，点击Notice弹窗中"submit a permission request in AppGallery Connect"或"Submit"，跳转至AGC申请权限，然后再返回DevEco Studio界面重新签名。

说明

在申请ACL权限前，请审视是否符合受限权限的使用场景。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限。申请方式请见申请使用受限权限。

涉及受限权限的应用，在上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限。如不符合，应用的上架申请将被驳回，审核方式请见发布HarmonyOS应用。

在ACL权限申请审批完成前，可获得一个有效期较短的临时Profile证书，使应用完成签名。临时证书到期后，若申请仍未审批通过，签名时需再次申请和再次获取临时证书。

在ACL权限申请审批完成后，可获取一个有效期较长的正式Profile证书。

签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

[h2]未关联注册应用

HarmonyOS工程按以下步骤操作：

说明

如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。

{
  "module": {
    ...
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
    ...
  }
}

说明

在调试签名时，不会强校验配置文件中添加的ACL权限。

涉及受限权限的应用，上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限，如不符合，应用的上架申请将被驳回。在配置ACL权限前，请审视是否符合受限权限的使用场景。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，申请方式请见申请使用受限权限。

签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

OpenHarmony工程按以下步骤操作：

签名完成后，如下图所示。在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b），数字证书在AGC网站的“证书、APP ID和Profile”页签中可以查看。

说明

OpenHarmony工程签名时，推荐使用HarmonyOS签名。因为OpenHarmony签名是Release签名，Release签名的应用不支持调试和打印debug日志等。此外，OpenHarmony签名可能会影响应用运行。

如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。

手动签名

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请调试数字证书和调试Profile文件前，需要通过DevEco Studio生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）

密钥：格式为.p12，包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，公钥和私钥用于数字签名和验证。

证书请求文件：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和通用名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。

数字证书：格式为.cer，由华为AppGallery Connect颁发。

Profile文件：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

从DevEco Studio 6.1.0 Beta2版本开始，手动签名时，生成密钥和证书请求文件的操作界面发生变更。

[h2]生成密钥和证书请求文件

DevEco Studio 6.1.0 Beta2及之后版本

在主菜单栏单击Build > Generate Key and CSR。

Keystore Name：填写p12文件名称，仅允许包含字母、数字、下划线（_）、中划线（-）、句号（.）。

Select file save path：设置密钥库文件存储路径。

Key store password：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。

Confirm password：再次输入密钥库密码。

Alias：密钥别名。请记住该别名，后续签名配置需要使用。

Validity(years)：选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。

First and last name：选填，通用名称，可填写应用名称或开发者姓名等。

Organizational unit：选填，组织单位，可填写部门名称或个人开发等。

Organization：选填，组织名称，可填写公司全称或开发者姓名等。

City or locality：选填，城市或地区。

State or province：选填，州或省。

Country code(XX)：选填，国家码。

说明

First and last name、Organizational unit、Organization、City or locality、State or province填写要求小于64个字符，不可使用双引号（"）、斜杠（\）、反引号（`）。

CSR File Name：填写CSR文件名称，仅允许包含字母、数字、下划线（_）、中划线（-）、句号（.）。

Select file save path：设置CSR文件存储路径。

DevEco Studio 6.1.0 Beta2之前版本

说明

如果本地已有对应的密钥，无需新生成密钥，可以在Generate Key界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。

Key store file：设置密钥库文件存储路径，并填写p12文件名。

Password：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。

Confirm password：再次输入密钥库密码。

Alias：必填，别名，用于标识密钥名称。请记住该别名，后续签名配置需要使用。

Password：必填，密码，与密钥库密码保持一致，无需手动输入。

Validity(years)：选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。

First and last name：选填，通用名称，可填写应用名称或开发者姓名等。

Organizational unit：选填，组织单位，可填写部门名称或个人开发等。

Organization：选填，组织名称，可填写公司全称或开发者姓名等。

City or locality：选填，城市或地区。

State or province：选填，州或省。

Country code(XX)：选填，国家码。

说明

First and last name、Organizational unit、Organization、City or locality、State or province要求：字符长度为（0，64），且不可使用双引号（"）、斜杠（\）、反引号（`）。

[h2]申请调试证书

说明

如您未在AGC中注册该应用，申请前需要在AGC中注册，具体请参考创建HarmonyOS应用。

[h2]申请调试Profile文件和添加权限信息

说明

ACL权限申请仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

若应用因特殊场景要求使用受限开放权限，请务必在此步骤进行申请，否则应用将在审核时被驳回。受限开放权限可申请的特殊场景请参考受限开放权限。

确保应用申请受限开放权限时提供的场景和功能信息准确。如果应用内使用的受限开放权限超出您申请的范围，或申请权限后使用的功能和场景超出可使用的范围，将影响应用上架。

{
  "module": {
    ...
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
    ...
  }
}

在AGC中申请和下载Profile文件，具体请参考申请调试Profile。

[h2]配置签名信息

Store file：选择密钥库文件，文件后缀为.p12，该文件为生成密钥和证书请求文件中生成的.p12文件。

Store password：输入密钥库密码，该密码与生成密钥和证书请求文件中填写的密钥库密码保持一致。

Key alias：输入密钥的别名信息，与生成密钥和证书请求文件中填写的别名保持一致。

Key password：输入密钥的密码，与生成密钥和证书请求文件中填写的Store Password保持一致。

Sign alg：签名算法，固定为SHA256withECDSA。

Profile file：选择申请调试Profile文件和添加权限信息中生成的Profile文件，文件后缀为.p7b。

Certpath file：选择申请调试证书中生成的数字证书文件，文件后缀为.cer。

说明

Store file，Profile file，Certpath file三个字段支持配置相对路径，以项目根目录为起点，配置文件所在位置的路径名称。

密钥库文件、密钥库密码、密钥别名、密钥密码、Profile文件、数字证书文件必须配套使用，否则会导致签名失败。若失败请根据报错信息进行修改，再进行签名。

配置完成后，将鼠标悬停在Provisioning Profile: DevEco Manage Profile后，可查看证书有效期、包名（bundle name）、企业名称（common name）、ACL权限（acl）、开放能力（capability）相关信息；或者进入工程级build-profile.json5文件，在“signingConfigs”下可查看到配置成功的签名信息。

附录

[h2]自动签名支持的ACL权限

自动签名当前支持申请的ACL权限的清单如下所示。执行操作步骤后，DevEco Studio将校验当前配置的ACL权限是否在以下列表中，然后通过应用市场（AGC）申请对应的Profile文件，用于签名打包，从而避免繁琐的手动签名步骤。

从DevEco Studio 6.1.0 Beta2版本开始，自动签名支持配置的ACL权限具体参考受限开放权限。

6.0.2 Beta1

新增权限

ohos.permission.SUBSCRIBE_NOTIFICATION

ohos.permission.ACCESS_USER_FULL_DISK

ohos.permission.CUSTOM_SCREEN_RECORDING

ohos.permission.GET_IP_MAC_INFO

6.0.1 Release（6.0.1.260）

新增权限

ohos.permission.SET_SYSTEMSHARE_APPLAUNCHTRUSTLIST

ohos.permission.HOOK_KEY_EVENT

ohos.permission.WEB_NATIVE_MESSAGING

6.0.0 Beta3

新增权限

ohos.permission.CUSTOMIZE_SAVE_BUTTON

ohos.permission.GET_ABILITY_INFO

ohos.permission.LINKTURBO

ohos.permission.GET_WIFI_LOCAL_MAC

ohos.permission.GET_ETHERNET_LOCAL_MAC

ohos.permission.USE_FLOAT_BALL

ohos.permission.READ_LOCAL_DEVICE_NAME

ohos.permission.ACCESS_NET_TRACE_INFO

ohos.permission.KEEP_BACKGROUND_RUNNING_SYSTEM

ohos.permission.atomicService.MANAGE_STORAGE

ohos.permission.MANAGE_SCREEN_TIME_GUARD

5.1.0 Release

新增权限

ohos.permission.ACCESS_DDK_USB_SERIAL

ohos.permission.ACCESS_DDK_SCSI_PERIPHERAL

ohos.permission.USE_FRAUD_APP_PICKER

5.0.5 Release

新增权限

ohos.permission.kernel.DISABLE_GOTPLT_RO_PROTECTION

ohos.permission.MANAGE_APN_SETTING

5.0.3 Release

新增权限

ohos.permission.READ_WRITE_USB_DEV

ohos.permission.USE_FRAUD_CALL_LOG_PICKER

ohos.permission.USE_FRAUD_MESSAGES_PICKER

ohos.permission.ACCESS_DISK_PHY_INFO

ohos.permission.SET_PAC_URL

ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

ohos.permission.START_PROVISIONING_MESSAGE

ohos.permission.PRELOAD_FILE

ohos.permission.kernel.ALLOW_WRITABLE_CODE_MEMORY

ohos.permission.kernel.DISABLE_CODE_MEMORY_PROTECTION

ohos.permission.kernel.ALLOW_EXECUTABLE_FORT_MEMORY

ohos.permission.GET_WIFI_PEERS_MAC

ohos.permission.READ_WRITE_DESKTOP_DIRECTORY

ohos.permission.MANAGE_PASTEBOARD_APP_SHARE_OPTION

ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

ohos.permission.READ_WRITE_USER_FILE

5.0.0 Release

支持权限

ohos.permission.READ_CONTACTS

ohos.permission.WRITE_CONTACTS

ohos.permission.READ_AUDIO

ohos.permission.WRITE_AUDIO

ohos.permission.READ_IMAGEVIDEO

ohos.permission.READ_PASTEBOARD

ohos.permission.WRITE_IMAGEVIDEO

ohos.permission.ACCESS_DDK_USB

ohos.permission.ACCESS_DDK_HID

ohos.permission.SYSTEM_FLOAT_WINDOW

ohos.permission.FILE_ACCESS_PERSIST

ohos.permission.INPUT_MONITORING

ohos.permission.INTERCEPT_INPUT_EVENT

ohos.permission.SHORT_TERM_WRITE_IMAGEVIDEO

[h2]自动签名支持的开放能力

26.0.0 Beta1

Intents Kit (意图框架)

Location Kit（定位服务）

Indoor high-precision positioning（室内高精度定位）

Semantic location（位置语义）

Background wake-up triggered by Beacon geofence（围栏后台唤醒）

Bluetooth scan information retrieval (获取蓝牙扫描信息)

Account Kit（华为账号）

HUAWEI ID instant login （华为账号一键登录）

Obtain user's mobile number （获取您的手机号）

Obtain shipping address （获取收货地址）

Push Kit（推送服务）

the In-App Call Message（推送应用内通话消息）

Push text-to-speech messages （推送语音播报消息）

Device status detection （应用设备状态检测）

Map Kit（地图服务）

Safety Detect （安全检测服务）

Standby form （待机屏保卡片）

Back transparent card （背板透明卡片）

Second-Level Game Launch (秒级启动)

Live View Kit （实况窗服务）

Agent-powered reminder （代理提醒）

SmartFill (智能填充)

Digital Shield Service (数字盾服务)

Lock screen widget （锁屏卡片）

6.0.0 Beta5

Push Kit（推送服务）

Device status detection（应用设备状态检测）

Map Kit（地图服务）

Safety Detect（安全检测服务）

## Code blocks

### Code block 1

```
{
  "module": {
    ...
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
    ...
  }
}
```

### Code block 2

```
{
  "module": {
    ...
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
    ...
  }
}
```

### Code block 3

```
{
  "module": {
    ...
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
    ...
  }
}
```
