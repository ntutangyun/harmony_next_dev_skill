# 关于实况窗模板使用的问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-faq-4_

采用进度可视化模板并且indicatorType为INDICATOR_TYPE_OVERLAY时，图片较宽，无法完全覆盖进度条

当indicatorType=INDICATOR_TYPE_OVERLAY时，图标区域为64*56vp，图片较宽时会按比例进行缩放。应用需要自己修改图片大小和样式来达到想要的效果。

理想效果图

如何修改 "实况窗左上角图标"

除导航模板通过currentNavigationIcon设置左上角图标外，其他模板不支持修改实况窗左上角图标，默认展示为应用Logo图标。
