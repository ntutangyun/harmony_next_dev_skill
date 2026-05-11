# 获取系统服务进程不可访问的后台用户数据状态

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-restricted-access-status_

Enterprise Space Kit为应用提供获取系统服务进程管控不可访问后台用户数据的状态，用于确认系统服务进程是否被管控访问后台用户数据。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getRestrictedAccessBackgroundUserdataStatus(userData: UserDataEnum): Promise<boolean>	获取系统服务进程管控不可访问后台用户数据的状态。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用接口getRestrictedAccessBackgroundUserdataStatus，提供获取系统服务进程管控不可访问后台用户数据的状态，并且查看打印信息。

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
try {
  const status: boolean = await spaceManager.getRestrictedAccessBackgroundUserdataStatus(userData);
  console.info(`Succeeded in getting restricted access background user data status. status: ${status}`);
} catch (err) {
  console.error(`Failed to get restricted access background user data status. Code: ${err.code}, message: ${err.message}`);
}
设置系统服务进程不可访问后台用户数据的功能
获取不可访问后台用户数据的系统服务进程列表
