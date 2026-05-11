# DumpAccChkPoint功能

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-function-dumpaccchkpoint_

固定为每个核分配的打印数据的最大可使用空间为1M，目前该大小不支持修改，若打印超过1M，打印内容不再显示，请开发者控制待打印的数据量。

使用方法（命令行）

在核函数代码中按需在需要打印Tensor偏移数据的地方调用DumpAccChkPoint接口，详情请参见接口说明，样例如下。

DumpAccChkPoint(srcLocal, 5, 32, dataLen);

simulator调测场景执行如下命令，使能Dump开关。

ascendebug kernel --backend simulator --dump-mode acc_chk ... {其他simulator调测参数}

--dump-mode取acc_chk，开启偏移位置打印Tensor模式，其他参数参考NPU调测参数按需配置。

查看dump结果。

Dump偏移位置Tensor数据存放在${root}/${work_dir}/npu路径下，其目录结构、结果说明与DumpTensor功能类似。

接口说明

DumpAccChkPoint接口说明如下。

函数原型：

void DumpAccChkPoint(const LocalTensor<T> &tensor, uint32_t desc, uint32_t offset, uint32_t dumpNum)
void DumpAccChkPoint(const GlobalTensor<T> &tensor, uint32_t desc, uint32_t offset, uint32_t dumpNum)

函数功能： 支持指定偏移位置的Tensor打印。

参数(IN)：

tensor： 开发者需要Dump的Tensor。多个DumpTensor调用时，不可重复。
待dump的Tensor位于Unified Buffer/L1 Buffer/L0C Buffer时使用LocalTensor类型的Tensor参数输入。
待dump的Tensor位于Global Memory时使用GlobalTensor类型的Tensor参数输入。
当前支持的数据类型为uint8_t、int8_t、int16_t、uint16_t、int32_t、uint32_t、float、half。
desc： 开发者自定义附加信息（行号或其他自定义数字）。
offset： 偏移元素个数。
dumpNum： 需要Dump的元素个数。

参数(OUT)： NA

返回值： NA

使用约束：

当前接口仅支持位于Unified Buffer/L1 Buffer/L0C Buffer/Global Memory的数据Dump。
偏移量需符合UB读取数据32B对齐的限制，即offset*sizeof(T)需按32B对齐。
每次Dump的大小(dataNum*sizeof(T))需要32B对齐。

调用示例：

DumpAccChkPoint(srcLocal, 7, 32 , 128);
DumpTensor功能
assert功能
