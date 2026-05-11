# 删除系统服务进程不可访问后台用户数据路径列表

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-del-restricted-access-process-list_

Enterprise Space Kit为应用提供删除系统服务进程不可访问后台用户数据路径列表的功能。用于应用删除管控系统服务进程时的场景。

接口说明

详细接口说明可参考接口文档。

接口名	描述
deleteRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum), processName: string): Promise<void>	删除系统服务进程不可访问后台用户数据路径列表。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用接口deleteRestrictedAccessBackgroundUserdataProcessList，删除系统服务进程不可访问后台用户数据路径列表，并且查看打印信息。

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
const processName: string = 'testSa';
try {
  await spaceManager.deleteRestrictedAccessBackgroundUserdataProcessList(userData, processName);
  console.info(`Succeeded in deleting restricted access background user data process list`);
} catch (err) {
  console.error(`Failed to delete restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
}
新增系统服务进程不可访问后台用户数据路径列表
设置工作空间策略
