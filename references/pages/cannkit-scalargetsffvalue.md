# ScalarGetSFFValue

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalargetsffvalue_

__aicore__ inline int64_t ScalarGetSFFValue(uint64_t valueIn)
参数说明

表1 参数说明

参数名	输入/输出	描述
valueIn	输入	输入数据，数据类型是uint64_t。
countValue	输入	获取到第一个0或1的位置。数据类型是int，值为0或1。
返回值

valueIn中第一个0或1出现的位置。

支持的型号

Kirin9020系列处理器

KirinX90系列处理器

约束说明

无。

调用示例
uint64_t valueIn = 28;
// 输出数据(oneCount): 2
int64_t oneCount = AscendC::ScalarGetSFFValue<1>(valueIn);
CountBitsCntSameAsSignBit
矢量计算
