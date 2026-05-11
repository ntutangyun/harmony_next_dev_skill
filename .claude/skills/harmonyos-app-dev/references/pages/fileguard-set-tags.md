# 设置文件属性标签

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fileguard-set-tags_

Enterprise Data Guard Kit为应用提供对文件设置属性标签的能力，方便应用对管控文件进行标识、分类。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setFileTag(path: string, level: SecurityLevel, tag: string, callback: AsyncCallback<void>): void	使用Callback方式设置文件属性标签。
setFileTag(path: string, level: SecurityLevel, tag: string): Promise<void>	使用Promise方式设置文件属性标签。
setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;	使用Callback方式设置文件自定义属性标签。
setFileCustomTag(path: string, tagList: Array<string>): Promise<void>;	使用Promise方式设置文件自定义属性标签。
unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void;	使用Callback方式取消设置文件自定义属性标签。
unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>;	使用Promise方式取消设置文件自定义属性标签。
开发步骤

导入模块。

import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';

初始化FileGuard对象guard，调用接口setFileTag或setFileCustomTag，设置文件属性标签，自定义属性标签可通过unsetFileCustomTag取消设置。

通过回调函数方式，设置文件属性标签。

function setFileTagCallback() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test.txt';
  let tag: string = 'test';
  guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
      return;
    }
    console.info(`Succeeded in setting file tag.`);
  });
}

通过Promise方式，设置文件属性标签。

function setFileTagPromise() {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/test/test.txt';
  let tag: string = 'test';
  guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
    console.info(`Succeeded in setting file tag.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
  });
}
打开文件
获取文件属性标签
