# 操作错误场景

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-operation-error_

Radio({ value: 'Radio1', group: 'radioGroup' }).checked(true)
              .radioStyle({
                checkedBackgroundColor: Color.Red
              })
              .height(50)
              .width(50)
              .onChange((isChecked: boolean) => {
                console.log('Radio1 status is ' + isChecked)
              })
            Text('Connection interrupted').fontColor(Color.Red)
          }.width('80%')
          .accessibilityGroup(true) //将单选和文本合并到单个对象中
        }
        .width('100%')
        .height('100%')
        .backgroundColor(Color.White)
      }
    }.title(this.title)
  }
}
控件状态变化场景
多语种场景
