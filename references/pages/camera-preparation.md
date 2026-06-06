# 申请相机开发的权限

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preparation_

在开发相机应用时，需要先申请相机相关权限，确保应用拥有访问相机硬件及其他功能的权限，需要的权限如下表。在申请权限前，请保证符合权限使用的基本原则。

使用相机拍摄前，需要申请ohos.permission.CAMERA相机权限。
当需要使用麦克风同时录制音频时，需要申请ohos.permission.MICROPHONE麦克风权限。
当需要拍摄的图片/视频显示地理位置信息时，需要申请ohos.permission.MEDIA_LOCATION，来访问用户媒体文件中的地理位置信息。

以上权限均需要配置文件权限声明和通过弹窗向用户申请授权，具体申请方式及校验方式，请参考声明权限和向用户申请授权。

当需要读取图片或视频文件时，请优先使用媒体库Picker选择媒体资源。
当需要保存图片或视频文件时，请优先使用安全控件保存媒体资源。
说明

仅应用需要克隆、备份或同步用户公共目录的图片、视频类文件时，可申请ohos.permission.READ_IMAGEVIDEO、ohos.permission.WRITE_IMAGEVIDEO权限来读写图片视频文件，申请方式请参考申请受控权限，通过AGC审核后才能使用。为避免应用的上架申请被驳回，开发者应优先使用Picker/控件等替代方案，仅少量符合特殊场景的应用被允许申请受限权限。

Camera Kit简介
开发相机应用必选能力(ArkTS)
