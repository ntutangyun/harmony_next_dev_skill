# 批量算路

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-navi-matrix_

getDrivingMatrix(params: DrivingMatrixParams): Promise<MatrixResult>	驾车批量算路。
getDrivingMatrix(context: common.Context, params: DrivingMatrixParams): Promise<MatrixResult>	驾车批量算路。支持传入Context上下文。
getWalkingMatrix(params: MatrixParams): Promise<MatrixResult>	步行批量算路。
getWalkingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>	步行批量算路。支持传入Context上下文。
getCyclingMatrix(params: MatrixParams): Promise<MatrixResult>	骑行批量算路。
getCyclingMatrix(context: common.Context, params: MatrixParams): Promise<MatrixResult>	骑行批量算路。支持传入Context上下文。
DrivingMatrixParams	驾车批量算路的参数。
MatrixParams	步行、骑行批量算路的参数。
MatrixResult	批量算路的结果。
开发步骤

导入相关模块。

import { navi } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';
驾车批量算路

根据多组起终点坐标批量检索符合条件的驾车路径规划方案。支持以下功能：

支持未来出行规划。

支持根据实时路况进行合理路线规划。

支持多种路线偏好选择，如时间最短、避免经过收费的公路、避开高速公路、距离优先等。

说明

为保证性能与准确性，单次请求中的起点数量乘以终点数量应小于100。

async testDrivingMatrix() {
  let params: navi.DrivingMatrixParams = {
    // 起点的经纬度
    origins: [{
      latitude: 31.9844,
      longitude: 118.766253
    }, {
      latitude: 31.9644,
      longitude: 118.746253
    }],
    // 终点的经纬度
    destinations: [{
      latitude: 31.9344,
      longitude: 118.706253
    }],
    // 时间预估模型
    trafficMode: 2,
    language: 'zh_CN'
  };
  try {
    const result = await navi.getDrivingMatrix(params);
    console.info(`Succeeded in getting driving matrix. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting driving matrix. Code is ${err.code}, message is ${err.message}`);
  }
}
步行批量算路

根据多组起终点坐标批量检索符合条件的步行路径规划方案。支持以下功能：

支持150km以内的步行路径规划能力。

融入出行策略（时间最短、避免轮渡）。

说明

为保证性能与准确性，单次请求中的起点数量乘以终点数量应小于100。

async testWalkingMatrix() {
  let params: navi.MatrixParams = {
    // 起点的经纬度
    origins: [
      {
        latitude: 31.9844,
        longitude: 118.766253
      }, {
      latitude: 31.9644,
      longitude: 118.746253
    }],
    // 终点的经纬度
    destinations: [{
      latitude: 31.9344,
      longitude: 118.706253
    }],
    language: 'zh_CN'
  };
  try {
    const result = await navi.getWalkingMatrix(params);
    console.info(`Succeeded in getting walking matrix. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting walking matrix. Code is ${err.code}, message is ${err.message}`);
  }
}
骑行批量算路

根据多组起终点坐标批量检索符合条件的骑行路径规划方案。支持以下功能：

支持500km以内的骑行路径规划能力。

融入出行策略（时间最短、避免轮渡）。

说明

为保证性能与准确性，单次请求中的起点数量乘以终点数量应小于100。

async testCyclingMatrix() {
  let params: navi.MatrixParams = {
    // 起点的经纬度
    origins: [{
      latitude: 31.9844,
      longitude: 118.766253
    }, {
      latitude: 31.9644,
      longitude: 118.746253
    }],
    // 终点的经纬度
    destinations: [{
      latitude: 31.9344,
      longitude: 118.706253
    }],
    language: 'zh_CN'
  };
  try {
    const result = await navi.getCyclingMatrix(params);
    console.info(`Succeeded in getting cycling matrix. result is ${JSON.stringify(result)}`);
  } catch (error) {
    const err: BusinessError = error as BusinessError;
    console.error(`Failed in getting cycling matrix. Code is ${err.code}, message is ${err.message}`);
  }
}
出行路线规划
轨迹绑路
