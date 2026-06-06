# 获取不可访问后台用户数据的系统服务进程列表

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-restricted-access-process-list_

Enterprise Space Kit为应用提供获取通过接口addRestrictedAccessBackgroundUserdataProcessList添加管控的系统服务进程列表的功能。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getRestrictedAccessBackgroundUserdataProcessList(userData: UserDataEnum): Promise<ProcessConfigInfo[]>	获取不可访问后台用户数据的系统服务进程列表。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用接口getRestrictedAccessBackgroundUserdataProcessList，获取不可访问后台用户数据的系统服务进程列表，并且查看打印信息。

const userData: spaceManager.UserDataEnum = spaceManager.UserDataEnum.ENTERPRISE;
try {
  const processConfigInfos: spaceManager.ProcessConfigInfo[] = await spaceManager.getRestrictedAccessBackgroundUserdataProcessList(userData);
  console.info(`Succeeded in getting restricted access background user data process list. process config infos: ${JSON.stringify(processConfigInfos)}`);
} catch (err) {
  console.error(`Failed to get restricted access background user data process list. Code: ${err.code}, message: ${err.message}`);
}
获取系统服务进程不可访问的后台用户数据状态
新增系统服务进程不可访问后台用户数据路径列表
