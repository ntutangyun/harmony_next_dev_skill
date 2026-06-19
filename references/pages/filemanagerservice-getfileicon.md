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

@Entry
@Component
struct Index {
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      // 1、根据文件的后缀名，获取后缀名对应文件类型的UTD-ID
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      // 2、调用getFileIconSync方法，根据UTD-ID获取对应的文件图标
      this.fileIcon = fileManagerService.getFileIconSync(typeId);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })
        Button('Update FileIcon')
          .onClick(() => {
            // 以txt格式为例
            this.getFileIconByFileExtension('.txt');
          })
      }
    }
    .height('100%')
    .width('100%')
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
@Entry
@Component
struct Index {
  @State fileIcon: string | Resource = '';

  private getFileIconByFileExtension(filenameExtension: string): void {
    try {
      // 1、根据文件的后缀名，获取后缀名对应文件类型的UTD-ID
      let typeId: string = uniformTypeDescriptor.getUniformDataTypeByFilenameExtension(filenameExtension);
      // 2、调用getFileIconSync方法，根据UTD-ID获取对应的文件图标
      this.fileIcon = fileManagerService.getFileIconSync(typeId);
    } catch (error) {
      let err: BusinessError = error as BusinessError;
      console.error('getFileIconByFileExtension failed with err: ' + JSON.stringify(err));
    }
  }

  build() {
    RelativeContainer() {
      Column() {
        Image(this.fileIcon)
          .height(88)
          .border({ width: 1, radius: 6 })
        Button('Update FileIcon')
          .onClick(() => {
            // 以txt格式为例
            this.getFileIconByFileExtension('.txt');
          })
      }
    }
    .height('100%')
    .width('100%')
  }
}
```
