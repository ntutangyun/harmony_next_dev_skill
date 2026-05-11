# 管理数据源

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/health-datasource-manage_

insertDataSource(dataSource: DataSourceBase): Promise<string>	插入数据源，入参为数据源基类DataSourceBase。
readDataSource(request: DataSourceReadRequest): Promise<DataSource[]>	查询数据源，通过DataSourceReadRequest设置查询条件，可按DataSourceId/包名/设备UniqueId查询数据源。
updateDataSource(dataSource: DataSource): Promise<void>	更新数据源，其中数据源的dataSourceId和uniqueId字段无法更新。
开发前检查

完成申请运动健康服务与配置Client ID。

接口首次调用前，需先使用init方法进行初始化。

需先通过用户授权接口引导用户授权，用户授权任意数据类型权限后，才有权限调用数据源相关接口。

错误码请参考ArkTS API错误码，常见问题请参考Health Service Kit常见问题。

开发步骤
插入数据源

1.导入运动健康服务功能模块及相关公共模块。

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

2.创建数据源。

let dataSource: healthStore.DataSourceBase = {
  deviceInfo: {
    uniqueId: 'test',
    name: 'test', // 插入数据源时此字段必填
    category: healthStore.DeviceCategory.WEARABLE_BAND, // 插入数据源时此字段必填
    productId: '0554', // 插入数据源时此字段必填
    model: 'lotana',
    manufacturer: 'HUAWEI',
    mac: 'testDeviceMac',
    sn: 'testDeviceSn',
    hardwareVersion: '1',
    softwareVersion: '2',
    firmwareVersion: '3',
    udid: ''
  }
}

3.调用insertDataSource方法执行插入请求，并处理返回结果。

try {
  const dataSourceId = await healthStore.insertDataSource(dataSource);
  hilog.info(0x0000, 'testTag', `Succeeded in inserting dataSource, the dataSourceId is ${dataSourceId}.`);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to insert dataSource. Code: ${err.code}, message: ${err.message}`);
}
读取数据源

1.导入运动健康服务功能模块及相关公共模块。

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

2.创建数据源读取请求。

let readSourceRequest: healthStore.DataSourceReadRequest = {
  deviceUniqueId: 'testudidupdate'
}

3.调用readDataSource方法执行查询请求，并处理返回结果。

try {
  let dataSources = await healthStore.readDataSource(readSourceRequest);
  dataSources.forEach((dataSource) => {
    hilog.info(0x0000, 'testTag', `Succeeded in reading dataSource, the dataSourceId is ${dataSource.dataSourceId}.`);
  });
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to read dataSource. Code: ${err.code}, message: ${err.message}`);
}
更新数据源

1.导入运动健康服务功能模块及相关公共模块。

import { healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

2.创建数据源。

let newDataSource: healthStore.DataSource = {
  deviceInfo: {
    uniqueId: 'test',
    name: 'test',
    category: healthStore.DeviceCategory.WEARABLE_BAND,
    productId: '0554',
    model: 'lotana',
    manufacturer: 'HUAWEI',
    mac: 'testDeviceMac',
    sn: 'testDeviceSn',
    hardwareVersion: '1',
    softwareVersion: '2',
    firmwareVersion: '3',
    // 修改udid
    udid: 'updateudid'
  },
  // 此处dataSourceId值为开发步骤插入数据源时，返回的dataSourceId
  dataSourceId: 'xxx'
}

3.调用updateDataSource方法执行更新请求，并处理返回结果。

try {
  await healthStore.updateDataSource(newDataSource);
  hilog.info(0x0000, 'testTag', 'Succeeded in updating dataSource.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to update dataSource. Code: ${err.code}, message: ${err.message}`);
}
管理用户授权
管理运动健康数据
