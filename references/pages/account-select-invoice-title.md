# 获取发票抬头

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-select-invoice-title_

场景介绍

当应用需要获取用户发票抬头时，可使用Account Kit提供的发票助手能力，打开发票抬头选择页面，帮助用户快速选择或管理发票抬头。以下对Account Kit提供的发票助手能力进行介绍，获取发票抬头功能还可使用场景化控件选择发票抬头Button进行实现。

约束与限制

Wearable、TV设备暂不支持使用获取发票抬头功能。

业务流程

流程说明：

用户需要使用发票抬头时，应用程序调用选择发票抬头API，打开华为账号发票抬头选择页。

用户可以在发票抬头选择页选择已有发票抬头或者跳转到发票抬头管理页进行增加，点击确认后可将选择的发票抬头返回给应用。

接口说明

获取发票抬头关键接口如下表所示，具体API说明详见API参考。

接口名	描述
selectInvoiceTitle(context: common.Context): Promise<InvoiceTitle>	调用该方法打开发票抬头选择页面，使用Promise异步回调返回选择的发票抬头。

注意

上述接口需在页面或自定义组件生命周期内调用。

开发前提

在进行代码开发前，请确保已按照“开发准备”章节中的指导完成配置签名和指纹、配置Client ID。此场景无需申请账号权限。

开发步骤

导入invoiceAssistant模块及相关公共模块。

import { hilog } from '@kit.PerformanceAnalysisKit';
import { invoiceAssistant } from '@kit.AccountKit';
import { BusinessError } from '@kit.BasicServicesKit';

调用selectInvoiceTitle方法选择发票抬头页面。

try {
  if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
    invoiceAssistant.selectInvoiceTitle(context).then((data: invoiceAssistant.InvoiceTitle) => {
      // ...
    }).catch((error: BusinessError) => {
      hilog.error(domainId, logTag,
        `Failed to selectInvoiceTitle. BusinessError errCode: ${error.code}, errMessage: ${error.message}`);
    });
  } else {
    hilog.error(domainId, logTag, 'The API is not supported on this device.');
  }
} catch (error) {
  hilog.error(domainId, logTag,
    `Failed to selectInvoiceTitle. errCode: ${error.code}, errMessage: ${error.message}`);
}

## Code blocks

### Code block 1

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { invoiceAssistant } from '@kit.AccountKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
try {
  if (canIUse('SystemCapability.HuaweiID.InvoiceAssistant')) {
    invoiceAssistant.selectInvoiceTitle(context).then((data: invoiceAssistant.InvoiceTitle) => {
      // ...
    }).catch((error: BusinessError) => {
      hilog.error(domainId, logTag,
        `Failed to selectInvoiceTitle. BusinessError errCode: ${error.code}, errMessage: ${error.message}`);
    });
  } else {
    hilog.error(domainId, logTag, 'The API is not supported on this device.');
  }
} catch (error) {
  hilog.error(domainId, logTag,
    `Failed to selectInvoiceTitle. errCode: ${error.code}, errMessage: ${error.message}`);
}
```
