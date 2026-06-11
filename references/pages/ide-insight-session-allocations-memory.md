# 内存分析介绍

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations-memory_

应用在开发过程中，可能因API使用错误、变量未及时释放、异常频繁创建/释放内存等情况引发各种内存问题。

DevEco Profiler提供了基础的Allocation内存场景分析功能。通过使用Allocation来分析应用或元服务在运行时的内存分配及使用情况，识别和定位内存泄漏、内存抖动以及内存溢出等问题，对应用或元服务的内存使用进行优化。

从DevEco Studio 6.1.0 Beta1版本开始，Allocation分析任务新增支持录制All Heap & Anonymous VM泳道、All Heap泳道、All Anonymous VM泳道，不支持录制Native Allocation泳道。

操作步骤

[h2]DevEco Studio 6.1.0 Beta1及以上版本

在设备连接完成后，可按照如下方法查看内存分析结果：

说明

Allocation分析支持离线符号解析能力，请参见离线符号解析。

在任务录制过程中，单击分析窗口左上角的可启动内存回收机制。

当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev/Stack、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

子泳道	说明
ArkTS Heap	ArkTS堆的内存占用。
Native Heap	Native层（主要是应用依赖的so库的C/C++代码）使用new/malloc分配的堆内存。
GL	包括应用和RS，应用为纹理内存，RS为纹理和图形渲染内存。
Graph	该进程按去重规则统计的dma内存占用，包括直接通过接口申请的dma buffer和通过allocator_host申请的dma buffer。
Guard	保护段所占内存。
AnonPage Other	其他所有匿名页所占内存（非heap、anon:native_heap、anon:ArkTS heap开头的匿名页）。
FilePage Other	其它映射到文件页但不能被归类到.so/.db/.ttf类型的内存占用。
Dev	进程加载的以/dev开头的文件所占内存。
Stack	栈内存。
.hap	进程加载的.hap文件所占内存。
.so	进程加载的.so动态库所占内存。
.ttf	进程加载的.ttf字体文件所占内存。

说明

该泳道即将下线，推荐使用Snapshot模板分析ArkTS内存泄漏。

ArkTS Snapshot泳道

All Heap & Anonymous VM泳道

All Heap泳道

All Anonymous VM泳道

System Resources泳道

Graphic Memory泳道

单击工具控制栏中的按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、内存数据采样大小、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

配置项	说明
Statistics Mode	该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。关闭后，处于非统计模式，每次内存分配后数据会实时从设备端返回。
Sampling Interval	统计时间间隔。仅在统计模式下需要设置，可设置范围为1s~3600s，默认为10s。
All Heap & Anonymous VM Filter Size	最小跟踪内存，该参数表示最小抓取的内存大小。 可配置范围为0-65535Bytes，默认为1024Bytes。
Sampling Size	DevEco Studio 6.1.1 Release版本新增。 内存数据采样大小，可配置范围为1-1048576Bytes，默认为4096Bytes。 配置后，仅对Native Heap和All Anonymous VM泳道中的mmap类型数据生效。
Backtrace Mode	内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。
Record JS Stack	是否开启JS回栈。开启后，系统回栈时会自动从Native向JS层回栈，完成Native到JS的栈缝合，适合ArkTS/JS代码调用Native的场景。 在DevEco Studio 6.1.0 Beta2之前版本，默认关闭。 从DevEco Studio 6.1.0 Beta2版本开始，默认开启。
JS Backtrace Depth	JS回栈深度。可配置范围为1-128，默认10层。
Native Backtrace Depth	Native回栈深度。可配置范围为5-100，默认10层。
Backtrace Stack	回栈深度。仅当Backtrace Mode选择为DWARF模式的情况下存在，其层数代表着JS与Native的共同回栈深度。可配置范围为5-100，默认20层。
Sync Backtrace Depth	DevEco Studio 6.1.1 Beta1版本新增。 同步回栈深度。仅当Record Async Stack开启的情况下存在，其层数代表着JS与Native的共同同步回栈深度。可配置范围为5-100，默认20层。
Record Async Stack	DevEco Studio 6.1.1 Beta1版本新增。 用于开启异步栈缝合。仅当Backtrace Mode选择为FP模式的情况下可以开启。开启后，在异步回栈时支持多回一层异步栈帧，最大异步回栈深度为16层，且暂不支持设置异步回栈深度。默认关闭。
Record Data Range Options	DevEco Studio 6.1.0 Release版本新增。 用于设置采样数据范围，包含Malloc、Local Handle和Global Handle，默认勾选Malloc。。 Malloc记录malloc系列函数的内存分配。 Local Handle用于管理JS对象生命周期的引用句柄（napi_value），仅支持Phone和PC设备。 Global Handle允许用户管理ArkTS/JS值的生命周期的引用句柄（napi_ref）。

说明

若勾选Local Handle，在应用生命周期内首次录制时会重启应用。若应用在生命周期内被强制终止后重启，再次录制时仍会重启应用。

最小跟踪内存设置的数值越小，回栈深度越大，这可能会导致DevEco Profiler卡顿，请根据应用实际的调测情况进行合理设置。

最小跟踪内存设置的数值大小不影响Local Handle和Global Handle。

统计模式适用于不关注单次分配，但关注应用较长时间的内存变化，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长。Sampling Interval设置为近似值，将尽可能在接近这个时间内做统计汇总，会有不超过1s偏差，不影响内存分配的正确性。

使用统计模式时，录制的结束时间需要是Sampling Interval即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。

Native Heap子泳道：用于显示Malloc、ArkLocalHandle和ArkGlobalHandle内存分配。

ArkTS Heap子泳道：用于显示ArkTS对象内存分配。

JS Heap子泳道：用于显示JS对象内存分配。

VM:ION子泳道：用于显示DMA内存分配数据。

VM:ASHMem子泳道：用于显示匿名共享内存。

VM:.so子泳道：用于显示.so文件内存消耗。

VM:others子泳道：用于显示除ION、ASHMem、.so外的mmap类型数据。

File Descriptors子泳道：用于显示进程的文件句柄使用情况。

Threads子泳道：用于显示进程的线程使用情况。

Vulkan子泳道：用于显示GPU_VK类型的内存分配数据。

OpenGL ES子泳道：用于显示GPU_GLES类型的内存分配数据。

OpenCL子泳道：用于显示GPU_CL类型的内存分配数据。

须知

Graph字段统计方式为：计算/proc/process_dmabuf_info节点下该进程使用的内存大小。

“Details”区域中带标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

在System Resources泳道的Statistics页签中不提供内存大小数据。

点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。

在System Resources泳道的Call Trees页签中不提供分配大小数据。

当未开启统计模式，以及录制了ArkTS Snapshot泳道时，框选All Heap & Anonymous VM或All Heap或Native Heap子泳道，单击任一行栈帧，“More”区域显示经过该栈帧的分配内存最大的调用栈和ArkTS对象列表（ArkTS Object List）。否则，单击任一行栈帧，“More”区域显示经过该栈帧的分配内存最大的调用栈。

点击“ArkTS Object List”列表中的跳转按钮，跳转到ArkTS Snapshot泳道中的目标对象节点。

说明

统计模式（Statistics Mode）开启后，不存在Allocations List信息。

选择任一对象，右侧会展示与该对象相关的所有库和调用者。

说明

Release应用暂不支持跳转到用户侧Native代码。

[h2]DevEco Studio 6.1.0 Beta1以下版本

在设备连接完成后，可按照如下方法查看内存分析结果：

说明

Allocation分析支持离线符号解析能力，请参见离线符号解析。

在任务录制过程中，单击分析窗口左上角的可启动内存回收机制。

当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。

PSS：进程独占内存和按比例分配共享库占用内存之和。

RSS：进程独占内存和相关共享库占用内存之和。

USS：进程独占内存。

默认只显示PSS的统计图，如需要查看USS或RSS，需要在Memory泳道的右上角点选相关数据类型。

展开Memory泳道，子泳道展示的是按照内存类型将进程PSS值拆分开的各个维度的内存信息，包含ArkTS Heap、Native Heap、GL、Graph、Guard、AnonPage Other、FilePage Other、Dev/Stack、.hap、.so、.ttf。默认展示其中的五个子泳道，可以点击主泳道的options标签并勾选其他子泳道查看其他子泳道。

子泳道	说明
ArkTS Heap	ArkTS堆的内存占用。
Native Heap	Native层（主要是应用依赖的so库的C/C++代码）使用new/malloc分配的堆内存。
GL	包括应用和RS，应用为纹理内存，RS为纹理和图形渲染内存。
Graph	该进程按去重规则统计的dma内存占用，包括直接通过接口申请的dma buffer和通过allocator_host申请的dma buffer。
Guard	保护段所占内存。
AnonPage Other	其他所有匿名页所占内存（非heap、anon:native_heap、anon:ArkTS heap开头的匿名页）。
FilePage Other	其它映射到文件页但不能被归类到.so/.db/.ttf类型的内存占用。
Dev	进程加载的以/dev开头的文件所占内存。
Stack	栈内存。
.hap	进程加载的.hap文件所占内存。
.so	进程加载的.so动态库所占内存。
.ttf	进程加载的.ttf字体文件所占内存。

说明

由于较大的性能开销可能导致卡顿/卡死问题，ArkTS Allocation暂不支持和如下泳道同时录制：

All Heap & Anonymous VM泳道

All Heap泳道

All Anonymous VM泳道

System Resources泳道

Graphic Memory泳道

单击工具控制栏中的按钮，可以设置是否为统计模式、统计间隔、最小跟踪内存、回栈模式、JS回栈、JS回栈深度和Native回栈深度。

配置项	说明
Statistics Mode	该项配置代表是否开启统计模式采集数据，默认开启。开启后，数据会每隔Sampling Interval中设置的时间从设备端汇总并返回。关闭后，处于非统计模式，每次内存分配后数据会实时从设备端返回。
Sampling Interval	统计时间间隔。仅在统计模式下需要设置，可设置范围为1s~3600s，默认为10s。
All Heap & Anonymous VM Filter Size	最小跟踪内存，该参数表示最小抓取的内存大小。可配置范围为0-65535Bytes，默认为1024Bytes。
Backtrace Mode	内存分配栈回栈模式。当前提供FP和DWARF两种回栈模式。FP回栈是通过帧指针（FP寄存器）链接栈帧，直接遍历调用链。DWARF回栈是基于编译器生成的DWARF调试信息进行栈回溯。默认FP回栈。FP回栈性能更好，但在某些特定场景下（例如so的编译参数控制），FP回栈可能失效，此时可选择DWARF回栈尝试。
Record JS Stack	是否开启JS回栈。开启后，系统回栈时会自动从Native向JS层回栈，完成Native到JS的栈缝合，适合ArkTS/JS代码调用Native的场景。
JS Backtrace Depth	JS回栈深度。可配置范围为1-128，默认10层。
Native Backtrace Depth	Native回栈深度。可配置范围为5-100，默认10层。
Backtrace Stack	回栈深度。仅当Backtrace Mode选择为DWARF模式的情况下存在，其层数代表着JS与Native的共同回栈深度。可配置范围为5-100，默认20层。

说明

最小跟踪内存设置的数值越小，回栈深度越大，这可能会导致DevEco Profiler卡顿，请根据应用实际的调测情况进行合理设置。

统计模式适用于不关注单次分配，但关注应用较长时间的内存变化，将指定的采样间隔内的数据做合并统计，以达到降低处理数据量，提高录制效率和时长。Sampling Interval设置为近似值，将尽可能在接近这个时间内做统计汇总，会有不超过1s偏差，不影响内存分配的正确性。

使用统计模式时，录制的结束时间需要是Sampling Interval即采样周期的整数倍，例如当采样周期是10s时，停止录制时间建议在11s+/21s+，以此类推，留出余量给系统做数据处理与传输。

展开主泳道，包括Vulkan、OpenGL ES、OpenCL三条子泳道。其中Vulkan子泳道对应GPU_VK类型的内存分配数据，OpenGL ES子泳道对应GPU_GLES类型的内存分配数据，OpenCL子泳道对应GPU_CL类型的内存分配数据。

须知

Graph字段统计方式为：计算/proc/process_dmabuf_info节点下该进程使用的内存大小。

“Details”区域中带标识的对象，表示其可以通过窗口访问。每个时段内已经释放的内存标记为灰色，未释放的内存标记为绿色。

在System Resources泳道的Statistics页签中不提供内存大小数据。

点击任意对象上的跳转按钮，可跳转至此类对象的详细占用/分配信息。当前统计模式下不支持跳转。

在System Resources泳道的Call Trees页签中不提供分配大小数据。单击任一行栈帧，“More”区域将显示经过该栈帧的分配内存最大的调用栈。

说明

统计模式（Statistics Mode）开启后，不存在Allocations List信息。

选择任一对象，右侧会展示与该对象相关的所有库和调用者。

说明

Release应用暂不支持跳转到用户侧Native代码。
