# 获取Native子进程退出信息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi-nativechildprocess-exit-info_

从API version 20开始，支持父进程通过注册回调函数监听子进程，获取子进程异常退出信息，以便父进程做后续优化处理。这里支持监听的子进程必须为OH_Ability_StartNativeChildProcess、OH_Ability_StartNativeChildProcessWithConfigs或startNativeChildProcess接口创建的子进程。

接口说明
名称	描述
Ability_NativeChildProcess_ErrCode OH_Ability_RegisterNativeChildProcessExitCallback (OH_Ability_OnNativeChildProcessExit onProcessExit)	注册子进程退出回调函数。
Ability_NativeChildProcess_ErrCode OH_Ability_UnregisterNativeChildProcessExitCallback (OH_Ability_OnNativeChildProcessExit onProcessExit)	解注册子进程退出回调函数。
开发步骤

动态库文件

libchild_process.so

头文件

#include <AbilityKit/native_child_process.h>
MainProcessFile.cpp

主进程-注册和解注册Native子进程异常退出回调。

调用OH_Ability_RegisterNativeChildProcessExitCallback注册Native子进程，如果返回值为NCP_NO_ERROR表示注册成功。

调用OH_Ability_UnregisterNativeChildProcessExitCallback解注册Native子进程，如果返回值为NCP_NO_ERROR表示解注册成功。

#include <AbilityKit/native_child_process.h>
#include <hilog/log.h>


// ···


void OnNativeChildProcessExit(int32_t pid, int32_t signal)
{
    OH_LOG_INFO(LOG_APP, "pid: %{public}d, signal: %{public}d", pid, signal);
}


void RegisterNativeChildProcessExitCallback()
{
    Ability_NativeChildProcess_ErrCode ret =
        OH_Ability_RegisterNativeChildProcessExitCallback(OnNativeChildProcessExit);
    if (ret != NCP_NO_ERROR) {
        OH_LOG_ERROR(LOG_APP, "register failed.");
    }
    // ···
}


void UnregisterNativeChildProcessExitCallback()
{
    Ability_NativeChildProcess_ErrCode ret =
        OH_Ability_UnregisterNativeChildProcessExitCallback(OnNativeChildProcessExit);
    if (ret != NCP_NO_ERROR) {
        OH_LOG_ERROR(LOG_APP, "unregister failed.");
    }
    // ···
}
MainProcessFile.cpp

主进程-添加编译依赖项。

修改CMaklist.txt添加必要的依赖库，假设主进程所在的so名称为libmainprocesssample.so（主进程和子进程的实现也可以选择编译到同一个动态库文件）。

target_link_libraries(mainprocesssample PUBLIC
    # 添加依赖的元能力动态库
    libchild_process.so
   
    # 其它依赖的动态库
    # ...
)
创建/终止Native子进程（C/C++）
Ability Kit术语
