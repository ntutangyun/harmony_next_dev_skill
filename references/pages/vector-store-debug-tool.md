# vector

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vector-store-debug-tool_

---- 1 shell shell u:object_r:debug_hap_data_file:s0  77824 2025-08-12 20:12 arkdata
-rw------- 1 shell shell u:object_r:debug_hap_data_file:s0   8208 2025-08-12 20:13 arkdata.ctrl
-rw------- 1 shell shell u:object_r:debug_hap_data_file:s0  24592 2025-08-12 20:13 arkdata.ctrl.dwr
-rw------- 1 shell shell u:object_r:debug_hap_data_file:s0    512 2025-08-12 20:13 arkdata.redo
-rw------- 1 shell shell u:object_r:debug_hap_data_file:s0      8 2025-08-12 20:13 arkdata.safe
-rw------- 1 shell shell u:object_r:debug_hap_data_file:s0  28672 2025-08-12 20:12 arkdata.undo

打开已有数据库。

$ arkdata -t vector -f ./data/vector/arkdata
Enter ".help" for usage hints.
vector>>>
创建表

在vector>>>提示符下，通过create table命令创建单个表。

// 单条单行创建表
vector>>> create table t1(a int unique, b text);
vector>>> .schema
+-------+------+----------+----------------------------------------+
| type  | name | tbl_name | sql                                    |
+-------+------+----------+----------------------------------------+
| TABLE | T1   | T1       | create table t1(a int unique, b text); |
+-------+------+----------+----------------------------------------+
// 单条多行创建表
vector>>> create table t7(
a int unique,
b text);
vector>>> .schema
+-------+------+----------+---------------------------------------+
| type  | name | tbl_name | sql                                   |
+-------+------+----------+---------------------------------------+
| TABLE | t7   | t7       | create table t7(a int unique,b text); |
+-------+------+----------+---------------------------------------+

在vector>>>提示符下，通过以下对应命令创建多个表。

// 单行多条创建表
vector>>> create table t7(a int unique, b text); create table t8(a int unique, b text);
vector>>> .schema
+-------+------+----------+-----------------------------------------+
| type  | name | tbl_name | sql                                     |
+-------+------+----------+-----------------------------------------+
| TABLE | t7   | t7       | create table t7(a int unique, b text);  |
| TABLE | t8   | t8       |  create table t8(a int unique, b text); |
+-------+------+----------+-----------------------------------------+
// 多行多条创建表
vector>>> create table t7(
a int unique,
b text);
create table t8(
a int unique,
b text);
vector>>> .schema
+-------+------+----------+---------------------------------------+
| type  | name | tbl_name | sql                                   |
+-------+------+----------+---------------------------------------+
| TABLE | t7   | t7       | create table t7(a int unique,b text); |
| TABLE | t8   | t8       | create table t8(a int unique,b text); |
+-------+------+----------+---------------------------------------+
查询表

在vector>>>提示符下，通过.table命令，列出数据库中所有表的名字，显示结果如下：

vector>>>.table
+------+
| name |
+------+
| T1   |
| T2   |
| T3   |
+------+

通过.schema命令，显示数据库中所有表的结构信息，显示结果如下：

vector>>>.schema
+-------+-------+----------+----------------------------------------+
| type  | name  | tbl_name | sql                                    |
+-------+-------+----------+----------------------------------------+
| TABLE | T1    | T1       | create table t1(a int unique, b text); |
| TABLE | T2    | T2       | create table t2(a int unique, b text); |
| TABLE | T3    | T3       | create table t3(a int, b text);        |
| TABLE | t7    | t7       | create table t7(a int unique,b text);  |
| TABLE | t8    | t8       | create table t8(a int unique,b text);  |
Press 'q' to quit, 'n' to continue: i
Invalid input. Press 'q' to quit, 'n' to continue: n
| TABLE | T9   | T9       | create table t9(a int unique,b text);  |
+-------+-------+----------+----------------------------------------+
说明

当显示数据条目达到5条时，为提升阅读体验，系统将提示用户是否继续显示或退出。输入q键退出显示，输入n继续显示结果。

重命名表名

在vector>>>提示符下，通过"alter table t1 rename to new_t1;"命令重命名对应的表名，显示结果如下：

vector>>> .schema
+-------+------+----------+--------------------------------------+
| type  | name | tbl_name | sql                                  |
+-------+------+----------+--------------------------------------+
| TABLE | T1   | T1       | create table t1( a int, new_b text); |
+-------+------+----------+--------------------------------------+
vector>>> alter table t1 rename to new_t1;  // 更改t1的表名为new_t1
vector>>> .schema
+-------+--------+----------+------------------------------------------+
| type  | name   | tbl_name | sql                                      |
+-------+--------+----------+------------------------------------------+
| TABLE | NEW_T1 | NEW_T1   | create table NEW_T1( a int, new_b text); |
+-------+--------+----------+------------------------------------------+
增加表字段

在vector>>>提示符下，通过"alter table t1 add column c text;"命令进行增加表字段，显示结果如下：

vector>>> create table t1( a int, b text);
vector>>> .schema
+-------+------+----------+----------------------------------+
| type  | name | tbl_name | sql                              |
+-------+------+----------+----------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text); |
+-------+------+----------+----------------------------------+
vector>>> alter table t1 add column c text;  // 在t1的表中，增加一个名为c，内容类型为text的字段
vector>>> .schema
+-------+------+----------+------------------------------------------+
| type  | name | tbl_name | sql                                      |
+-------+------+----------+------------------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text, c text); |
+-------+------+----------+------------------------------------------+
重命名表字段

在vector>>>提示符下，通过"alter table t1 rename b to new_b;"命令重命名对应的表字段，显示结果如下：

vector>>> .schema
+-------+------+----------+----------------------------------+
| type  | name | tbl_name | sql                              |
+-------+------+----------+----------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text); |
+-------+------+----------+----------------------------------+
vector>>> alter table t1 rename b to new_b; // 重命名t1表b字段为new_b
vector>>> .schema
+-------+------+----------+--------------------------------------+
| type  | name | tbl_name | sql                                  |
+-------+------+----------+--------------------------------------+
| TABLE | T1   | T1       | create table t1( a int, new_b text); |
+-------+------+----------+--------------------------------------+
删除表字段

在vector>>>提示符下，通过"alter table t1 drop column c;"命令删除指表中指定字段，显示结果如下：

vector>>> .schema
+-------+------+----------+------------------------------------------+
| type  | name | tbl_name | sql                                      |
+-------+------+----------+------------------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text, c text); |
+-------+------+----------+------------------------------------------+
vector>>> alter table t1 drop column c;  // 删除t1表中名为c的字段
vector>>> .schema
+-------+------+----------+----------------------------------+
| type  | name | tbl_name | sql                              |
+-------+------+----------+----------------------------------+
| TABLE | T1   | T1       | create table t1( a int, b text); |
+-------+------+----------+----------------------------------+
删除表

在vector>>>提示符下，通过"drop table t1;"命令，删除数据库中的名为t1的表，显示结果如下：

vector>>>drop table t1;  // 删除表t1
vector>>>.table
+------+
| name |
+------+
| T2   |
+------+
添加表索引

在vector>>>提示符下，通过"create index idx_1 on t3(a);"命令给该表对应字段，添加索引，显示结果如下：

vector>>> create table t3(a int, b text);  // 仅在表内未添加数据的情况下才能创建索引。
vector>>> create index idx_1 on t3(a);     // 给该表对应字段，添加索引为idx_1
vector>>> .index
+-------+
| name  |
+-------+
| idx_1 |
+-------+
插入数据

在vector>>>提示符下，通过"insert into t2 values(1,'xx'),(2,'yy');"命令插入指定键值对，显示结果如下：

vector>>> insert into t2 values(1,'xx'),(2,'yy');
vector>>> select * from t2;
+----+----+
| a  | b  |
+----+----+
| 1  | xx |
| 2  | yy |
+----+----+
vector>>> create table t1(a int unique, b text);
vector>>> insert into t1 values(1,'x'),(2,'y');
vector>>> select * from t1;
+----+----+
| a  | b  |
+----+----+
| 1  | x  |
| 2  | y  |
+----+----+

在vector>>>提示符下，通过以下对应命令插入多条数据。

// 单条多行插入数据
vector>>> insert into t7 values(1,'x'),
(2,'y');
vector>>> select * from t7;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
+----+---+
// 单行多条插入数据
vector>>> insert into t7 values(1,'x');insert into t7 values(2,'y');
vector>>> select * from t7;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
+----+---+
// 多行多条插入数据
vector>>> insert into t7 values(1,'x'),
(2,'y');
insert into t8 values(1,'xx'),
(2,'yy');
vector>>> select * from t7;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
+----+---+
vector>>> select * from t8;
+----+----+
| a  | b  |
+----+----+
| 1  | xx |
| 2  | yy |
+----+----+
查询数据

全表查询。

在vector>>>提示符下，通过".mode print"和"select * from 表名;"命令查询指定表所有内容，显示结果如下：

vector>>> .mode print
vector>>> select * from t1;
[row-0]
a            = 1
b            = x
[row-1]
a            = 2
b            = y

通过".mode table"和"select * from 表名;"命令查询指定表所有内容，显示结果如下：

vector>>> .mode table
vector>>> select * from t1;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
+----+---+

在vector>>>提示符下，通过"select * from 表名 where 筛选条件"命令查询指定key的键值对，显示结果如下：

vector>>> select * from t1 where a =1;
+----+---+
| a  | b |
+----+---+
| 1  | x |
+----+---+

在vector>>>提示符下，通过.count命令列出所有表的记录总数，显示结果如下：

vector>>> .count
+------------+--------------+
| table_name | record_count |
+------------+--------------+
| T1         | 2            |
| T2         | 2            |
| T3         | 0            |
+------------+--------------+
更新数据

在vector>>>提示符下，通过"update t1 set b = 'z' where a =3;"命令更新键值对，显示结果如下：

vector>>> select * from t1;
+----+----+
| a  | b  |
+----+----+
| 1  | x  |
| 2  | y  |
| 3  | xx |
+----+----+
vector>>> update t1 set b = 'z' where a =3;
vector>>> select * from t1;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
| 3  | z |
+----+---+
删除数据

在vector>>>提示符下，通过"delete from t1 where b = 'z';"命令删除表中指定键值对，显示结果如下：

vector>>> select * from t1;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
| 3  | z |
+----+---+
vector>>> delete from t1 where b = 'z';// 删除t1表中的z
vector>>> select * from t1;
+----+---+
| a  | b |
+----+---+
| 1  | x |
| 2  | y |
+----+---+

在vector>>>提示符下，可以使用 .q或者.quit命令退出数据库交互模式，显示结果如下：

vector>>>.q
$
模拟器支持情况

当前工具支持模拟器。

常见问题
如何删除字符

使用Ctrl+BackSpace删除单个字符，使用Ctrl+U删除全部字符。

preferences数据库调试工具指导
SQLite调试工具指导
