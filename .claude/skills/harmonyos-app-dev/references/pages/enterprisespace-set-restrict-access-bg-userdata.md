# 设置系统服务进程不可访问后台用户数据的功能

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-set-restrict-access-bg-userdata_

Enterprise Space Kit为应用提供设置系统服务进程不可访问后台用户数据的功能。例如，当前台是企业用户，后台是个人用户时，应用设置了对应个人用户的管控，此时不允许系统服务进程访问后台个人用户的数据。

接口说明

详细接口说明可参考接口文档。

接口名	描述
setRestrictedAccessBackgroundUserdata(userData: UserDataEnum, enable: boolean): Promise<void>	设置系统服务进程不可访问后台用户数据的功能。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用接口setRestrictedAccessBackgroundUserdata，设置系统服务进程不可访问后台用户数据的功能，并且查看打印信息。

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
const enable: boolean = false;
try {
  await spaceManager.setRestrictedAccessBackgroundUserdata(userData, enable)
  console.info(`Succeeded in setting restricted access background user data. userData: ${userData}, enable: ${enable}`);
} catch (err) {
  console.error(`Failed to set restricted access background user data. Code: ${err.code}, message: ${err.message}`);
}
取消订阅空间事件
获取系统服务进程不可访问的后台用户数据状态
