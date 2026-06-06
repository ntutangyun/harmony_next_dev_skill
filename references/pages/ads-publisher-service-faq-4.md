# 展示广告时显示白屏

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-faq-4_

展示广告时出现白屏可能原因为展示的广告样式与UI展示页面不匹配，横幅广告使用AutoAdComponent组件展示；原生广告、开屏广告、贴片广告使用AdComponent组件展示；激励广告、插屏广告调用showAd方法展示。

建议排查步骤：

获取请求广告时返回的广告数据并记录。

打印展示广告时入参的广告数据，对比两者是否一致。

检查请求的广告类型与使用的展示组件是否匹配。

流量变现服务常见问题
鲸鸿动能媒体服务平台打开受限
