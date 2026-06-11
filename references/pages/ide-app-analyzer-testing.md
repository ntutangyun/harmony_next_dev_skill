# 导入DevEco Testing的检测报告进行诊断

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-app-analyzer-testing_

从DevEco Studio 6.0.0 Beta3版本开始，支持在DevEco Testing中进行性能相关测试生成检测报告后，导入到AppAnalyzer进行诊断和分析，获得可能的故障原因并生成体检报告。

前置操作

体检前，请先在DevEco Testing中测试并导出检测报告，具体操作方式请参考性能基础质量测试或场景化性能测试。

进行体检

说明

由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

[h2]DevEco Studio 6.0.1 Beta1及以上版本

源文件、调优文件（包含trace文件和调用栈文件）或snapshot文件、时间戳等：点击源文件可跳转到问题源码，点击调优文件或snapshot文件支持直接拉起性能分析工具Profiler并导入性能检测的问题数据进行调优分析，点击时间戳可以打开Profiler并定位到问题发生的时间范围。

分析文档：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。

优化建议：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

从DevEco Studio 6.0.2 Beta1版本开始，如果在体检中遇到问题，可点击报告右上角的User Feedback向我们反馈。

[h2]DevEco Studio 6.0.1 Beta1以下版本

点击菜单栏Tools > AppAnalyzer，打开AppAnalyzer页面，点击底部历史记录按钮，进入历史记录页面。

开始/结束页面、时间戳、调优文件（包含trace文件和调用栈文件）或snapshot文件等：点击开始/结束页面可跳转到问题源码，点击时间戳可以打开性能分析工具Profiler并定位到问题发生的时间范围，点击调优文件或snapshot文件支持直接拉起Profiler并导入性能检测的问题数据进行调优分析。

分析文档：点击链接可跳转至官网文档，参考文档对检测出来的问题进行分析。

优化建议：针对可能的故障原因，给出对应的最佳实践，点击链接可跳转至官网文档。

说明

由于DevEco Testing和AppAnalyzer在检测能力、检测方法以及场景识别上存在差异，所以通过DevEco Testing检测并导入AppAnalyzer诊断和直接通过AppAnalyzer检测并诊断，检测和诊断结果会出现不一致的情况。

检测指标

AppAnalyzer会将DevEco Testing测试用例的操作归类为以下场景，仅支持对部分指标进行诊断，具体如下。

场景	检测指标
页面间转场	点击响应时延
点击完成时延
转场卡顿率
页面滑动	滑动响应时延
滑动卡顿率
冷启动	完成时延
页面内转场	滑动响应时延
点击响应时延
点击完成时延
滑动卡顿率
起播时延
