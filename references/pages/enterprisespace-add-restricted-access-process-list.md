# 新增系统服务进程不可访问后台用户数据路径列表

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-add-restricted-access-process-list_

Enterprise Space Kit为应用提供新增系统服务进程不可访问后台用户数据路径列表的功能。用于应用新增管控系统服务进程时的场景。

接口说明

详细接口说明可参考接口文档。

接口名	描述
addRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum, processName: string, disallowPaths?: string[]): Promise<void>	新增系统服务进程不可访问后台用户数据路径列表。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用接口addRestrictedAccessBackgroundUserdataProcessList，新增系统服务进程不可访问后台用户数据路径列表，并且查看打印信息。

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
const processName: string = 'testSa';
const disallowPaths: string[] = ['/data/service', '/data/app'];
try {
  await spaceManager.addRestrictedAccessBackgroundUserdataProcessList(userData, processName, disallowPaths);
  console.info(`Succeeded in adding restricted access background user data process list`);
} catch (err) {
  console.error(`Failed to add restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
}
获取不可访问后台用户数据的系统服务进程列表
删除系统服务进程不可访问后台用户数据路径列表
