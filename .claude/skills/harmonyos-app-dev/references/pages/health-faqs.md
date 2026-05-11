# Health Service Kit常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-faqs_

参考配置Client ID，请登录AppGallery Connect平台，确认代码中配置的包名与client ID是匹配的。若问题仍未解决，请通过在线提单提交问题，华为支持人员会及时处理。

更多错误码请参考ArkTS API错误码。

在授权时上报1001502014错误

确保授权请求参数中的数据类型已经在Health Service Kit卡片中申请相应的权限，申请步骤请参考申请运动健康服务，数据类型对应的权限参考权限说明。

更多错误码请参考ArkTS API错误码。

用户隐私未同意，如何引导用户打开运动健康App

接口响应错误码1002703001，可通过以下方式引导用户打开运动健康App，同意隐私授权：

调用canOpenLink判断运动健康App是否安装。运动健康App Scheme：huaweischeme://healthapp/home/main。

App已安装，调用openLink接口拉起运动健康App。运动健康App Scheme：huaweischeme://healthapp/home/main。

App未安装，调用应用市场推荐接口，引导用户下载运动健康App，运动健康App包名：com.huawei.hmos.health。

个人数据处理说明
附录
