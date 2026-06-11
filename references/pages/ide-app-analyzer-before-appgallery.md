# 上架前体检

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-before-appgallery_

从DevEco Studio 6.0.0 Beta1版本开始，AppAnalyzer新增上架前体检，针对上架阻塞问题进行快速检测，提前发现可能影响上架的问题，检测完成之后可以选择上传检测结果，用于应用市场上架参考，提升上架效率。

前置操作

单击菜单栏Tools > AppAnalyzer，打开AppAnalyzer页面。

在编辑窗口右侧的工具栏，点击AppAnalyzer或，打开AppAnalyzer页面。

确保DevEco Studio与真机设备已连接，并对应用进行签名。

如果使用DevEco Studio 6.0.1版本，未配置Python环境时，请根据界面提示，下载Python及三方库。或者点击AppAnalyzer底部Python 配置按钮进行配置。

进行体检

[h2]DevEco Studio 6.0.1 Beta1及以上版本

该体检模式无法自定义测试方式和体检规则，默认勾选所有规则，这些规则是规则体检的子集。单击底部的开始体检按钮，等待AppAnalyzer完成构建、签名、安装等操作。

安装完成后，根据提示登录账号，开始进行测试。在测试过程中，请保持连接的设备为解锁亮屏状态。

说明

如需上传报告，请在体检结束后上传，历史报告中无法上传报告。

如果测试分数不是100分，无法上传报告，可根据详情报告中的信息，对问题进行分析优化，详情报告的具体内容可参考规则体检。

从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的User Feedback向我们反馈。

从DevEco Studio 6.1.0 Release版本开始，支持导出报告，以实现报告的共享，具体可查看导出报告。

[h2]DevEco Studio 6.0.1 Beta1以下版本

该体检模式无法自定义测试方式、模块和体检规则，默认勾选所有规则，这些规则是规则体检的子集。单击底部的开始按钮，等待AppAnalyzer完成构建、签名、安装等操作。

安装完成后，根据提示登录账号，开始进行测试。在测试过程中，请保持连接的设备为解锁亮屏状态。

说明

如需上传报告，请在体检结束后上传，历史报告中无法上传报告。

如果测试分数不是100分，无法上传报告，可根据详情报告中的信息，对问题进行分析优化，详情报告的具体内容可参考规则体检。
