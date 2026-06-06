# 隔离查询

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-query_

当安全防护类应用更新或卸载，导致原本存储在应用数据库中的隔离信息丢失时，可通过隔离查询接口，为安全防护类应用提供隔离信息查询的能力，快速获取自身应用已隔离的当前用户的文件信息，保障隔离恢复和隔离查询的可操作性。

接口说明

详细接口说明可参考接口文档。

接口	描述
queryIsolatedFiles(callback: QueryCallback, batchNum?: number): void	获取已隔离文件的文件信息。
开发步骤

导入模块。

import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';

通过声明查询结果回调queryCallback，并调用queryIsolatedFiles接口，获取已隔离文件的文件信息。

function startQueryTask() {
  // 查询隔离文件信息回调
  let onQuery: (files: virusRemediation.IsolatedFileInfo[]) => void = (files: virusRemediation.IsolatedFileInfo[]) => {
    files.forEach((value: virusRemediation.IsolatedFileInfo, index: number) => {
      console.info(`Succeeded in getting isolated file, file id: ${value.id}.`);
    })
  };
  // 查询隔离文件信息结束通知
  let onComplete: () => void = () => {
    console.info(`Query completed`);
  };
  // 查询隔离文件信息错误报告
  let onError: (code: number, message: string) => void = (code: number, message: string) => {
    console.error(`Query error, error code: ${code}, message: ${message}`);
  }
  let queryCallback: virusRemediation.QueryCallback = {
    onQuery: onQuery,
    onComplete: onComplete,
    onError: onError
  };
  try {
    virusRemediation.queryIsolatedFiles(queryCallback);
  } catch (error) {
    console.error(`Failed to get isolated file. Error: ${error}`);
  }
}
文件隔离删除
Enterprise Threat Protection Kit常见问题
