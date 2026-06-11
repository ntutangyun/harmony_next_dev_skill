# 保存用户文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/save-user-file_

在从网络下载文件到本地或将已有用户文件另存为新的文件路径等场景下，需要使用FilePicker提供的保存用户文件的能力。需关注以下关键点：

权限说明

通过Picker获取的URI默认只具备临时读写权限，临时授权在应用退出后台自动失效。

如果设置autoCreateEmptyFile参数为false，获取的URI除了具备临时读写权限外，还具备临时创建和删除权限。

获取持久化权限需要通过FilePicker设置永久授权方式获取。

使用Picker对音频、图片、视频、文档类文件的保存操作无需申请权限。

系统隔离说明

通过Picker保存的文件存储在用户指定的目录。此类文件与图库管理的资源隔离，无法在图库中看到。

若开发者需要保存图片、视频资源到图库，可使用用户无感的安全控件进行保存。

保存图片或视频类文件

PhotoViewPicker在后续版本不再演进，建议使用Media Library Kit（媒体文件管理服务）中能力来保存媒体库资源。

如果开发场景无法调用安全控件进行图片、视频保存，可使用相册管理模块PhotoAccessHelper.showAssetsCreationDialog接口进行保存操作。

保存文档类文件

模块导入。

import { picker } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

根据实际业务需求配置文件保存选项。以下代码仅例举各选项的配置参考。

// 创建文件管理器选项实例。
const documentSaveOptions = new picker.DocumentSaveOptions();
// 保存文件名（可选）。 默认为空。
documentSaveOptions.newFileNames = ["DocumentViewPicker01.txt"];
// 指定保存的文件或者目录的URI（可选）。
documentSaveOptions.defaultFilePathUri = "file://docs/storage/Users/currentUser/test";
// 保存文件类型['后缀类型描述|后缀类型'],选择所有文件：'所有文件(*.*)|.*'（可选） ，如果选择项存在多个后缀（最多限制100个过滤后缀），默认选择第一个。如果不传该参数，默认无过滤后缀。
documentSaveOptions.fileSuffixChoices = ['文档|.txt', '.pdf'];
// 保存文件时，由应用决定是否预置空文件。默认为true，Picker会预置空文件并且返回文件的URI数组。false不预置空文件，只会返回文件的URI数组。
documentSaveOptions.autoCreateEmptyFile = false;

创建文件选择器DocumentViewPicker实例。调用save()接口拉起FilePicker界面进行文件保存。

let uris: string[] = [];
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
const documentViewPicker = new picker.DocumentViewPicker(context);
documentViewPicker.save(documentSaveOptions).then((documentSaveResult: string[]) => {
  uris = documentSaveResult;
  console.info('documentViewPicker.save to file succeed and uris are:' + uris);
  // ···
}).catch((err: BusinessError) => {
  console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
});

注意

Picker会默认预置空文件并返回保存文件的URI数组，应用拿到URI后可使用文件管理模块的接口进行文件读写操作。

避免在Picker回调中直接操作URI。

建议使用全局变量保存URI以供后续使用。

可以通过DOWNLOAD模式直达下载目录。

待界面从FilePicker返回后，使用fileIo.openSync接口，通过URI打开这个文件得到文件描述符（fd）。

if (uris.length > 0) {
   let uri: string = uris[0];
   // 这里需要注意接口权限参数是fileIo.OpenMode.READ_WRITE。
   let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
   console.info('file fd: ' + file.fd);
}

通过（fd）使用fileIo.writeSync接口对这个文件进行编辑修改，编辑修改完成后关闭（fd）。

let writeLen: number = fileIo.writeSync(file.fd, 'hello, world');
console.info('write data to file succeed and size is:' + writeLen);
fileIo.closeSync(file);

保存音频类文件

模块导入。

import { picker } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

配置保存选项。

const audioSaveOptions = new picker.AudioSaveOptions();
// 保存文件名（可选）
audioSaveOptions.newFileNames = ['AudioViewPicker01.mp3'];

创建音频选择器AudioViewPicker实例。调用save()接口拉起FilePicker界面进行文件保存。

let uris: string[] = [];
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
const audioViewPicker = new picker.AudioViewPicker(context);
audioViewPicker.save(audioSaveOptions).then((audioSelectResult: string[]) => {
  uris = audioSelectResult;
  console.info('audioViewPicker.save to file succeed and uri is:' + uris);
  // ···
}).catch((err: BusinessError) => {
  console.error(`Invoke audioViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
});

注意

Picker会默认预置空文件并返回保存文件的URI数组，应用拿到URI后可使用文件管理模块的接口进行文件读写操作。

避免在Picker回调中直接操作URI。

建议使用全局变量保存URI以供后续使用。

可以通过DOWNLOAD模式直达下载目录。

待界面从FilePicker返回后，可以使用fileIo.openSync接口，通过URI打开这个文件得到文件描述符（fd）。

if (uris.length > 0) {
   let uri: string = uris[0];
   // 这里需要注意接口权限参数是fileIo.OpenMode.READ_WRITE。
   let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
   console.info('file fd: ' + file.fd);
}

通过（fd）使用fileIo.writeSync接口对这个文件进行编辑修改，编辑修改完成后关闭（fd）。

let writeLen = fileIo.writeSync(file.fd, 'hello, world');
console.info('write data to file succeed and size is:' + writeLen);
fileIo.closeSync(file);

DOWNLOAD模式保存文件

模式特点

自动创建在Download/包名/目录。

跳过文件选择界面直接保存。

返回的URI已具备持久化权限， 用户可在该URI下创建文件。

注意

DOWNLOAD模式创建的目录仅用于保存文件，目录之间无访问隔离，不建议保存应用敏感数据。

模块导入。

import { fileUri, picker } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

配置下载模式。

const documentSaveOptions = new picker.DocumentSaveOptions();
// 配置保存的模式为DOWNLOAD，若配置了DOWNLOAD模式，此时配置的其他documentSaveOptions参数将不会生效。
documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;

保存到下载目录。

let uri: string = '';
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
const documentViewPicker = new picker.DocumentViewPicker(context);
const documentSaveOptions = new picker.DocumentSaveOptions();
documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
  uri = documentSaveResult[0];
  console.info('documentViewPicker.save succeed and uri is:' + uri);
  const testFilePath = new fileUri.FileUri(uri + '/test.txt').path;
  const file = fileIo.openSync(testFilePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  fileIo.writeSync(file.fd, 'Hello World!');
  fileIo.closeSync(file.fd);
}).catch((err: BusinessError) => {
  console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
})

## Code blocks

### Code block 1

```
import { picker } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
```

### Code block 2

```
// 创建文件管理器选项实例。
const documentSaveOptions = new picker.DocumentSaveOptions();
// 保存文件名（可选）。 默认为空。
documentSaveOptions.newFileNames = ["DocumentViewPicker01.txt"];
// 指定保存的文件或者目录的URI（可选）。
documentSaveOptions.defaultFilePathUri = "file://docs/storage/Users/currentUser/test";
// 保存文件类型['后缀类型描述|后缀类型'],选择所有文件：'所有文件(*.*)|.*'（可选） ，如果选择项存在多个后缀（最多限制100个过滤后缀），默认选择第一个。如果不传该参数，默认无过滤后缀。
documentSaveOptions.fileSuffixChoices = ['文档|.txt', '.pdf'];
// 保存文件时，由应用决定是否预置空文件。默认为true，Picker会预置空文件并且返回文件的URI数组。false不预置空文件，只会返回文件的URI数组。
documentSaveOptions.autoCreateEmptyFile = false;
```

### Code block 3

```
let uris: string[] = [];
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
const documentViewPicker = new picker.DocumentViewPicker(context);
documentViewPicker.save(documentSaveOptions).then((documentSaveResult: string[]) => {
  uris = documentSaveResult;
  console.info('documentViewPicker.save to file succeed and uris are:' + uris);
  // ···
}).catch((err: BusinessError) => {
  console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
});
```

### Code block 4

```
if (uris.length > 0) {
   let uri: string = uris[0];
   // 这里需要注意接口权限参数是fileIo.OpenMode.READ_WRITE。
   let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
   console.info('file fd: ' + file.fd);
}
```

### Code block 5

```
let writeLen: number = fileIo.writeSync(file.fd, 'hello, world');
console.info('write data to file succeed and size is:' + writeLen);
fileIo.closeSync(file);
```

### Code block 6

```
import { picker } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
```

### Code block 7

```
const audioSaveOptions = new picker.AudioSaveOptions();
// 保存文件名（可选）
audioSaveOptions.newFileNames = ['AudioViewPicker01.mp3'];
```

### Code block 8

```
let uris: string[] = [];
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
const audioViewPicker = new picker.AudioViewPicker(context);
audioViewPicker.save(audioSaveOptions).then((audioSelectResult: string[]) => {
  uris = audioSelectResult;
  console.info('audioViewPicker.save to file succeed and uri is:' + uris);
  // ···
}).catch((err: BusinessError) => {
  console.error(`Invoke audioViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
});
```

### Code block 9

```
if (uris.length > 0) {
   let uri: string = uris[0];
   // 这里需要注意接口权限参数是fileIo.OpenMode.READ_WRITE。
   let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
   console.info('file fd: ' + file.fd);
}
```

### Code block 10

```
let writeLen = fileIo.writeSync(file.fd, 'hello, world');
console.info('write data to file succeed and size is:' + writeLen);
fileIo.closeSync(file);
```

### Code block 11

```
import { fileUri, picker } from '@kit.CoreFileKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
```

### Code block 12

```
const documentSaveOptions = new picker.DocumentSaveOptions();
// 配置保存的模式为DOWNLOAD，若配置了DOWNLOAD模式，此时配置的其他documentSaveOptions参数将不会生效。
documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
```

### Code block 13

```
let uri: string = '';
// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
const documentViewPicker = new picker.DocumentViewPicker(context);
const documentSaveOptions = new picker.DocumentSaveOptions();
documentSaveOptions.pickerMode = picker.DocumentPickerMode.DOWNLOAD;
documentViewPicker.save(documentSaveOptions).then((documentSaveResult: Array<string>) => {
  uri = documentSaveResult[0];
  console.info('documentViewPicker.save succeed and uri is:' + uri);
  const testFilePath = new fileUri.FileUri(uri + '/test.txt').path;
  const file = fileIo.openSync(testFilePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
  fileIo.writeSync(file.fd, 'Hello World!');
  fileIo.closeSync(file.fd);
}).catch((err: BusinessError) => {
  console.error(`Invoke documentViewPicker.save failed, code is ${err.code}, message is ${err.message}`);
})
```
