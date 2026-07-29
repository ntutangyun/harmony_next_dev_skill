# 设置KIA文件水印图片

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-kia-watermark_

场景介绍

为应用提供设置KIA文件水印图片能力。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>	使用Promise方式设置KIA文件水印图片。

开发步骤

导入模块。

import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

初始化FileGuard对象guard，调用接口setKiaWatermarkImage，设置KIA文件水印图片。

const TAG: string = 'FileGuard_KIAWatermarkImage';
const DOMAIN: number = 0x0000;

/**
 * 设置KIA文件水印图片。使用Promise异步回调。
 */
async function testSetKiaWaterMarkImage() {
  let fd: number = -1;
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let imagePath: string = `/data/service/el2/test_water.png`;
    fd = await guard.openFile(imagePath);
    let stat: fileIo.Stat = fileIo.statSync(fd);
    let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
    fileIo.readSync(fd, buffer);

    let image: Uint8Array = new Uint8Array(buffer);
    let info: string = new Date().toLocaleString();
    guard.setKiaWatermarkImage(image, info).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in setting the watermark image for Kia file.`);
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.`);
    })
  } catch (e) {
    hilog.error(DOMAIN, TAG, `testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}`);
  } finally {
    if (fd !== -1) {
      fileIo.close(fd);
    }
  }
}

## Code blocks

### Code block 1

```
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Code block 2

```
const TAG: string = 'FileGuard_KIAWatermarkImage';
const DOMAIN: number = 0x0000;

/**
 * 设置KIA文件水印图片。使用Promise异步回调。
 */
async function testSetKiaWaterMarkImage() {
  let fd: number = -1;
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let imagePath: string = `/data/service/el2/test_water.png`;
    fd = await guard.openFile(imagePath);
    let stat: fileIo.Stat = fileIo.statSync(fd);
    let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
    fileIo.readSync(fd, buffer);

    let image: Uint8Array = new Uint8Array(buffer);
    let info: string = new Date().toLocaleString();
    guard.setKiaWatermarkImage(image, info).then(() => {
      hilog.info(DOMAIN, TAG, `Succeeded in setting the watermark image for Kia file.`);
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, TAG,
        `Failed to set the watermark image for Kia file. Code: ${err.code}, message: ${err.message}.`);
    })
  } catch (e) {
    hilog.error(DOMAIN, TAG, `testSetKiaWaterMarkImage Exception, Code: ${e.code}, message: ${e.message}`);
  } finally {
    if (fd !== -1) {
      fileIo.close(fd);
    }
  }
}
```
