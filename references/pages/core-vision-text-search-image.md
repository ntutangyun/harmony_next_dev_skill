# 通过文本搜索图片

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-text-search-image_

适用场景

从26.0.0版本开始，新增通过文本搜索图片的能力，支持基于文本语义对图片进行检索。用户可以通过输入文本语意，从图片库中搜索匹配的图像结果。该服务适用于图片检索、相册管理、内容推荐等场景。

开发步骤

将实现文本搜索图片相关的工具和依赖导入工程。

import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

在aboutToAppear中调用textSearchImage.init()初始化文本搜索图片分析器服务，在aboutToDisappear中调用textSearchImage.release()释放资源。

async aboutToAppear(): Promise<void> {
  const initResult = await textSearchImage.init();
  hilog.info(0x0000, 'textSearchImageSample', `Text search image initialization result:${initResult}`);
}

async aboutToDisappear(): Promise<void> {
  await textSearchImage.release();
  hilog.info(0x0000, 'textSearchImageSample', 'Text search image released successfully');
}

调用textSearchImage.insertImage方法，将图片特征插入数据库。

async insertImageToDatabase(imagePath: string, scope: string): Promise<void> {
  try {
    const result = await textSearchImage.insertImage(imagePath, scope);
    hilog.info(0x0000, 'textSearchImageSample', `Insert image result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Insert image failed. Code: ${err.code}, message: ${err.message}`);
  }
}

调用textSearchImage.search方法，获取匹配的图像结果。

async searchImages(query: string, scope: string, topKey: number = 100): Promise<void> {
  try {
    const results = await textSearchImage.search(query, scope, topKey);
    hilog.info(0x0000, 'textSearchImageSample', `Search results count: ${results.length}`);
    results.forEach((imageObject, index) => {
      hilog.info(0x0000, 'textSearchImageSample', `Result ${index}: imagePath=${imageObject.imagePath}, similarity=${imageObject.similarity}`);
    });
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Search failed. Code: ${err.code}, message: ${err.message}`);
  }
}

调用textSearchImage.deleteImage方法，从数据库中删除指定的图片数据。

async deleteImageFromDatabase(imagePath: string, scope: string): Promise<void> {
  try {
    const result = await textSearchImage.deleteImage(imagePath, scope);
    hilog.info(0x0000, 'textSearchImageSample', `Delete image result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Delete image failed. Code: ${err.code}, message: ${err.message}`);
  }
}

调用textSearchImage.clearData方法，清除数据库中的所有数据。

async clearAllData(): Promise<void> {
  try {
    const result = await textSearchImage.clearData();
    hilog.info(0x0000, 'textSearchImageSample', `Clear data result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Clear data failed. Code: ${err.code}, message: ${err.message}`);
  }
}

开发实例

[h2]Index.ets

import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State searchQuery: string = '';
  @State scope: string = 'default_scope';
  @State resultMessage: string = '';

  async aboutToAppear(): Promise<void> {
    const initResult = await textSearchImage.init();
    hilog.info(0x0000, 'textSearchImageSample', `Text search image initialization result:${initResult}`);
  }

  async aboutToDisappear(): Promise<void> {
    await textSearchImage.release();
    hilog.info(0x0000, 'textSearchImageSample', 'Text search image released successfully');
  }

  build() {
    Column() {
      Text('Text Search Image Sample')
        .fontSize(24)
        .margin(10)

      TextInput({ placeholder: 'Enter image path' })
        .width('80%')
        .margin(10)
        .onChange((value: string) => {
          this.searchQuery = value;
        })

      TextInput({ placeholder: 'Enter scope' })
        .width('80%')
        .margin(10)
        .onChange((value: string) => {
          this.scope = value;
        })

      Button('Insert Image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.insertImageToDatabase();
        })

      Button('Search Images')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.searchImages();
        })

      Button('Delete Image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.deleteImageFromDatabase();
        })

      Button('Clear All Data')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.clearAllData();
        })

      Text(this.resultMessage)
        .copyOption(CopyOptions.LocalDevice)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async insertImageToDatabase(): Promise<void> {
    try {
      const result = await textSearchImage.insertImage(this.searchQuery, this.scope);
      this.resultMessage = `Insert image result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Insert image result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Insert image failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Insert image failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async searchImages(): Promise<void> {
    try {
      const results = await textSearchImage.search(this.searchQuery, this.scope, 100);
      this.resultMessage = `Search results count: ${results.length}`;
      hilog.info(0x0000, 'textSearchImageSample', `Search results count: ${results.length}`);
      results.forEach((imageObject, index) => {
        hilog.info(0x0000, 'textSearchImageSample', `Result ${index}: imagePath=${imageObject.imagePath}, similarity=${imageObject.similarity}`);
      });
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Search failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Search failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async deleteImageFromDatabase(): Promise<void> {
    try {
      const result = await textSearchImage.deleteImage(this.searchQuery, this.scope);
      this.resultMessage = `Delete image result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Delete image result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Delete image failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Delete image failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async clearAllData(): Promise<void> {
    try {
      const result = await textSearchImage.clearData();
      this.resultMessage = `Clear data result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Clear data result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Clear data failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Clear data failed. Code: ${err.code}, message: ${err.message}`);
    }
  }
}

## Code blocks

### Code block 1

```
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
async aboutToAppear(): Promise<void> {
  const initResult = await textSearchImage.init();
  hilog.info(0x0000, 'textSearchImageSample', `Text search image initialization result:${initResult}`);
}

async aboutToDisappear(): Promise<void> {
  await textSearchImage.release();
  hilog.info(0x0000, 'textSearchImageSample', 'Text search image released successfully');
}
```

### Code block 3

```
async insertImageToDatabase(imagePath: string, scope: string): Promise<void> {
  try {
    const result = await textSearchImage.insertImage(imagePath, scope);
    hilog.info(0x0000, 'textSearchImageSample', `Insert image result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Insert image failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### Code block 4

```
async searchImages(query: string, scope: string, topKey: number = 100): Promise<void> {
  try {
    const results = await textSearchImage.search(query, scope, topKey);
    hilog.info(0x0000, 'textSearchImageSample', `Search results count: ${results.length}`);
    results.forEach((imageObject, index) => {
      hilog.info(0x0000, 'textSearchImageSample', `Result ${index}: imagePath=${imageObject.imagePath}, similarity=${imageObject.similarity}`);
    });
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Search failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### Code block 5

```
async deleteImageFromDatabase(imagePath: string, scope: string): Promise<void> {
  try {
    const result = await textSearchImage.deleteImage(imagePath, scope);
    hilog.info(0x0000, 'textSearchImageSample', `Delete image result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Delete image failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### Code block 6

```
async clearAllData(): Promise<void> {
  try {
    const result = await textSearchImage.clearData();
    hilog.info(0x0000, 'textSearchImageSample', `Clear data result: ${result}`);
  } catch (error) {
    const err = error as BusinessError;
    hilog.error(0x0000, 'textSearchImageSample', `Clear data failed. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### Code block 7

```
import { textSearchImage } from '@kit.CoreVisionKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State searchQuery: string = '';
  @State scope: string = 'default_scope';
  @State resultMessage: string = '';

  async aboutToAppear(): Promise<void> {
    const initResult = await textSearchImage.init();
    hilog.info(0x0000, 'textSearchImageSample', `Text search image initialization result:${initResult}`);
  }

  async aboutToDisappear(): Promise<void> {
    await textSearchImage.release();
    hilog.info(0x0000, 'textSearchImageSample', 'Text search image released successfully');
  }

  build() {
    Column() {
      Text('Text Search Image Sample')
        .fontSize(24)
        .margin(10)

      TextInput({ placeholder: 'Enter image path' })
        .width('80%')
        .margin(10)
        .onChange((value: string) => {
          this.searchQuery = value;
        })

      TextInput({ placeholder: 'Enter scope' })
        .width('80%')
        .margin(10)
        .onChange((value: string) => {
          this.scope = value;
        })

      Button('Insert Image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.insertImageToDatabase();
        })

      Button('Search Images')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.searchImages();
        })

      Button('Delete Image')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.deleteImageFromDatabase();
        })

      Button('Clear All Data')
        .type(ButtonType.Capsule)
        .fontColor(Color.White)
        .alignSelf(ItemAlign.Center)
        .width('80%')
        .margin(10)
        .onClick(() => {
          void this.clearAllData();
        })

      Text(this.resultMessage)
        .copyOption(CopyOptions.LocalDevice)
        .margin(10)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }

  private async insertImageToDatabase(): Promise<void> {
    try {
      const result = await textSearchImage.insertImage(this.searchQuery, this.scope);
      this.resultMessage = `Insert image result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Insert image result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Insert image failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Insert image failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async searchImages(): Promise<void> {
    try {
      const results = await textSearchImage.search(this.searchQuery, this.scope, 100);
      this.resultMessage = `Search results count: ${results.length}`;
      hilog.info(0x0000, 'textSearchImageSample', `Search results count: ${results.length}`);
      results.forEach((imageObject, index) => {
        hilog.info(0x0000, 'textSearchImageSample', `Result ${index}: imagePath=${imageObject.imagePath}, similarity=${imageObject.similarity}`);
      });
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Search failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Search failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async deleteImageFromDatabase(): Promise<void> {
    try {
      const result = await textSearchImage.deleteImage(this.searchQuery, this.scope);
      this.resultMessage = `Delete image result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Delete image result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Delete image failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Delete image failed. Code: ${err.code}, message: ${err.message}`);
    }
  }

  private async clearAllData(): Promise<void> {
    try {
      const result = await textSearchImage.clearData();
      this.resultMessage = `Clear data result: ${result}`;
      hilog.info(0x0000, 'textSearchImageSample', `Clear data result: ${result}`);
    } catch (error) {
      const err = error as BusinessError;
      this.resultMessage = `Clear data failed. Code: ${err.code}, message: ${err.message}`;
      hilog.error(0x0000, 'textSearchImageSample', `Clear data failed. Code: ${err.code}, message: ${err.message}`);
    }
  }
}
```
