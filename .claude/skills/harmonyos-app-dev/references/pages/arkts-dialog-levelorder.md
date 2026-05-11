# 弹出框层级管理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-levelorder_

ArkUI的弹出框节点都是直接挂载在根节点上，会根据层级从小到大依次挂载。根节点下，右边的弹出框节点会覆盖显示在左边的弹出框节点上，新创建的弹出框节点会根据层级大小插入到对应的位置，同一层级大小的弹窗节点按照创建的先后顺序进行挂载。

从API version 18开始，可以通过设置levelOrder参数来管理弹出框的显示顺序，确保层级较高的弹出框覆盖在层级较低的弹出框之上，从而根据需要灵活控制各层弹出框的显示效果。

使用约束

目前openCustomDialog、CustomDialog、AlertDialog、ActionSheet、showDialog支持通过levelOrder参数来管理弹出框的层次。

说明

弹出框层级管理不支持子窗场景，即当showInSubWindow设置为true时，levelOrder参数设置无效。不支持动态刷新弹出框的显示顺序。

创建不同层级的弹出框
说明

详细变量定义请参考完整示例。

初始化一个弹出框内容区，内部包含一个Text组件。

@Builder
normalCustomDialog(index: number) {
  Column() {
    // 请在resources\base\element\string.json文件中配置name为'open_normal_dialog'，value为非空字符串的资源
    Text(this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('open_normal_dialog') as string +
      index).fontSize(30)
  }.height(400).padding(5).justifyContent(FlexAlign.SpaceBetween)
}
DialogBoxLayer.ets

初始化另一个弹出框内容区，内部包含一个点击打开普通弹出框的按钮，点击事件中通过调用UIContext中getPromptAction方法获取PromptAction对象，再通过该对象调用openCustomDialog接口，并且设置层级为0的levelOrder参数来创建普通层级弹出框。

@Builder
topCustomDialog() {
  Column() {
    // 请将$r('app.string.top_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"我是置顶弹窗"
    Text($r('app.string.top_dialog')).fontSize(30)
    Row({ space: 50 }) {
      // 请将$r('app.string.open_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点我打开普通弹窗"
      Button($r('app.string.open_dialog'))
        .onClick(() => {
          this.getUIContext().getPromptAction().openCustomDialog({
            builder: () => {
              this.normalCustomDialog(this.dialogIndex);
            },
            levelOrder: LevelOrder.clamp(0),
          })
            .catch((err: BusinessError) => {
              hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + '' + err.message);
            });
          this.dialogIndex++;
        })
    }
  }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
}
DialogBoxLayer.ets

通过调用UIContext中getPromptAction方法获取PromptAction对象，再通过该对象调用openCustomDialog接口，并且设置层级为100000的levelOrder参数来创建最高层级弹出框。

this.getUIContext().getPromptAction().openCustomDialog({
  builder: () => {
    this.topCustomDialog();
  },
  levelOrder: LevelOrder.clamp(100000)
}).catch((err: BusinessError) => {
  hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + ' ' + err.message);
});
DialogBoxLayer.ets
完整示例
import { LevelOrder } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';


const INDEX: number = 0;
const DOMAIN = 0x0000;


@Entry
@Component
export struct DialogBoxLayer {
  @StorageLink('dialogIndex') dialogIndex: number = INDEX;


  @Builder
  normalCustomDialog(index: number) {
    Column() {
      // 请在resources\base\element\string.json文件中配置name为'open_normal_dialog'，value为非空字符串的资源
      Text(this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('open_normal_dialog') as string +
        index).fontSize(30)
    }.height(400).padding(5).justifyContent(FlexAlign.SpaceBetween)
  }




  @Builder
  topCustomDialog() {
    Column() {
      // 请将$r('app.string.top_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"我是置顶弹窗"
      Text($r('app.string.top_dialog')).fontSize(30)
      Row({ space: 50 }) {
        // 请将$r('app.string.open_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点我打开普通弹窗"
        Button($r('app.string.open_dialog'))
          .onClick(() => {
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.normalCustomDialog(this.dialogIndex);
              },
              levelOrder: LevelOrder.clamp(0),
            })
              .catch((err: BusinessError) => {
                hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + '' + err.message);
              });
            this.dialogIndex++;
          })
      }
    }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
  }




  build() {
    NavDestination() {
      Row() {
        Column({ space: 5 }) {
          // 请将$r('app.string.click_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点击弹窗"
          Button($r('app.string.click_dialog'))
            .fontSize(20)
            .onClick(() => {
              this.getUIContext().getPromptAction().openCustomDialog({
                builder: () => {
                  this.topCustomDialog();
                },
                levelOrder: LevelOrder.clamp(100000)
              }).catch((err: BusinessError) => {
                hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + ' ' + err.message);
              });
            })
        }.width('100%')
      }
    }
  }
}
DialogBoxLayer.ets

页面级弹出框
弹出框控制器
