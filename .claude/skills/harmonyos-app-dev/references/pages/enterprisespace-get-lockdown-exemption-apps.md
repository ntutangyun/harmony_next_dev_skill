# 查询深度冻结豁免名单

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-lockdown-exemption-apps_

Enterprise Space Kit为应用提供查询深度冻结豁免名单的能力。当设置深度冻结豁免名单后，可使用该接口查询深度冻结豁免名单。

接口说明

详细接口说明可参考接口文档。

接口名	描述
getLockdownExemptionApps(workspaceId?: number): Promise<string[]>	查询深度冻结豁免名单。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块和相关依赖模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用接口getLockdownExemptionApps，查询深度冻结豁免名单，并且查看打印信息。

  const workspaceId: number = 100;
  try {
    const apps: string[] = await spaceManager.getLockdownExemptionApps(workspaceId);
    console.info(`Succeeded in getting lockdown exemption apps. apps:` + JSON.stringify(apps));
  } catch (err) {
    console.error(`Failed to get lockdown exemption apps. Code: ${err.code}, message: ${err.message}`);
  }
设置深度冻结豁免名单
企业账号认证
