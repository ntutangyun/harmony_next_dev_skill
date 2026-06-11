# 修改翻页方式、字体大小及行间距

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/reader-setting-other_

当应用需要支持修改默认的翻页方式、字体大小、行间距时，开发者可通过ReaderSetting的flipMode、fontSize、lineHeight属性，实现对翻页方式、字体大小、行间距的实时修改。

接口说明

修改翻页方式、字体大小及行间距主要涉及1个接口，具体介绍如下表所示。

接口名	描述
setPageConfig(pageConfig: ReaderSetting): void	设置或者修改页面排版属性。

开发准备

在修改翻页方式、字体大小及行间距之前，请先确保已经“构建阅读器”。

开发步骤

修改翻页方式。

this.readerSetting.flipMode = '1'; // 0代表仿真翻页，1代表横滑翻页

修改字体大小。

this.readerSetting.fontSize = 20;

修改行间距。

this.readerSetting.lineHeight = 2;

调用ReaderComponentController组件控制器的setPageConfig接口，重新渲染界面。

this.readerComponentController.setPageConfig(this.readerSetting);

## Code blocks

### Code block 1

```
this.readerSetting.flipMode = '1'; // 0代表仿真翻页，1代表横滑翻页
```

### Code block 2

```
this.readerSetting.fontSize = 20;
```

### Code block 3

```
this.readerSetting.lineHeight = 2;
```

### Code block 4

```
this.readerComponentController.setPageConfig(this.readerSetting);
```
