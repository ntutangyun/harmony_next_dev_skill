# 使用AVCastPicker组件常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avsession-faq-avcastpicker_

本文汇总音视频应用在使用投播组件AVCastPicker过程中遇到的典型问题及其定位与解决方法。开发者可结合媒体会话管理错误码和HiLog日志进一步定位问题。

组件拉起后设备列表为空

问题现象

点击AVCastPicker组件后，弹出的设备选择界面为空。

可能原因

未创建对应类型的AVSession：以通话场景为例，需要创建voice_call类型的AVSession，否则将显示空列表。

当前设备无可用投播设备：周围不存在可投播的远端设备。

解决措施

创建对应类型的AVSession。以通话场景为例，请参考切换通话输出设备完成voice_call类型会话的创建。

确认周围存在可投播的远端设备。远端设备包括：HarmonyOS 5.0.0及以上版本的PC/2in1设备、HarmonyOS 3.1及以上的TV设备，或其他支持标准DLNA协议的设备。

自定义样式不随设备切换刷新

问题现象

使用customPicker自定义了组件样式，但设备切换后样式未更新。

可能原因

自定义样式不会随设备切换自动刷新，需要应用自行根据设备变化刷新。

解决措施

监听音频设备的切换事件on('preferOutputDeviceChangeForRendererInfo')，在回调中调用getPreferredOutputDeviceForRendererInfoSync获取当前设备并刷新自定义样式。具体实现请参考自定义样式实现。
