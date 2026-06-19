# 地理编码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-site-geocode_

场景介绍

提供正地理编码、逆地理编码的能力：

正地理编码：根据地址获取地点的经纬度。

逆地理编码：获取经纬度对应的地点信息。

接口说明

以下是地理编码相关接口，主要由site命名空间下的方法提供，更多接口及使用方法请参见接口文档。

接口名	描述
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

[h2]正地理编码

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

[h2]逆地理编码

let params: site.ReverseGeocodeParams = {
  // 位置经纬度
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: 'en',
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

## Code blocks

### Code block 1

```
import { site } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### Code block 2

```
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
```

### Code block 3

```
let params: site.ReverseGeocodeParams = {
  // 位置经纬度
  location: {
    latitude: 31.984410259206815,
    longitude: 118.76625379397866
  },
  language: 'en',
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
```
