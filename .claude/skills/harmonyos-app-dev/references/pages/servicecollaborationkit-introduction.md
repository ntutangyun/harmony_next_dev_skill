# Service Collaboration Kit简介

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaborationkit-introduction_

跨设备互通通常是指相机、扫描以及图库（图片和视频）能力的跨设备调用，例如：平板或2in1设备可以调用手机的相机、扫描、图库等功能。

约束与限制
支持的设备

跨设备互通（ArkTS）支持Phone、Tablet、PC/2in1、TV设备；跨设备互通NDK支持Phone、Tablet、PC/2in1、TV设备。

功能使用限制
能力	限制条件
跨设备互通能力	

- 双端设备需要登录同一华为账号；双端设备需要打开WLAN和蓝牙开关。

- 本端需使用HarmonyOS NEXT及以上版本的平板或2in1设备，远端需为具备相机能力的HarmonyOS NEXT及以上版本的手机或平板。

- 跨设备互通API支持根据特定调用策略调用设备。调用策略：2in1设备可以调用平板和手机，平板可以调用手机，从API 6.1.0(23)开始，TV、手机、平板或2in1设备可调用具备如下能力的远程设备：支持拍照、扫描及图库（图片与视频）能力的手机和平板，支持图库（图片与视频）能力的2in1设备。

- 对于6.1.0(23)之前版本，跨设备互通能力的接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力；对于6.1.0(23)及之后版本，跨设备互通能力的接口在TV、PC/2in1、Tablet、Phone可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。

模拟器支持情况

本Kit暂不支持模拟器。

Service Collaboration Kit（协同服务）
跨设备互通（ArkTS）
