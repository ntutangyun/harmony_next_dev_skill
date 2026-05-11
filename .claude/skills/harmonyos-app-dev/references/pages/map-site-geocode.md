# 地理编码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-geocode_

geocode(geocodeParams: GeocodeParams): Promise<GeocodeResult>	正地理编码。
geocode(context: common.Context, geocodeParams: GeocodeParams): Promise<GeocodeResult>	正地理编码。支持上传Context上下文。
reverseGeocode(reverseGeocodeParams: ReverseGeocodeParams): Promise<ReverseGeocodeResult>	逆地理编码。
reverseGeocode(context: common.Context, reverseGeocodeParams: ReverseGeocodeParams): Promise<ReverseGeocodeResult>	逆地理编码。支持上传Context上下文。
GeocodeParams	正地理编码的参数。
GeocodeResult	正地理编码的结果。
ReverseGeocodeParams	逆地理编码的参数。
ReverseGeocodeResult	逆地理编码的结果。
开发步骤

导入相关模块。

import { site } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';
正地理编码
说明

根据地址获取地点的空间坐标，如经纬度，最多返回10条记录。

let params: site.GeocodeParams = {
  // 地址信息
  query: 'Piazzale Dante, 41, 55049 Viareggio',
  language: 'en'
};
try {
  // 调用正地理编码接口进行地址查询
  const result = await site.geocode(params);
  console.info(`Succeeded in geocoding. result is ${JSON.stringify(result)}`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed in geocoding. Code is ${err.code}, message is ${err.message}`);
}
逆地理编码
let params: site.ReverseGeocodeParams = {
  // 位置经纬度
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: "en",
  radius: 0,
  isExtension: true,
  isNearbyAoi: true
};
try {
  // 调用逆地理编码接口进行坐标地址查询
  const result = await site.reverseGeocode(params);
  console.info(`Succeeded in reversing. result is ${JSON.stringify(result)}`);
} catch (error) {
  const err: BusinessError = error as BusinessError;
  console.error(`Failed in reversing. Code is ${err.code}, message is ${err.message}`);
}
POI搜索
路径规划
