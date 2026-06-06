# GetLibApiWorkSpaceSize

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getlibapiworkspacesize_

static ge::graphStatus TilingFunc(gert::TilingContext* context)
{
    AddApiTiling tiling;
    // ...
    size_t usrSize = 256; // 设置开发者需要使用的workspace大小。
    // 如需要使用系统workspace需要调用GetLibApiWorkSpaceSize获取系统workspace的大小。
    auto ascendcPlatform = platform_ascendc:: PlatformAscendC(context->GetPlatformInfo());
    uint32_t sysWorkspaceSize = ascendcPlatform.GetLibApiWorkSpaceSize();
    size_t *currentWorkspace = context->GetWorkspaceSizes(1); // 通过框架获取workspace的指针，GetWorkspaceSizes入参为所需workspace的块数。当前限制使用一块。
    currentWorkspace[0] = usrSize + sysWorkspaceSize; // 设置总的workspace的数值大小，总的workspace空间由框架来申请并管理。
    // ...
}
GetCoreMemBw
内部关联接口
