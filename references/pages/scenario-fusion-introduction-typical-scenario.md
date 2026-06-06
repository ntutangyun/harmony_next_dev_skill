# 典型场景展示

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-introduction-typical-scenario_

TextInput().width('75%').contentType(ContentType.NICKNAME).selectionMenuHidden(true)
      }


      Row() {
        Text('姓名：').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
      }


      Row() {
        Text('手机号码：').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.PHONE_NUMBER).selectionMenuHidden(true)
      }


      Row() {
        Text('邮箱：').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.EMAIL_ADDRESS).selectionMenuHidden(true)
      }


      Row() {
        Text('身份证号：').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.ID_CARD_NUMBER).selectionMenuHidden(true)
      }


      Row() {
        Text('地址：').textAlign(TextAlign.End).width('25%')
        TextInput().width('75%').contentType(ContentType.FORMAT_ADDRESS).selectionMenuHidden(true)
      }


      Button('保存')
        .onClick(() => {
          if (!this.isClicked) {
            // 主动触发保存历史表单输入。
            try {
              autoFillManager.requestAutoSave(this.getUIContext())
            } catch (err) {
              let e: BusinessError = err as BusinessError;
              hilog.error(0x0000, 'DemoTest', 'error: %{public}d %{public}s', e.code, e.message);
            }
            this.isClicked = true;
            // 设置超时时间以防止重复点击按钮保存历史表单输入。
            setTimeout(() => {
              this.isClicked = false;
            }, 1000)
            // 或者通过路由跳转其他页面触发保存历史表单输入。
            this.getUIContext().getRouter().pushUrl({
              url: 'xxx'
            })
          }
        })
        .width("50%")
    }
    .alignItems(HorizontalAlign.Center)
    .height('100%')
    .width('100%')
  }
}
说明

智能填充在页面发生跳转的时候，或者手动触发保存逻辑的时候，方可触发保存表单逻辑。

剪贴板文本内容识别功能现已实现超过90%的准确率。尽管如此，我们认识到在特定场景下仍可能出现识别误差。为了提升填表数据的准确性，我们建议在关键环节引入增强校验。这些校验措施包括但不限于：

格式校验：自动检测输入格式，确保数据符合预设标准。
确认提示：在提交前通过弹窗提示用户再次确认信息，避免输入错误。

若在页面中也提供了弹窗提醒填充建议的功能，为避免弹窗冲突，建议将对应输入组件的enableAutoFill属性设置为"false"以关闭智能填充功能。

智能填充概述
动态修改ContentType值
