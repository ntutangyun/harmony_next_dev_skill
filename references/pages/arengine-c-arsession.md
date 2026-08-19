# 管理AR会话（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arsession_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.0.0(12)开始，管理AR会话支持部分Phone、部分Tablet设备。并且从6.1.0(23)版本开始，新增支持TV设备。请参考硬件要求判断设备是否支持。

引入AR Engine

引入头文件。

#include "ar/ar_engine_core.h"

编写CMakeLists.txt。

find_library(
    # 设置路径变量的名称。
    arengine-lib
    # 指定希望CMake定位的NDK库的名称。
    libarengine_ndk.z.so
)

target_link_libraries(entry PUBLIC
    ${arengine-lib}
)

创建AR会话

应用开始时，调用HMS_AREngine_ARSession_Create函数创建一个AR会话。

CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));

自定义配置AR会话

创建一个AREngine_ARConfig对象来配置当前AR会话。如缺省，则使用默认配置，具体配置可参考HMS_AREngine_ARConfig_Create。

AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
HMS_AREngine_ARConfig_Destroy(arConfig);

具体可配置项，请参考AR Engine API参考。

销毁AR会话

应用结束时，调用HMS_AREngine_ARSession_Destroy函数销毁当前的AR会话。

HMS_AREngine_ARSession_Destroy(mArSession);

## Code blocks

### Code block 1

```
#include "ar/ar_engine_core.h"
```

### Code block 2

```
find_library(
    # 设置路径变量的名称。
    arengine-lib
    # 指定希望CMake定位的NDK库的名称。
    libarengine_ndk.z.so
)

target_link_libraries(entry PUBLIC
    ${arengine-lib}
)
```

### Code block 3

```
CHECK(HMS_AREngine_ARSession_Create(nullptr, nullptr, &mArSession));
```

### Code block 4

```
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
HMS_AREngine_ARConfig_Destroy(arConfig);
```

### Code block 5

```
HMS_AREngine_ARSession_Destroy(mArSession);
```
