# 企业账号认证

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-authenticate_

Enterprise Space Kit为企业应用提供企业账号认证的能力。在企业空间初始化阶段，实现企业用户的账号认证。

接口说明

详细接口说明可参考接口文档。

接口名	描述
authenticate(enterpriseAuthInfo: WorkspaceDomainInfo, credential: Uint8Array): Promise<AuthResult>	企业账号认证并返回结果。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用authenticate接口，进行企业账号认证。

try {
  const enterpriseAuthInfo: spaceManager.WorkspaceDomainInfo = {
    domain: 'testDomain', // 域名。
    workspaceName: 'testAccountName', // 工作空间域账号名称。
    serverConfigId: 'testServerConfigId' // 工作空间所属域的服务器配置标识符。
  };
  const credential = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0])
  const authResult: spaceManager.AuthResult = await spaceManager.authenticate(enterpriseAuthInfo, credential);
  console.info(`Succeeded in authenticating. Auth result is: ` + JSON.stringify(authResult));
} catch (err) {
  console.error(`Failed to authenticate. Code: ${err.code}, message: ${err.message}`);
}
查询深度冻结豁免名单
获取企业应用访问令牌
