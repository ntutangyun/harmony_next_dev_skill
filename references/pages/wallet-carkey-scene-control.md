# 使用车钥匙

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-control_

用户可在车主App中查看钥匙连接状态，执行开锁、闭锁、开启后备箱等远程车控操作。

交互流程

开发流程

序号	步骤	说明
1	查询连接状态	进入车控页面时向钱包查询移动端与车端的连接状态。
2	注册监听回调	进入车控页面时注册监听，用于接收移动端和车端状态变化等通知。
3	进行配对连接	未配对/连接状态下，车主App主动发起配对/连接。
4	获取配对码	DK服务器计算配对码返回给钱包App。
5	发送车控消息	移动端与车端已配对/连接后，由移动端发起主动车控。
6	解注册监听回调	退出车控页面后，解除监听回调。

服务端开发

收到钱包App通过钱包服务器代理的获取配对码请求之后，DK服务器基于请求中的广播内容计算配对码并返回给钱包App（JUSTWORK配对方式不涉及）。

客户端开发

[h2]查询连接状态

进入车主App的车控页面之后，车主App需要向钱包查询移动端和车端的连接状态。移动端和车端的状态有如下三种：

状态	说明
配对状态	移动端和车端是否已配对。
连接状态	移动端和车端是否已完成BLE/SLE协议层的连接。
认证状态	移动端和车端是否已完成车钥匙认证过程，该过程由车端在连接完成后主动发起。

一般情况情况下，移动端和车端已建立连接，则视为：已完成车钥匙认证过程。

查询连接状态有同步和异步两种查询方式：

同步查询

车钥匙已开通的情况下，车主App调用queryICCEConnectionState接口查询连接状态。

async queryICCEConnectionState(): Promise<void> {
   const passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
   });
   try {
      const result = await this.walletPassClient.queryICCEConnectionState(passStr);
      const queryICCEConnectionStateResult = JSON.parse(result) as QueryICCEConnectionStateResult;
      if (queryICCEConnectionStateResult.authState === '1') {
         // 显示已连接。
      } else {
         // 未成功连接，页面根据queryICCEConnectionStateResult.connectionState展示对应连接状态。
         // 页面展示点击连接按钮，点击后调用this.startICCEConnection()发起配对连接。
      }
   } catch (err) {
      console.error(`Failed to query connection state, code: ${err.code} message: ${err.message}`);
   }
}

异步查询

车钥匙已开通的情况下，车主App调用registerICCEListener接口注册监听，当移动端和车端状态发生变化，钱包App会通过监听回调通知车主App；当车钥匙被删除或者车主App进程退出，车主App需要调用unregisterICCEListener取消监听。

async registerICCEListener(): Promise<void> {
   const rkeStr = JSON.stringify({
      passType: this.passType,
      registerName: this.registerName
   });
   try {
      // 创建rpc RemoteObject，用于接收钱包回调通知结果。
      const callback = new ICCECallBack();
      const result = await this.walletPassClient.registerICCEListener(rkeStr, callback);
      const registerICCEListenerResult = JSON.parse(result) as RegisterICCEListenerResult;
      if (registerICCEListenerResult.result === '0') {
         console.info('Succeeded in registering listener');
      }
   } catch (err) {
      console.error(`Failed to register listener, code:${err.code} message:${err.message}`);
   }
}

async unregisterICCEListener(): Promise<void> {
   const rkeStr = JSON.stringify({
      passType: this.passType,
      registerName: this.registerName
   });
   try {
      const result = await this.walletPassClient.unregisterICCEListener(rkeStr);
      const unregisterICCEListenerResult = JSON.parse(result) as UnregisterICCEListenerResult;
      if (unregisterICCEListenerResult.result === '0') {
         console.info('Succeeded in unregistering listener');
      }
   } catch (err) {
      console.error(`Failed to unregister listener, code:${err.code} message:${err.message}`);
   }
}

[h2]配对和连接

车钥匙已开通的情况下，如果未配对或者未连接，车主App可以调用startICCEConnection接口（connectionAction不传入）开始配对/连接，连接完成之后车端要主动触发认证流程并上报认证状态，在这个过程中车主App需要通过监听接收状态变化并显示。

async startICCEConnection(): Promise<void> {
   const rkeStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
   });
   try {
      const result = await this.walletPassClient.startICCEConnection(rkeStr);
      const startICCEConnectionResult = JSON.parse(result) as StartICCEConnectionResult;
      if (startICCEConnectionResult.result === '0') {
         // 连接成功，可以调用this.sendICCERKEMessage()发起车控。
      }
   } catch (err) {
      console.error(`Failed to start connection, code:${err.code} message:${err.message}`);
   }
}

[h2]主动车控

车钥匙已开通并且移动端和车端已连接（已完成车钥匙认证过程）的情况下，车主App可以调用sendICCERKEMessage接口通过钱包App作为中继，发送车控指令给车端，然后通过监听接收车端对于车控指令的响应指令。

async sendICCERKEMessage(): Promise<void> {
   const rkeStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber,
      rkeCommand: this.rkeCommand,
      encryptFlag: '0',
      directionFlag: '1'
   });
   try {
      const result = await this.walletPassClient.sendICCERKEMessage(rkeStr);
      const sendICCERKEMessageResult = JSON.parse(result) as SendICCERKEMessageResult;
      if (sendICCERKEMessageResult.result === '0') {
         // 车控指令发送成功。
      }
   } catch (err) {
      console.error(`Failed to send message, code:${err.code} message:${err.message}`);
   }
}

## Code blocks

### Code block 1

```
async queryICCEConnectionState(): Promise<void> {
   const passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
   });
   try {
      const result = await this.walletPassClient.queryICCEConnectionState(passStr);
      const queryICCEConnectionStateResult = JSON.parse(result) as QueryICCEConnectionStateResult;
      if (queryICCEConnectionStateResult.authState === '1') {
         // 显示已连接。
      } else {
         // 未成功连接，页面根据queryICCEConnectionStateResult.connectionState展示对应连接状态。
         // 页面展示点击连接按钮，点击后调用this.startICCEConnection()发起配对连接。
      }
   } catch (err) {
      console.error(`Failed to query connection state, code: ${err.code} message: ${err.message}`);
   }
}
```

### Code block 2

```
async registerICCEListener(): Promise<void> {
   const rkeStr = JSON.stringify({
      passType: this.passType,
      registerName: this.registerName
   });
   try {
      // 创建rpc RemoteObject，用于接收钱包回调通知结果。
      const callback = new ICCECallBack();
      const result = await this.walletPassClient.registerICCEListener(rkeStr, callback);
      const registerICCEListenerResult = JSON.parse(result) as RegisterICCEListenerResult;
      if (registerICCEListenerResult.result === '0') {
         console.info('Succeeded in registering listener');
      }
   } catch (err) {
      console.error(`Failed to register listener, code:${err.code} message:${err.message}`);
   }
}

async unregisterICCEListener(): Promise<void> {
   const rkeStr = JSON.stringify({
      passType: this.passType,
      registerName: this.registerName
   });
   try {
      const result = await this.walletPassClient.unregisterICCEListener(rkeStr);
      const unregisterICCEListenerResult = JSON.parse(result) as UnregisterICCEListenerResult;
      if (unregisterICCEListenerResult.result === '0') {
         console.info('Succeeded in unregistering listener');
      }
   } catch (err) {
      console.error(`Failed to unregister listener, code:${err.code} message:${err.message}`);
   }
}
```

### Code block 3

```
async startICCEConnection(): Promise<void> {
   const rkeStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
   });
   try {
      const result = await this.walletPassClient.startICCEConnection(rkeStr);
      const startICCEConnectionResult = JSON.parse(result) as StartICCEConnectionResult;
      if (startICCEConnectionResult.result === '0') {
         // 连接成功，可以调用this.sendICCERKEMessage()发起车控。
      }
   } catch (err) {
      console.error(`Failed to start connection, code:${err.code} message:${err.message}`);
   }
}
```

### Code block 4

```
async sendICCERKEMessage(): Promise<void> {
   const rkeStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber,
      rkeCommand: this.rkeCommand,
      encryptFlag: '0',
      directionFlag: '1'
   });
   try {
      const result = await this.walletPassClient.sendICCERKEMessage(rkeStr);
      const sendICCERKEMessageResult = JSON.parse(result) as SendICCERKEMessageResult;
      if (sendICCERKEMessageResult.result === '0') {
         // 车控指令发送成功。
      }
   } catch (err) {
      console.error(`Failed to send message, code:${err.code} message:${err.message}`);
   }
}
```
