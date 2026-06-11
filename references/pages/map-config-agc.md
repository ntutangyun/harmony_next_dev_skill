# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-config-agc_

请优先开通地图服务后，再参考“应用开发准备”完成基本准备工作，然后再继续进行以下开发活动。

说明

从HarmonyOS 5.0.2(14)版本开始，开发者无需配置公钥指纹和Client ID。

从DevEco Studio 6.0.0 Beta5版本开始，支持在DevEco Studio中开通地图服务。

开通地图服务

Map Kit提供2种方式开通地图服务：

通过DevEco Studio开通地图服务。

通过AppGallery Connect网站开通地图服务。

方式一：通过DevEco Studio开通地图服务

登录DevEco Studio应用。

选择文件，点击项目结构。

进入“Signing Configs”页面，点击“Enable open capabilities”。

勾选“Map Kit”选项，点击“OK”。

选择“Apply”应用地图服务配置，点击“OK”完成地图服务配置。

方式二：通过AppGallery Connect网站开通地图服务。

登录AppGallery Connect网站，选择“开发与服务”。

在项目列表中找到您的项目，在项目下的应用列表中选择需要打开“地图服务”的应用。

选择开放能力管理，找到“地图服务”开关，打开开关。

确认已经开启“地图服务”开放能力，并完成签名。

调试阶段必须申请调试证书、注册设备、开启"地图服务"后重新申请调试Profile文件，并完成手动签名。

说明

若使用原有的Profile文件，请确保在申请Profile文件之前已开启“地图服务”。
