# hilog

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog_

---------------------------------------------------------
Domain Table:
LOGTYPE- DOMAIN---- TAG----------------------------- MAX_FREQ-- TIME---------------- MAX_TP---- TIME---------------- LINES----- LENGTH---- DROPPED---
app----- 0xf00----- -------------------------------- 924.00---- 11-15 16:04:25.594-- 111975.00- 11-15 16:04:25.594-- 3386------ 371.5K---- 0---------
app----- 0x0------- -------------------------------- 285.00---- 11-15 16:04:34.877-- 44242.00-- 11-15 16:04:34.877-- 990------- 129.2K---- 0---------

统计信息说明

MAX_FREQ：日志打印频率最高的每秒行数。
TIME：    对应发生时间。
MAX_TP：  日志打印频率最高的每秒字节数。
LINES：   统计周期内的总行数。
LENGTH：  统计周期内的总字节数。
DROPPED： 统计周期内丢失的行数。
清除统计信息
hilog -S

使用样例：

$ hilog -S
Statistic info clear successfully
进程超限开关
hilog -Q pidon/pidoff

使用样例：

开启进程超限管控：

$ hilog -Q pidon
Set flow control by process to enabled successfully

关闭进程超限管控：

$ hilog -Q pidoff
Set flow control by process to disabled successfully
domain超限开关
hilog -Q domainon/domainoff

使用样例：

开启domain超限管控：

$ hilog -Q domainon
Set flow control by domain to enabled successfully

关闭domain超限管控：

$ hilog -Q domainoff
Set flow control by domain to disabled successfully
hilog超限机制介绍

日志打印量过大时，会触发hilog超限管控机制。触发后，超出部分的日志会被丢弃，并且打印超限提示日志。debug应用默认关闭此机制。

超限机制介绍如下：

应用日志

进程维度管控，打印到LOG_APP buffer里面的应用日志适配了pid超限机制，当某进程打印的LOG_APP类型日志量在一秒内超过阈值时会触发管控，超限提示日志示例如下：

04-19 17:02:34.219  5394  5394 W A00032/com.example.myapplication/LOGLIMIT: ==com.example.myapplication LOGS OVER PROC QUOTA, 3091 DROPPED==

本条日志表示进程com.example.myapplication存在日志打印超限，在17:02:34.219时间点前，有3091行日志由于超限管控丢弃，未打印出来。

处理方式：可参考进程超限开关，关闭对应管控机制。

系统日志

domainID维度管控，打印到LOG_CORE buffer里面的系统日志适配了domain超限机制，当某domainID打印的LOG_CORE类型日志量在一秒内超过阈值时触发管控，超限提示日志示例如下：

04-19 17:02:34.219  5394  5394 W C02C02/system_test/LOGLIMIT: 108 line(s) dropped in a second!

本条日志表示domainID为02C02的日志存在日志打印超限，在17:02:34.219时间点前，有108行日志由于超限管控丢弃，未打印出来。

处理方式：可参考domain超限开关，关闭对应管控机制。

日志丢失处理方法

目前日志丢失场景都有相应的维测信息，可以在hilog日志里面搜索对应关键字查看日志具体丢失的原因。

可以使用正则表达式来搜索包含这些关键字的日志行：LOGLIMIT|Slow reader missed|write socket failed。

LOGLIMIT是进程或domainID超限管控的丢失；Slow reader missed是全局的日志丢失；write socket failed是进程对应的日志丢失。

说明

当出现这些打印时，说明日志已经丢失，无法恢复找回。

如果是在线运维场景出现，需要参考下方处理方式并且本地复现，然后查看完整日志。

LOGLIMIT

含义：日志打印超限，该进程或者domainID被管控。属于领域日志量超出hilog规格后的主动管控，需要领域对日志进行精简和整改。提示日志示例如下：

04-19 17:02:34.219  5394  5394 W A00032/com.example.myapplication/LOGLIMIT: ==com.example.myapplication LOGS OVER PROC QUOTA, 3091 DROPPED==

处理方式：可参考hilog超限机制介绍，关闭对应管控机制。

Slow reader missed

含义：打印时间点前后日志量太大，hilog buffer中的日志还未落盘已经被循环覆盖了。提示日志示例如下：

04-19 17:02:34.219     0     0 I C00000/HiLog: ========Slow reader missed log lines: 137

原因：以下任意一种情况，均有可能导致全局日志丢失。

日志级别设置为D。

关闭了超限管控。

有模块在循环打印日志。

处理方式：

通过hilog -g命令查询当前buffer大小。

通过hilog -G命令扩大hilog buffer大小。如下命令表示将buffer大小修改为16MB（当前允许的最大规格为16MB）。

hilog -G 16M

同时查看是否后台有领域频繁打印日志。若发现某个领域日志频繁打印，影响正常日志读取，可参考“write socket failed”的规避方式，通过命令关闭其领域的日志打印。

write socket failed

含义：日志写入socket失败，出现丢包问题。提示日志示例如下：

04-19 17:02:34.219  5394  5394 W A00032/com.example.myapplication/HiLog: write socket failed, 8 line(s) dropped!

原因：以下任意一种情况，均有可能导致进程日志丢失。

日志级别设置为D。

关闭了超限管控。

有模块在循环打印日志。

存在高负载问题，如果出现CPU高负载或者低内存问题，会导致socket服务端处理日志过慢，socket通道中日志堆积严重，也会导致客户端写入socket数据失败。

处理方式：关闭其他领域的日志打印，只打印本模块的日志。

关闭其他领域日志：

hilog -b X

打开本模块的日志打印：

LOG_APP类型：

hilog -b I -D 0x3200（将03200 domain能够打印出来的日志级别设为INFO）


hilog -b I -D 0x3201（将03201 domain能够打印出来的日志级别设为INFO）

LOG_CORE类型：

hilog -b I -D d003200（将03200 domain能够打印出来的日志级别设为INFO）


hilog -b I -D d003201（将03201 domain能够打印出来的日志级别设为INFO）
network-cfg工具
hilogtool
