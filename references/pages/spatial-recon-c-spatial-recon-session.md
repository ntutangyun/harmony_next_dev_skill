# 管理Spatial Recon会话

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-c-spatial-recon-session_

概要

从6.1.0(23)开始，对于任何需要使用空间重建能力的应用，都需要创建一个会话HMS_SpatialRecon_Session，用于管理SpatialRecon Kit的系统状态。该会话需要应用开发者使用本Kit提供的API创建，并在相关任务结束后使用本Kit提供的API手动销毁。

由于空间重建能力会消耗大量系统资源，并非所有设备都支持重建。推荐先通过HMS_SpatialRecon_IsSupport接口来查询当前设备是否支持该特性。

检查当前设备是否支持重建

引入头文件。

#include "SpatialReconKit/spatial_recon_interface.h"

调用接口，根据返回值判断当前设备是否支持使用该特性。

HMS_SpatialReconStatus ret = HMS_SpatialRecon_IsSupport(SPATIAL_RECON_MODEL_TYPE_GS);

如果当前设备支持此特性，会返回SPATIAL_RECON_STATUS_SUCCESS，否则会返回SPATIAL_RECON_STATUS_DEVICE_NOT_SUPPORT。

引入Spatial Recon Kit

引入头文件。

#include "SpatialReconKit/spatial_recon_interface.h"

编写CMakeLists.txt。

find_library(
    # Sets the name of the path variable.
    spatialrecon-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    libspatial_recon_ndk.z.so
)

target_link_libraries(entry PUBLIC
    ${spatialrecon-lib}
)

创建Spatial Recon Kit会话

当需要使用空间重建能力时，应调用HMS_SpatialRecon_CreateSession函数创建一个Spatial Recon Kit会话。

在创建时，需要指定一个工作目录，用于存放重建过程中的必要数据。此工作目录必须是已经存在的目录，且必须是应用文件目录的子目录。

HMS_SpatialRecon_Session* spatialReconSession = nullptr;

const char* workPath = "/data/storage/el1/base/spatial_recon_files/"; // 指定工作目录为 /data/storage/el[1-5]/base/的子目录。开发者可视情况选取不同的加密等级。

HMS_SpatialReconStatus ret = HMS_SpatialRecon_CreateSession(SPATIAL_RECON_MODEL_TYPE_GS, workPath, &spatialReconSession);

创建会话成功后，会返回SPATIAL_RECON_STATUS_SUCCESS，否则返回SPATIAL_RECON_STATUS_FAILED。

销毁Spatial Recon Kit会话

在空间重建session的所有相关任务完成后，开发者可以调用HMS_SpatialRecon_DestroySession函数销毁当前的Spatial Recon Kit会话。

和C/C++的裸指针行为类似，Spatial Recon Kit不保证session具备并发能力，开发者应在确认session相关任务执行完毕，再销毁session。

HMS_SpatialRecon_DestroySession(spatialReconSession);

请注意，如果某session正在执行任务（如重建、保存）时要求销毁，会导致未定义行为。一旦调用了此函数销毁session，则不应该对此session进行任何操作，否则结果是未定义的。

## Code blocks

### Code block 1

```
#include "SpatialReconKit/spatial_recon_interface.h"
```

### Code block 2

```
HMS_SpatialReconStatus ret = HMS_SpatialRecon_IsSupport(SPATIAL_RECON_MODEL_TYPE_GS);
```

### Code block 3

```
#include "SpatialReconKit/spatial_recon_interface.h"
```

### Code block 4

```
find_library(
    # Sets the name of the path variable.
    spatialrecon-lib
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    libspatial_recon_ndk.z.so
)

target_link_libraries(entry PUBLIC
    ${spatialrecon-lib}
)
```

### Code block 5

```
HMS_SpatialRecon_Session* spatialReconSession = nullptr;

const char* workPath = "/data/storage/el1/base/spatial_recon_files/"; // 指定工作目录为 /data/storage/el[1-5]/base/的子目录。开发者可视情况选取不同的加密等级。

HMS_SpatialReconStatus ret = HMS_SpatialRecon_CreateSession(SPATIAL_RECON_MODEL_TYPE_GS, workPath, &spatialReconSession);
```

### Code block 6

```
HMS_SpatialRecon_DestroySession(spatialReconSession);
```
