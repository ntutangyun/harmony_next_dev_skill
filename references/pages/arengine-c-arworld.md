# 物体摆放（C/C++）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-arworld_

本章节给出了关键开发步骤，完整代码可以参考示例代码。

约束与限制

从5.0.0(12)开始，物体摆放能力支持部分Phone、部分Tablet设备。请参考硬件要求判断设备是否支持运动跟踪及平面识别特性（ARENGINE_FEATURE_TYPE_SLAM）。

接口说明

以下接口为AR物体摆放相关接口。详细接口和说明，请参考AR Engine API参考。

接口名	描述
HMS_AREngine_ARSession_Create	创建一个新的AREngine_ARSession会话。
HMS_AREngine_ARSession_Update	更新AR Engine的计算结果。
HMS_AREngine_ARSession_Configure	配置AREngine_ARSession会话。
HMS_AREngine_ARFrame_Create	创建一个新的AREngine_ARFrame对象，将指针存储到中*outFrame。
HMS_AREngine_ARSession_SetDisplayGeometry	设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。
HMS_AREngine_ARSession_SetCameraGLTexture	设置可用于存储相机预览流数据的openGL纹理。
HMS_AREngine_ARSession_GetAllTrackables	获取所有指定类型的可跟踪对象集合。
HMS_AREngine_ARTrackableList_AcquireItem	从可跟踪列表中获取指定index的对象。
HMS_AREngine_ARPlane_GetCenterPose	获取从平面的局部坐标系到世界坐标系转换的位姿信息。
HMS_AREngine_ARFrame_HitTest	根据屏幕上兴趣点位置获取命中检测结果。
HMS_AREngine_ARHitResultList_GetSize	获取命中检测结果对象列表中包含的对象数。
HMS_AREngine_ARHitResultList_GetItem	在命中检测结果列表中获取指定索引的命中检测结果对象。
HMS_AREngine_ARHitResult_Create	创建一个空的命中检测结果对象。
HMS_AREngine_ARHitResult_AcquireNewAnchor	在碰撞命中位置创建一个新的锚点。
HMS_AREngine_ARHitResult_AcquireTrackable	获取被命中的可追踪对象。
HMS_AREngine_ARFrame_AcquireCamera	获取当前帧的相机参数对象。
HMS_AREngine_ARPose_Create	分配并初始化一个新的位姿对象。
HMS_AREngine_ARCamera_GetPose	获取当前相机对象在AR世界空间中的位姿。

开发步骤

[h2]声明Native接口

ArkTS接口声明。

import { resourceManager } from '@kit.LocalizationKit';
// ...
export const start: (id: string, params: Int32Array) => void;
export const show: (id: string) => void;
export const hide: (id: string) => void;
export const update: (id: string) => number;
export const stop: (id: string) => void;
export const init: (resmgr: resourceManager.ResourceManager) => void;
export const getDistance: (id: string) => string;
export const initImage: (id: string, width: number, height: number, buffer: ArrayBuffer) => number;
export const setPath: (id: string, path: string) => void;
export const saveImageDataBaseToLocal: (id: string, path: string) => void;
export const getImageCount: (id: string) => number;
export const getVolume: (id: string) => string;
export const getLandmark: (id: string) => Landmark[];
export const getBoneLine: (id: string) => SkeletonConnectionAndType;

建立ArkTS接口与C++接口之间的映射。

napi_property_descriptor desc[] = {
    {"init", nullptr, Global::Init, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"start", nullptr, NapiManager::NapiOnPageAppear, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"show", nullptr, NapiManager::NapiOnPageShow, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"hide", nullptr, NapiManager::NapiOnPageHide, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"update", nullptr, NapiManager::NapiOnPageUpdate, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"stop", nullptr, NapiManager::NapiOnPageDisappear, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getDistance", nullptr, NapiManager::NapiGetDistance, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"initImage", nullptr, NapiManager::NapiInitImage, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"setPath", nullptr, NapiManager::NapiSetPath, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"saveImageDataBaseToLocal", nullptr, NapiManager::NapiSaveImageDataBaseToLocal, nullptr, nullptr, nullptr,
     napi_default, nullptr},
    {"getImageCount", nullptr, NapiManager::NapiGetImageCount, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getVolume", nullptr, NapiManager::NapiGetVolume, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getLandmark", nullptr, NapiManager::NapiGetBodyPoint2D, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getBoneLine", nullptr, NapiManager::NapiGetSkeletonConnections, nullptr, nullptr, nullptr, napi_default,
     nullptr}};

[h2]创建UI界面

创建一个UI界面，使用XComponent组件用于显示相机预览画面，并定时触发每一帧绘制。

import { display, PromptAction } from '@kit.ArkUI';
import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARWorldBuilder() {
  ARWorld();
}

@Component
struct ARWorld {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State numberOfPlans: number = 0;
  @State rotation: number = 0;
  private currentMillisecond: number = 0;
  private interval: number = -1;
  private isUpdate: boolean = true;
  private xComponentId: string = 'ARWorld';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                // Call the update Native API to update the calculation result of each frame by AR Engine.
                this.numberOfPlans = arEngineDemo.update(this.idStr);
                this.planeNum();
              }
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.idStr);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private messageNotification(): void {
    let promptAction: PromptAction = this.getUIContext().getPromptAction();
    try {
      promptAction.showToast({
        message: $r('app.string.alert_desc'),
        bottom: 300
      })
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`promptAction Failed. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private planeNum(): void {
    if (this.numberOfPlans < 1) {
      // The number of planes is less than 1.
      let tempMillisecond: number = new Date().getTime();
      // Assign a value to the time when the feature is started for the first time.
      if (this.currentMillisecond === 0) {
        this.currentMillisecond = tempMillisecond;
        return;
      }
      // Display a pop-up window if the plane fails to be recognized within 10 seconds.
      if (tempMillisecond - this.currentMillisecond > 10000) {
        this.messageNotification();
        this.currentMillisecond = 0;
      }
    } else {
      this.currentMillisecond = 0;
    }
  }
}

[h2]引入AR Engine

开发者可参考管理AR会话章节的引入AR Engine。

[h2]创建AR场景

调用HMS_AREngine_ARSession_Create函数创建AREngine_ARSession会话。您可以参考管理AR会话创建ARSession。

配置AR会话及预览尺寸。

AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
HMS_AREngine_ARConfig_Destroy(arConfig);
// Create an AREngine_ARFrame object.
CHECK(HMS_AREngine_ARFrame_Create(mArSession, &mArFrame));
NativeDisplayManager_Rotation displayRotation;
if (OH_NativeDisplayManager_GetDefaultDisplayRotation(&displayRotation) == DISPLAY_MANAGER_OK) {
    mDisplayRotation = ArEngineRotateType(displayRotation);
}
// ...
CHECK(HMS_AREngine_ARSession_SetDisplayGeometry(mArSession, mDisplayRotation, mWidth, mHeight));
// Set the display height and width (in pixels). Make sure that the height and width you set here are consistent
// with those of the display view.

通过OpenGL接口获取纹理ID。

glGenTextures(1, &textureId);

设置OpenGL纹理，存储相机预览流数据。

HMS_AREngine_ARSession_SetCameraGLTexture(mArSession, mWorldRenderManager.GetPreviewTextureId());

[h2]获取平面

调用HMS_AREngine_ARSession_Update函数更新当前AREngine_ARFrame对象。

HMS_AREngine_ARSession_Update(mArSession, mArFrame);

获取相机的视图矩阵和相机的投影矩阵，用于后续渲染。

// Obtain the camera parameters of the current frame.
AREngine_ARCamera *arCamera = nullptr;
CHECK(HMS_AREngine_ARFrame_AcquireCamera(arSession, arFrame, &arCamera));
// Obtain the view matrix of the camera in the latest frame.
CHECK(HMS_AREngine_ARCamera_GetViewMatrix(arSession, arCamera, viewMat->data(), 16));
// Obtain the projection matrix used for rendering virtual content on top of the camera image. This matrix can be
// used for converting from the camera coordinate system to the clip coordinate system. Near (0.1) Far (100).
CHECK(HMS_AREngine_ARCamera_GetProjectionMatrix(arSession, arCamera, {0.1f, 100.f}, projectionMat->data(), 16));

说明

这里直接获取相机的视图矩阵和相机的投影矩阵，是为了便于渲染。获取相机运动中的位姿变化，还可以调用HMS_AREngine_ARCamera_GetPose函数配合HMS_AREngine_ARPose_GetPoseRaw函数进行获取。详细可参考获取设备当前位姿。

调用HMS_AREngine_ARSession_GetAllTrackables函数获取平面列表。详细可参考检测环境中的平面章节。

// Update and render the plane.
AREngine_ARTrackableList *planeList = nullptr;
// Create a list of trackable objects.
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &planeList));
// Obtain the list of all trackable objects of the specified type.
AREngine_ARTrackableType planeTrackedType = ARENGINE_TRACKABLE_PLANE;
CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList));
int32_t planeListSize = 0;
// Obtain the number of trackable objects in the list.
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize));
mPlaneCount = planeListSize;

for (int i = 0; i < planeListSize; ++i) {
    AREngine_ARTrackable *arTrackable = nullptr;
    // Obtain the object at a specified index from the trackable object list.
    CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable));
    AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane *>(arTrackable);
    // Obtain the tracking status of the current trackable object. Plane drawing is performed only when the tracking
    // status is ARENGINE_TRACKING_STATE_TRACKING (trackable).
    AREngine_ARTrackingState outTrackingState;
    CHECK(HMS_AREngine_ARTrackable_GetTrackingState(arSession, arTrackable, &outTrackingState));
    AREngine_ARPlane *subsumePlane = nullptr;
    // Obtain a plane's parent plane (generated when the plane is merged with another one). If there is no parent
    // plane, NULL is returned.
    CHECK(HMS_AREngine_ARPlane_AcquireSubsumedBy(arSession, arPlane, &subsumePlane));
    if (subsumePlane != nullptr) {
        HMS_AREngine_ARTrackable_Release(reinterpret_cast<AREngine_ARTrackable *>(subsumePlane));
        continue;
    }
    if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
        continue;
    }
    // ...
}
HMS_AREngine_ARTrackableList_Destroy(planeList);
planeList = nullptr;

调用HMS_AREngine_ARPlane_GetPolygon函数获取平面的二维顶点坐标数组，用于绘制平面边界。

int32_t polygonLength = 0;
// Obtain the size of the 2D vertex array of the detected plane.
CHECK(HMS_AREngine_ARPlane_GetPolygonSize(session, plane, &polygonLength));

if (polygonLength == 0) {
    LOGE("WorldPlaneRenderer::UpdateForPlane, no valid plane polygon is found.");
    return;
}
const int32_t verticesSize = polygonLength / 2;
std::vector<Eigen::Vector2f> raw_vertices(verticesSize);
// Obtain the 2D vertex array of the detected plane, in the format of [x1, z1, x2, z2, ...].
CHECK(HMS_AREngine_ARPlane_GetPolygon(session, plane, raw_vertices.front().data(), polygonLength));
// Fill in vertices 0 to 3. Use the vertex.
// xy coordinates for the x and z coordinates of the vertex.
// The z coordinate of the vertex is used for alpha.
// The alpha value of the outer polygon is 0.
for (int32_t i = 0; i < verticesSize; ++i) {
    vertices.emplace_back(raw_vertices[i].x(), raw_vertices[i].y(), 0.75f);
}

说明

调用HMS_AREngine_ARPlane_GetPolygon函数获取平面的二维顶点坐标数组格式为[x1，z1，x2，z2，...]。这些值均在平面局部坐标系的x-z平面中定义，须先调用HMS_AREngine_ARPlane_GetCenterPose函数获取从平面的局部坐标系到世界坐标系转换的位姿数据，然后调用HMS_AREngine_ARPose_GetMatrix函数将位姿数据转换成4X4的矩阵，该矩阵与局部坐标系的坐标点做乘法，可以得到局部坐标系到世界坐标系的转换。

将平面的二维顶点坐标转换到世界坐标系，并绘制平面。

AREngine_ARPose *scopedArPose = nullptr;
// Obtain the pose information for the conversion from the local coordinate system of a plane to the world
// coordinate system.
CHECK(HMS_AREngine_ARPose_Create(session, nullptr, 0, &scopedArPose));
CHECK(HMS_AREngine_ARPlane_GetCenterPose(session, plane, scopedArPose));
// Convert the pose data into a 4 x 4 matrix. outMatrixColMajor4x4 is the array for storing the matrix, where data
// is stored in column-major order. Coordinates in the local coordinate system can be converted into ones in the
// world coordinate system by multiplying this matrix with the coordinates in the local coordinate system.
CHECK(HMS_AREngine_ARPose_GetMatrix(session, scopedArPose, modelMat.data(), 16));
HMS_AREngine_ARPose_Destroy(scopedArPose);

// Generate a triangle.
for (int i = 1; i < verticesSize - 1; ++i) {
    triangles.push_back(0);
    triangles.push_back(i);
    triangles.push_back(i + 1);
}
// Generate the plane boundary.
for (int i = 0; i < verticesSize; ++i) {
    lines.push_back(i);
}

[h2]点击屏幕

用户点击屏幕后，基于点击事件获取屏幕坐标。可参考Native XComponent。

添加头文件：native_interface_xcomponent.h。

#include <ace/xcomponent/native_interface_xcomponent.h>

通过点击事件获取屏幕点击坐标。

float pixeLX = 0.0f;
float pixeLY = 0.0f;
int32_t ret = OH_NativeXComponent_GetTouchEvent(component, window, &mTouchEvent);
if (ret == OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
    if (mTouchEvent.type == OH_NATIVEXCOMPONENT_DOWN) {
        pixeLX = mTouchEvent.touchPoints[0].x;
        pixeLY = mTouchEvent.touchPoints[0].y;
        LOGD("Pos: %{public}f %{public}f.", pixeLX, pixeLY);
    } else {
        return;
    }
} else {
    LOGE("Touch fail");
    return;
}

调用HMS_AREngine_ARFrame_HitTest函数进行碰撞检测，结果存放在碰撞检测结果列表中。

AREngine_ARHitResultList *hitResultList = nullptr;
CHECK(HMS_AREngine_ARHitResultList_Create(mArSession, &hitResultList));
CHECK(HMS_AREngine_ARFrame_HitTest(mArSession, mArFrame, pixeLX, pixeLY, hitResultList));

说明

碰撞结果按照交点与设备的距离从近到远进行排序，存放在碰撞结果列表中。

[h2]放置虚拟物体

调用HMS_AREngine_ARHitResultList_GetItem函数遍历碰撞检测结果列表，获取命中的可跟踪对象。

AREngine_ARHitResult *arHit = nullptr;
CHECK(HMS_AREngine_ARHitResult_Create(mArSession, &arHit));
CHECK(HMS_AREngine_ARHitResultList_GetItem(mArSession, hitResultList, i, arHit));
if (arHit == nullptr) {
    return false;
}
AREngine_ARTrackable *arTrackable = nullptr;
CHECK(HMS_AREngine_ARHitResult_AcquireTrackable(mArSession, arHit, &arTrackable));

判断碰撞结果是否存在于平面内部。

AREngine_ARTrackableType ar_trackable_type = ARENGINE_TRACKABLE_INVALID;
CHECK(HMS_AREngine_ARTrackable_GetType(mArSession, arTrackable, &ar_trackable_type));

// If a plane or directional point is encountered, an anchor point is created.
if (ARENGINE_TRACKABLE_PLANE == ar_trackable_type) {
    AREngine_ARPose *arPose = nullptr;
    CHECK(HMS_AREngine_ARPose_Create(mArSession, nullptr, 0, &arPose));
    CHECK(HMS_AREngine_ARHitResult_GetHitPose(mArSession, arHit, arPose));
    int32_t inPolygon = 0;
    AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane *>(arTrackable);
    // Check whether the pose is within the plane's bounding polygon. Value 0 indicates that it is out of the
    // range, and other values indicate that it is within the range.
    CHECK(HMS_AREngine_ARPlane_IsPoseInPolygon(mArSession, arPlane, arPose, &inPolygon));
    HMS_AREngine_ARPose_Destroy(arPose);
    if (!inPolygon) {
        continue;
    }
    // ...

在碰撞结果位置创建一个新的锚点，并基于此锚点放置虚拟模型。

AREngine_ARAnchor *anchor = nullptr;
CHECK(HMS_AREngine_ARHitResult_AcquireNewAnchor(mArSession, arHitResult, &anchor));

AREngine_ARTrackingState trackingState = ARENGINE_TRACKING_STATE_STOPPED;
CHECK(HMS_AREngine_ARAnchor_GetTrackingState(mArSession, anchor, &trackingState));
if (trackingState != ARENGINE_TRACKING_STATE_TRACKING) {
    HMS_AREngine_ARAnchor_Release(anchor);
    return;
}

绘制模型。

调用HMS_AREngine_ARAnchor_GetPose函数获取锚点位姿，并基于该位姿绘制虚拟模型。

AREngine_ARPose *pose = nullptr;
CHECK(HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &pose));
CHECK(HMS_AREngine_ARAnchor_GetPose(arSession, coloredAnchor.anchor, pose));
CHECK(HMS_AREngine_ARPose_GetMatrix(arSession, pose, modelMat.data(), 16));
HMS_AREngine_ARPose_Destroy(pose);

## Code blocks

### Code block 1

```
import { resourceManager } from '@kit.LocalizationKit';
// ...
export const start: (id: string, params: Int32Array) => void;
export const show: (id: string) => void;
export const hide: (id: string) => void;
export const update: (id: string) => number;
export const stop: (id: string) => void;
export const init: (resmgr: resourceManager.ResourceManager) => void;
export const getDistance: (id: string) => string;
export const initImage: (id: string, width: number, height: number, buffer: ArrayBuffer) => number;
export const setPath: (id: string, path: string) => void;
export const saveImageDataBaseToLocal: (id: string, path: string) => void;
export const getImageCount: (id: string) => number;
export const getVolume: (id: string) => string;
export const getLandmark: (id: string) => Landmark[];
export const getBoneLine: (id: string) => SkeletonConnectionAndType;
```

### Code block 2

```
napi_property_descriptor desc[] = {
    {"init", nullptr, Global::Init, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"start", nullptr, NapiManager::NapiOnPageAppear, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"show", nullptr, NapiManager::NapiOnPageShow, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"hide", nullptr, NapiManager::NapiOnPageHide, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"update", nullptr, NapiManager::NapiOnPageUpdate, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"stop", nullptr, NapiManager::NapiOnPageDisappear, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getDistance", nullptr, NapiManager::NapiGetDistance, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"initImage", nullptr, NapiManager::NapiInitImage, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"setPath", nullptr, NapiManager::NapiSetPath, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"saveImageDataBaseToLocal", nullptr, NapiManager::NapiSaveImageDataBaseToLocal, nullptr, nullptr, nullptr,
     napi_default, nullptr},
    {"getImageCount", nullptr, NapiManager::NapiGetImageCount, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getVolume", nullptr, NapiManager::NapiGetVolume, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getLandmark", nullptr, NapiManager::NapiGetBodyPoint2D, nullptr, nullptr, nullptr, napi_default, nullptr},
    {"getBoneLine", nullptr, NapiManager::NapiGetSkeletonConnections, nullptr, nullptr, nullptr, napi_default,
     nullptr}};
```

### Code block 3

```
import { display, PromptAction } from '@kit.ArkUI';
import { BusinessError, systemDateTime } from '@kit.BasicServicesKit';
import { resourceManager } from '@kit.LocalizationKit';
import arEngineDemo from 'libentry.so';
import { logger } from '../utils/Logger';

@Builder
export function ARWorldBuilder() {
  ARWorld();
}

@Component
struct ARWorld {
  pageInfos: NavPathStack = new NavPathStack();
  @State context: Context = this.getUIContext().getHostContext() as Context;
  @State numberOfPlans: number = 0;
  @State rotation: number = 0;
  private currentMillisecond: number = 0;
  private interval: number = -1;
  private isUpdate: boolean = true;
  private xComponentId: string = 'ARWorld';
  private idStr: string = systemDateTime.getTime(false).toString() + this.xComponentId;
  private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
  // ...
  build(): void {
    NavDestination() {
      RelativeContainer() {
        XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'entry' })
          .width('100%')
          .height('100%')
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onLoad(() => {
            this.interval = setInterval(() => {
              if (this.isUpdate) {
                // Call the update Native API to update the calculation result of each frame by AR Engine.
                this.numberOfPlans = arEngineDemo.update(this.idStr);
                this.planeNum();
              }
            }, 33) // Set the frame rate to 30 fps (with the frame refreshed every 33 ms).
          })
          .onDestroy(() => {
            clearInterval(this.interval);
          })
      }
    }
    .onAppear(() => {
      arEngineDemo.init(this.resMgr);
      let config: Int32Array = new Int32Array([1, this.rotation]);
      arEngineDemo.start(this.idStr, config);
    })
    .onWillDisappear(() => {
      arEngineDemo.stop(this.idStr);
    })
    .onShown(() => {
      this.isUpdate = true;
      arEngineDemo.show(this.idStr);
    })
    .onHidden(() => {
      this.isUpdate = false;
      arEngineDemo.hide(this.idStr);
    })
    .onReady((context: NavDestinationContext) => {
      this.pageInfos = context.pathStack;
    })
    .hideTitleBar(true)
    .hideBackButton(true)
    .hideToolBar(true)
  }

  private messageNotification(): void {
    let promptAction: PromptAction = this.getUIContext().getPromptAction();
    try {
      promptAction.showToast({
        message: $r('app.string.alert_desc'),
        bottom: 300
      })
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      logger.error(`promptAction Failed. Code is ${err.code}, message is ${err.message}`);
    }
  }

  private planeNum(): void {
    if (this.numberOfPlans < 1) {
      // The number of planes is less than 1.
      let tempMillisecond: number = new Date().getTime();
      // Assign a value to the time when the feature is started for the first time.
      if (this.currentMillisecond === 0) {
        this.currentMillisecond = tempMillisecond;
        return;
      }
      // Display a pop-up window if the plane fails to be recognized within 10 seconds.
      if (tempMillisecond - this.currentMillisecond > 10000) {
        this.messageNotification();
        this.currentMillisecond = 0;
      }
    } else {
      this.currentMillisecond = 0;
    }
  }
}
```

### Code block 4

```
AREngine_ARConfig *arConfig = nullptr;
CHECK(HMS_AREngine_ARConfig_Create(mArSession, &arConfig));
// ...
CHECK(HMS_AREngine_ARSession_Configure(mArSession, arConfig));
HMS_AREngine_ARConfig_Destroy(arConfig);
// Create an AREngine_ARFrame object.
CHECK(HMS_AREngine_ARFrame_Create(mArSession, &mArFrame));
NativeDisplayManager_Rotation displayRotation;
if (OH_NativeDisplayManager_GetDefaultDisplayRotation(&displayRotation) == DISPLAY_MANAGER_OK) {
    mDisplayRotation = ArEngineRotateType(displayRotation);
}
// ...
CHECK(HMS_AREngine_ARSession_SetDisplayGeometry(mArSession, mDisplayRotation, mWidth, mHeight));
// Set the display height and width (in pixels). Make sure that the height and width you set here are consistent
// with those of the display view.
```

### Code block 5

```
glGenTextures(1, &textureId);
```

### Code block 6

```
HMS_AREngine_ARSession_SetCameraGLTexture(mArSession, mWorldRenderManager.GetPreviewTextureId());
```

### Code block 7

```
HMS_AREngine_ARSession_Update(mArSession, mArFrame);
```

### Code block 8

```
// Obtain the camera parameters of the current frame.
AREngine_ARCamera *arCamera = nullptr;
CHECK(HMS_AREngine_ARFrame_AcquireCamera(arSession, arFrame, &arCamera));
// Obtain the view matrix of the camera in the latest frame.
CHECK(HMS_AREngine_ARCamera_GetViewMatrix(arSession, arCamera, viewMat->data(), 16));
// Obtain the projection matrix used for rendering virtual content on top of the camera image. This matrix can be
// used for converting from the camera coordinate system to the clip coordinate system. Near (0.1) Far (100).
CHECK(HMS_AREngine_ARCamera_GetProjectionMatrix(arSession, arCamera, {0.1f, 100.f}, projectionMat->data(), 16));
```

### Code block 9

```
// Update and render the plane.
AREngine_ARTrackableList *planeList = nullptr;
// Create a list of trackable objects.
CHECK(HMS_AREngine_ARTrackableList_Create(arSession, &planeList));
// Obtain the list of all trackable objects of the specified type.
AREngine_ARTrackableType planeTrackedType = ARENGINE_TRACKABLE_PLANE;
CHECK(HMS_AREngine_ARSession_GetAllTrackables(arSession, planeTrackedType, planeList));
int32_t planeListSize = 0;
// Obtain the number of trackable objects in the list.
CHECK(HMS_AREngine_ARTrackableList_GetSize(arSession, planeList, &planeListSize));
mPlaneCount = planeListSize;

for (int i = 0; i < planeListSize; ++i) {
    AREngine_ARTrackable *arTrackable = nullptr;
    // Obtain the object at a specified index from the trackable object list.
    CHECK(HMS_AREngine_ARTrackableList_AcquireItem(arSession, planeList, i, &arTrackable));
    AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane *>(arTrackable);
    // Obtain the tracking status of the current trackable object. Plane drawing is performed only when the tracking
    // status is ARENGINE_TRACKING_STATE_TRACKING (trackable).
    AREngine_ARTrackingState outTrackingState;
    CHECK(HMS_AREngine_ARTrackable_GetTrackingState(arSession, arTrackable, &outTrackingState));
    AREngine_ARPlane *subsumePlane = nullptr;
    // Obtain a plane's parent plane (generated when the plane is merged with another one). If there is no parent
    // plane, NULL is returned.
    CHECK(HMS_AREngine_ARPlane_AcquireSubsumedBy(arSession, arPlane, &subsumePlane));
    if (subsumePlane != nullptr) {
        HMS_AREngine_ARTrackable_Release(reinterpret_cast<AREngine_ARTrackable *>(subsumePlane));
        continue;
    }
    if (AREngine_ARTrackingState::ARENGINE_TRACKING_STATE_TRACKING != outTrackingState) {
        continue;
    }
    // ...
}
HMS_AREngine_ARTrackableList_Destroy(planeList);
planeList = nullptr;
```

### Code block 10

```
int32_t polygonLength = 0;
// Obtain the size of the 2D vertex array of the detected plane.
CHECK(HMS_AREngine_ARPlane_GetPolygonSize(session, plane, &polygonLength));

if (polygonLength == 0) {
    LOGE("WorldPlaneRenderer::UpdateForPlane, no valid plane polygon is found.");
    return;
}
const int32_t verticesSize = polygonLength / 2;
std::vector<Eigen::Vector2f> raw_vertices(verticesSize);
// Obtain the 2D vertex array of the detected plane, in the format of [x1, z1, x2, z2, ...].
CHECK(HMS_AREngine_ARPlane_GetPolygon(session, plane, raw_vertices.front().data(), polygonLength));
// Fill in vertices 0 to 3. Use the vertex.
// xy coordinates for the x and z coordinates of the vertex.
// The z coordinate of the vertex is used for alpha.
// The alpha value of the outer polygon is 0.
for (int32_t i = 0; i < verticesSize; ++i) {
    vertices.emplace_back(raw_vertices[i].x(), raw_vertices[i].y(), 0.75f);
}
```

### Code block 11

```
AREngine_ARPose *scopedArPose = nullptr;
// Obtain the pose information for the conversion from the local coordinate system of a plane to the world
// coordinate system.
CHECK(HMS_AREngine_ARPose_Create(session, nullptr, 0, &scopedArPose));
CHECK(HMS_AREngine_ARPlane_GetCenterPose(session, plane, scopedArPose));
// Convert the pose data into a 4 x 4 matrix. outMatrixColMajor4x4 is the array for storing the matrix, where data
// is stored in column-major order. Coordinates in the local coordinate system can be converted into ones in the
// world coordinate system by multiplying this matrix with the coordinates in the local coordinate system.
CHECK(HMS_AREngine_ARPose_GetMatrix(session, scopedArPose, modelMat.data(), 16));
HMS_AREngine_ARPose_Destroy(scopedArPose);

// Generate a triangle.
for (int i = 1; i < verticesSize - 1; ++i) {
    triangles.push_back(0);
    triangles.push_back(i);
    triangles.push_back(i + 1);
}
// Generate the plane boundary.
for (int i = 0; i < verticesSize; ++i) {
    lines.push_back(i);
}
```

### Code block 12

```
#include <ace/xcomponent/native_interface_xcomponent.h>
```

### Code block 13

```
float pixeLX = 0.0f;
float pixeLY = 0.0f;
int32_t ret = OH_NativeXComponent_GetTouchEvent(component, window, &mTouchEvent);
if (ret == OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
    if (mTouchEvent.type == OH_NATIVEXCOMPONENT_DOWN) {
        pixeLX = mTouchEvent.touchPoints[0].x;
        pixeLY = mTouchEvent.touchPoints[0].y;
        LOGD("Pos: %{public}f %{public}f.", pixeLX, pixeLY);
    } else {
        return;
    }
} else {
    LOGE("Touch fail");
    return;
}
```

### Code block 14

```
AREngine_ARHitResultList *hitResultList = nullptr;
CHECK(HMS_AREngine_ARHitResultList_Create(mArSession, &hitResultList));
CHECK(HMS_AREngine_ARFrame_HitTest(mArSession, mArFrame, pixeLX, pixeLY, hitResultList));
```

### Code block 15

```
AREngine_ARHitResult *arHit = nullptr;
CHECK(HMS_AREngine_ARHitResult_Create(mArSession, &arHit));
CHECK(HMS_AREngine_ARHitResultList_GetItem(mArSession, hitResultList, i, arHit));
if (arHit == nullptr) {
    return false;
}
AREngine_ARTrackable *arTrackable = nullptr;
CHECK(HMS_AREngine_ARHitResult_AcquireTrackable(mArSession, arHit, &arTrackable));
```

### Code block 16

```
AREngine_ARTrackableType ar_trackable_type = ARENGINE_TRACKABLE_INVALID;
CHECK(HMS_AREngine_ARTrackable_GetType(mArSession, arTrackable, &ar_trackable_type));

// If a plane or directional point is encountered, an anchor point is created.
if (ARENGINE_TRACKABLE_PLANE == ar_trackable_type) {
    AREngine_ARPose *arPose = nullptr;
    CHECK(HMS_AREngine_ARPose_Create(mArSession, nullptr, 0, &arPose));
    CHECK(HMS_AREngine_ARHitResult_GetHitPose(mArSession, arHit, arPose));
    int32_t inPolygon = 0;
    AREngine_ARPlane *arPlane = reinterpret_cast<AREngine_ARPlane *>(arTrackable);
    // Check whether the pose is within the plane's bounding polygon. Value 0 indicates that it is out of the
    // range, and other values indicate that it is within the range.
    CHECK(HMS_AREngine_ARPlane_IsPoseInPolygon(mArSession, arPlane, arPose, &inPolygon));
    HMS_AREngine_ARPose_Destroy(arPose);
    if (!inPolygon) {
        continue;
    }
    // ...
```

### Code block 17

```
AREngine_ARAnchor *anchor = nullptr;
CHECK(HMS_AREngine_ARHitResult_AcquireNewAnchor(mArSession, arHitResult, &anchor));

AREngine_ARTrackingState trackingState = ARENGINE_TRACKING_STATE_STOPPED;
CHECK(HMS_AREngine_ARAnchor_GetTrackingState(mArSession, anchor, &trackingState));
if (trackingState != ARENGINE_TRACKING_STATE_TRACKING) {
    HMS_AREngine_ARAnchor_Release(anchor);
    return;
}
```

### Code block 18

```
AREngine_ARPose *pose = nullptr;
CHECK(HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &pose));
CHECK(HMS_AREngine_ARAnchor_GetPose(arSession, coloredAnchor.anchor, pose));
CHECK(HMS_AREngine_ARPose_GetMatrix(arSession, pose, modelMat.data(), 16));
HMS_AREngine_ARPose_Destroy(pose);
```
