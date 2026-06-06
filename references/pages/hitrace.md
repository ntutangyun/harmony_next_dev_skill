# hitrace

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitrace_

--=> irqs-off
#                                         / _----=> need-resched
#                                        | / _---=> hardirq/softirq
#                                        || / _--=> preempt-depth
#                                        ||| /     delay
#           TASK-PID       TGID    CPU#  ||||   TIMESTAMP  FUNCTION
#              | |           |       |   ||||      |         |
 KstateRecvThrea-1132    (    952) [003] .... 589942.951387: tracing_mark_write: B|952|H:CheckMsgFromNetlink|I62
 KstateRecvThrea-1132    (    952) [003] .... 589942.951554: tracing_mark_write: B|952|H:OnKstateCallback, mask: 8, data: [PID 15461 KILLED][SIG 9]|I62
 KstateRecvThrea-1132    (    952) [003] .... 589942.951693: tracing_mark_write: E|952|I62
 KstateRecvThrea-1132    (    952) [003] .... 589942.951737: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 589942.951909: tracing_mark_write: B|952|H:ProcessEvent, eventId: 6|I62
 state_change_ha-1139    (    952) [001] .... 589942.952510: tracing_mark_write: E|952|I62
2025/06/04 10:15:02 TraceFinish done.

指定-o参数时，可以将trace信息保存到指定目录，建议保存在/data/local/tmp路径下。

hitrace -t 10 -b 204800 app -o /data/local/tmp/test.ftrace

使用样例：

$ hitrace -t 10 -b 204800 app -o /data/local/tmp/test.ftrace
2025/06/04 10:19:47 start capture, please wait 10s ...
2025/06/04 10:19:57 capture done, start to read trace.
2025/06/04 10:19:57 trace read done, output: /data/local/tmp/test.ftrace
2025/06/04 10:19:57 TraceFinish done.
捕获指定时长二进制格式trace

命令带--raw参数时可捕获二进制格式trace，捕获二进制格式trace时不支持指定路径，固定保存在路径/data/log/hitrace下。采集结束后，采集结束后生成文件的绝对路径会显示在命令行窗口。

hitrace -t 10 -b 204800 app --raw

使用样例：

$ hitrace -t 10 -b 204800 app --raw
2025/06/04 10:21:16 hitrace enter, running_state is RECORDING_SHORT_RAW
2025/06/04 10:21:16 args: tags:app bufferSize:204800 overwrite:1
2025/06/04 10:21:16 start capture, please wait 10s ...
2025/06/04 10:21:27 capture done, output files:
    /data/log/hitrace/record_trace_20250604102116@590322-695861087.sys
快照模式捕获文本格式trace

快照模式下，trace信息保存在内核缓冲区。当数据量超出缓冲区大小时，默认丢弃最早的数据。

使用以下命令开启快照模式，指定缓冲区大小为204800KB，采集的tag为app和graphic。

hitrace --trace_begin -b 204800 app graphic

使用样例：

$ hitrace --trace_begin -b 204800 app graphic
2025/06/04 16:03:39 hitrace enter, running_state is RECORDING_LONG_BEGIN
2025/06/04 16:03:39 args: tags:app,graphic bufferSize:204800 overwrite:1
2025/06/04 16:03:39 OpenRecording done.

在开启快照模式后，可以使用下面的命令将当前缓冲区内的数据导出。默认将trace信息显示到命令行窗口。

hitrace --trace_dump

使用样例：

$ hitrace --trace_dump
2025/06/04 16:07:57 start to read trace.
# tracer: nop
#                                          _-----=> irqs-off
#                                         / _----=> need-resched
#                                        | / _---=> hardirq/softirq
#                                        || / _--=> preempt-depth
#                                        ||| /     delay
#           TASK-PID       TGID    CPU#  ||||   TIMESTAMP  FUNCTION
#              | |           |       |   ||||      |         |
 KstateRecvThrea-1132    (    952) [002] .... 610865.463378: tracing_mark_write: B|952|H:CheckMsgFromNetlink|I62
 KstateRecvThrea-1132    (    952) [002] .... 610865.463503: tracing_mark_write: B|952|H:OnKstateCallback, mask: 8, data: [PID 14446 KILLED][SIG 9]|I62
 KstateRecvThrea-1132    (    952) [002] .... 610865.463626: tracing_mark_write: E|952|I62
 KstateRecvThrea-1132    (    952) [002] .... 610865.463654: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610865.463767: tracing_mark_write: B|952|H:ProcessEvent, eventId: 6|I62
 state_change_ha-1139    (    952) [001] .... 610865.463879: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610866.506055: tracing_mark_write: B|952|H:ProcessEvent, eventId: 0|I62
 state_change_ha-1139    (    952) [001] .... 610866.506297: tracing_mark_write: B|952|H:HandleStateTransition, 20020111_com.ohos.medialibrary.medialibrarydata_[6255]|I62
 state_change_ha-1139    (    952) [001] .... 610866.506782: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610866.506824: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610866.557458: tracing_mark_write: B|952|H:ProcessEvent, eventId: 0|I62
 state_change_ha-1139    (    952) [001] .... 610866.558060: tracing_mark_write: E|952|I62
 state_change_ha-1139    (    952) [001] .... 610866.558101: tracing_mark_write: E|952|I62

导出时也可以使用-o命令保存到指定文件，建议保存到/data/local/tmp路径下。

hitrace --trace_dump -o /data/local/tmp/test.ftrace

使用样例：

$ hitrace --trace_dump -o /data/local/tmp/test.ftrace
2025/06/04 16:09:10 start to read trace.
2025/06/04 16:09:10 trace read done, output: /data/local/tmp/test.ftrace

需要停止采集时，有如下三种命令：

停止采集，并将当前缓冲区内的trace信息显示到命令行窗口。

hitrace --trace_finish

使用样例：

$ hitrace --trace_finish
2025/06/04 16:22:02 start to read trace.
# tracer: nop
#                                          _-----=> irqs-off
#                                         / _----=> need-resched
#                                        | / _---=> hardirq/softirq
#                                        || / _--=> preempt-depth
#                                        ||| /     delay
#           TASK-PID       TGID    CPU#  ||||   TIMESTAMP  FUNCTION
#              | |           |       |   ||||      |         |
KstateRecvThrea-1132    (    952) [002] .... 610865.463378: tracing_mark_write: B|952|H:CheckMsgFromNetlink|I62
KstateRecvThrea-1132    (    952) [002] .... 610865.463503: tracing_mark_write: B|952|H:OnKstateCallback, mask: 8, data: [PID 14446 KILLED][SIG 9]|I62
KstateRecvThrea-1132    (    952) [002] .... 610865.463626: tracing_mark_write: E|952|I62
KstateRecvThrea-1132    (    952) [002] .... 610865.463654: tracing_mark_write: E|952|I62

停止采集，并将当前缓冲区内的trace信息保存到指定文件。建议保存路径为/data/local/tmp。

hitrace --trace_finish -o /data/local/tmp/test.ftrace

使用样例：

$ hitrace --trace_finish -o /data/local/tmp/test.ftrace
2025/06/04 16:24:52 start to read trace.
2025/06/04 16:24:52 trace read done, output: /data/local/tmp/test.ftrace
2025/06/04 16:24:52 Trace Closed.

停止采集，不输出trace信息。

hitrace --trace_finish_nodump

使用样例：

$ hitrace --trace_finish_nodump
2025/06/04 16:26:11 hitrace enter, running_state is RECORDING_LONG_FINISH_NODUMP
2025/06/04 16:26:11 end capture trace.
快照模式捕获二进制格式trace

快照模式下捕获二进制格式trace时不支持指定tag，默认采集以下tag。

"net", "dsched", "graphic", "multimodalinput", "dinput", "ark", "ace", "window","zaudio", "daudio", "zmedia", "dcamera", "zcamera", "dhfwk", "app", "gresource", "ability", "power", "samgr", "ffrt", "nweb", "hdf", "virse", "workq", "ipa", "sched", "freq", "disk", "sync", "binder", "mmc", "membus", "load"

使用下面的命令开启捕获二进制trace。

hitrace --start_bgsrv

使用样例：

$ hitrace --start_bgsrv
2025/06/04 16:44:54 hitrace enter, running_state is SNAPSHOT_START
2025/06/04 16:44:54 OpenSnapshot done.

使用以下命令将当前缓冲区的trace信息导出到文件。二进制格式trace支持指定路径（目前仅支持设定路径为/data/local/tmp）导出或显示到命令行窗口。

hitrace --dump_bgsrv

使用样例1：

不指定路径的标准快照模式命令例如：

$ hitrace --dump_bgsrv
2025/06/04 16:50:34 hitrace enter, running_state is SNAPSHOT_DUMP
2025/06/04 16:50:35 DumpSnapshot done, output:
    /data/log/hitrace/trace_20250604164454@613340-339960.sys

使用样例2：

从API version 24开始，快照模式下支持指定路径，例如：

$ hitrace --dump_bgsrv -o /data/local/tmp/test.sys
2025/06/04 16:50:34 hitrace enter, running_state is SNAPSHOT_DUMP
2025/06/04 16:50:35 DumpSnapshot done, output:
     /data/local/tmp/test.sys

在结束捕获时，可以使用下面的命令停止采集。

hitrace --stop_bgsrv

使用样例：

$ hitrace --stop_bgsrv
2025/06/04 16:52:51 hitrace enter, running_state is SNAPSHOT_STOP
2025/06/04 16:52:52 CloseSnapshot done.
录制模式捕获trace

录制模式下，系统会持续保存运行时生成的二进制格式trace，文件大小超过设定的值时会生成新文件。支持指定保存路径（目前仅支持设定路径为/data/local/tmp）。

使用以下命令开启录制模式。缓冲区大小设定为204800KB，文件大小设为102400KB，采集的tag为app和graphic。

hitrace --trace_begin --record -b 204800 --file_size 102400 app graphic

使用样例1：

不指定路径的录制模式下例如：

$ hitrace --trace_begin --record -b 204800 --file_size 102400 app graphic
2025/06/04 17:03:37 hitrace enter, running_state is RECORDING_LONG_BEGIN_RECORD
2025/06/04 17:03:37 args: tags:app,graphic bufferSize:204800 overwrite:1 fileSize:102400
2025/06/04 17:03:37 trace capturing.

使用样例2：

从API version 24开始，录制模式下支持指定路径，例如：

$ hitrace --trace_begin --record sched app -o /data/local/tmp --total_size 1024000
2025/06/04 17:03:37 hitrace enter, running_state is RECORDING_LONG_BEGIN_RECORD
2025/06/04 17:03:37 args: tags:sched, app bufferSize:18432 overwrite:1 totalSize:1024000
2025/06/04 17:03:37 trace capturing.

采集结束时，使用以下命令停止采集，命令行窗口会显示生成的文件的绝对路径。

hitrace --trace_finish --record

使用样例：

$ hitrace --trace_finish --record
2025/06/04 17:06:14 hitrace enter, running_state is RECORDING_LONG_FINISH_RECORD
2025/06/04 17:06:15 capture done, output files:
    /data/log/hitrace/record_trace_20250604170337@614463-183970330.sys
    /data/log/hitrace/record_trace_20250604170423@614508-554071886.sys
    /data/log/hitrace/record_trace_20250604170552@614597-598551039.sys
捕获trace后进行压缩
hitrace -z -b 102400 -t 10 sched freq idle disk -o /data/local/tmp/test.ftrace

使用样例：

$ hitrace -z -b 102400 -t 10 sched freq idle disk -o /data/local/tmp/test.ftrace
2024/11/14 12:00:18 start capture, please wait 10s ...
2024/11/14 12:00:28 capture done, start to read trace.
2024/11/14 12:00:29 trace read done, output: /data/local/tmp/test.ftrace
2024/11/14 12:00:29 TraceFinish done.
设置和查询trace输出级别阈值

打点级别优先级从高到低分别为 M（Commercial）、C（Critical）、I（Info）、D（Debug），低于trace输出级别阈值的打点将不会生效。

开发者可使用带trace级别的打点接口（参考@ohos.hiTraceMeter和trace.h中的API version 19的trace打点接口），测试不同阈值下的trace输出是否符合预期。

// 设置trace输出级别阈值
hitrace --trace_level D/I/C/M
hitrace --trace_level Debug/Info/Critical/Commercial
// 查询trace输出级别阈值
hitrace --get_level

使用样例：

$ hitrace --trace_level Info
2025/08/16 10:34:23 hitrace enter, running_state is SET_TRACE_LEVEL
2025/08/16 10:34:23 success to set trace level.
$ hitrace --get_level
2025/08/16 10:34:29 hitrace enter, running_state is GET_TRACE_LEVEL
2025/08/16 10:34:29 the current trace level threshold is Info
trace文件名说明

使用hitrace命令行工具采集二进制格式trace信息时，可以指定文件路径（目前仅支持设定路径为/data/local/tmp）。默认保存在/data/log/hitrace路径下，hitrace自动生成文件名并将绝对路径显示在命令行窗口。

快照模式下生成的trace文件名以trace开头，录制模式下生成的trace文件名以record开头，后面为本地时间和boot time（从开机时间开始的时间戳）。

以下面这个文件名为例：20250701215441说明这个文件生成的时间为2025年7月1日21时54分41秒，此时对应的boot time为6016.653165227。

$ hitrace --dump_bgsrv
2025/07/01 21:54:41 hitrace enter, running_state is SNAPSHOT_DUMP
2025/07/01 21:54:42 DumpSnapshot done, output:
    /data/log/hitrace/trace_20250701215441@6016-653165227.sys
常见问题
执行hitrace命令后显示错误码1

现象描述

执行hitrace命令后报错，错误码为1。

$ hitrace --dump_bgsrv
2025/07/04 17:20:38 hitrace enter, running_state is SNAPSHOT_DUMP
2025/07/04 17:20:38 error: DumpSnapshot failed, errorCode(1)

可能原因&解决方法

错误码1表示hiview进程状态异常，可以尝试重启手机后重新采集。

执行hitrace命令后报错“not support category on this device”

现象描述

执行hitrace命令后报错，命令行窗口显示“not support category on this device”。

$ hitrace -t 10 aaa
2025/07/04 17:24:21 error: aaa is not support category on this device.
2025/07/04 17:24:21 error: parsing args failed, exit.

可能原因&解决方法

命令中指定的tag不存在，建议使用“hitrace -l”命令查看支持的tag范围。

执行hitrace命令后显示错误码1004

现象描述

执行hitrace命令后报错，错误码为1004。

$ hitrace --dump_bgsrv
2025/07/04 17:25:58 hitrace enter, running_state is SNAPSHOT_DUMP
2025/07/04 17:25:58 error: DumpSnapshot failed, errorCode(1004)

可能原因&解决方法

1004表示写入文件错误，可能的原因包括：

采集文本格式trace时，使用-o参数指定输出的文件路径不存在或无权限。建议将trace保存到/data/local/tmp路径下。

磁盘空间已满时，不会生成新的trace文件，建议释放磁盘空间，确保空闲空间大于500MB，然后重新采集。

执行hitrace命令后报错“illegal path”

现象描述

执行hitrace命令后报错，命令行窗口显示“illegal path”。

$ hitrace --dump_bgsrv -o /data/local/test
2026/03/27 17:25:58 hitrace enter, running_state is SNAPSHOT_DUMP
2026/03/27 17:25:58 error: illegal path

可能原因&解决方法

illegal path表示指定的路径非法，可能的原因包括：

采集二进制格式trace时，使用-o参数指定输出的文件路径不是/data/local/tmp或其子目录。改为/data/local/tmp或其子目录即可。

录制模式下，使用-o参数指定输出的文件路径不是/data/local/tmp或其子目录。改为/data/local/tmp或其子目录即可。

PrivacyManagerService
hiperf
