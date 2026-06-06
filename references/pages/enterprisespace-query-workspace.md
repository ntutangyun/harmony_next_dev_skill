# 查询工作空间

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-query-workspace_

queryWorkspace(queryFlag: QueryType): Promise<WorkspaceInfo[]>	查询工作空间信息并返回结果。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用queryWorkspace接口，查询工作空间，并且查看打印信息。

const queryFlag: spaceManager.QueryType = spaceManager.QueryType.ALL;
try {
  const spaces: spaceManager.WorkspaceInfo[] = await spaceManager.queryWorkspace(queryFlag);
  console.info(`Succeeded in querying workspace` + JSON.stringify(spaces));
} catch (err) {
  console.error(`Failed to query workspace. Code: ${err.code}, message: ${err.message}`);
}
使能工作空间
移除工作空间
