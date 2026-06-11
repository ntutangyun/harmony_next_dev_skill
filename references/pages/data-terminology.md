# ArkData术语

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-terminology_

WAL模式

WAL（Write Ahead Log）模式是SQLite日志模式中的一种，区别于传统的rollback journal（回滚日志）模式，用于提升并发性能和写入效率。

详细介绍，请查看SQLite Write-Ahead Logging介绍。

FULL模式

FULL模式是SQLite中数据库同步写入策略之一，当每次执行数据修改时，SQLite都会调用底层操作系统的xSync方法，保证所有数据均安全写入磁盘。可在系统崩溃、断电场景保证数据库不会损坏。

详细介绍，请查看SQLite synchronous。
