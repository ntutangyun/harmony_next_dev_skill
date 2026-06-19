# Enterprise Threat Protection Kit术语

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-glossary_

A

[h2]Access Restriction；访问限制

Enterprise Threat Protection Kit中对文件访问范围设定的限制规则，规定了哪些目录下的文件可以被应用扫描。默认支持用户公共目录、云盘目录、外部存储目录、网络邻居目录和应用el2级别加密数据目录、应用安装包目录，且访问和处置操作受限于应用类型为调试类型或企业应用。

D

[h2]Disposal Restriction；处置限制

Enterprise Threat Protection Kit中对文件处置操作（隔离、恢复、删除）设定的限制规则，规定了哪些目录下的文件允许被处置。不同目录的处置能力不同，例如应用安装包目录不支持处置，建议以应用维度处置而非直接文件操作。

I

Isolation ID；隔离ID

隔离文件唯一标识符，格式为UUID，长度为36个字符。在文件被隔离时由系统生成并返回，用于后续的隔离文件查询、恢复和删除等操作。

Q

[h2]Quarantine Query；隔离查询

获取当前用户下由指定应用隔离的处于隔离状态的文件信息列表的能力。当安全防护类应用更新或卸载导致本地数据库中隔离信息丢失时，可通过此能力获取自身已隔离的文件信息，保障隔离恢复和隔离删除的可操作性。

[h2]Quarantine Zone；隔离区

设备中临时存放被识别为威胁的文件的存储区域，会占用磁盘空间。文件被隔离后转移至此区域，与正常文件系统隔离存放。
