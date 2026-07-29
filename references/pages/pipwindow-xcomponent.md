# 使用XComponent实现画中画功能开发（ArkTS）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-xcomponent_

本文以视频播放为例，介绍通过XComponent实现画中画功能的基本开发步骤。

约束与限制

HarmonyOS 6.0.0之前，支持在Phone、Tablet设备使用XComponent实现画中画功能开发；从HarmonyOS 6.0.0开始，支持在Phone、PC/2in1、Tablet设备使用XComponent实现画中画功能开发。

仅支持以XComponent作为媒体流播放组件的界面进入画中画模式，XComponent的type必须为XComponentType.SURFACE。

UIAbility使用Navigation管理页面时，需要设置Navigation控件的id属性，并将该id传递给画中画控制器，确保还原时可以正常恢复原页面。

如果应用主窗口不在前台，不建议在画中画回调方法中执行UI操作，例如页面push/pop等，这些操作不会立即执行，可能产生预期之外的结果。

在关闭画中画时，需要检查自定义组件节点是否释放，避免出现内存泄漏。

开发步骤

创建画中画控制器，注册生命周期事件以及控制事件回调。

通过在PiPConfiguration中新增PiPControlGroup类型的数组配置当前画中画控制层控件。

function getControlGroups(templateType: PiPWindow.PiPTemplateType): PiPControlGroups {
  switch (templateType) {
    case PiPWindow.PiPTemplateType.VIDEO_PLAY:
      return [PiPWindow.VideoPlayControlGroup.VIDEO_PREVIOUS_NEXT];
    case PiPWindow.PiPTemplateType.VIDEO_CALL:
      return [PiPWindow.VideoCallControlGroup.MICROPHONE_SWITCH,
        PiPWindow.VideoCallControlGroup.HANG_UP_BUTTON, PiPWindow.VideoCallControlGroup.CAMERA_SWITCH];
    case PiPWindow.PiPTemplateType.VIDEO_MEETING:
      return [PiPWindow.VideoMeetingControlGroup.MICROPHONE_SWITCH,
        PiPWindow.VideoMeetingControlGroup.HANG_UP_BUTTON, PiPWindow.VideoMeetingControlGroup.CAMERA_SWITCH];
    case PiPWindow.PiPTemplateType.VIDEO_LIVE:
      return [PiPWindow.VideoLiveControlGroup.VIDEO_PLAY_PAUSE,
        PiPWindow.VideoLiveControlGroup.MUTE_SWITCH];
    default:
      return [];
  }
}

// ...

@Component
export struct Page1 {
  // ...
  @State currentTemplateType: PiPWindow.PiPTemplateType = PiPWindow.PiPTemplateType.VIDEO_PLAY;
  // ...
  startPip() {
    // ...
    let config: PiPWindow.PiPConfiguration = {
      context: this.getUIContext().getHostContext() as Context,
      componentController: this.mXComponentController,
      // 当前page导航id
      // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
      // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
      // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
      navigationId: this.navId,
      // 对于视频通话、视频会议等场景，需要设置相应的模板类型
      templateType: this.currentTemplateType,
      // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
      contentWidth: 1920,
      // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
      contentHeight: 1080,
      // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
      controlGroups: getControlGroups(this.currentTemplateType),
      // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
      customUIController: this.nodeController,
    };
    // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
    PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
      // ...
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
    });
  }

  // ...
}

通过在PiPConfiguration中传入customUIController来显示自定义UI。

// 开发者可通过继承NodeController实现自定义UI控制器
class TextNodeController extends NodeController {
  private message: string;
  private textNode: BuilderNode<[Params]> | null = null;

  constructor(message: string) {
    super();
    this.message = message;
  }

  // 通过BuilderNode加载自定义布局
  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
    return this.textNode.getFrameNode();
  }

  // 开发者可自定义该方法实现布局更新
  update(message: string) {
    Logger.info(`update message: ${message}`);
    if (this.textNode !== null) {
      this.textNode.update(new Params(message));
    }
  }

  // 开发者需要定义该方法实现布局的注销，避免内存泄漏
  dispose() {
    Logger.info('dispose message: execute node dispose');
    if (this.textNode !== null) {
      this.textNode.dispose();
    }
  }
}

class Params {
  public text: string = '';

  constructor(text: string) {
    this.text = text;
  }
}

// 开发者可以通过@Builder装饰器实现布局构建
@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(20)
      .fontColor(Color.Red)
  }
  .width('100%') // 宽度方向充满画中画窗口
  .height('100%') // 高度方向充满画中画窗口
}

@Component
export struct Page1 {
  // ...
  private nodeController: TextNodeController = new TextNodeController('this is custom UI');
  // ...
  startPip() {
    if (!PiPWindow.isPiPEnabled()) {
      Logger.error(`picture in picture disabled for current OS`);
      return;
    }
    let config: PiPWindow.PiPConfiguration = {
      context: this.getUIContext().getHostContext() as Context,
      componentController: this.mXComponentController,
      // 当前page导航id
      // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
      // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
      // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
      navigationId: this.navId,
      // 对于视频通话、视频会议等场景，需要设置相应的模板类型
      templateType: this.currentTemplateType,
      // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
      contentWidth: 1920,
      // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
      contentHeight: 1080,
      // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
      controlGroups: getControlGroups(this.currentTemplateType),
      // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
      customUIController: this.nodeController,
    };
    // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
    PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
      // ...
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
    });
  }

  // ...
}

通过create(config: PiPConfiguration)接口创建画中画控制器实例。

创建画中画控制器实例后，注册生命周期事件以及控制事件回调。

通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调。

this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
  this.onStateChange(state, reason);
});

通过画中画控制器实例的on('controlPanelActionEvent')接口注册控制事件回调。

this.pipController.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
  this.onActionEvent(event, status);
});

启动画中画。

创建画中画控制器实例后，通过startPiP接口启动画中画。

startPip() {
  if (!PiPWindow.isPiPEnabled()) {
    Logger.error(`picture in picture disabled for current OS`);
    return;
  }
  let config: PiPWindow.PiPConfiguration = {
    context: this.getUIContext().getHostContext() as Context,
    componentController: this.mXComponentController,
    // 当前page导航id
    // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
    // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
    // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
    navigationId: this.navId,
    // 对于视频通话、视频会议等场景，需要设置相应的模板类型
    templateType: this.currentTemplateType,
    // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
    contentWidth: 1920,
    // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
    contentHeight: 1080,
    // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
    controlGroups: getControlGroups(this.currentTemplateType),
    // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
    customUIController: this.nodeController,
  };
  // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
  PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
    this.pipController = controller;
    // 步骤1：初始化画中画控制器
    this.initPipController();
    // 步骤2：通过startPiP接口启动画中画
    this.pipController.startPiP().then(() => {
      Logger.info(`Succeeded in starting pip.`);
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to start pip. Cause:${err.code}, message:${err.message}`);
    });
  }).catch((err: BusinessError) => {
    Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
  });
}

通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画。

this.pipController.setAutoStartEnabled(false /* or true if necessary */); // 默认为false

更新媒体源尺寸信息。

画中画提供的交互方式中支持通过双击或者拖拽画中画窗口四边以及四个对角缩放画中画窗口大小。除此之外，画中画媒体源更新后（如切换视频），通过画中画控制器实例的updateContentSize接口更新媒体源尺寸信息，以调整画中画窗口比例。

Button('updateSize') // 更新视频尺寸
  .onClick(() => {
    // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
    // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
    this.updateContentSize(900, 1600);
  })
  .stateStyles({
    pressed: {
      .backgroundColor(Color.Red);
    },
    normal: {
      .backgroundColor(Color.Blue);
    }
  })

关闭画中画。

当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的stopPiP接口关闭画中画。

// 步骤4：当不再需要显示画中画时，通过stopPiP接口关闭画中画
stopPip() {
  if (this.pipController) {
    this.pipController.stopPiP()
    .then(() => {
      Logger.info(`Succeeded in stopping pip.`);
      this.pipController?.off('stateChange'); // 如果已注册stateChange回调，停止画中画时取消注册该回调
      this.pipController?.off('controlPanelActionEvent'); // 如果已注册controlPanelActionEvent回调，停止画中画时取消注册该回调
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to stop pip. Cause:${err.code}, message:${err.message}`);
    });
  }
}

示例中的视频播放需要使用AVPlayer，具体示例可参考视频播放。

以上示例代码对应的示意图如下所示：

## Code blocks

### Code block 1

```
function getControlGroups(templateType: PiPWindow.PiPTemplateType): PiPControlGroups {
  switch (templateType) {
    case PiPWindow.PiPTemplateType.VIDEO_PLAY:
      return [PiPWindow.VideoPlayControlGroup.VIDEO_PREVIOUS_NEXT];
    case PiPWindow.PiPTemplateType.VIDEO_CALL:
      return [PiPWindow.VideoCallControlGroup.MICROPHONE_SWITCH,
        PiPWindow.VideoCallControlGroup.HANG_UP_BUTTON, PiPWindow.VideoCallControlGroup.CAMERA_SWITCH];
    case PiPWindow.PiPTemplateType.VIDEO_MEETING:
      return [PiPWindow.VideoMeetingControlGroup.MICROPHONE_SWITCH,
        PiPWindow.VideoMeetingControlGroup.HANG_UP_BUTTON, PiPWindow.VideoMeetingControlGroup.CAMERA_SWITCH];
    case PiPWindow.PiPTemplateType.VIDEO_LIVE:
      return [PiPWindow.VideoLiveControlGroup.VIDEO_PLAY_PAUSE,
        PiPWindow.VideoLiveControlGroup.MUTE_SWITCH];
    default:
      return [];
  }
}

// ...

@Component
export struct Page1 {
  // ...
  @State currentTemplateType: PiPWindow.PiPTemplateType = PiPWindow.PiPTemplateType.VIDEO_PLAY;
  // ...
  startPip() {
    // ...
    let config: PiPWindow.PiPConfiguration = {
      context: this.getUIContext().getHostContext() as Context,
      componentController: this.mXComponentController,
      // 当前page导航id
      // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
      // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
      // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
      navigationId: this.navId,
      // 对于视频通话、视频会议等场景，需要设置相应的模板类型
      templateType: this.currentTemplateType,
      // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
      contentWidth: 1920,
      // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
      contentHeight: 1080,
      // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
      controlGroups: getControlGroups(this.currentTemplateType),
      // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
      customUIController: this.nodeController,
    };
    // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
    PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
      // ...
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
    });
  }

  // ...
}
```

### Code block 2

```
// 开发者可通过继承NodeController实现自定义UI控制器
class TextNodeController extends NodeController {
  private message: string;
  private textNode: BuilderNode<[Params]> | null = null;

  constructor(message: string) {
    super();
    this.message = message;
  }

  // 通过BuilderNode加载自定义布局
  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
    return this.textNode.getFrameNode();
  }

  // 开发者可自定义该方法实现布局更新
  update(message: string) {
    Logger.info(`update message: ${message}`);
    if (this.textNode !== null) {
      this.textNode.update(new Params(message));
    }
  }

  // 开发者需要定义该方法实现布局的注销，避免内存泄漏
  dispose() {
    Logger.info('dispose message: execute node dispose');
    if (this.textNode !== null) {
      this.textNode.dispose();
    }
  }
}
```

### Code block 3

```
class Params {
  public text: string = '';

  constructor(text: string) {
    this.text = text;
  }
}

// 开发者可以通过@Builder装饰器实现布局构建
@Builder
function buildText(params: Params) {
  Column() {
    Text(params.text)
      .fontSize(20)
      .fontColor(Color.Red)
  }
  .width('100%') // 宽度方向充满画中画窗口
  .height('100%') // 高度方向充满画中画窗口
}
```

### Code block 4

```
@Component
export struct Page1 {
  // ...
  private nodeController: TextNodeController = new TextNodeController('this is custom UI');
  // ...
  startPip() {
    if (!PiPWindow.isPiPEnabled()) {
      Logger.error(`picture in picture disabled for current OS`);
      return;
    }
    let config: PiPWindow.PiPConfiguration = {
      context: this.getUIContext().getHostContext() as Context,
      componentController: this.mXComponentController,
      // 当前page导航id
      // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
      // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
      // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
      navigationId: this.navId,
      // 对于视频通话、视频会议等场景，需要设置相应的模板类型
      templateType: this.currentTemplateType,
      // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
      contentWidth: 1920,
      // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
      contentHeight: 1080,
      // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
      controlGroups: getControlGroups(this.currentTemplateType),
      // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
      customUIController: this.nodeController,
    };
    // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
    PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
      // ...
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
    });
  }

  // ...
}
```

### Code block 5

```
this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
  this.onStateChange(state, reason);
});
```

### Code block 6

```
this.pipController.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
  this.onActionEvent(event, status);
});
```

### Code block 7

```
startPip() {
  if (!PiPWindow.isPiPEnabled()) {
    Logger.error(`picture in picture disabled for current OS`);
    return;
  }
  let config: PiPWindow.PiPConfiguration = {
    context: this.getUIContext().getHostContext() as Context,
    componentController: this.mXComponentController,
    // 当前page导航id
    // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
    // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
    // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
    navigationId: this.navId,
    // 对于视频通话、视频会议等场景，需要设置相应的模板类型
    templateType: this.currentTemplateType,
    // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
    contentWidth: 1920,
    // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
    contentHeight: 1080,
    // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
    controlGroups: getControlGroups(this.currentTemplateType),
    // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
    customUIController: this.nodeController,
  };
  // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
  PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
    this.pipController = controller;
    // 步骤1：初始化画中画控制器
    this.initPipController();
    // 步骤2：通过startPiP接口启动画中画
    this.pipController.startPiP().then(() => {
      Logger.info(`Succeeded in starting pip.`);
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to start pip. Cause:${err.code}, message:${err.message}`);
    });
  }).catch((err: BusinessError) => {
    Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
  });
}
```

### Code block 8

```
this.pipController.setAutoStartEnabled(false /* or true if necessary */); // 默认为false
```

### Code block 9

```
Button('updateSize') // 更新视频尺寸
  .onClick(() => {
    // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
    // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
    this.updateContentSize(900, 1600);
  })
  .stateStyles({
    pressed: {
      .backgroundColor(Color.Red);
    },
    normal: {
      .backgroundColor(Color.Blue);
    }
  })
```

### Code block 10

```
// 步骤4：当不再需要显示画中画时，通过stopPiP接口关闭画中画
stopPip() {
  if (this.pipController) {
    this.pipController.stopPiP()
    .then(() => {
      Logger.info(`Succeeded in stopping pip.`);
      this.pipController?.off('stateChange'); // 如果已注册stateChange回调，停止画中画时取消注册该回调
      this.pipController?.off('controlPanelActionEvent'); // 如果已注册controlPanelActionEvent回调，停止画中画时取消注册该回调
    }).catch((err: BusinessError) => {
      Logger.error(`Failed to stop pip. Cause:${err.code}, message:${err.message}`);
    });
  }
}
```
