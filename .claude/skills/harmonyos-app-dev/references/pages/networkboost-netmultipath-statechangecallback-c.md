# 多网状态监听(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-statechangecallback-c_

int32_t HMS_NetworkBoost_RegisterMultiPathStateChangeCallback(HMS_NetworkBoost_OnMultiPathStateChangecallback, uint32_t *callbackId)	注册多网状态变化事件。
int32_t HMS_NetworkBoost_UnregisterMultiPathStateChangeCallback(uint32_t callbackId)	去注册多网状态变化事件。
开发步骤

导入Network Boost Kit模块。

#include "NetworkBoostKit/network_boost_handover.h"
#include <cstdio>

CMakeLists.txt中添加以下lib，具体请见C API开发准备。

libnetwork_boost.so

调用HMS_NetworkBoost_RegisterMultiPathStateChangeCallback接口，获取多网状态变化信息。

uint32_t callbackId = 0;
void onMultiPathStateChangeCallback(NetworkBoost_MultiPathStateChange* result)
{
    // 多网状态变化回调处理
}


int32_t RegisterMultiPathStateChange()
{
    // 注册回调，获取回调Id
    int32_t ret = HMS_NetworkBoost_RegisterMultiPathStateChangeCallback(onMultiPathStateChangeCallback, &callbackId);
    printf("注册多网状态监听回调结果: %d, Id：%d\n", ret, callbackId);
    return ret;
}

当应用业务流程结束，通过取消注册的方式取消多网状态监听。

int32_t UnregisterMultiPathStateChange() {
    // 使用注册时获取的回调Id取消注册
    int32_t ret = HMS_NetworkBoost_UnregisterMultiPathStateChangeCallback(callbackId);
    printf("取消多网状态监听回调结果: %d\n", ret);
    return ret;
}
业务场景设置(C/C++)
多网建议监听(C/C++)
