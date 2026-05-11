# 已连接对端设备查询

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/watch_query_connected_devices_

let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
// 声明目标设备
let targetDevice: wearEngine.Device;


// 步骤2：调用getConnectedDevices方法，查询用户是否有已连接的对端设备
deviceClient.getConnectedDevices().then(devices => {
  console.info(`Succeeded in getting deviceList, deviceList number is ${devices.length}`);
  // 步骤3：从已连接设备列表中选定需要通信的设备
  if (devices.length > 0) {
    targetDevice = devices[0];
    console.info(`Succeeded to get target device.`);
    // 步骤4：查询对端设备的操作系统类型
    let osCategory: wearEngine.OsCategory | undefined = targetDevice.osCategory;
    console.info(`The osCategory of target device is ${osCategory}`);
  } else {
    console.warn(`Failed to get target device. deviceList is empty.`);
  }
}).catch((error: BusinessError) => {
  // 处理调用失败时捕获到的异常
  console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
});
穿戴侧应用开发
应用间消息通信
