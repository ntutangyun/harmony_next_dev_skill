# 受限ACL权限申请

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screentimeguard-permission-application_

调用Screen Time Guard Kit相关能力之前，需要检查是否已经获取"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限。该权限允许应用调用屏幕时间守护相关接口，进行屏幕使用限制、应用访问控制、管控使用时间等操作。如未获取授权，则需申请相应的权限。

在 申请调试Profile和发布Profile文件之前，需要申请相应的ACL权限。

登录AppGallery Connect，点击“开发与服务”，在项目列表中找到对应的项目，并点击选择您需要申请ACL权限的应用。在“项目设置”页面，选择“ACL权限”页签，开始为应用申请ACL权限。

在核对注意事项后，在“未获取权限”区域中勾选“我已知晓”。在权限搜索框中输入"ohos.permission.MANAGE_SCREEN_TIME_GUARD"，查找并勾选权限，提交申请。

根据实际业务需求填写申请原因并提交，提交后将在1个工作日回复。

权限申请通过后，在申请profile文件时，在“申请权限”栏选中“受限ACL权限（HarmonyOS API9及以上）”选项，点击“选择”。

在弹出的“选择受限ACL权限”窗口可以看到已申请的权限，勾选后点击确定。

选择权限后点击“添加”生成新的Profile文件，下载后按手动配置签名信息替换profile文件。

在工程中entry模块的module.json5文件中添加"ohos.permission.MANAGE_SCREEN_TIME_GUARD"权限，如下所示：

"requestPermissions": [{
  "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
}]

## Code blocks

### Code block 1

```
"requestPermissions": [{
  "name": "ohos.permission.MANAGE_SCREEN_TIME_GUARD"
}]
```
