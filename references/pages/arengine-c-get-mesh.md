# 获取网格扫描信息（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-get-mesh_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.1.0(18)开始，获取网格扫描信息能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持环境Mesh识别特性（ARENGINE_FEATURE_TYPE_MESH）。

接口说明

以下接口为AR网格扫描相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
HMS_AREngine_ARSession_Create	创建一个新的AREngine_ARSession会话。
HMS_AREngine_ARSession_Update	更新AR Engine的计算结果。
HMS_AREngine_ARSession_Configure	配置AREngine_ARSession会话。
HMS_AREngine_ARFrame_Create	创建一个新的AREngine_ARFrame对象，将指针存储到*outFrame中。
HMS_AREngine_ARSession_SetDisplayGeometry	设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。
HMS_AREngine_ARSession_SetCameraGLTexture	设置可用于存储相机预览流数据的openGL纹理。
HMS_AREngine_ARSession_GetAllTrackables	获取所有指定类型的可跟踪对象集合。
HMS_AREngine_ARTrackableList_AcquireItem	从可跟踪列表中获取指定index的对象。
HMS_AREngine_ARPlane_GetCenterPose	获取从平面的局部坐标系到世界坐标系转换的位姿信息。
HMS_AREngine_ARFrame_AcquireCamera	获取当前帧的相机参数对象。
HMS_AREngine_ARPose_Create	分配并初始化一个新的位姿对象。
HMS_AREngine_ARCamera_GetPose	获取当前相机对象在AR世界空间中的位姿。
HMS_AREngine_ARFrame_AcquireSceneMesh	获取当前帧的mesh信息。
HMS_AREngine_ARSceneMesh_AcquireVerticesSize	获取mesh的顶点个数。
HMS_AREngine_ARSceneMesh_AcquireVertexList	获取mesh顶点集合。
HMS_AREngine_ARSceneMesh_AcquireIndexListSize	获取mesh面片的索引个数。
HMS_AREngine_ARSceneMesh_AcquireIndexList	获取mesh面片的索引集合。
HMS_AREngine_ARSceneMesh_Release	释放当前帧的mesh信息。

开发步骤

[h2]声明Native接口

开发者可参考AR物体摆放章节的声明Native接口。

[h2]创建UI界面

创建一个UI界面，使用XComponent组件用于显示相机预览画面，并定时触发每一帧绘制。

// 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARMesh.ets。
import { deviceInfo } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARMeshBuilder() {
  ARMesh();
}

@Component
struct ARMesh {
  pageInfo: NavPathStack = new NavPathStack();
  private interval: number = -1;
  private xComponentId: string = 'ARMesh';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            console.info(`XComponent onLoad ${this.xComponentId}.`);
            this.interval = setInterval(() => {
              // 调用更新Native API来更新AR Engine每帧的计算结果
              arEngineDemo.update(this.xComponentId);
            }, 33) // 将帧速率设置为30fps（每33ms刷新一次帧）
          })
          .onDestroy(() => {
            console.info(`XComponent onDestroy ${this.xComponentId}.`);
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.xComponentId, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.xComponentId);
    })
    .onShown(() => {
      arEngineDemo.show(this.xComponentId);
    })
    .onHidden(() => {
      arEngineDemo.hide(this.xComponentId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}

[h2]引入AR Engine

开发者可参考AR物体摆放章节的引入AR Engine。

[h2]创建AR会话

创建AR会话并配置为开启mesh模式。

AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置mesh模式为开启状态。
HMS_AREngine_ARConfig_SetMeshMode(arSession, arConfig, ARENGINE_MESH_MODE_ENABLED);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);

[h2]获取当前环境中的mesh信息

调用HMS_AREngine_ARFrame_AcquireSceneMesh函数，获取当前环境中的mesh信息，并将结果存放在sceneMesh中。

AREngine_ARFrame *arFrame = nullptr;
// 创建AR单帧对象
HMS_AREngine_ARFrame_Create(arSession, &arFrame);
AREngine_ARSceneMesh *sceneMesh = nullptr;
// 获取当前帧的mesh信息
HMS_AREngine_ARFrame_AcquireSceneMesh(arSession, arFrame, &sceneMesh);

[h2]获取当前mesh信息对应的mesh顶点信息

调用HMS_AREngine_ARSceneMesh_AcquireVerticesSize函数，获取mesh顶点信息包含的浮点数数量，每三个浮点数组成一个mesh顶点，将结果存放在meshVerticesSize 中。

int32_t meshVerticesSize = 0;
// 获取mesh顶点信息包含的浮点数数量
HMS_AREngine_ARSceneMesh_AcquireVerticesSize(arSession, sceneMesh, &meshVerticesSize);

调用HMS_AREngine_ARSceneMesh_AcquireVertexList函数，获取mesh顶点信息，并将结果保存在meshVertices中。

float *meshVertices = new float[meshVerticesSize];
// 获取mesh顶点信息
HMS_AREngine_ARSceneMesh_AcquireVertexList(arSession, sceneMesh, meshVertices, meshVerticesSize);
// 获取mesh顶点个数
int32_t mPointsNum = meshVerticesSize / 3;

[h2]获取当前mesh信息对应的mesh面片信息

调用HMS_AREngine_ARSceneMesh_AcquireIndexListSize函数，获取mesh面片信息对应顶点的索引个数，每三个顶点索引表示一个mesh面片，将结果存放在triangleIndicesSize 中。

int32_t triangleIndicesSize = 0;
// 获取mesh面片信息对应顶点的索引个数
HMS_AREngine_ARSceneMesh_AcquireIndexListSize(arSession, sceneMesh, &triangleIndicesSize);

调用HMS_AREngine_ARSceneMesh_AcquireIndexList函数，获取mesh面片信息对应顶点的索引列表，并将结果保存在meshTriangleIndices中。

int32_t *meshTriangleIndices = new int32_t[triangleIndicesSize];
// 获取mesh面片信息对应顶点的索引列表
HMS_AREngine_ARSceneMesh_AcquireIndexList(arSession, sceneMesh, meshTriangleIndices, triangleIndicesSize);
// 获取mesh面片个数
int32_t mTrianglesNum = triangleIndicesSize / 3;

[h2]使用完毕后，销毁mesh信息

void HMS_AREngine_ARSceneMesh_Release(AREngine_ARSceneMesh *sceneMesh);

## Code blocks

### Code block 1

```
// 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARMesh.ets。
import { deviceInfo } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';

@Builder
export function ARMeshBuilder() {
  ARMesh();
}

@Component
struct ARMesh {
  pageInfo: NavPathStack = new NavPathStack();
  private interval: number = -1;
  private xComponentId: string = 'ARMesh';
  @State context: Context = this.getUIContext().getHostContext() as Context;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;

  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            console.info(`XComponent onLoad ${this.xComponentId}.`);
            this.interval = setInterval(() => {
              // 调用更新Native API来更新AR Engine每帧的计算结果
              arEngineDemo.update(this.xComponentId);
            }, 33) // 将帧速率设置为30fps（每33ms刷新一次帧）
          })
          .onDestroy(() => {
            console.info(`XComponent onDestroy ${this.xComponentId}.`);
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.xComponentId, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.xComponentId);
    })
    .onShown(() => {
      arEngineDemo.show(this.xComponentId);
    })
    .onHidden(() => {
      arEngineDemo.hide(this.xComponentId);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfo = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }
}
```

### Code block 2

```
AREngine_ARSession *arSession = nullptr;
// 创建AR会话。
HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
AREngine_ARConfig *arConfig = nullptr;
// 创建AR会话配置器。
HMS_AREngine_ARConfig_Create(arSession, &arConfig);
// 设置mesh模式为开启状态。
HMS_AREngine_ARConfig_SetMeshMode(arSession, arConfig, ARENGINE_MESH_MODE_ENABLED);
// 配置器设置给AR会话。
HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### Code block 3

```
AREngine_ARFrame *arFrame = nullptr;
// 创建AR单帧对象
HMS_AREngine_ARFrame_Create(arSession, &arFrame);
AREngine_ARSceneMesh *sceneMesh = nullptr;
// 获取当前帧的mesh信息
HMS_AREngine_ARFrame_AcquireSceneMesh(arSession, arFrame, &sceneMesh);
```

### Code block 4

```
int32_t meshVerticesSize = 0;
// 获取mesh顶点信息包含的浮点数数量
HMS_AREngine_ARSceneMesh_AcquireVerticesSize(arSession, sceneMesh, &meshVerticesSize);
```

### Code block 5

```
float *meshVertices = new float[meshVerticesSize];
// 获取mesh顶点信息
HMS_AREngine_ARSceneMesh_AcquireVertexList(arSession, sceneMesh, meshVertices, meshVerticesSize);
// 获取mesh顶点个数
int32_t mPointsNum = meshVerticesSize / 3;
```

### Code block 6

```
int32_t triangleIndicesSize = 0;
// 获取mesh面片信息对应顶点的索引个数
HMS_AREngine_ARSceneMesh_AcquireIndexListSize(arSession, sceneMesh, &triangleIndicesSize);
```

### Code block 7

```
int32_t *meshTriangleIndices = new int32_t[triangleIndicesSize];
// 获取mesh面片信息对应顶点的索引列表
HMS_AREngine_ARSceneMesh_AcquireIndexList(arSession, sceneMesh, meshTriangleIndices, triangleIndicesSize);
// 获取mesh面片个数
int32_t mTrianglesNum = triangleIndicesSize / 3;
```

### Code block 8

```
void HMS_AREngine_ARSceneMesh_Release(AREngine_ARSceneMesh *sceneMesh);
```
