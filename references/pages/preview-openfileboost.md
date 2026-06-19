# 文件打开加速（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preview-openfileboost_

从5.0.3(15)版本开始，新增文件打开加速功能。提供注册和取消注册接口，应用可以注册一系列回调，文件打开加速服务通过调用回调接口向应用推荐文件进行预加载动作。

从26.0.0版本开始，文件打开加速过程中，新增支持应用扫描文件并同步结果给加速服务，加速服务判断该文件是否具备加速条件。

从26.0.0版本起，新增动态参数配置功能，允许应用根据自身需求定制文件预加载策略（如文件后缀、大小范围）。同时，系统还提供文件打开加速服务可用性查询和文件操作事件上报功能，有助于提升预加载的准确性。

接口说明

具体API说明详见文件打开加速接口文档。

表1 文件预加载接口介绍（C API）

接口名	描述
OpenFileBoost_ErrCode HMS_OpenFileBoost_RegisterFilePreload( HMS_OpenFileBoost_QueryAppState queryAppState, HMS_OpenFileBoost_OnFilePreload filePreload, HMS_OpenFileBoost_OnFilePreload cancelFilePreload);	向系统注册文件预加载回调。
typedef OpenFileBoost_AppState (*HMS_OpenFileBoost_QueryAppState)(void);	系统查询APP状态的回调函数定义。
typedef OpenFileBoost_CbErrCode (*HMS_OpenFileBoost_OnFilePreload)(void* fileInfo);	系统向应用推荐或取消推荐预加载文件的回调函数定义。
OpenFileBoost_ErrCode HMS_OpenFileBoost_GetFdFromPreloadFileInfo( void* fileInfo, int32_t* fd);	在向应用推荐文件进行预加载或取消预加载的回调上下文中，应用通过调用该接口获取文件描述符信息。
OpenFileBoost_ErrCode HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo( void* fileInfo, char* sandboxPath, int32_t pathLen);	在向应用推荐文件进行预加载或取消预加载的回调上下文中，应用通过调用该接口获取文件沙箱路径信息。
OpenFileBoost_ErrCode HMS_OpenFileBoost_UnregisterFilePreload(void);	取消注册预加载回调。
OpenFileBoost_ErrCode HMS_OpenFileBoost_NotifyPreloadHit( int32_t fd, char* sandboxPath, int32_t pathLen);	当用户打开预加载文件时，应用调用该接口通知系统预加载命中，这将有助于提高预加载文件预测的准确性。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanOptionCreate (FileScanBoost_ScanOption **outOption)	创建FileScanBoost_ScanOption实例。
void HMS_Preview_FileScanBoost_ScanOptionDestroy (FileScanBoost_ScanOption *option)	销毁FileScanBoost_ScanOption实例。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanOptionAddSupportFile (FileScanBoost_ScanOption *option, const char *suffix, uint32_t suffixLen)	向扫描选项添加支持的文件类型。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultCreate (FileScanBoost_ScanResult **outResult)	创建FileScanBoost_ScanResult实例。
void HMS_Preview_FileScanBoost_ScanResultDestroy (FileScanBoost_ScanResult *result)	销毁FileScanBoost_ScanResult实例。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetState (FileScanBoost_ScanResult *result, FileScanBoost_ScanState state)	在结果中设置扫描状态。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetMaxAtomicTime (FileScanBoost_ScanResult *result, int64_t maxAtomicTime)	在结果中设置最大原子时间。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ScanResultSetMemSize (FileScanBoost_ScanResult *result, int64_t memSize)	在结果中设置内存大小。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_RegisterFileScan (HMS_Preview_FileScanBoost_OnFileScan fileScanCb, FileScanBoost_ScanOption *option)	使用扩展名过滤方式注册多文件类型的回调函数。 在上一次注册结果注销之前，请勿重复注册。 重复注册将返回错误码FILE_SCAN_BOOST_ERROR_ALREADY_REGISTERED， 且仅首次注册的信息生效。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_UnregisterFileScan (void)	移除已注册的文件扫描回调函数。
FileScanBoost_ErrCode HMS_Preview_FileScanBoost_ReportScanResult (const char *path, uint32_t pathLen, FileScanBoost_ScanResult *result)	报告文件扫描操作的完成结果。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_SupportFileCreate (const char *suffix, uint32_t suffixLen, uint64_t lowerLimitKb, uint64_t upperLimitKb, OpenFileBoost_SupportFile **outSupportFile)	创建OpenFileBoost_SupportFile。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_SupportFileDestroy (OpenFileBoost_SupportFile *supportFile)	销毁OpenFileBoost_SupportFile。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsCreate (OpenFileBoost_Options **outOptions)	创建一个空的OpenFileBoost_Options。 使用HMS_Preview_OpenFileBoost_OptionsAddSupportFile添加文件。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsAddSupportFile (OpenFileBoost_Options *options, const OpenFileBoost_SupportFile *supportFile)	向OpenFileBoost_Options添加支持预加载的文件类型。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_OptionsDestroy (OpenFileBoost_Options *options)	销毁OpenFileBoost_Options。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_RegisterFilePreloadWithOption (HMS_OpenFileBoost_QueryAppState queryAppState, HMS_OpenFileBoost_OnFilePreload filePreload, HMS_OpenFileBoost_OnFilePreload cancelFilePreload, OpenFileBoost_Options *options)	注册预加载回调，允许应用传入支持预加载的文件信息。
bool HMS_Preview_OpenFileBoost_IsEnabled (void)	查询应用加速特性是否使能。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_FileOperationInfoCreate (const char *path, uint32_t pathLen, const char *operation, uint32_t operationLen, OpenFileBoost_FileOperationInfo **outFileOperationInfo)	创建OpenFileBoost_FileOperationInfo。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_FileOperationInfoDestroy (OpenFileBoost_FileOperationInfo *fileOperationInfo)	销毁OpenFileBoost_FileOperationInfo。
OpenFileBoost_ErrCode HMS_Preview_OpenFileBoost_NotifyFileOperation (OpenFileBoost_FileOperationInfo *fileOperationInfo)	当用户对文件进行操作时，app调用该接口通知系统文件操作类型，这将有助于提高预加载文件预测的准确性。

开发准备

需要先通过Syscap查询您的目标设备是否支持SystemCapability.PCService.OpenFileBoost系统能力，当前仅在PC/2in1设备上支持该能力。

开发步骤

申请文件打开加速服务的对应权限，在module.json5文件中添加文件预加载权限。注意ohos.permission.PRELOAD_FILE为受限权限，具体可参考申请使用受限权限 。

"requestPermissions":[
  {
    "name": "ohos.permission.PRELOAD_FILE"
  }
]

添加对应的头文件。

#include "PreviewKit/open_file_boost.h"

编写CMakeLists.txt，新增对文件打开加速功能的依赖。

target_link_libraries(entry PUBLIC
    libopen_file_boost.so
)

注册文件预加载回调，注册后系统在条件符合时调用回调向应用推荐文件。

OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_RegisterFilePreload(AppQueryAppStateCb,
    AppOnFilePreload, AppCancelFilePreload);
if (ret != OPEN_FILE_BOOST_SUCCESS){
    // 注册失败，用户可自定义错误处理
}

注册文件预加载回调，应用可传入支持预加载的文件信息，注册后系统在条件符合时调用回调向应用推荐文件。

OpenFileBoost_SupportFile* supportFiles[2] = {nullptr};

// 创建文件类型
OpenFileBoost_ErrCode ret = HMS_Preview_OpenFileBoost_SupportFileCreate(".pptx", 5, 20 * 1024,
    2 * 1024 * 1024, &supportFiles[0]);
if (ret != OPEN_FILE_BOOST_SUCCESS) {
// 应用可自定义错误处理
}

ret = HMS_Preview_OpenFileBoost_SupportFileCreate(".docx", 5, 5 * 1024, 2 * 1024 * 1024, &supportFiles[1]);
if (ret != OPEN_FILE_BOOST_SUCCESS) {
// 销毁之前的创建
    HMS_Preview_OpenFileBoost_SupportFileDestroy(supportFiles[0]);
}

// 创建选项
OpenFileBoost_Options* options = nullptr;
ret = HMS_Preview_OpenFileBoost_OptionsCreate(&options);
if (ret != OPEN_FILE_BOOST_SUCCESS) {

}

// 添加文件类型到选项
ret = HMS_Preview_OpenFileBoost_OptionsAddSupportFile(options, supportFiles[0]);
if (ret != OPEN_FILE_BOOST_SUCCESS) {

}

// 注册文件预加载回调，同时应用传递自己支持的文件后缀类型和文件大小上下限
ret = HMS_Preview_OpenFileBoost_RegisterFilePreloadWithOption(AppQueryAppStateCb,
        AppOnFilePreload, AppCancelFilePreload, options);
if (ret != OPEN_FILE_BOOST_SUCCESS){
    // 注册失败，应用可自定义错误处理
}

应用在当前回调上下文中同步解析预加载文件，或同步阻塞等待解析完毕后再返回，以便系统评估本次预加载文件的资源消耗。

// 查询应用当前状态的回调函数，系统在向应用推荐文件前会先调用状态查询回调函数向应用查询当前是否适合推荐
OpenFileBoost_AppState AppQueryAppStateCb(void)
{
    // 如果当前状态允许进行文件预加载则返回OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD，这里的CanPreload函数为代码示例，表示应用根据实际业务判断是否允许预加载
    if (CanPreload()) {
        return OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD;
    } else {
        return OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD;
    }
}

// 文件预加载回调
OpenFileBoost_CbErrCode AppOnFilePreload(void* fileInfo)
{
    int32_t fileDescriptor = 0;
    // 指针fileInfo仅在当前回调上下文有效，在回调中调用HMS_OpenFileBoost_GetFdFromPreloadFileInfo获取文件描述符
    OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
    if (ret != OPEN_FILE_BOOST_SUCCESS) {
        return OPEN_FILE_BOOST_CALLBACK_FAILURE;
    }
    char sandboxPath[MAX_BUFFER_LENGTH] = {0};
    // 指针fileInfo仅在当前回调上下文有效，在回调中调用HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo获取文件路径
    ret = HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX_BUFFER_LENGTH);
    if (ret != OPEN_FILE_BOOST_SUCCESS) {
        return OPEN_FILE_BOOST_CALLBACK_FAILURE;
    }
    // 用户可保存文件描述符和文件路径，方便后续通知取消预加载时对文件取消预加载
    // 用户自定义具体的文件预加载逻辑
    return OPEN_FILE_BOOST_CALLBACK_SUCCESS;
}

// 取消预加载回调
OpenFileBoost_CbErrCode AppCancelFilePreload(void* fileInfo)
{
    // 同样的方法获取文件描述符和沙箱路径
    int32_t fileDescriptor = 0;
    OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
    if (ret != OPEN_FILE_BOOST_SUCCESS) {
        return OPEN_FILE_BOOST_CALLBACK_FAILURE;
    }
    char sandboxPath[MAX_BUFFER_LENGTH] = {0};
    ret = HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX_BUFFER_LENGTH);
    if (ret != OPEN_FILE_BOOST_SUCCESS) {
        return OPEN_FILE_BOOST_CALLBACK_FAILURE;
    }
    // 用户自定义具体的取消文件预加载逻辑
    return OPEN_FILE_BOOST_CALLBACK_SUCCESS;
}

如果用户打开了已经预加载的文件，应用需要调用HMS_OpenFileBoost_NotifyPreloadHit通知系统，系统会更改文件的预加载状态。

// 传入用户打开的已经预加载的文件描述符、文件路径和长度
OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_NotifyPreloadHit(fileDescriptor, sandboxPath, pathLen);
if (ret != OPEN_FILE_BOOST_SUCCESS){
    // 通知失败，用户可自定义错误处理
}

应用不再需要收到回调，或者在退出流程中时，调用取消预加载接口。

OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_UnregisterFilePreload();
if (ret != OPEN_FILE_BOOST_SUCCESS){
    // 取消注册失败，用户可自定义错误处理
}

应用向系统查询加速开关特性是否可用。

bool switchInfo = HMS_Preview_OpenFileBoost_IsEnabled();
if (switchInfo) {
    // 加速特性可用，应用可处理加速相关业务逻辑
} else {
    // 加速特性不可用，应用可处理自身相关业务逻辑
}

应用向系统传递用户对文件的操作信息。

const char* filePath = "/data/storage/el2/base/files/text.docx";
const char* operationType = "open";
// 创建文件操作信息
OpenFileBoost_FileOperationInfo* fileOpInfo = nullptr;

OpenFileBoost_ErrCode ret = HMS_Preview_OpenFileBoost_FileOperationInfoCreate(
    filePath, static_cast<uint32_t>(strlen(filePath)),
    operationType, static_cast<uint32_t>(strlen(operationType)),
    &fileOpInfo);

if (ret != OPEN_FILE_BOOST_SUCCESS) {
    // 创建失败，应用可自定义错误处理
}

ret = HMS_Preview_OpenFileBoost_NotifyFileOperation(fileOpInfo);
if (ret != OPEN_FILE_BOOST_SUCCESS) {
    // 传递失败，应用可自定义错误处理
}

注册文件扫描回调，确保系统在扫描文件时可以调用回调向应用通知扫描任务。

// 创建扫描选项，添加应用支持的文件类型
FileScanBoost_ScanOption* scanOption = nullptr;
FileScanBoost_ErrCode res = HMS_Preview_FileScanBoost_ScanOptionCreate(&scanOption);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

res = HMS_Preview_FileScanBoost_ScanOptionAddSupportFile(scanOption, "xlsx", 4);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

res = HMS_Preview_FileScanBoost_ScanOptionAddSupportFile(scanOption, "xls", 3);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 注册文件扫描回调
res = HMS_Preview_FileScanBoost_RegisterFileScan(AppOnFileScan, scanOption);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 注册失败，应用可自定义错误处理
}

// 扫描完成需销毁扫描选项
HMS_Preview_FileScanBoost_ScanOptionDestroy(scanOption);

// 文件扫描回调函数，系统调用此回调发送扫描任务
// 应用应在当前回调上下文中同步完成文件解析或同步阻塞等待解析完毕后再返回
FileScanBoost_CbErrCode AppOnFileScan(int32_t fd, const char* path, uint32_t pathLen)
{
    // 应用可在回调中实现具体文件解析逻辑
    // 返回FILE_SCAN_BOOST_CALLBACK_SUCCESS表示接受扫描任务
    // 返回其他值表示拒绝
    return FILE_SCAN_BOOST_CALLBACK_SUCCESS;
}

应用向系统传递扫描结果，确保文件扫描完成后，系统能收到文件扫描结果。

const char* filePath = "/data/storage/el2/base/files/text.xlsx";
// 创建扫描结果
FileScanBoost_ScanResult* scanResult = nullptr;
res = HMS_Preview_FileScanBoost_ScanResultCreate(&scanResult);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 设置扫描状态为成功
res = HMS_Preview_FileScanBoost_ScanResultSetState(scanResult, FILE_SCAN_BOOST_SCAN_STATE_SUCCESS);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 设置最大原子耗时（单位：ms）
res = HMS_Preview_FileScanBoost_ScanResultSetMaxAtomicTime(scanResult, 1500);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 设置内存占用（单位：MB）
res = HMS_Preview_FileScanBoost_ScanResultSetMemSize(scanResult, 3);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 向系统报告扫描结果
res = HMS_Preview_FileScanBoost_ReportScanResult(
    filePath, static_cast<uint32_t>(strlen(filePath)), scanResult);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 报告失败，应用可自定义错误处理
}

// 扫描完成需销毁扫描结果
HMS_Preview_FileScanBoost_ScanResultDestroy(scanResult);

// 报告扫描失败的示例
FileScanBoost_ScanResult* errorResult = nullptr;
res = HMS_Preview_FileScanBoost_ScanResultCreate(&errorResult);
if (res == FILE_SCAN_BOOST_SUCCESS) {
    // 设置扫描状态为处理错误
    HMS_Preview_FileScanBoost_ScanResultSetState(errorResult, FILE_SCAN_BOOST_SCAN_STATE_PROCESS_ERROR);
    HMS_Preview_FileScanBoost_ScanResultSetMaxAtomicTime(errorResult, 0);
    HMS_Preview_FileScanBoost_ScanResultSetMemSize(errorResult, 0);

    // 报告扫描错误结果
    res = HMS_Preview_FileScanBoost_ReportScanResult(
        filePath, static_cast<uint32_t>(strlen(filePath)), errorResult);
    if (ret == FILE_SCAN_BOOST_SUCCESS) {
        // 报告成功
    }

    HMS_Preview_FileScanBoost_ScanResultDestroy(errorResult);
}

应用注销文件扫描回调，确保应用将不再接收扫描任务通知。

res = HMS_Preview_FileScanBoost_UnregisterFileScan();
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 注销失败，应用可自定义错误处理
}

## Code blocks

### Code block 1

```
"requestPermissions":[
  {
    "name": "ohos.permission.PRELOAD_FILE"
  }
]
```

### Code block 2

```
#include "PreviewKit/open_file_boost.h"
```

### Code block 3

```
target_link_libraries(entry PUBLIC
    libopen_file_boost.so
)
```

### Code block 4

```
OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_RegisterFilePreload(AppQueryAppStateCb,
    AppOnFilePreload, AppCancelFilePreload);
if (ret != OPEN_FILE_BOOST_SUCCESS){
    // 注册失败，用户可自定义错误处理
}
```

### Code block 5

```
OpenFileBoost_SupportFile* supportFiles[2] = {nullptr};

// 创建文件类型
OpenFileBoost_ErrCode ret = HMS_Preview_OpenFileBoost_SupportFileCreate(".pptx", 5, 20 * 1024,
    2 * 1024 * 1024, &supportFiles[0]);
if (ret != OPEN_FILE_BOOST_SUCCESS) {
// 应用可自定义错误处理
}

ret = HMS_Preview_OpenFileBoost_SupportFileCreate(".docx", 5, 5 * 1024, 2 * 1024 * 1024, &supportFiles[1]);
if (ret != OPEN_FILE_BOOST_SUCCESS) {
// 销毁之前的创建
    HMS_Preview_OpenFileBoost_SupportFileDestroy(supportFiles[0]);
}

// 创建选项
OpenFileBoost_Options* options = nullptr;
ret = HMS_Preview_OpenFileBoost_OptionsCreate(&options);
if (ret != OPEN_FILE_BOOST_SUCCESS) {

}

// 添加文件类型到选项
ret = HMS_Preview_OpenFileBoost_OptionsAddSupportFile(options, supportFiles[0]);
if (ret != OPEN_FILE_BOOST_SUCCESS) {

}

// 注册文件预加载回调，同时应用传递自己支持的文件后缀类型和文件大小上下限
ret = HMS_Preview_OpenFileBoost_RegisterFilePreloadWithOption(AppQueryAppStateCb,
        AppOnFilePreload, AppCancelFilePreload, options);
if (ret != OPEN_FILE_BOOST_SUCCESS){
    // 注册失败，应用可自定义错误处理
}
```

### Code block 6

```
// 查询应用当前状态的回调函数，系统在向应用推荐文件前会先调用状态查询回调函数向应用查询当前是否适合推荐
OpenFileBoost_AppState AppQueryAppStateCb(void)
{
    // 如果当前状态允许进行文件预加载则返回OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD，这里的CanPreload函数为代码示例，表示应用根据实际业务判断是否允许预加载
    if (CanPreload()) {
        return OPEN_FILE_BOOST_APP_STATE_ALLOW_PRELOAD;
    } else {
        return OPEN_FILE_BOOST_APP_STATE_REJECT_PRELOAD;
    }
}

// 文件预加载回调
OpenFileBoost_CbErrCode AppOnFilePreload(void* fileInfo)
{
    int32_t fileDescriptor = 0;
    // 指针fileInfo仅在当前回调上下文有效，在回调中调用HMS_OpenFileBoost_GetFdFromPreloadFileInfo获取文件描述符
    OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
    if (ret != OPEN_FILE_BOOST_SUCCESS) {
        return OPEN_FILE_BOOST_CALLBACK_FAILURE;
    }
    char sandboxPath[MAX_BUFFER_LENGTH] = {0};
    // 指针fileInfo仅在当前回调上下文有效，在回调中调用HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo获取文件路径
    ret = HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX_BUFFER_LENGTH);
    if (ret != OPEN_FILE_BOOST_SUCCESS) {
        return OPEN_FILE_BOOST_CALLBACK_FAILURE;
    }
    // 用户可保存文件描述符和文件路径，方便后续通知取消预加载时对文件取消预加载
    // 用户自定义具体的文件预加载逻辑
    return OPEN_FILE_BOOST_CALLBACK_SUCCESS;
}

// 取消预加载回调
OpenFileBoost_CbErrCode AppCancelFilePreload(void* fileInfo)
{
    // 同样的方法获取文件描述符和沙箱路径
    int32_t fileDescriptor = 0;
    OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_GetFdFromPreloadFileInfo(fileInfo, &fileDescriptor);
    if (ret != OPEN_FILE_BOOST_SUCCESS) {
        return OPEN_FILE_BOOST_CALLBACK_FAILURE;
    }
    char sandboxPath[MAX_BUFFER_LENGTH] = {0};
    ret = HMS_OpenFileBoost_GetSandboxPathFromPreloadFileInfo(fileInfo, sandboxPath, MAX_BUFFER_LENGTH);
    if (ret != OPEN_FILE_BOOST_SUCCESS) {
        return OPEN_FILE_BOOST_CALLBACK_FAILURE;
    }
    // 用户自定义具体的取消文件预加载逻辑
    return OPEN_FILE_BOOST_CALLBACK_SUCCESS;
}
```

### Code block 7

```
// 传入用户打开的已经预加载的文件描述符、文件路径和长度
OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_NotifyPreloadHit(fileDescriptor, sandboxPath, pathLen);
if (ret != OPEN_FILE_BOOST_SUCCESS){
    // 通知失败，用户可自定义错误处理
}
```

### Code block 8

```
OpenFileBoost_ErrCode ret = HMS_OpenFileBoost_UnregisterFilePreload();
if (ret != OPEN_FILE_BOOST_SUCCESS){
    // 取消注册失败，用户可自定义错误处理
}
```

### Code block 9

```
bool switchInfo = HMS_Preview_OpenFileBoost_IsEnabled();
if (switchInfo) {
    // 加速特性可用，应用可处理加速相关业务逻辑
} else {
    // 加速特性不可用，应用可处理自身相关业务逻辑
}
```

### Code block 10

```
const char* filePath = "/data/storage/el2/base/files/text.docx";
const char* operationType = "open";
// 创建文件操作信息
OpenFileBoost_FileOperationInfo* fileOpInfo = nullptr;

OpenFileBoost_ErrCode ret = HMS_Preview_OpenFileBoost_FileOperationInfoCreate(
    filePath, static_cast<uint32_t>(strlen(filePath)),
    operationType, static_cast<uint32_t>(strlen(operationType)),
    &fileOpInfo);

if (ret != OPEN_FILE_BOOST_SUCCESS) {
    // 创建失败，应用可自定义错误处理
}

ret = HMS_Preview_OpenFileBoost_NotifyFileOperation(fileOpInfo);
if (ret != OPEN_FILE_BOOST_SUCCESS) {
    // 传递失败，应用可自定义错误处理
}
```

### Code block 11

```
// 创建扫描选项，添加应用支持的文件类型
FileScanBoost_ScanOption* scanOption = nullptr;
FileScanBoost_ErrCode res = HMS_Preview_FileScanBoost_ScanOptionCreate(&scanOption);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

res = HMS_Preview_FileScanBoost_ScanOptionAddSupportFile(scanOption, "xlsx", 4);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

res = HMS_Preview_FileScanBoost_ScanOptionAddSupportFile(scanOption, "xls", 3);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 注册文件扫描回调
res = HMS_Preview_FileScanBoost_RegisterFileScan(AppOnFileScan, scanOption);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 注册失败，应用可自定义错误处理
}

// 扫描完成需销毁扫描选项
HMS_Preview_FileScanBoost_ScanOptionDestroy(scanOption);

// 文件扫描回调函数，系统调用此回调发送扫描任务
// 应用应在当前回调上下文中同步完成文件解析或同步阻塞等待解析完毕后再返回
FileScanBoost_CbErrCode AppOnFileScan(int32_t fd, const char* path, uint32_t pathLen)
{
    // 应用可在回调中实现具体文件解析逻辑
    // 返回FILE_SCAN_BOOST_CALLBACK_SUCCESS表示接受扫描任务
    // 返回其他值表示拒绝
    return FILE_SCAN_BOOST_CALLBACK_SUCCESS;
}
```

### Code block 12

```
const char* filePath = "/data/storage/el2/base/files/text.xlsx";
// 创建扫描结果
FileScanBoost_ScanResult* scanResult = nullptr;
res = HMS_Preview_FileScanBoost_ScanResultCreate(&scanResult);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 设置扫描状态为成功
res = HMS_Preview_FileScanBoost_ScanResultSetState(scanResult, FILE_SCAN_BOOST_SCAN_STATE_SUCCESS);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 设置最大原子耗时（单位：ms）
res = HMS_Preview_FileScanBoost_ScanResultSetMaxAtomicTime(scanResult, 1500);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 设置内存占用（单位：MB）
res = HMS_Preview_FileScanBoost_ScanResultSetMemSize(scanResult, 3);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 应用可自定义错误处理
}

// 向系统报告扫描结果
res = HMS_Preview_FileScanBoost_ReportScanResult(
    filePath, static_cast<uint32_t>(strlen(filePath)), scanResult);
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 报告失败，应用可自定义错误处理
}

// 扫描完成需销毁扫描结果
HMS_Preview_FileScanBoost_ScanResultDestroy(scanResult);

// 报告扫描失败的示例
FileScanBoost_ScanResult* errorResult = nullptr;
res = HMS_Preview_FileScanBoost_ScanResultCreate(&errorResult);
if (res == FILE_SCAN_BOOST_SUCCESS) {
    // 设置扫描状态为处理错误
    HMS_Preview_FileScanBoost_ScanResultSetState(errorResult, FILE_SCAN_BOOST_SCAN_STATE_PROCESS_ERROR);
    HMS_Preview_FileScanBoost_ScanResultSetMaxAtomicTime(errorResult, 0);
    HMS_Preview_FileScanBoost_ScanResultSetMemSize(errorResult, 0);

    // 报告扫描错误结果
    res = HMS_Preview_FileScanBoost_ReportScanResult(
        filePath, static_cast<uint32_t>(strlen(filePath)), errorResult);
    if (ret == FILE_SCAN_BOOST_SUCCESS) {
        // 报告成功
    }

    HMS_Preview_FileScanBoost_ScanResultDestroy(errorResult);
}
```

### Code block 13

```
res = HMS_Preview_FileScanBoost_UnregisterFileScan();
if (res != FILE_SCAN_BOOST_SUCCESS) {
    // 注销失败，应用可自定义错误处理
}
```
