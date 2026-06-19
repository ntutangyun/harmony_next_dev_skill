# Frame分析

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame_

功能介绍

开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据并进行分析，从而识别出导致卡顿丢帧的原因。

Frame模板支持的泳道包括：Anomaly、User Events、Frame、ArkUI Component、ArkUI State、User Trace、ArkTS Callstack、Callstack、Network Traffic、Network Request、Energy、CPU Core、Process。本文介绍Anomaly、User Events、Frame泳道，其他泳道的详细信息请参考对应模板内容。

ArkUI Component、ArkUI State泳道的介绍请参考ArkUI分析。

User Trace、ArkTS Callstack、Callstack泳道的介绍请参考基础耗时：Time分析。

Network Traffic、Network Request泳道的介绍请参考网络诊断：Network分析。

Energy泳道的介绍请参考能耗诊断：Energy分析。

CPU Core、Process泳道的介绍请参考CPU活动分析。

说明

卡顿丢帧分析前，需创建Frame分析任务并录制相关数据，操作方法可参考性能问题定位：深度录制，或在会话区选择Open File，导入历史数据。

查看GPU使用情况

Frame泳道显示当前设备的GPU的使用率，将其展开，子泳道显示渲染服务（Render Service）侧帧数据和App侧帧数据。

在带有RS Frame和App Frame标签的子泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。

说明

一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。

一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。

查看指定时间段内所有进程的Frame数据统计信息

在时间轴上拖拽鼠标选定要查看的时间段。

点击Frame List中任意一帧，在右侧的More区域会中显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击跳转至关联的切片。

查看指定时间段内指定进程的Frame数据统计信息

在时间轴上拖拽鼠标选定要查看的时间段。

窗口下方的Details区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。

单击列表中任意一帧，右侧的More区域中会显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击跳转至关联的切片。

查看指定Frame信息

展开Frame主泳道，选择带App Frame或带RS Frame标签的子泳道，该泳道图区域上方是耗时最长的非UI函数，下方是UI主线程泳道。将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。

说明

在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。

如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。

卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。

查看指定Frame页面布局信息

从DevEco Studio 5.1.0 Release版本开始，支持查看最新录制的Session中指定的Frame页面布局信息。

从DevEco Studio 6.1.0 Beta1版本开始，按钮中新增Frame Layout开关，开发者可自行设置开关状态。开关关闭时，不支持查看最新录制的Session中指定的Frame页面布局信息，默认关闭。

暂不支持在Wearable设备上查看指定Frame页面布局信息。

说明

单击Download Layout或 Open Layout前，应用进程需置于前台，才能正确回放全量渲染数据，获取arkli文件。

BackgroundFilter：背景滤波器。

nodeGroup：节点组类型，0表示非节点组节点，1表示被动画标记的节点组，2表示被UI标记的节点组，4表示被用户标记的节点组，8表示被前景滤波器标记的节点组。

nodeGroupReuseCache： 0表示在生成缓存或无需缓存，1表示在重用缓存。

查看帧率统计信息

展开Frame泳道，框选一段数据。

查看动效详细信息

开发者在开发应用时，会使用到动效，动效的卡顿影响到用户的使用体验。DevEco Profiler提供动效场景的调优，能帮助开发者优化动效场景。

展开Frame主泳道，查看Animation子泳道，将鼠标放置在某个动效上，泳道会显示该动效的详细信息，包括响应时延、动效持续时间、完成时延、期望帧率、FPS。

响应时延：<=85ms 绿色，85ms~150ms 浅绿色，150ms ~250ms 浅红色，>250ms深红色。

动效持续时间：根据帧率展示颜色，FPS大于达标帧率即为绿色，小于则为深红色。智能刷新率模式下，帧率可变，颜色为灰色。达标帧率与期望帧率的大小有关，一般情况下期望帧率为60HZ，则达标帧率= 60HZ * 91.7%。

完成时延：响应时延和动效持续时间只要有一个为深红色，完成时延为深红色。

期望帧率：当前系统运行满帧帧率，如60HZ、90HZ、120HZ。智能刷新率模式下，不展示期望帧率。

说明

在Launch模板中，点击Frame泳道，Details区展示启动动效的详情信息，More区域展示动效帧的Animation Data List信息。

查看组件动画信息

从DevEco Studio 6.0.0.828版本开始，Frame泳道下新增Component Animation子泳道，用于从组件的角度展示应用中包含的各种动画类型，包括属性动画 (animation)、显式动画 (animateTo)、关键帧动画 (keyframeAnimateTo)以及页面间转场 (pageTransition)。

在Details区域，可以查看每个动画的详细信息，包括起止时间、帧率、动画曲线类型以及影响的组件属性等。单击列表中任意一动画，右侧的More区域中会显示该动画所影响的组件属性的具体变化过程。

查看屏幕帧率动态变化场景下丢帧和卡顿信息

Frame泳道下新增Lost Frames和Hitch Time两个子泳道，用于识别和优化卡顿和丢帧问题。

Lost Frames子泳道：展示当前时间段内丢帧数。Lost Frames计算出的结果，六舍七入统计取整。

Hitch Time子泳道：展示当前时间段内卡顿时长。计算方式为渲染前后两帧的间隔减去单帧耗时，若计算结果大于单帧耗时*70%，则视为出现卡顿现象。

查看组件帧率信息

Display Vsync子泳道：该泳道显示对应时间段的屏幕刷新率，支持对框选的时间段内的vsync进行分布统计。区分“<=30HZ”、“30~60HZ”、“60~90HZ”、“>90HZ”。统计值包括框选时间段内各区间的分布比率、最小/最大/平均时长以及平均HZ。如果某场景满足了帧率改变的要求，当底层系统根据机制进行变帧，相应的情况会展现在对应的泳道，帮助开发者了解vsync的变化情况是否符合预期。该泳道仅支持在配备硬件屏幕的设备上进行数据采集。

如下图所示，vsync2和vsync4中，vsync周期内的组件由于渲染耗时长，导致以下两个vsync周期挤掉下一个vsync周期的渲染时间，导致掉帧的情况产生。

选择Display Vsync子泳道，在时间轴上拖拽鼠标选定要查看的时间段。

查看解码过度耗时和超过阈值的序列化、反序列化操作

如果工程中存在图片资源，并感知到解码绘制/渲染过程存在卡顿，可以通过Anomaly泳道查看主线程解码过程中是否存在解码过度耗时告警，并确认发生告警的时段。

如果应用中使用了worker、Taskpool工作线程等场景，通常会触发跨线程对象传递，并触发序列化和反序列化的操作。对于耗时超过阈值的序列化、反序列化操作，Anomaly泳道也会给出对应的耗时告警，并给出发送这个操作的开始时间和耗时时间。

在时间轴上拖拽鼠标选定出现告警的时间段。当耗时超过VSync周期的50%时，将在Anomaly泳道中出现红色告警，提示“Image decoding has exceeded 50% of the VSync time”。

对于耗时超过阈值的序列化、反序列化操作，Anomaly泳道也会给出对应的耗时告警。其中可以通过泳道启动配置按钮配置检测阈值，默认配置阈值为8ms。

说明

已上架应用市场的应用不支持录制Anomaly泳道。

查看用户事件耗时

开发者在卡顿丢帧场景可通过User Event泳道查看用户事件，可查看用户事件开始时间、应用开始处理时间以及应用处理耗时等情况。

选择User Event泳道，在时间轴上拖拽鼠标选定要查看的时间段。

更多性能调优最佳实践，请参考点击响应时延分析、点击完成时延分析、帧率问题分析、Web点击响应时延分析、Web加载完成时延分析。
