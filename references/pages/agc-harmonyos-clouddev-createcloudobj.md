# 创建云对象

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-createcloudobj_

首先您需要在云侧工程下创建云对象。

与云函数名一样，云对象名称长度2-63个字符，仅支持小写英文字母、数字、中划线（-），首字符必须为小写字母，结尾不能为中划线（-）。

handler: 云对象的入口模块及云对象导出的类，通过“.”连接。

functionType：表示函数类型，“0”表示云函数，“1”表示云对象。

triggers：定义了云对象使用的触发器类型，当前云对象仅支持HTTP触发器。

说明

云对象的配置文件“function-config.json”不建议手动修改，否则将导致云对象部署失败或其它错误。
