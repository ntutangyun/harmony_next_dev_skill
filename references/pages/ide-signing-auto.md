# 自动签名

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing-auto_

功能介绍

HarmonyOS应用调试时，自动签名分为关联注册应用和未关联注册应用两种。

关联注册应用的自动签名：从DevEco Studio 6.0.0 Beta5版本开始支持，与应用市场（AppGallery Connect，简称AGC）的应用绑定，可在DevEco Studio开通开放能力和添加ACL权限，以及AGC与DevEco Studio的开放能力和权限信息可同步。

未关联注册应用的自动签名：未与应用市场的应用绑定。

约束与限制

DevEco Studio 6.1.1 Beta1及以上版本，关联注册应用的自动签名支持在各国家/地区使用。DevEco Studio 6.1.1 Beta1以下版本，关联注册应用的自动签名仅支持中国境内（不包含中国香港、中国澳门、中国台湾）。

使用自动签名前，请确保本地系统时间与北京时间（UTC/GMT+08:00）保持一致。如果不一致，将导致签名失败。

HarmonyOS工程

[h2]关联注册应用

说明

从26.0.0版本开始，支持在AGC注册设备后开始签名。

如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。

说明

点击Team下拉框，可以切换团队账号。

DevEco Studio根据Bundle name查询该团队在AGC上同包名的应用。若在AGC查询到应用，则进行自动签名；若在AGC未查询到应用或应用冲突，请根据提示信息修改后重新自动签名，具体修改请参考常见问题。

默认开启：默认勾选该开放能力，包括Account Kit、Location Kit、Intents Kit。

直接开启：点击开放能力名称，在界面右侧查看功能简介，勾选后可直接开启。

申请开启：点击开放能力名称，在界面右侧查看功能简介，填写申请理由（Application Reason）和上传附件（Upload Attachment）。申请后在AGC的互动中心页面可看到已提交的申请消息，具体请参考管理接入的华为开放能力。

说明

Push Kit（推送服务）开放能力接入后不可取消。

26.0.0以下版本

{
  "module": {
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
  }
}

说明

在申请ACL权限前，请审视是否符合受限权限的使用场景。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限。申请方式请见申请使用受限权限。

涉及受限权限的应用，在上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限。如不符合，应用的上架申请将被驳回，审核方式请见发布HarmonyOS应用。

在ACL权限申请审批完成前，可获得一个有效期较短的临时Profile证书，使应用完成签名。临时证书到期后，若申请仍未审批通过，签名时需再次申请和再次获取临时证书。

在ACL权限申请审批完成后，可获取一个有效期较长的正式Profile证书。

签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。

[h2]未关联注册应用

说明

从26.0.0版本开始，支持在AGC注册设备后开始签名。

如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。

{
  "module": {
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
  }
}

说明

在调试签名时，不会强制校验配置文件中添加的ACL权限。

涉及受限权限的应用，上架时，应用市场（AGC）将根据应用的使用场景审核是否可以使用对应的受限权限，如不符合，应用的上架申请将被驳回。在配置ACL权限前，请审视是否符合受限权限的使用场景。当前仅少量符合特殊场景的应用可在通过审批后，使用受限权限，申请方式请见申请使用受限权限。

签名完成后，在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b）。将鼠标悬停在Provisioning Profile: DevEco Managed Profile后，可查看证书有效期、包名（bundle name）、ACL权限（acl）、开放能力（capability）等信息；或进入工程级build-profile.json5文件，在“signingConfigs”下查看到配置成功的签名信息。

（可选）OpenHarmony工程

说明

OpenHarmony工程签名时，推荐使用HarmonyOS签名。因为OpenHarmony签名是Release签名，Release签名的应用不支持调试和打印debug日志等。此外，OpenHarmony签名可能会影响应用运行。

如果同时连接多个设备，则使用自动签名时，会同时将这多个设备的信息写到证书文件中。

连接本地真机设备/模拟器设备，或将真机调试设备注册到AGC设备列表后，开始签名。从26.0.0版本开始，支持在AGC注册设备后开始签名。

签名完成后，如下图所示。在本地生成密钥（.p12）、证书请求文件（.csr）、数字证书（.cer）及Profile文件（.p7b），数字证书在AGC网站的“证书、APP ID和Profile”页签中可以查看。

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

26.0.0版本

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
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
  }
}
```

### Code block 2

```
{
  "module": {
    "requestPermissions": [{
      "name": "ohos.permission.ACCESS_DDK_USB",
    }],
  }
}
```
