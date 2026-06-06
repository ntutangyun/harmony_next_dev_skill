# GetUserWorkspace

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getuserworkspace_

获取开发者使用的workspace指针。如果使用了Matmul等需要系统workspace的高阶API，kernel侧需要通过SetSysWorkSpace设置系统workspace，此时开发者workspace需要通过该接口获取。

函数原型
__aicore__ inline GM_ADDR GetUserWorkspace(GM_ADDR workspace)
参数说明

表1 接口参数说明

参数名称	输入/输出	描述
workspace	输入	传入workspace的指针，包括系统workspace和开发者使用的workspace。
支持的型号

Kirin9020系列处理器

KirinX90系列处理器

注意事项

无

返回值

开发者使用workspace指针。

SetSysWorkSpace
核内同步
