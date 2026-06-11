# 弹出框焦点策略

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-focusable_

ArkUI的弹出框焦点策略可以设定是否中断用户当前操作，并聚焦到新弹出的弹出框。若设定弹出框不获取焦点，则新弹出时不会中断用户当前操作，例如，当用户正在文本框中输入内容时，新弹出的弹出框不会关闭软键盘，焦点仍保留在文本框中。

从API version 19开始，可以通过设置focusable参数来管理弹出框是否获取焦点。

使用约束

openCustomDialog和CustomDialog支持通过focusable参数来管理弹出框是否获取焦点。

说明

只有弹出覆盖在当前窗口之上的弹出框才可以获取焦点。

创建不获取焦点的弹出框

说明

详细变量定义请参考完整示例。

初始化一个弹出框内容区域，内含一个Text组件。

@State dialogIdIndex: number = 0;
// 请在resources\base\element\string.json文件中配置name为'dialog_message'，value为非空字符串的资源
private message: string =
  this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('dialog_message') as string;

@Builder
customDialogComponent() {
  Column({ space: 5 }) {
    Text(this.message + this.dialogIdIndex)
      .fontSize(30)
  }
  .height(200)
  .padding(5)
  .justifyContent(FlexAlign.SpaceBetween)
}

创建一个TextInput组件，在onChange事件函数中通过调用UIContext中的getPromptAction方法获取PromptAction对象，再通过该对象调用openCustomDialog接口，并设置focusable参数为false，以创建弹出框。

TextInput()
  .onChange(() => {
    this.dialogIdIndex++;
    this.getUIContext().getPromptAction().openCustomDialog({
      builder: () => {
        this.customDialogComponent();
      },
      focusable: false
    }).then((dialogId: number) => {
      setTimeout(() => {
        this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
      }, 3000);
    });
  })

完整示例

当用户正在文本框中输入内容时，新弹出的弹出框不会关闭软键盘，焦点仍保留在文本框中。

@Entry
@Component
export struct Index {
  @State dialogIdIndex: number = 0;
  // 请在resources\base\element\string.json文件中配置name为'dialog_message'，value为非空字符串的资源
  private message: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('dialog_message') as string;

  @Builder
  customDialogComponent() {
    Column({ space: 5 }) {
      Text(this.message + this.dialogIdIndex)
        .fontSize(30)
    }
    .height(200)
    .padding(5)
    .justifyContent(FlexAlign.SpaceBetween)
  }


  build() {
    NavDestination() {
      Column({ space: 5 }) {
        TextInput()
          .onChange(() => {
            this.dialogIdIndex++;
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent();
              },
              focusable: false
            }).then((dialogId: number) => {
              setTimeout(() => {
                this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
              }, 3000);
            });
          })
      }.width('100%')
    }
  }
}

## Code blocks

### Code block 1

```
@State dialogIdIndex: number = 0;
// 请在resources\base\element\string.json文件中配置name为'dialog_message'，value为非空字符串的资源
private message: string =
  this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('dialog_message') as string;

@Builder
customDialogComponent() {
  Column({ space: 5 }) {
    Text(this.message + this.dialogIdIndex)
      .fontSize(30)
  }
  .height(200)
  .padding(5)
  .justifyContent(FlexAlign.SpaceBetween)
}
```

### Code block 2

```
TextInput()
  .onChange(() => {
    this.dialogIdIndex++;
    this.getUIContext().getPromptAction().openCustomDialog({
      builder: () => {
        this.customDialogComponent();
      },
      focusable: false
    }).then((dialogId: number) => {
      setTimeout(() => {
        this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
      }, 3000);
    });
  })
```

### Code block 3

```
@Entry
@Component
export struct Index {
  @State dialogIdIndex: number = 0;
  // 请在resources\base\element\string.json文件中配置name为'dialog_message'，value为非空字符串的资源
  private message: string =
    this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('dialog_message') as string;

  @Builder
  customDialogComponent() {
    Column({ space: 5 }) {
      Text(this.message + this.dialogIdIndex)
        .fontSize(30)
    }
    .height(200)
    .padding(5)
    .justifyContent(FlexAlign.SpaceBetween)
  }


  build() {
    NavDestination() {
      Column({ space: 5 }) {
        TextInput()
          .onChange(() => {
            this.dialogIdIndex++;
            this.getUIContext().getPromptAction().openCustomDialog({
              builder: () => {
                this.customDialogComponent();
              },
              focusable: false
            }).then((dialogId: number) => {
              setTimeout(() => {
                this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
              }, 3000);
            });
          })
      }.width('100%')
    }
  }
}
```
