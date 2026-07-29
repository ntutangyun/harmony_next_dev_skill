# 获取文件图标

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/filemanagerservice-getfileicon_

场景介绍

根据文件类型获取对应的文件图标。

接口说明

接口名	描述
getFileIconSync(fileType: string): string | Resource	根据文件类型获取文件图标。
getFileIcon(fileType: string): Promise<string | Resource>	根据文件类型获取文件图标。使用Promise异步回调。

示例代码

1.导入文件管理服务模块及相关模块。

import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';

2.申请权限。使用获取文件图标接口时，需要在module.json5中声明申请接口所需的权限：ohos.permission.GET_FILE_ICON。具体指导可见声明权限。

3.获取文件图标。

@Component
export struct GetFileIcon {
  @State inputText: string = ''
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      // 根据文件的后缀名，获取后缀名对应文件类型的UTD-ID
      // filenameExtension为文件后缀，以txt文件为例，filenameExtension可以输入为：“.txt”
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      // 调用getFileIconSync方法，根据UTD-ID获取对应的文件图标
      this.fileIcon = fileManagerService.getFileIconSync(typeId);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }
  }

  build() {
    NavDestination() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })

        TextInput({ placeholder: '请输入文件后缀名', text: $$this.inputText })
          .width('85%')
          .height(50)
          .borderRadius(8)
          .padding(12)

        Button('获取文件图标')
          .width('60%')
          .height(48)
          .type(ButtonType.Capsule)
          .onClick(() => {
            this.getFileIconByFileExtension(this.inputText);
          })
        Blank()
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.White)
    }
    .width('100%')
    .height('100%')
  }
}

## Code blocks

### Code block 1

```
import { fileManagerService } from '@kit.FileManagerServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { uniformTypeDescriptor } from '@kit.ArkData';
```

### Code block 2

```
@Component
export struct GetFileIcon {
  @State inputText: string = ''
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      // 根据文件的后缀名，获取后缀名对应文件类型的UTD-ID
      // filenameExtension为文件后缀，以txt文件为例，filenameExtension可以输入为：“.txt”
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      // 调用getFileIconSync方法，根据UTD-ID获取对应的文件图标
      this.fileIcon = fileManagerService.getFileIconSync(typeId);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }
  }

  build() {
    NavDestination() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })

        TextInput({ placeholder: '请输入文件后缀名', text: $$this.inputText })
          .width('85%')
          .height(50)
          .borderRadius(8)
          .padding(12)

        Button('获取文件图标')
          .width('60%')
          .height(48)
          .type(ButtonType.Capsule)
          .onClick(() => {
            this.getFileIconByFileExtension(this.inputText);
          })
        Blank()
      }
      .width('100%')
      .height('100%')
      .backgroundColor(Color.White)
    }
    .width('100%')
    .height('100%')
  }
}
```
