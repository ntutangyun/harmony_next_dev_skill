# 加载丢帧：ArkWeb分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-arkweb_

功能介绍

应用开发过程中，会通过在App中嵌入WebView以提高开发效率，可能面临ArkWeb加载和丢帧等问题。DevEco Profiler提供ArkWeb分析模板，可以结合ArkWeb执行流程的关键trace点来定位问题发生的阶段。如果问题发生在渲染阶段，可以结合H:RosenWeb数据，线程运行状态以及帧渲染流程打点数据，进一步分析丢帧问题。

ArkWeb模板支持的泳道包括：ArkWeb、User Events、ArkTS Callstack、Callstack、CPU Core、Process。本文介绍ArkWeb泳道，其他泳道的详细信息请参考对应模板内容。

User Events泳道的介绍请参考Frame分析。

ArkTS Callstack、Callstack泳道的介绍请参考基础耗时：Time分析。

CPU Core、Process泳道的介绍请参考CPU活动分析。

说明

任务分析前，需创建ArkWeb模板，完成一次录制，录制期间触发Web相关场景，操作方法可参考性能问题定位：深度录制，或在会话区选择Open File，导入历史数据。

ArkWeb加载问题分析

根据Web页面加载过程中的关键trace点，划分了五个阶段，分别是：点击事件（Click Event）， 组件初始化（Component Initialization），主资源下载（Primary Resource Download），子资源下载（Sub-resource Download），渲染输出（Render And Output）。

框选ArkWeb泳道，可以查看耗时阶段划分的关键trace点，并可以根据trace信息，关联到所在线程信息。

Details区域可以跳转关键trace所在泳道，进一步分析加载问题。

ArkWeb丢帧问题分析

H:RosenWeb：用于记录准备提交给Render Service进行统一渲染的数据量。

Compositor：合成线程，负责图层CPU指令合成，承载动态效果。

CompositorGpuTh：用于从GPU获取渲染结果和将合成的buffer送至图形子系统执行渲染。

Chrome_InProcGpu：光栅化。

VsyncGenerator：图形侧vsync信号，用于定时生成vsync信号，通知渲染线程或动画线程准备下一帧的渲染。

VSync-webview：用于接收图形侧发送的vsync信号，并根据信号触发WebView页面的渲染或重绘。

VizCompositorTh：绘制信号监听线程，向图形请求Web本身的vsync信号，触发系统Web相关绘制或执行。

Web应用Render线程：以 :render 结尾的线程，主要用于图形渲染任务，包括html、css解析，进行分层布局绘制。

H:RosenWeb上标识有待提交给渲染服务的数据量。正常情况下，每个数据量都会提交给硬件进行上屏，即Present Fence泳道上的H:Waiting for Present Fence trace点。如果某个数据量在Present Fence泳道上没有该trace点，那么很可能是存在丢帧问题。

包括统一资源定位符、缓存类型、是否为本地资源替换、请求资源时间（ns）、队列时间（ns）、停滞时间（ms）、dns解析时间（ms）、连接耗时（ms）、ssl连接时间（ms）、服务器响应耗时（ms）、下载耗时（ms）、传输时间（ms）、请求方法、状态码、编码前资源大小、编码后资源大小以及HTTP版本。
