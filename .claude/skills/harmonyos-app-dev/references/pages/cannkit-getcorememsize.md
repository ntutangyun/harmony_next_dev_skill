# GetCoreMemSize

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorememsize_

void GetCoreMemSize(const CoreMemType &memType, uint64_t &size) const;
参数说明
参数	输入/输出	说明
memType	输入	硬件存储空间类型。
size	输出	对应类型的存储空间大小，单位：字节。
返回值

无

约束说明

无

调用示例
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint64_t ub_size, l1_size;
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ub_size);
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::L1, l1_size);
    // ...
    return ret;
}
CalcTschBlockDim
GetCoreMemBw
