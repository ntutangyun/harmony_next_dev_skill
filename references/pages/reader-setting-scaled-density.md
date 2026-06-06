# 监听文本缩放因子变化

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-setting-scaled-density_

在智慧多窗等场景时，文本缩放因子Display.scaledDensity属性会发生变化。如果文本缩放因子的值与当前值不符，开发者需要更新ReaderSetting的scaledDensity属性，触发ReaderComponentController组件控制器的setPageConfig接口重新进行页面排版。

接口说明

监听文本缩放因子变化主要涉及1个接口，具体介绍如下表所示。

接口名	描述
setPageConfig(pageConfig: ReaderSetting): void	设置或者修改页面排版属性。
开发准备

在监听文本缩放因子变化之前，请先确保已经'构建阅读器'。

开发步骤

导入相关模块。

import { display } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

通过display.on接口监听文本缩放因子的变化。

在监听接口中比对系统值与当前值是否一致，如果不一致则通过应用级变量的状态管理AppStorage将isDensityChange值设为true，并退出阅读页。

@Entry
@Component
struct Reader {
  private screenDensityCallBack: Callback<number> | null = null;


  aboutToAppear(): void {
    this.registerScreenDensityChange();
    hilog.info(0x0000, 'testTag',
      'aboutToAppear : current scaledDensity = ' + this.readerSetting.scaledDensity + ', change scaledDensity = ' +
      display.getDefaultDisplaySync().scaledDensity);
  }


  /**
   * 注册缩放文本缩放因子变化监听
   */
  registerScreenDensityChange() {
    this.screenDensityCallBack = (data: number) => {
      let displaySync = display.getDefaultDisplaySync();
      let scaledDensity = displaySync.scaledDensity;
      if (scaledDensity !== this.readerSetting.scaledDensity) {
        AppStorage.setOrCreate('isDensityChange', true);
        this.getUIContext().getRouter().back();
      }
    }
    display.on('change', this.screenDensityCallBack);
  }


  aboutToDisappear(): void {
    display.off('change', this.screenDensityCallBack);
  }


  build() {
    // 需要开发者根据构建阅读器章节自行实现
  }
}

在阅读页的上级页面通过@StorageLink装饰器监听isDensityChange字段的变化。

当退出阅读页时，会触发上级Index页面的onPageShow生命周期回调。若检测到isDensityChange字段值变更，将执行重新进入阅读页的方法。

开发者可参考阅读进度通知章节保存阅读进度，在进阅读页时将保存的进度信息传入到阅读页，在阅读页通过startPlay接口继续阅读。

import { hilog } from '@kit.PerformanceAnalysisKit';


@Entry
@Component
struct Index {
  /**
   * 系统字体缩放因子是否发生变化，如果变化需要重启阅读器
   */
  @StorageLink('isDensityChange') isDensityChange: boolean = false;


  onPageShow(): void {
    // 文本缩放因子变化需要重新打开书籍
    if (this.isDensityChange) {
      this.jumper();
      AppStorage.setOrCreate('isDensityChange', false);
    }
  }


  private jumper() {
    this.getUIContext().getRouter().pushUrl({ url: "pages/Reader" }).catch(() => {
      hilog.error(0x0000, 'testTag', 'pushUrl failed');
    });
  }


  build() {
    // 需要开发者根据业务需要自行实现
  }
}
适配深、浅色模式
书籍内容交互
