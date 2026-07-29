# 删除交通卡

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-transitcard-scene-delete_

删除钱包中的交通卡，同时取消与交通卡公司的关联关系。

交互流程

交通卡的删卡过程分为：卡片展示、生成删卡业务订单和发起删卡三个步骤，如下图所示：

开发步骤

开发者App启动后，可调用getCardMetadataInDevice接口获取指定设备上可访问的交通卡信息，并以数组形式返回。

如返回的数组为空，则表示开发者App在该设备上没有可访问的交通卡，无需显示卡片开通入口；如返回数组不为空，则根据返回的交通卡数据进行页面展示。

async getCardMetadataInDevice() {
   try {
      // 如果是手机设备，数组只有一个元素。如果是穿戴设备，会根据连接的穿戴设备数返回对应数量的数组元素。
      const cardMetadataInDeviceList = await this.transitCardClient.getCardMetadataInDevice(this.deviceType);
      console.info(`Succeeded in getting cardMetadataInDevice, card length is ${cardMetadataInDeviceList.length}`);
      return cardMetadataInDeviceList;
   } catch (err) {
      console.error(`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}`);
      return [];
   }
}

如果交通卡信息中包括卡号、余额信息，则表明该卡片在设备上已开通，显示卡片信息即可；否则可显示卡片的开通入口。

用户选择了要删除的交通卡后，开发者App需向开发者的后台服务器发起删卡业务订单的生成请求。

开发者可调用deleteTransitCard接口发起删卡处理过程。如删卡过程出现异常导致失败，开发者会收到相应的错误码。

async deleteTransitCard(cardMetadataInDevice: walletTransitCard.CardMetadataInDevice) {
   try {
      const logicalCardNumber = cardMetadataInDevice.cardMetadata[0].logicalCardNumber;
      const specifiedDeviceId = cardMetadataInDevice.deviceId;
      await this.transitCardClient.deleteTransitCard(logicalCardNumber, specifiedDeviceId, this.serverOrderId);
      console.info('Succeeded in deleting');
   } catch (err) {
      console.error(`Failed to delete, code:${err.code}, message:${err.message}`);
   }
}

## Code blocks

### Code block 1

```
async getCardMetadataInDevice() {
   try {
      // 如果是手机设备，数组只有一个元素。如果是穿戴设备，会根据连接的穿戴设备数返回对应数量的数组元素。
      const cardMetadataInDeviceList = await this.transitCardClient.getCardMetadataInDevice(this.deviceType);
      console.info(`Succeeded in getting cardMetadataInDevice, card length is ${cardMetadataInDeviceList.length}`);
      return cardMetadataInDeviceList;
   } catch (err) {
      console.error(`Failed to get CardMetadataInDevice, code:${err.code}, message:${err.message}`);
      return [];
   }
}
```

### Code block 2

```
async deleteTransitCard(cardMetadataInDevice: walletTransitCard.CardMetadataInDevice) {
   try {
      const logicalCardNumber = cardMetadataInDevice.cardMetadata[0].logicalCardNumber;
      const specifiedDeviceId = cardMetadataInDevice.deviceId;
      await this.transitCardClient.deleteTransitCard(logicalCardNumber, specifiedDeviceId, this.serverOrderId);
      console.info('Succeeded in deleting');
   } catch (err) {
      console.error(`Failed to delete, code:${err.code}, message:${err.message}`);
   }
}
```
