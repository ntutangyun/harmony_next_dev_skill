# 业务场景设置(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-netmultipath-setscenedesc-c_

int32_t HMS_NetworkBoost_SetSceneDesc(NetworkBoost_SceneDesc sceneDesc)	设置业务场景。
开发步骤

导入Network Boost Kit模块。

#include "NetworkBoostKit/network_boost.h"
#include <cstdio>

CMakeLists.txt中添加以下lib，具体请见C API开发准备。

libnetwork_boost.so

调用SetSceneDesc接口。

int32_t SetSceneDesc()
{
    NetworkBoost_SceneDesc sceneDesc;
    sceneDesc.duration = 0;
    sceneDesc.startTime = 0;
    sceneDesc.scene = NB_SERVICE_LOGIN;
    sceneDesc.sceneEvent = SCENE_EVENT_ENTER;
    int32_t ret = HMS_NetworkBoost_SetSceneDesc(sceneDesc);
    printf("业务场景设置结果: %d\n", ret);
    return ret;
}
连接迁移(多网并发)（C/C++）
多网状态监听(C/C++)
