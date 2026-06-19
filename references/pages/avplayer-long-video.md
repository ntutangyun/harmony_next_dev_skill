# 基于AVPlayer播放长视频实践

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/avplayer-long-video_

概述

本文适用于视频播放类应用的开发，针对市场上主流视频播放类应用的常见场景，介绍了如何基于AVPlayer系统播放器实现长视频播放。本文指导开发者实现亮度控制、焦点管理、前后台感知、弹幕发送与显示、视频截图、画中画播放、后台播放与接入播控中心、视频首帧显示等开发场景。

基本播控、精准跳转、静音播放、窗口缩放设置、倍速播放、音量控制、字幕挂载场景参见《基于AVPlayer基础播控实践》。

本篇文章主要介绍以下内容：

亮度控制

焦点管理

前后台感知

弹幕发送与显示

视频截图

画中画播放

接入播控中心

后台播放

视频首帧显示

横竖屏切换与旋转感知

视频无缝转场播放

亮度控制

[h2]场景描述

用户在横屏播放视频时可通过手势滑动调节屏幕亮度。

[h2]实现原理

使用Slider组件设置亮度面板，绑定PanGesture滑动手势事件，当Pan手势在移动过程中调用setWindowBrightness()方法，实现上滑增加亮度、下滑减少亮度的功能。

[h2]开发步骤

当进入全屏播放模式时，在视频播放界面右侧区域添加Slider组件，用来展示屏幕亮度变化情况。

Column() {
  Stack() {
    Slider({
      value: this.screenBrightness,
      min: 0,
      max: 1,
      step: 0.05,
      style: SliderStyle.NONE,
      direction: Axis.Vertical,
      reverse: true
    })
      .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
      .height(160)
      .selectedColor(Color.White)
      .trackColor(Color.Black)
      .trackThickness(40)
      .onChange(async (value: number) => {
        this.screenBrightness = value;
        let windowStage: window.WindowStage = AppStorage.get(KeyConstants.KEY_WINDOW_STAGE) as window.WindowStage;
        try {
          let mainWin: window.Window = windowStage.getMainWindowSync();
          await mainWin.setWindowBrightness(value);
        } catch (exception) {
          Logger.error(TAG, `getMainWindowSync failed: code: ${exception.code}, message: ${exception.message}`);
        }
      })

    Image($r('app.media.sun_max_fill'))
      .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
      .margin({ top: 120 })
      .width(20)
      .height(20)
  }
  .margin({
    top: 0,
    right: 0
  })
}
.width('50%')
.alignItems(HorizontalAlign.End)
.justifyContent(FlexAlign.Center)
.padding({
  right: 30,
  bottom: 20
})

在视频播放界面绑定PanGesture滑动手势事件，设置触发条件为仅在屏幕右侧区域且垂直方向滑动Pan手势时，调用setWindowBrightness()方法，实现亮度的调节。此处setScreenBrightness()为setWindowBrightness()的封装。

private processGesture(event: GestureEvent) {
  if (event.fingerList.length === 0) {
    return;
  }
  if (event.fingerList[0].globalX > (this.getUIContext().px2vp(this.screenWidth / 2))) {
    if (this.isInputtingBulletComment) {
      return;
    }
    this.visible = true;
    let curBrightness = this.screenBrightness - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
    curBrightness = this.getValidValue(curBrightness, 0.0, 1.0);
    this.screenBrightness = curBrightness;
    this.setScreenBrightness(this.screenBrightness);
  } else {
    this.visible = false;
    let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
    curVolume = this.getValidValue(curVolume, 0.0, 15.0);
    this.volume = curVolume;
  }
}

.gesture(
  PanGesture({ direction: PanDirection.Vertical })
    .onActionStart(() => {
    })
    .onActionUpdate((event: GestureEvent) => {
      this.processGesture(event);
    })
    .onActionEnd(() => {
      setTimeout(() => {
        this.visible = false;
      }, 3000)
    })
)

焦点管理

[h2]场景描述

通过正确设置音频流类型、中断事件处理和自定义焦点策略，完成播放过程中的音频焦点管理。

[h2]实现原理

通过AVPlayer的on('audioInterrupt')方法，监听音频焦点变化，根据不同的打断类型和中断提示作相应的处理，更多焦点管理相关说明可参考音频焦点管理。

当闹钟或电话等外部打断事件发生时，打断类型为强制打断（INTERRUPT_FORCE），视频会自动中断播放。

当闹钟或电话提示音结束后，系统会发送一个打断事件，其打断类型为共享打断（INTERRUPT_SHARE），中断提示为音频可继续播放（INTERRUPT_HINT_RESUME）。应用监听到该事件后，应调用AVPlayer的play()函数恢复播放。

[h2]开发步骤

通过AVPlayer实例注册on('audioInterrupt')方法，监听外部打断事件，当打断类型为INTERRUPT_FORCE时，视频会自动中断播放。

当打断类型为INTERRUPT_SHARE、中断提示为INTERRUPT_HINT_RESUME时，调用videoPlay()函数恢复播放视频。此处videoPlay()为play()的封装。

private setInterruptCallback() {
  if (!this.avPlayer) {
    return;
  }
  this.avPlayer.on('audioInterrupt', async (interruptEvent: audio.InterruptEvent) => {
    if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_FORCE) {
      switch (interruptEvent.hintType) {
        case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        case audio.InterruptHint.INTERRUPT_HINT_STOP:
          this.isPlaying = false;
          this.updateIsPlay();
          break;
        case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
          break;
        default:
          break;
      }
    } else if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_SHARE) {
      switch (interruptEvent.hintType) {
        case audio.InterruptHint.INTERRUPT_HINT_RESUME:
          this.videoPlay();
          break;
        default:
          break;
      }
    }
  });
}

前后台感知

[h2]场景描述

应用从前台切到后台，再从后台切回前台时，能够保持原有进度继续播放原视频。

[h2]实现原理

在切换到前台的生命周期方法onPageShow()里调用AVPlayer的播放方法play()，并在切换到后台的生命周期方法onPageHide()里调用AVPlayer的暂停方法pause()。

[h2]开发步骤

在主页面的onPageShow()和onPageHide()里变更状态变量。

onPageHide(): void {
  this.isPageShow = false;
}

onPageShow(): void {
  this.isPageShow = true;
}

在视频播放组件里对该状态变量添加@Watch装饰器。

@Prop @Watch('onPageShowChange') isPageShow: boolean = false;

通过监听事件onPageShowChange调用AVPlayer的播放/暂停方法，以实现切换到后台时视频暂停播放、切回前台时视频恢复播放。此处avPlayerController为基于AVPlayer实现基本播控的控制器实例，resumePlayback()和pausePlay()分别为play()和pause()的封装。

onPageShowChange() {
  if (!this.isPIPShow && this.curIndex === this.index) {
    this.isPageShow ? this.resumePlayback() : this.pausePlay();
  }
}

private resumePlayback() {
  if (!this.avPlayerController.isPlaying) {
    this.avPlayerController.videoPlay();
  }
}

private pausePlay() {
  if (this.avPlayerController.isPlaying) {
    this.avPlayerController.videoPause();
  }
}

弹幕发送与显示

[h2]场景描述

视频弹幕发送与显示是影音娱乐类应用中的高频使用场景之一，如用户在播放视频、观看直播时可以发送弹幕，实时评论互动，增强用户参与度。

[h2]实现原理

通过数组保存实现弹幕发送，基于setInterval()函数和translate属性实现弹幕水平移动的动画效果。

[h2]开发步骤

在视频播放组件里定义一个空数组，用来保存发送的弹幕，用户输入弹幕点击发送后将输入内容存入当前数组中。

private sendBulletComment() {
  if (this.bulletCommentInput.trim()) {
    this.bulletComments = [...this.bulletComments, new BulletComment(this.bulletCommentInput, true)];
    this.bulletCommentInput = '';
    if (this.bulletComments.length > 50) {
      this.bulletComments = this.bulletComments.slice(1);
    }
  }
  this.resumePlayback();
}

在弹幕展示组件中，通过调用setInterval函数设置定时器，定时器定时刷新承载弹幕内容的Text组件的translate属性，刷新所有弹幕位置。

private startAnimation() {
  if (this.timerId > 0) {
    clearInterval(this.timerId);
  }
  this.timerId = setInterval(() => {
    let needUpdate = false;
    this.bulletComments.forEach(item => {
      const positionX = item.translateX - item.speed;
      if (positionX !== item.translateX) {
        item.translateX = positionX;
        needUpdate = true;
      }
    });
    const beforeLength = this.bulletComments.length;
    this.bulletComments =
      this.bulletComments.filter(item => item.translateX > -20);
    if (needUpdate || this.bulletComments.length !== beforeLength) {
      this.forceUpdate = !this.forceUpdate;
    }
  }, 16);
}

视频截图

[h2]场景描述

视频截图是影音娱乐类应用中的典型场景之一，如用户可在观看视频时截取画面，并对截图的前后帧进行微调，避免所截图片与预期不符。

[h2]实现原理

以XComponent作为媒体流播放组件，通过ComponentSnapshot对象获取组件截图的能力。

[h2]开发步骤

通过getUIContext().getComponentSnapshot().get()方法获取视频播放组件XComponent当前截图。

private async screenshot() {
  try {
    this.pixmap = await this.getUIContext().getComponentSnapshot().get(`videoXComponent_${this.curSource.index}`);
  } catch (exception) {
    Logger.error(TAG, `screenshot failed: code: ${exception.code}, message: ${exception.message}`);
  }
}

调用AVPlayer的seek()方法跳转到视频播放的上一秒或下一秒，再次通过步骤1的方法获取当前截图。此处avPlayerController为基于AVPlayer实现基本播控的控制器实例，videoSeek()为seek()的封装。

private async clickPreviousFrame() {
  this.avPlayerController?.videoSeek(this.screenshotTime - 1000 / ScreenShotConstants.FRAME_RATE);
  this.pausePlay();
  if (this.previousFrameTimerId) {
    clearTimeout(this.previousFrameTimerId);
  }
  this.previousFrameTimerId = setTimeout(() => {
    this.screenshot()
  }, 500)
  this.screenshotTime -= 1000 / ScreenShotConstants.FRAME_RATE;
  this.screenshotTime = Math.max(0, Math.min(this.screenshotTime, this.avPlayerController.durationTime));
}

private async clickNextFrame() {
  this.avPlayerController?.videoSeek(this.screenshotTime + 1000 / ScreenShotConstants.FRAME_RATE);
  this.pausePlay();
  if (this.nextFrameTimerId) {
    clearTimeout(this.nextFrameTimerId);
  }
  this.nextFrameTimerId = setTimeout(() => {
    this.screenshot()
  }, 500)
  this.screenshotTime += 1000 / ScreenShotConstants.FRAME_RATE;
  this.screenshotTime = Math.max(0, Math.min(this.screenshotTime, this.avPlayerController.durationTime));
}

画中画播放

[h2]场景描述

应用在视频播放时，可以使用画中画能力将视频内容以小窗（画中画）模式呈现。切换为小窗（画中画）模式后，用户可以进行其他界面操作，提升使用体验。

[h2]实现原理

以XComponent作为媒体流播放组件，通过PiPWindow模块实现画中画基础功能。

说明

仅支持以XComponent作为媒体流播放组件的界面进入画中画模式，XComponent的type必须为XComponentType.SURFACE。

在API version 20之前，支持在Phone、Tablet设备使用XComponent实现画中画功能开发；从API version 20开始，支持在Phone、PC/2in1、Tablet设备使用XComponent实现画中画功能开发。

[h2]开发步骤

创建画中画控制器，设置setAutoStartEnabled()为true以在应用返回桌面时启动画中画。

async createPipController() {
  if (!this.pipController) {
    try {
      this.pipController = await PiPWindow.create({
        context: this.context,
        componentController: this.xComponentController,
        templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY
      });
    } catch (exception) {
      Logger.error(TAG,
        `pipController init failed, Code:${exception.code}, message:${exception.message}`);
    }
  }
  this.pipController?.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
    this.onStateChange(state, reason);
  });

  this.pipController?.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
    this.onActionEvent(event, status);
  });
  this.pipController?.setAutoStartEnabled(true);
}

注册生命周期事件和控制事件回调。

onStateChange(state: PiPWindow.PiPState, reason: string) {
  switch (state) {
    case PiPWindow.PiPState.ABOUT_TO_START:
      this.curState = 'ABOUT_TO_START';
      break;
    case PiPWindow.PiPState.STARTED:
      this.curState = 'STARTED';
      let status: PiPWindow.PiPControlStatus =
        this.avPlayerController?.isPlaying ? PiPWindow.PiPControlStatus.PLAY : PiPWindow.PiPControlStatus.PAUSE;
      this.pipController?.updatePiPControlStatus(PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE, status);
      break;
    case PiPWindow.PiPState.ABOUT_TO_STOP:
      this.curState = 'ABOUT_TO_STOP';
      break;
    case PiPWindow.PiPState.STOPPED:
      this.curState = 'STOPPED';
      break;
    case PiPWindow.PiPState.ABOUT_TO_RESTORE:
      this.curState = 'ABOUT_TO_RESTORE';
      break;
    case PiPWindow.PiPState.ERROR:
      this.curState = 'ERROR';
      break;
    default:
      break;
  }
}

onActionEvent(event: PiPWindow.PiPActionEventType, status?: number) {
  switch (event) {
    case 'playbackStateChanged':
      if (status === 0) {
        this.avPlayerController?.videoPause();
      } else if (status === 1) {
        this.avPlayerController?.videoPlay();
      }
      break;
    default:
      break;
  }
}

销毁画中画控制器，设置setAutoStartEnabled()为false以关闭画中画。

destroyPipController() {
  if (!this.pipController) {
    return;
  }
  this.pipController.setAutoStartEnabled(false);
  this.pipController.off('stateChange');
  this.pipController.off('controlPanelActionEvent');
  this.pipController = undefined;
}

接入播控中心

[h2]场景描述

通过播控中心，控制视频的播放、暂停和上下切换。

[h2]实现原理

通过AVSessionKit音频播控服务实现视频应用接入播控中心。

[h2]开发步骤

通过createAVSession()创建AVSession实例并激活媒体会话，AVSessionType设置为“video”。

public initAvSession() {
  this.context = AppStorage.get(KeyConstants.KEY_CONTEXT);
  if (!this.context) {
    Logger.error(TAG, 'session create failed : context is undefined');
    return;
  }
  avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video').then(async (avSession) => {
    this.avSession = avSession;
    BackgroundTaskManager.startContinuousTask(this.context);
    this.setLaunchAbility();
    this.avSession.activate().catch((err: BusinessError) => {
      Logger.error(TAG, `avSession activate failed, code is ${err.code}, message is ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `createAVSession failed, code is ${err.code}, message is ${err.message}`);
  });
}

通过setAVMetadata()把会话的一些元数据信息设置给系统，从而在播控中心界面进行展示。如媒体ID（assetId）、标题（title）、播控中心显示的图片（mediaImage）、媒体时长（duration）等。

public async setAVMetadata(curSource: VideoData, duration: number) {
  if (curSource === undefined) {
    Logger.error(TAG, 'SetAVMetadata Error, curSource is null');
    return;
  }
  let metadata: avSession.AVMetadata = {
    assetId: `${curSource.index}`,
    title: curSource.name,
    duration: duration
  };
  if (this.avSession) {
    this.avSession.setAVMetadata(metadata).then(() => {
      this.avSessionMetadata = metadata;
    }).catch((err: BusinessError) => {
      Logger.error(TAG, `SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
    });
  }
}

设置用于被播控中心拉起的UIAbility。

private setLaunchAbility() {
  if (!this.context) {
    return;
  }
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: this.context.abilityInfo.bundleName,
        abilityName: this.context.abilityInfo.name
      }
    ],
    actionType: wantAgent.OperationType.START_ABILITIES,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
  };
  wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
    if (this.avSession) {
      this.avSession.setLaunchAbility(agent).catch((err: BusinessError) => {
        Logger.error(TAG, `setLaunchAbility failed: code: ${err.code}, message: ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `getWantAgent failed: code: ${err.code}, message: ${err.message}`);
  });
}

注册播控命令事件监听，便于响应用户通过播控中心下发的播控命令，比如播放on('play')、暂停on('pause')、上一曲on('playPrevious')、下一曲on('playNext')等。

public async setAvSessionListener() {
  if (!this.avSessionController) {
    return;
  }
  try {
    this.avSessionController.getAvSession()?.on('play', () => this.sessionPlayCallback());
    this.avSessionController.getAvSession()?.on('pause', () => this.sessionPauseCallback());
    this.avSessionController.getAvSession()?.on('seek', (seekTime: number) => this.sessionSeekCallback(seekTime));
    this.avSessionController.getAvSession()?.on('setLoopMode', (mode: avSession.LoopMode) => {
      Logger.info(`on setLoopMode: ${mode}`);
    });
    this.avSessionController.getAvSession()?.on('playPrevious', () => {
      this.sessionPlayPreviousCallback();
    });
    this.avSessionController.getAvSession()?.on('playNext', () => {
      this.sessionPlayNextCallback();
    });
  } catch (exception) {
    Logger.error(TAG,
      `Invoke setAvSessionListener failed, code is ${exception.code}, message is ${exception.message}`);
  }
}

应用状态上报播控中心，当视频状态发生改变时，需要通过setAVPlaybackState()向播控中心上报视频状态，来达到播控中心与应用的状态同步，包括播放状态（state）、播放位置（position）、当前媒体播放时长（duration）等。

private updateIsPlay() {
  this.avSessionController.setAvSessionPlayState({
    state: this.isPlaying ? avSession.PlaybackState.PLAYBACK_STATE_PLAY :
      avSession.PlaybackState.PLAYBACK_STATE_PAUSE,
    position: {
      elapsedTime: this.currentTime,
      updateTime: new Date().getTime()
    },
    duration: this.durationTime,
    speed: this.curSpeed
  });
}

public setAvSessionPlayState(playbackState: avSession.AVPlaybackState) {
  if (this.avSession) {
    this.avSession.setAVPlaybackState(playbackState, (err: BusinessError) => {
      if (err) {
        Logger.error(TAG, `SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
      } else {
        Logger.info(TAG, 'SetAVPlaybackState successfully');
      }
    });
  }
}

后台播放

[h2]场景描述

视频切换到后台播放。

[h2]实现原理

首先需实现播控中心的接入，在此基础上申请后台运行权限并设置后台模式，同时为视频应用创建长时后台任务，从而实现视频在后台持续播放的功能。

说明

后台播放的实现依赖于播控中心，建议开发者先完成接入播控中心章节的学习。

[h2]开发步骤

在module.json5配置文件中配置ohos.permission.KEEP_BACKGROUND_RUNNING权限和后台模式为“audioPlayback”。

"requestPermissions": [
  {
    "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
    "reason": "$string:reason_background",
    "usedScene": {
      "abilities": [
        "AvplayerlongvideoAbility"
      ],
      "when": "always"
    }
  }
],

"backgroundModes": [
  "audioPlayback"
],

创建后台任务管理类，实现后台任务的申请（startContinuousTask）与取消（stopContinuousTask），长时任务类型选择AUDIO_PLAYBACK，表示视频后台播放。

public static startContinuousTask(context?: common.UIAbilityContext): void {
  if (!context) {
    return;
  }
  let wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: context.abilityInfo.bundleName,
        abilityName: context.abilityInfo.name
      }
    ],
    actionType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
  };
  wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
    if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.Core')) {
      backgroundTaskManager.startBackgroundRunning(context,
        backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
      }).catch((err: BusinessError) => {
        Logger.error(TAG, `startBackgroundRunning failed, code is ${err.code}, message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `getWantAgent failed, code is ${err.code}, message is ${err.message}`);
  });
}

public static stopContinuousTask(context?: common.UIAbilityContext): void {
  if (!context) {
    return;
  }
  if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.Core')) {
    backgroundTaskManager.stopBackgroundRunning(context).then(() => {
    }).catch((err: BusinessError) => {
      Logger.error(TAG, `stopBackgroundRunning failed, code is ${err.code}, message is ${err.message}`);
    });
  }
}

在AVSession创建和释放时，分别申请和销毁后台长时任务。

public initAvSession() {
  this.context = AppStorage.get(KeyConstants.KEY_CONTEXT);
  if (!this.context) {
    Logger.error(TAG, 'session create failed : context is undefined');
    return;
  }
  avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video').then(async (avSession) => {
    this.avSession = avSession;
    BackgroundTaskManager.startContinuousTask(this.context);
    this.setLaunchAbility();
    this.avSession.activate().catch((err: BusinessError) => {
      Logger.error(TAG, `avSession activate failed, code is ${err.code}, message is ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `createAVSession failed, code is ${err.code}, message is ${err.message}`);
  });
}

async unregisterSessionListener() {
  if (!this.avSession) {
    return;
  }
  try {
    this.avSession.off('play');
    this.avSession.off('pause');
    this.avSession.off('playNext');
    this.avSession.off('playPrevious');
    this.avSession.off('setLoopMode');
    this.avSession.off('seek');
  } catch (exception) {
    Logger.error(TAG, `unregisterSessionListener failed: code: ${exception.code}, message: ${exception.message}`);
  }
  BackgroundTaskManager.stopContinuousTask(this.context);
}

视频首帧显示

[h2]场景描述

在播放列表或者窗口中显示视频的首帧。

[h2]实现原理

通过fetchFrameByTime()方法获取本地视频的首帧图片在视频列表展示。

通过设置播放策略setPlaybackStrategy的showFirstFrameOnPrepare属性为true来实现AVPlayer显示视频起播首帧。

[h2]开发步骤

播放列表中显示视频首帧的实现：

使用media.AVImageGenerator实例的fetchFrameByTime()方法获取本地视频的首帧图片在列表展示。

public static async getThumbnailFromVideo(src: string, timeUs: number) {
  let pixelMap: image.PixelMap | undefined;
  let queryOption = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;
  let param: media.PixelMapParams = {
    width: 540,
    height: 304
  };
  let generator: media.AVImageGenerator | null = null;
  try {
    let fileDescriptor = await uiContext?.getHostContext()?.resourceManager?.getRawFd(src);
    if (!fileDescriptor) {
      Logger.error(TAG, 'Failed to get file descriptor');
      return null;
    }
    generator = await media.createAVImageGenerator();
    generator.fdSrc = fileDescriptor;
    pixelMap = await generator.fetchFrameByTime(timeUs, queryOption, param);
    await generator.release();
  } catch (exception) {
    Logger.error(TAG, `getThumbnailFromVideo failed, code is ${exception.code}, message is ${exception.message}`);
  }
  return pixelMap;
}

播放窗口中显示视频首帧的实现：

确认AVPlayer实例中的on('stateChange')方法在prepared状态下没有调用this.avPlayer.play()，如有调用，则去掉，避免视频在加载完毕后自动播放。

在on('stateChange')方法中initialized状态下，设置播放策略setPlaybackStrategy的showFirstFrameOnPrepare为true。

case 'initialized':
  Logger.info(TAG, 'setAVPlayerCallback AVPlayerState initialized called.');
  await this.onInitialized();
  break;

private async onInitialized() {
  if (!this.avPlayer) {
    return;
  }
  this.avPlayer.surfaceId = this.surfaceID;
  try {
    await this.avPlayer.setPlaybackStrategy({
      preferredBufferDuration: 20,
      showFirstFrameOnPrepare: true
    });
  } catch (exception) {
    Logger.error(TAG,
      `setPlaybackStrategy failed. Cause code: ${exception.code}, message: ${exception.message}`);
  }
  this.avPlayer.prepare().catch((err: BusinessError) => {
    Logger.error(TAG, `prepare failed. Code:${err.code}, message:${err.message}`);
  });
}

横竖屏切换与旋转感知

[h2]场景描述

用户播放视频时可以根据实际需求进行横竖屏切换。

[h2]实现原理

通过设置orientation为auto_rotation_restricted实现传感器自动感知。

通过设置window.Orientation为USER_ROTATION_LANDSCAPE/USER_ROTATION_PORTRAIT实现横竖屏的手动切换。

[h2]开发步骤

通过传感器旋转自动感知切换：

在模块级配置文件module.json5中设置窗口显示方向为AUTO_ROTATION_RESTRICTED。

"orientation": "auto_rotation_restricted",

通过点击按钮实现横竖屏切换：

封装横竖屏切换的实现方法。

setMainWindowOrientation(orientation: window.Orientation, callback?: Function): void {
  if (this.mainWindowClass === undefined) {
    Logger.error(TAG, 'MainWindowClass is undefined');
    return;
  }
  this.mainWindowClass.setPreferredOrientation(orientation).then(() => {
    callback?.();
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `Failed to set the ${orientation} of main window. Code:${err.code}, message:${err.message}`);
  });
}

点击横屏播放按钮时，设置window.Orientation为USER_ROTATION_LANDSCAPE。

this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_LANDSCAPE);

点击返回按钮时，设置window.Orientation为USER_ROTATION_PORTRAIT。

this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_PORTRAIT);

视频无缝转场播放

[h2]场景描述

用户在横竖屏切换后，视频保持原有进度继续播放。

[h2]实现原理

基于AVPlayer与XComponent实现视频播放，在横竖屏来回切换时，AVPlayer本身具有保持原有进度继续播放的特性，开发者无需进行额外开发。

示例代码

基于AVPlayer实现长视频播放

## Code blocks

### Code block 1

```
Column() {
  Stack() {
    Slider({
      value: this.screenBrightness,
      min: 0,
      max: 1,
      step: 0.05,
      style: SliderStyle.NONE,
      direction: Axis.Vertical,
      reverse: true
    })
      .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
      .height(160)
      .selectedColor(Color.White)
      .trackColor(Color.Black)
      .trackThickness(40)
      .onChange(async (value: number) => {
        this.screenBrightness = value;
        let windowStage: window.WindowStage = AppStorage.get(KeyConstants.KEY_WINDOW_STAGE) as window.WindowStage;
        try {
          let mainWin: window.Window = windowStage.getMainWindowSync();
          await mainWin.setWindowBrightness(value);
        } catch (exception) {
          Logger.error(TAG, `getMainWindowSync failed: code: ${exception.code}, message: ${exception.message}`);
        }
      })

    Image($r('app.media.sun_max_fill'))
      .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
      .margin({ top: 120 })
      .width(20)
      .height(20)
  }
  .margin({
    top: 0,
    right: 0
  })
}
.width('50%')
.alignItems(HorizontalAlign.End)
.justifyContent(FlexAlign.Center)
.padding({
  right: 30,
  bottom: 20
})
```

### Code block 2

```
private processGesture(event: GestureEvent) {
  if (event.fingerList.length === 0) {
    return;
  }
  if (event.fingerList[0].globalX > (this.getUIContext().px2vp(this.screenWidth / 2))) {
    if (this.isInputtingBulletComment) {
      return;
    }
    this.visible = true;
    let curBrightness = this.screenBrightness - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
    curBrightness = this.getValidValue(curBrightness, 0.0, 1.0);
    this.screenBrightness = curBrightness;
    this.setScreenBrightness(this.screenBrightness);
  } else {
    this.visible = false;
    let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
    curVolume = this.getValidValue(curVolume, 0.0, 15.0);
    this.volume = curVolume;
  }
}
```

### Code block 3

```
.gesture(
  PanGesture({ direction: PanDirection.Vertical })
    .onActionStart(() => {
    })
    .onActionUpdate((event: GestureEvent) => {
      this.processGesture(event);
    })
    .onActionEnd(() => {
      setTimeout(() => {
        this.visible = false;
      }, 3000)
    })
)
```

### Code block 4

```
private setInterruptCallback() {
  if (!this.avPlayer) {
    return;
  }
  this.avPlayer.on('audioInterrupt', async (interruptEvent: audio.InterruptEvent) => {
    if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_FORCE) {
      switch (interruptEvent.hintType) {
        case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
        case audio.InterruptHint.INTERRUPT_HINT_STOP:
          this.isPlaying = false;
          this.updateIsPlay();
          break;
        case audio.InterruptHint.INTERRUPT_HINT_DUCK:
        case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
          break;
        default:
          break;
      }
    } else if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_SHARE) {
      switch (interruptEvent.hintType) {
        case audio.InterruptHint.INTERRUPT_HINT_RESUME:
          this.videoPlay();
          break;
        default:
          break;
      }
    }
  });
}
```

### Code block 5

```
onPageHide(): void {
  this.isPageShow = false;
}
```

### Code block 6

```
onPageShow(): void {
  this.isPageShow = true;
}
```

### Code block 7

```
@Prop @Watch('onPageShowChange') isPageShow: boolean = false;
```

### Code block 8

```
onPageShowChange() {
  if (!this.isPIPShow && this.curIndex === this.index) {
    this.isPageShow ? this.resumePlayback() : this.pausePlay();
  }
}
```

### Code block 9

```
private resumePlayback() {
  if (!this.avPlayerController.isPlaying) {
    this.avPlayerController.videoPlay();
  }
}
```

### Code block 10

```
private pausePlay() {
  if (this.avPlayerController.isPlaying) {
    this.avPlayerController.videoPause();
  }
}
```

### Code block 11

```
private sendBulletComment() {
  if (this.bulletCommentInput.trim()) {
    this.bulletComments = [...this.bulletComments, new BulletComment(this.bulletCommentInput, true)];
    this.bulletCommentInput = '';
    if (this.bulletComments.length > 50) {
      this.bulletComments = this.bulletComments.slice(1);
    }
  }
  this.resumePlayback();
}
```

### Code block 12

```
private startAnimation() {
  if (this.timerId > 0) {
    clearInterval(this.timerId);
  }
  this.timerId = setInterval(() => {
    let needUpdate = false;
    this.bulletComments.forEach(item => {
      const positionX = item.translateX - item.speed;
      if (positionX !== item.translateX) {
        item.translateX = positionX;
        needUpdate = true;
      }
    });
    const beforeLength = this.bulletComments.length;
    this.bulletComments =
      this.bulletComments.filter(item => item.translateX > -20);
    if (needUpdate || this.bulletComments.length !== beforeLength) {
      this.forceUpdate = !this.forceUpdate;
    }
  }, 16);
}
```

### Code block 13

```
private async screenshot() {
  try {
    this.pixmap = await this.getUIContext().getComponentSnapshot().get(`videoXComponent_${this.curSource.index}`);
  } catch (exception) {
    Logger.error(TAG, `screenshot failed: code: ${exception.code}, message: ${exception.message}`);
  }
}
```

### Code block 14

```
private async clickPreviousFrame() {
  this.avPlayerController?.videoSeek(this.screenshotTime - 1000 / ScreenShotConstants.FRAME_RATE);
  this.pausePlay();
  if (this.previousFrameTimerId) {
    clearTimeout(this.previousFrameTimerId);
  }
  this.previousFrameTimerId = setTimeout(() => {
    this.screenshot()
  }, 500)
  this.screenshotTime -= 1000 / ScreenShotConstants.FRAME_RATE;
  this.screenshotTime = Math.max(0, Math.min(this.screenshotTime, this.avPlayerController.durationTime));
}
```

### Code block 15

```
private async clickNextFrame() {
  this.avPlayerController?.videoSeek(this.screenshotTime + 1000 / ScreenShotConstants.FRAME_RATE);
  this.pausePlay();
  if (this.nextFrameTimerId) {
    clearTimeout(this.nextFrameTimerId);
  }
  this.nextFrameTimerId = setTimeout(() => {
    this.screenshot()
  }, 500)
  this.screenshotTime += 1000 / ScreenShotConstants.FRAME_RATE;
  this.screenshotTime = Math.max(0, Math.min(this.screenshotTime, this.avPlayerController.durationTime));
}
```

### Code block 16

```
async createPipController() {
  if (!this.pipController) {
    try {
      this.pipController = await PiPWindow.create({
        context: this.context,
        componentController: this.xComponentController,
        templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY
      });
    } catch (exception) {
      Logger.error(TAG,
        `pipController init failed, Code:${exception.code}, message:${exception.message}`);
    }
  }
  this.pipController?.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
    this.onStateChange(state, reason);
  });

  this.pipController?.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
    this.onActionEvent(event, status);
  });
  this.pipController?.setAutoStartEnabled(true);
}
```

### Code block 17

```
onStateChange(state: PiPWindow.PiPState, reason: string) {
  switch (state) {
    case PiPWindow.PiPState.ABOUT_TO_START:
      this.curState = 'ABOUT_TO_START';
      break;
    case PiPWindow.PiPState.STARTED:
      this.curState = 'STARTED';
      let status: PiPWindow.PiPControlStatus =
        this.avPlayerController?.isPlaying ? PiPWindow.PiPControlStatus.PLAY : PiPWindow.PiPControlStatus.PAUSE;
      this.pipController?.updatePiPControlStatus(PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE, status);
      break;
    case PiPWindow.PiPState.ABOUT_TO_STOP:
      this.curState = 'ABOUT_TO_STOP';
      break;
    case PiPWindow.PiPState.STOPPED:
      this.curState = 'STOPPED';
      break;
    case PiPWindow.PiPState.ABOUT_TO_RESTORE:
      this.curState = 'ABOUT_TO_RESTORE';
      break;
    case PiPWindow.PiPState.ERROR:
      this.curState = 'ERROR';
      break;
    default:
      break;
  }
}
```

### Code block 18

```
onActionEvent(event: PiPWindow.PiPActionEventType, status?: number) {
  switch (event) {
    case 'playbackStateChanged':
      if (status === 0) {
        this.avPlayerController?.videoPause();
      } else if (status === 1) {
        this.avPlayerController?.videoPlay();
      }
      break;
    default:
      break;
  }
}
```

### Code block 19

```
destroyPipController() {
  if (!this.pipController) {
    return;
  }
  this.pipController.setAutoStartEnabled(false);
  this.pipController.off('stateChange');
  this.pipController.off('controlPanelActionEvent');
  this.pipController = undefined;
}
```

### Code block 20

```
public initAvSession() {
  this.context = AppStorage.get(KeyConstants.KEY_CONTEXT);
  if (!this.context) {
    Logger.error(TAG, 'session create failed : context is undefined');
    return;
  }
  avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video').then(async (avSession) => {
    this.avSession = avSession;
    BackgroundTaskManager.startContinuousTask(this.context);
    this.setLaunchAbility();
    this.avSession.activate().catch((err: BusinessError) => {
      Logger.error(TAG, `avSession activate failed, code is ${err.code}, message is ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `createAVSession failed, code is ${err.code}, message is ${err.message}`);
  });
}
```

### Code block 21

```
public async setAVMetadata(curSource: VideoData, duration: number) {
  if (curSource === undefined) {
    Logger.error(TAG, 'SetAVMetadata Error, curSource is null');
    return;
  }
  let metadata: avSession.AVMetadata = {
    assetId: `${curSource.index}`,
    title: curSource.name,
    duration: duration
  };
  if (this.avSession) {
    this.avSession.setAVMetadata(metadata).then(() => {
      this.avSessionMetadata = metadata;
    }).catch((err: BusinessError) => {
      Logger.error(TAG, `SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
    });
  }
}
```

### Code block 22

```
private setLaunchAbility() {
  if (!this.context) {
    return;
  }
  const wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: this.context.abilityInfo.bundleName,
        abilityName: this.context.abilityInfo.name
      }
    ],
    actionType: wantAgent.OperationType.START_ABILITIES,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
  };
  wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
    if (this.avSession) {
      this.avSession.setLaunchAbility(agent).catch((err: BusinessError) => {
        Logger.error(TAG, `setLaunchAbility failed: code: ${err.code}, message: ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `getWantAgent failed: code: ${err.code}, message: ${err.message}`);
  });
}
```

### Code block 23

```
public async setAvSessionListener() {
  if (!this.avSessionController) {
    return;
  }
  try {
    this.avSessionController.getAvSession()?.on('play', () => this.sessionPlayCallback());
    this.avSessionController.getAvSession()?.on('pause', () => this.sessionPauseCallback());
    this.avSessionController.getAvSession()?.on('seek', (seekTime: number) => this.sessionSeekCallback(seekTime));
    this.avSessionController.getAvSession()?.on('setLoopMode', (mode: avSession.LoopMode) => {
      Logger.info(`on setLoopMode: ${mode}`);
    });
    this.avSessionController.getAvSession()?.on('playPrevious', () => {
      this.sessionPlayPreviousCallback();
    });
    this.avSessionController.getAvSession()?.on('playNext', () => {
      this.sessionPlayNextCallback();
    });
  } catch (exception) {
    Logger.error(TAG,
      `Invoke setAvSessionListener failed, code is ${exception.code}, message is ${exception.message}`);
  }
}
```

### Code block 24

```
private updateIsPlay() {
  this.avSessionController.setAvSessionPlayState({
    state: this.isPlaying ? avSession.PlaybackState.PLAYBACK_STATE_PLAY :
      avSession.PlaybackState.PLAYBACK_STATE_PAUSE,
    position: {
      elapsedTime: this.currentTime,
      updateTime: new Date().getTime()
    },
    duration: this.durationTime,
    speed: this.curSpeed
  });
}
```

### Code block 25

```
public setAvSessionPlayState(playbackState: avSession.AVPlaybackState) {
  if (this.avSession) {
    this.avSession.setAVPlaybackState(playbackState, (err: BusinessError) => {
      if (err) {
        Logger.error(TAG, `SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
      } else {
        Logger.info(TAG, 'SetAVPlaybackState successfully');
      }
    });
  }
}
```

### Code block 26

```
"requestPermissions": [
  {
    "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
    "reason": "$string:reason_background",
    "usedScene": {
      "abilities": [
        "AvplayerlongvideoAbility"
      ],
      "when": "always"
    }
  }
],
```

### Code block 27

```
"backgroundModes": [
  "audioPlayback"
],
```

### Code block 28

```
public static startContinuousTask(context?: common.UIAbilityContext): void {
  if (!context) {
    return;
  }
  let wantAgentInfo: wantAgent.WantAgentInfo = {
    wants: [
      {
        bundleName: context.abilityInfo.bundleName,
        abilityName: context.abilityInfo.name
      }
    ],
    actionType: wantAgent.OperationType.START_ABILITY,
    requestCode: 0,
    wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
  };
  wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
    if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.Core')) {
      backgroundTaskManager.startBackgroundRunning(context,
        backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
      }).catch((err: BusinessError) => {
        Logger.error(TAG, `startBackgroundRunning failed, code is ${err.code}, message is ${err.message}`);
      });
    }
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `getWantAgent failed, code is ${err.code}, message is ${err.message}`);
  });
}
```

### Code block 29

```
public static stopContinuousTask(context?: common.UIAbilityContext): void {
  if (!context) {
    return;
  }
  if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.Core')) {
    backgroundTaskManager.stopBackgroundRunning(context).then(() => {
    }).catch((err: BusinessError) => {
      Logger.error(TAG, `stopBackgroundRunning failed, code is ${err.code}, message is ${err.message}`);
    });
  }
}
```

### Code block 30

```
public initAvSession() {
  this.context = AppStorage.get(KeyConstants.KEY_CONTEXT);
  if (!this.context) {
    Logger.error(TAG, 'session create failed : context is undefined');
    return;
  }
  avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video').then(async (avSession) => {
    this.avSession = avSession;
    BackgroundTaskManager.startContinuousTask(this.context);
    this.setLaunchAbility();
    this.avSession.activate().catch((err: BusinessError) => {
      Logger.error(TAG, `avSession activate failed, code is ${err.code}, message is ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `createAVSession failed, code is ${err.code}, message is ${err.message}`);
  });
}
```

### Code block 31

```
async unregisterSessionListener() {
  if (!this.avSession) {
    return;
  }
  try {
    this.avSession.off('play');
    this.avSession.off('pause');
    this.avSession.off('playNext');
    this.avSession.off('playPrevious');
    this.avSession.off('setLoopMode');
    this.avSession.off('seek');
  } catch (exception) {
    Logger.error(TAG, `unregisterSessionListener failed: code: ${exception.code}, message: ${exception.message}`);
  }
  BackgroundTaskManager.stopContinuousTask(this.context);
}
```

### Code block 32

```
public static async getThumbnailFromVideo(src: string, timeUs: number) {
  let pixelMap: image.PixelMap | undefined;
  let queryOption = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;
  let param: media.PixelMapParams = {
    width: 540,
    height: 304
  };
  let generator: media.AVImageGenerator | null = null;
  try {
    let fileDescriptor = await uiContext?.getHostContext()?.resourceManager?.getRawFd(src);
    if (!fileDescriptor) {
      Logger.error(TAG, 'Failed to get file descriptor');
      return null;
    }
    generator = await media.createAVImageGenerator();
    generator.fdSrc = fileDescriptor;
    pixelMap = await generator.fetchFrameByTime(timeUs, queryOption, param);
    await generator.release();
  } catch (exception) {
    Logger.error(TAG, `getThumbnailFromVideo failed, code is ${exception.code}, message is ${exception.message}`);
  }
  return pixelMap;
}
```

### Code block 33

```
case 'initialized':
  Logger.info(TAG, 'setAVPlayerCallback AVPlayerState initialized called.');
  await this.onInitialized();
  break;
```

### Code block 34

```
private async onInitialized() {
  if (!this.avPlayer) {
    return;
  }
  this.avPlayer.surfaceId = this.surfaceID;
  try {
    await this.avPlayer.setPlaybackStrategy({
      preferredBufferDuration: 20,
      showFirstFrameOnPrepare: true
    });
  } catch (exception) {
    Logger.error(TAG,
      `setPlaybackStrategy failed. Cause code: ${exception.code}, message: ${exception.message}`);
  }
  this.avPlayer.prepare().catch((err: BusinessError) => {
    Logger.error(TAG, `prepare failed. Code:${err.code}, message:${err.message}`);
  });
}
```

### Code block 35

```
"orientation": "auto_rotation_restricted",
```

### Code block 36

```
setMainWindowOrientation(orientation: window.Orientation, callback?: Function): void {
  if (this.mainWindowClass === undefined) {
    Logger.error(TAG, 'MainWindowClass is undefined');
    return;
  }
  this.mainWindowClass.setPreferredOrientation(orientation).then(() => {
    callback?.();
  }).catch((err: BusinessError) => {
    Logger.error(TAG, `Failed to set the ${orientation} of main window. Code:${err.code}, message:${err.message}`);
  });
}
```

### Code block 37

```
this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_LANDSCAPE);
```

### Code block 38

```
this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_PORTRAIT);
```
