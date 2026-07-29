# 自定义界面扫码如何增加重试机制

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-17_

问题现象

调用init成功后，调用start启动相机流时抛出1000500001内部错误。

解决措施

可以尝试增加扫码相机流重试机制。

先暂停并释放相机流（stop、release），再重启相机流（init、start）。

示例代码（仅供参考）：

import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan, scanBarcode, scanCore } from '@kit.ScanKit';

const MAX_RETRY_SCAN_TIMES: number = 3; // 扫码重试最大次数，根据应用实际需求设置
const DELAY_RETRY_SCAN_TIME: number = 100; // 重试延时，根据应用实际需求设置

export class ScanService {
  private retryScanTimes: number = 0; // 重试次数

  // customScan的start接口callback回调，可调用此函数根据错误信息判断是否重试。
  private retryOnCondition(error: BusinessError, options: scanBarcode.ScanOptions,
    viewControl: customScan.ViewControl): boolean {
    if (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `An error is returned during customScanCallback. Code: ${error.code}, message: ${error.message}`);
      // 出现1000500001内部错误并且重试次数没超过设置的最大重试次数时触发重启相机流
      if (this.retryScanTimes < MAX_RETRY_SCAN_TIMES && error.code === scanCore.ScanErrorCode.INTERNAL_ERROR) {
        this.retryScanTimes++;
        let timeId = setTimeout(async () => {
          hilog.info(0x0001, '[Scan Sample]',
            `Retry preview stream by customScanCallback. Times: ${this.retryScanTimes}.`);
          await this.stopPreviewStream();
          this.startPreviewStream(options, viewControl);
          hilog.info(0x0001, '[Scan Sample]', 'Retry preview stream end.');
          clearTimeout(timeId);
        }, DELAY_RETRY_SCAN_TIME);
        return true; // 重试
      }
    }
    return false; // 不重试
  }

  // 暂停并释放相机预览流
  public async stopPreviewStream(): Promise<void> {
    hilog.info(0x0001, '[Scan Sample]', 'Stop Preview Stream start.');
    await this.stopCustomScan();
    this.resetRetryScanTimes();
    await this.releaseCustomScan();
    hilog.info(0x0001, '[Scan Sample]', 'Stop Preview Stream end.');
  }

  // 初始化并启动自定义界面扫码
  public startPreviewStream(options: scanBarcode.ScanOptions, viewControl: customScan.ViewControl) {
    hilog.info(0x0001, '[Scan Sample]', 'Start Preview Stream.');
    this.initCustomScan(options);
    this.startCustomScan(options, viewControl);
    hilog.info(0x0001, '[Scan Sample]', 'Start Preview Stream end.');
  }

  // 初始化自定义界面扫码
  private initCustomScan(options: scanBarcode.ScanOptions) {
    try {
      hilog.info(0x0001, '[Scan Sample]', 'Init customScan start.');
      customScan.init(options);
      hilog.info(0x0001, '[Scan Sample]', 'Init customScan end.');
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to init customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 启动自定义界面扫码
  private startCustomScan(options: scanBarcode.ScanOptions, viewControl: customScan.ViewControl): void {
    try {
      hilog.info(0x0001, '[Scan Sample]', `Start customScan start. ${JSON.stringify(viewControl)}`);
      customScan.start(viewControl, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
        if (this.retryOnCondition(err, options, viewControl)) {
          return;
        }
        hilog.info(0x0001, '[Scan Sample]',
          `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
        // 从data获取扫码结果并进行业务处理
        // ...
      });
      hilog.info(0x0001, '[Scan Sample]', 'Start customScan end.');
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to start customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 暂停相机预览流
  private async stopCustomScan(): Promise<void> {
    try {
      hilog.info(0x0001, '[Scan Sample]', 'Stop customScan start.');
      await customScan.stop();
      hilog.info(0x0001, '[Scan Sample]', 'Stop customScan end.');
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to stop customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 释放相机预览流
  private async releaseCustomScan(): Promise<void> {
    try {
      hilog.info(0x0001, '[Scan Sample]', 'Release customScan start.');
      await customScan.release();
      hilog.info(0x0001, '[Scan Sample]', 'Release customScan end.');
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to release customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 重置重试次数
  resetRetryScanTimes(): void {
    hilog.info(0x0001, '[Scan Sample]', 'Reset retry scan times.');
    this.retryScanTimes = 0;
  }
}

## Code blocks

### Code block 1

```
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan, scanBarcode, scanCore } from '@kit.ScanKit';

const MAX_RETRY_SCAN_TIMES: number = 3; // 扫码重试最大次数，根据应用实际需求设置
const DELAY_RETRY_SCAN_TIME: number = 100; // 重试延时，根据应用实际需求设置

export class ScanService {
  private retryScanTimes: number = 0; // 重试次数

  // customScan的start接口callback回调，可调用此函数根据错误信息判断是否重试。
  private retryOnCondition(error: BusinessError, options: scanBarcode.ScanOptions,
    viewControl: customScan.ViewControl): boolean {
    if (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `An error is returned during customScanCallback. Code: ${error.code}, message: ${error.message}`);
      // 出现1000500001内部错误并且重试次数没超过设置的最大重试次数时触发重启相机流
      if (this.retryScanTimes < MAX_RETRY_SCAN_TIMES && error.code === scanCore.ScanErrorCode.INTERNAL_ERROR) {
        this.retryScanTimes++;
        let timeId = setTimeout(async () => {
          hilog.info(0x0001, '[Scan Sample]',
            `Retry preview stream by customScanCallback. Times: ${this.retryScanTimes}.`);
          await this.stopPreviewStream();
          this.startPreviewStream(options, viewControl);
          hilog.info(0x0001, '[Scan Sample]', 'Retry preview stream end.');
          clearTimeout(timeId);
        }, DELAY_RETRY_SCAN_TIME);
        return true; // 重试
      }
    }
    return false; // 不重试
  }

  // 暂停并释放相机预览流
  public async stopPreviewStream(): Promise<void> {
    hilog.info(0x0001, '[Scan Sample]', 'Stop Preview Stream start.');
    await this.stopCustomScan();
    this.resetRetryScanTimes();
    await this.releaseCustomScan();
    hilog.info(0x0001, '[Scan Sample]', 'Stop Preview Stream end.');
  }

  // 初始化并启动自定义界面扫码
  public startPreviewStream(options: scanBarcode.ScanOptions, viewControl: customScan.ViewControl) {
    hilog.info(0x0001, '[Scan Sample]', 'Start Preview Stream.');
    this.initCustomScan(options);
    this.startCustomScan(options, viewControl);
    hilog.info(0x0001, '[Scan Sample]', 'Start Preview Stream end.');
  }

  // 初始化自定义界面扫码
  private initCustomScan(options: scanBarcode.ScanOptions) {
    try {
      hilog.info(0x0001, '[Scan Sample]', 'Init customScan start.');
      customScan.init(options);
      hilog.info(0x0001, '[Scan Sample]', 'Init customScan end.');
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to init customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 启动自定义界面扫码
  private startCustomScan(options: scanBarcode.ScanOptions, viewControl: customScan.ViewControl): void {
    try {
      hilog.info(0x0001, '[Scan Sample]', `Start customScan start. ${JSON.stringify(viewControl)}`);
      customScan.start(viewControl, (err: BusinessError, data: Array<scanBarcode.ScanResult>) => {
        if (this.retryOnCondition(err, options, viewControl)) {
          return;
        }
        hilog.info(0x0001, '[Scan Sample]',
          `Succeeded in getting ScanResult by callback, result is ${JSON.stringify(data)}`);
        // 从data获取扫码结果并进行业务处理
        // ...
      });
      hilog.info(0x0001, '[Scan Sample]', 'Start customScan end.');
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to start customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 暂停相机预览流
  private async stopCustomScan(): Promise<void> {
    try {
      hilog.info(0x0001, '[Scan Sample]', 'Stop customScan start.');
      await customScan.stop();
      hilog.info(0x0001, '[Scan Sample]', 'Stop customScan end.');
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to stop customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 释放相机预览流
  private async releaseCustomScan(): Promise<void> {
    try {
      hilog.info(0x0001, '[Scan Sample]', 'Release customScan start.');
      await customScan.release();
      hilog.info(0x0001, '[Scan Sample]', 'Release customScan end.');
    } catch (error) {
      hilog.error(0x0001, '[Scan Sample]',
        `Failed to release customScan. Code: ${error.code}, message: ${error.message}.`);
    }
  }

  // 重置重试次数
  resetRetryScanTimes(): void {
    hilog.info(0x0001, '[Scan Sample]', 'Reset retry scan times.');
    this.retryScanTimes = 0;
  }
}
```
