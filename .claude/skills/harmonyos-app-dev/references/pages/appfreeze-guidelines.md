# AppFreeze（应用冻屏）检测

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines_

--------------------------------StaticsDuration-----------------------------------|.
|-------------------------CpuTime----------------------|--------SyncWaitTime----------|.
|----OptimalCpuTime----|------SupplyAvailableTime------|--------SyncWaitTime----------|.


#Basic Statistical Infomation  <- CPU基本统计信息
ProcessCpuTime: 0 ms  <- 统计周期内，进程运行时间
DeviceRuntime: 0 ms  <- 统计周期内，设备所有CPU的运行时间
Tid: 2320  <- 故障主线程号
StartTime: 2021-01-01 20:05:58:177  <- 统计开始时间
EndTime: 2021-01-01 20:06:01:172  <- 统计结束时间
StaticsDuration: 2995 ms  <- 统计持续时间
CpuTime: 0 ms  <- 统计周期内，主线程运行时间
SyncWaitTime: 2995 ms  <- 主线程等待时间
OptimalCpuTime: 0 ms  <- 统计周期内，主线程最优负载运行时间（使用最大核的最高算力运行）
SupplyAvailableTime: 0 ms  <- 调度可优化时间


#CpuFreq Usage (usage >=1%)  <- 当CPU单个频点使用率>=1%时，这些频点及频点的使用率就会被列出来。
start time: 2021-01-01 20:06:00:888  <- 计算CPU使用率开始时间
cpu0 Usage 23.5%, 1430MHZ 21.04%  <- cpu0的总使用率，cpu0单个频点的使用率（在1430MHZ频点下的使用率）
cpu1 Usage 23.5%, 1430MHZ 21.04%
cpu2 Usage 23.5%, 1430MHZ 21.04%
cpu3 Usage 23.5%, 1430MHZ 21.04%
.......
end time: 2021-01-01 20:06:00:888  <- 计算CPU使用率结束时间
#ThreadInfos Tid: 2204, Name: com.example.freeze  <- 故障线程号，线程名
SnapshotTime:2021-01-01-20-05-58.292875  <- 获取主线程的时间
#00 pc 00000000000015b8 [shmm](__kernel_gettimeofday+72) <- 主线程调用栈
#01 pc 00000000001d7e44 /system/lib64/ld-musl-aarck64.so.1(clock_gettime+48)(f8a0616c89b184992d0e8883cc78f638)
#02 pc 00000000001d9f20 /system/lib64/ld-musl-aarck64.so.1(time+32)(f8a0616c89b184992d0e8883cc78f638)
#03 pc 0000000000007e2c /data/storage/el1/bundle/libs/arm64/libsample.so(WaitSomeTime()+76)(8b74cdc906ea6b2eba95d891bc91c72a)
#04 pc 0000000000009b2c /data/storage/el1/bundle/libs/arm64/libsample.so(8b74cdc906ea6b2eba95d891bc91c72a)
#05 pc 00000000000a0500 /system/lib64/platformsdk/libruntime.z.so(c2f75213ee12fdf08da323fe546923ff)
#06 pc 0000000000017b04 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(366b4d7f2eba693ad06f14469b08943b)
#07 pc 0000000000016f38 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(366b4d7f2eba693ad06f14469b08943b)
#08 pc 000000000003e160 /system/lib64/chipset-sdk-sp/libeventhandler.z.so(OHOS::AppExecFwk::EventRunner::Run()+396)(366b4d7f2eba693ad06f14469b08943b)
.......
========SubmitterStacktrace======== <- 任务提交者调用栈(最多抓取16层调用栈)
#00 pc 0000000000013108 /system/lib64/platformsdk/libuv.so(uv_queue_work+292)(366b4d7f2eba693ad06f14469b08943b)
#01 pc 0000000000008cdc /data/storage/el1bundle/libs/arm64/libsample.so(8b74cdc906ea6b2eba95d891bc91c72a)
#02 pc 000000000005ae00 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+272)(bc1c64aabbe5c7d4db2282a6137443e1)
#03 pc 0000000000de3efc /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+44)
#04 pc 0000000000448dd4 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+372)
#05 at anonymous (sample|sample|1.0.0|src/main/ets/pages/Index.ts:381:36)
#06 pc 00000000001e5c8c /system/lib64/platformsdk/libark_jsruntime.so(ce0b05d90b9fae02e7abf8e9f1e5a0f3)
.......


SnapshotTime: 2021-01-01-20-05-58.549685
#00 pc 00000000000015b8 [shmm](__kernel_gettimeofday+72)
#01 pc 00000000001d7e44 /system/lib64/ld-musl-aarck64.so.1(clock_gettime+48)(f8a0616c89b184992d0e8883cc78f638)
#02 pc 00000000001d9f20 /system/lib64/ld-musl-aarck64.so.1(time+32)(f8a0616c89b184992d0e8883cc78f638)
#03 pc 0000000000007e2c /data/storage/el1/bundle/libs/arm64/libsample.so(WaitSomeTime()+76)(8b74cdc906ea6b2eba95d891bc91c72a)
#04 pc 0000000000009b2c /data/storage/el1/bundle/libs/arm64/libsample.so(8b74cdc906ea6b2eba95d891bc91c72a)
#05 pc 00000000000a0500 /system/lib64/platformsdk/libruntime.z.so(c2f75213ee12fdf08da323fe546923ff)
.......
========SubmitterStacktrace========
#00 pc 0000000000013108 /system/lib64/platformsdk/libuv.so(uv_queue_work+292)(366b4d7f2eba693ad06f14469b08943b)
#01 pc 0000000000008cdc /data/storage/el1bundle/libs/arm64/libsample.so(8b74cdc906ea6b2eba95d891bc91c72a)
#02 pc 000000000005ae00 /system/lib64/platformsdk/libace_napi.z.so(panda::JSValueRef ArkNativeFunctionCallBack<true>(panda::JsiRuntimeCallInfo*)+272)(bc1c64aabbe5c7d4db2282a6137443e1)
#03 pc 0000000000de3efc /system/lib64/module/arkcompiler/stub.an(RTStub_PushCallArgsAndDispatchNative+44)
#04 pc 0000000000448dd4 /system/lib64/module/arkcompiler/stub.an(BCStub_HandleCallthis0Imm8V8StwCopy+372)
#05 at anonymous (sample|sample|1.0.0|src/main/ets/pages/Index.ts:381:36)
.......
AppFreeze聚类
聚类简介

应用程序在不同版本或同一版本的不同时间产生的AppFreeze可能为同一原因，但在AppFreeze故障日志中生成的大部分信息会随版本、时间等因素变化，无法快速确定是否为重复问题。

AppFreeze故障信息包含系统侧和应用侧的调用栈，不利于应用开发者快速排查应用侧的问题。

因此，为避免重复分析多份故障信息，提高应用故障问题的分析效率，需要对AppFreeze故障信息进行聚类；

同时，聚类也能帮助开发者对不同原因问题进行分类统计。

聚类信息范围

AppFreeze故障日志信息中的故障线程信息表示业务线程发生故障时代码调用信息，相同的故障线程调用栈信息必然表示相同的故障原因。

因此，将故障线程信息作为聚类范围是最为准确的，开发者可根据业务聚类的需求调整增加其他故障日志的信息。

故障线程信息可参考堆栈信息介绍获取。

AppFreeze故障信息聚类

AppFreeze故障信息聚类方法同Cpp Crash一致，参考CppCrash聚类。

注意

如果故障线程堆栈中有IPC栈帧，可获取binder堆栈信息用于聚类。

增强日志信息聚类

增强日志信息聚类规格与AppFreeze故障信息提取堆栈聚类规格一致，该部分参与聚类主要是为了解决AppFreeze故障堆栈信息不足导致的无法聚类问题。

开发者可参考AppFreeze故障信息聚类方法获取聚类特征，对增强日志信息进行聚类。

AddrSanitizer（地址越界）检测
Resource Leak（资源泄漏）检测
