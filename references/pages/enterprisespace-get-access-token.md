# 获取企业应用访问令牌

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-get-access-token_

getAccessToken(businessParams: Record<string, string>): Promise<Uint8Array>	获取企业应用令牌并返回结果。使用Promise异步回调。
开发步骤

导入Enterprise Space Kit模块。

import { spaceManager } from '@kit.EnterpriseSpaceKit';

调用getAccessToken接口，进行企业账号认证。

try {
  const params: Record<string, string> = {
    'clientId': 'test1' // 业务参数，由业务方根据请求协议自定义。
  };
  const result: Uint8Array = await spaceManager.getAccessToken(params);
  console.info(`Succeeded in getting access token. Result is: ` + JSON.stringify(result));
} catch (err) {
  console.error(`Failed to get access token. Code: ${err.code}, message: ${err.message}`);
}
企业账号认证
设置工作空间状态栏图标
