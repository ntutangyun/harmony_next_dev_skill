# preferences数据库调试工具指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preferences-debug-tool_

- 1 shell shell u:object_r:debug_hap_data_file:s0  73728 2025-08-12 20:31 arkdata
-rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0   4112 2025-08-12 20:31 arkdata.ctrl
-rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0  12304 2025-08-12 20:31 arkdata.ctrl.dwr
-rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0      0 2025-08-12 20:31 arkdata.map
-rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0    512 2025-08-12 20:31 arkdata.redo
-rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0      8 2025-08-12 20:31 arkdata.safe
-rw-rw---- 1 shell shell u:object_r:debug_hap_data_file:s0  16384 2025-08-12 20:31 arkdata.undo


$ ls -lZ ./data/preference_xml/
total 12
-rw-rw---- 1 root ddms u:object_r:debug_hap_data_file:s0  105 2025-09-05 15:11 arkdata
-rw-rw---- 1 root ddms u:object_r:debug_hap_data_file:s0    0 2025-09-05 15:11 arkdata.lock

打开已有数据库。

$ arkdata -t preference_kv -f ./data/preference_kv/arkdata
Enter ".help" for usage hints.
preference_kv>>>
插入数据

在preference_kv>>>提示符下，可通过put命令插入指定键值对，显示结果如下：

preference_kv>>> put key:name
 ...>>> value:123
preference_kv>>> put key:id_name
 ...>>> value:'123'
preference_kv>>> get key:name   // 不带引号结果
type int: 123
preference_kv>>> get key:id_name   // 带引号结果
type string: 123
全表查询

在preference_xml>>>提示符下，可通过scan命令全表查询，显示结果如下：

preference_xml>>> scan
==========================PREFERENCES XML INFO============================
DataCount:7
==========================PREFERENCES XML DATA============================
==========================Data Index:1==========================
key:
1
value:
type int: 1
==========================Data Index:2==========================
key:
2
value:
type int: 2
==========================Data Index:3==========================
key:
3
value:
type int: 3
==========================Data Index:4==========================
key:
4
value:
type int: 4
==========================Data Index:5==========================
key:
5
value:
type int: 5
Press 'q' to quit, 'n' to continue: n
==========================Data Index:6==========================
key:
6
value:
type int: 6
==========================Data Index:7==========================
key:
7
value:
type int: 7
preference_xml>>>

preference_kv不支持全表扫描，显示结果如下：

preference_kv>>> scan
[unsucc] Unable to parse command.
说明

当显示数据条目达到5条时，为提升阅读体验，系统将提示用户是否继续显示或退出。输入q键退出显示，输入n继续显示结果。

单值查询

在preference_kv>>>提示符下，可通过get命令指定key查询指定键值对，显示结果如下：

preference_kv>>> get key:name
 No data for key = name  // 表示没有值

带引号与不带引号查询的值不同，显示结果如下：

preference_kv>>> put key:name
 ...>>> value:123
preference_kv>>> put key:id_name
 ...>>> value:'123'
preference_kv>>> put key:name
 ...>>> value:true
preference_kv>>> put key:name1
 ...>>> value:'true'
preference_kv>>> get key:name      // 数字不带引号结果
type int: 123
preference_kv>>> get key:id_name   // 数字带引号结果
type string: 123
preference_kv>>> get key:name      // true不带引号结果
type bool: 1
preference_kv>>> get key:name1     // true带引号结果
type string: true
更新数据

在preference_kv>>>提示符下，当key值存在时， 可通过put命令更新键值对，显示结果如下：

preference_kv>>> put key:name
 ...>>> value:x
preference_kv>>> get key:name
type string: x
preference_kv>>> put key:name
 ...>>> value:y
preference_kv>>> get key:name
type string: y
删除数据

在preference_kv>>>提示符下，可通过delete命令删除指定键值对，显示结果如下：

preference_kv>>> get key:name
type string: y
preference_kv>>> delete key:name
preference_kv>>> get key:name
 No data for key = key:name

delete命令不指定键值对全表删除，显示结果如下：

preference_kv>>> get key:name
type int: xx
preference_kv>>> get key:id_name
type int: yy
preference_kv>>> delete
preference_kv>>> get key:name
 No data for key = name
preference_kv>>> get key:id_name
 No data for key = id_name

在preference_kv>>>提示符下，可以使用 .q或者.quit命令退出数据库交互模式，显示结果如下：

preference_kv>>>.q
$
模拟器支持情况

当前工具支持模拟器。

常见问题
如何删除字符

使用Ctrl+BackSpace删除单个字符，使用Ctrl+U删除全部字符。

arkdata数据库调试工具
vector-store数据库调试工具指导
