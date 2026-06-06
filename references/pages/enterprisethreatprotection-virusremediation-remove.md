# 文件隔离删除

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-remove_

当隔离区文件的日益增加，内存占用持续增长时，可通过调用隔离文件删除接口，对已隔离文件进行删除，保证系统资源的高效利用并持续维护防护性能。

接口说明

详细接口说明可参考接口文档。

接口	描述
removeIsolatedFile(id: string): Promise<void>	对指定隔离ID的文件进行删除。删除后无法恢复。
开发步骤

导入模块。

import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';

通过调用接口removeIsolatedFile，实现对指定隔离ID文件的删除。id参数为隔离文件的唯一标识符，可通过调用queryIsolatedFiles接口获取。

import { BusinessError } from '@kit.BasicServicesKit';


// 对指定隔离文件ID进行删除
function removeIsolatedFilePromise() {
  // 隔离文件ID，可通过queryIsolatedFiles()接口获取
  let isolatedFileId: string = 'example-id-12345';
  virusRemediation.removeIsolatedFile(isolatedFileId).then(() => {
    console.info('Succeeded in removing isolated file.');
  }).catch((err: BusinessError) => {
  // 根据错误码进行不同的业务处理
    if (err.code === 1023806001) {
      console.error('Database error, please retry or contact support.');
    } else if (err.code === 1023804003) {
      console.error('Invalid isolation ID, please verify the ID exists.');
    } else {
      console.error(`Failed to remove isolated file. Code: ${err.code}, message: ${err.message}.`);
    }
  });
}
文件隔离恢复
隔离查询
