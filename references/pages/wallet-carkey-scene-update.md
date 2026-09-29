# 更新车钥匙

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-update_

当车钥匙信息发生变化时，车主App通知钱包更新实例数据，完成移动端数字车钥匙更新。

交互流程

服务端开发

收到车主App或者DK服务器管理台的更新请求之后，由DK服务器调用车钥匙更新到钱包服务器完成更新车钥匙。然后钱包服务器会推送更新请求给钱包App完成移动端的更新。

客户端开发（可选）

DK服务器调用钱包服务器接口更新车钥匙为异步流程，可能存在延迟。车主App可以调用updatePass接口，立刻触发钱包端云对账，及时更新车钥匙。

async updatePass(): Promise<void> {
  const passStr = JSON.stringify({
    passType: this.passType,
  });
  try {
    const result = await this.walletPassClient.updatePass(passStr);
    const updatePassResult = JSON.parse(result) as UpdatePassResult;
    if (updatePassResult.result === '0') {
      console.info('Succeeded in updating pass');
    }
  } catch (err) {
    console.error(`Failed to update pass, code:${err.code} message:${err.message}`);
  }
}

## Code blocks

### Code block 1

```
async updatePass(): Promise<void> {
  const passStr = JSON.stringify({
    passType: this.passType,
  });
  try {
    const result = await this.walletPassClient.updatePass(passStr);
    const updatePassResult = JSON.parse(result) as UpdatePassResult;
    if (updatePassResult.result === '0') {
      console.info('Succeeded in updating pass');
    }
  } catch (err) {
    console.error(`Failed to update pass, code:${err.code} message:${err.message}`);
  }
}
```
