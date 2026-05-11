# 文档中心

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-location-division_

区划选择控件功能主要由sceneMap命名空间下的selectDistrict方法提供，更多接口及使用方法请参见接口文档。

接口名	描述
DistrictSelectOptions	区划选择页面初始选项。
selectDistrict(context: common.Context, options: DistrictSelectOptions): Promise<DistrictSelectResult>	调出区划选择页面。
DistrictSelectResult	区划选择结果。
开发步骤

导入相关模块。

import { sceneMap } from '@kit.MapKit';
import { BusinessError } from '@kit.BasicServicesKit';

创建区划选择请求参数，调用selectDistrict方法拉起区划选择页。

let districtSelectOptions: sceneMap.DistrictSelectOptions = {
  countryCode: "CN",
  // 使用子窗拉起方式
  subWindowEnabled: true,
  // 区划选择控件的最大显示层级
  maxAdminLevel: 3
};
// 拉起区划选择页
sceneMap.selectDistrict(this.getUIContext().getHostContext(), districtSelectOptions).then((data) => {
  console.info("SelectDistrict", "Succeeded in selecting district.");
}).catch((err: BusinessError) => {
  console.error("SelectDistrict", `Failed to select district, code: ${err.code}, message: ${err.message}`);
});
