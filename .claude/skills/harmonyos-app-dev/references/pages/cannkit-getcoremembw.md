# GetCoreMemBw

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcoremembw_

void GetCoreMemBw(const CoreMemType &memType, uint64_t &bwSize) const;
参数说明
参数	输入/输出	说明
memType	输入	硬件存储空间类型。
bwSize	输出	对应硬件的存储空间的带宽大小。单位是Byte/cycle，cycle代表时钟周期。
返回值

无

约束说明

memType输入仅支持L2、HBM。

调用示例
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint64_t l2_bw;
    ascendcPlatform.GetCoreMemBw(platform_ascendc::CoreMemType::L2, l2_bw);
    // ...
    return ret;
}
GetCoreMemSize
GetLibApiWorkSpaceSize
