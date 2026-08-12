# 目标设备选择

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/we-device-selection_

当获取到的已连接设备列表中包含多个设备时，需要根据业务需求正确挑选目标设备。

选择某种类型的设备

获取到的设备Device类中，包含有DeviceCategory字段，表明了当前设备的类型，可根据设备的类型挑选目标设备。

参见已连接穿戴设备查询章节，获取已连接设备列表。

从已连接设备列表中根据设备类型选定需要通信的设备。

async function fun(deviceList: wearEngine.Device[]) {
  let targetDevice: wearEngine.Device | undefined;
  for (let index = 0; index < deviceList.length; index++) {
    // 挑选类型为手表的设备
    if (deviceList[index].category === wearEngine.DeviceCategory.WATCH) {
      targetDevice = deviceList[index];
      break;
    }
    if (index === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  }
  // targetDevice为undefined则抛出错误
  if (!targetDevice) {
    throw new Error('The value of targetDevice is undefined');
  } else {
    console.info('Get targetDevice success.');
  }
}

选择支持某种能力集的设备

获取到的设备中包含了查询能力集的方法，可参考穿戴设备信息查询章节。

[h2]根据设备支持的WearEngine能力集挑选目标设备

参见已连接穿戴设备查询章节，获取已连接设备列表。

从已连接设备列表中根据WearEngine能力集选定需要通信的设备。

async function fun(deviceList: wearEngine.Device[]) {
  // 声明目标设备
  let targetDevice: wearEngine.Device | undefined;
  for (let index = 0; index < deviceList.length; index++) {
    // 挑选支持的WearEngine能力集的设备
    try {
      if (await deviceList[index].isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.MONITOR)) {
        targetDevice = deviceList[index];
        break;
      }
    } catch (error) {
      // 检查设备能力支持失败，记录错误并继续检查下一个设备
      console.error(
        `Failed to check capability for device at index ${index}. Code is ${error.code}, message is ${error.message}`);
      continue;
    }
    if (index === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  }
  // targetDevice为undefined则抛出错误
  if (!targetDevice) {
    throw new Error('The value of targetDevice is undefined.');
  } else {
    console.info('Get targetDevice success.');
  }
}

[h2]根据设备支持的Device能力集挑选目标设备

参见已连接穿戴设备查询章节，获取已连接设备列表。

从已连接设备列表中根据Device能力集选定需要通信的设备。

async function fun(deviceList: wearEngine.Device[]) {
  // 声明目标设备
  let targetDevice: wearEngine.Device | undefined;
  for (let index = 0; index < deviceList.length; index++) {
    // 挑选支持的Device能力集的设备
    try {
      if (await deviceList[index].isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        targetDevice = deviceList[index];
        break;
      }
    } catch (error) {
      // 检查设备能力支持失败，记录错误并继续检查下一个设备
      console.error(
        `Failed to check capability for device at index ${index}. Code is ${error.code}, message is ${error.message}`);
      continue;
    }
    if (index === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  }
  // targetDevice为undefined则抛出错误
  if (!targetDevice) {
    throw new Error('The value of targetDevice is undefined.');
  } else {
    console.info('Get targetDevice success.');
  }
}

## Code blocks

### Code block 1

```
async function fun(deviceList: wearEngine.Device[]) {
  let targetDevice: wearEngine.Device | undefined;
  for (let index = 0; index < deviceList.length; index++) {
    // 挑选类型为手表的设备
    if (deviceList[index].category === wearEngine.DeviceCategory.WATCH) {
      targetDevice = deviceList[index];
      break;
    }
    if (index === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  }
  // targetDevice为undefined则抛出错误
  if (!targetDevice) {
    throw new Error('The value of targetDevice is undefined');
  } else {
    console.info('Get targetDevice success.');
  }
}
```

### Code block 2

```
async function fun(deviceList: wearEngine.Device[]) {
  // 声明目标设备
  let targetDevice: wearEngine.Device | undefined;
  for (let index = 0; index < deviceList.length; index++) {
    // 挑选支持的WearEngine能力集的设备
    try {
      if (await deviceList[index].isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.MONITOR)) {
        targetDevice = deviceList[index];
        break;
      }
    } catch (error) {
      // 检查设备能力支持失败，记录错误并继续检查下一个设备
      console.error(
        `Failed to check capability for device at index ${index}. Code is ${error.code}, message is ${error.message}`);
      continue;
    }
    if (index === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  }
  // targetDevice为undefined则抛出错误
  if (!targetDevice) {
    throw new Error('The value of targetDevice is undefined.');
  } else {
    console.info('Get targetDevice success.');
  }
}
```

### Code block 3

```
async function fun(deviceList: wearEngine.Device[]) {
  // 声明目标设备
  let targetDevice: wearEngine.Device | undefined;
  for (let index = 0; index < deviceList.length; index++) {
    // 挑选支持的Device能力集的设备
    try {
      if (await deviceList[index].isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
        targetDevice = deviceList[index];
        break;
      }
    } catch (error) {
      // 检查设备能力支持失败，记录错误并继续检查下一个设备
      console.error(
        `Failed to check capability for device at index ${index}. Code is ${error.code}, message is ${error.message}`);
      continue;
    }
    if (index === deviceList.length - 1) {
      // 若不存在目标设备则抛出错误
      throw new Error('cannot find target device');
    }
  }
  // targetDevice为undefined则抛出错误
  if (!targetDevice) {
    throw new Error('The value of targetDevice is undefined.');
  } else {
    console.info('Get targetDevice success.');
  }
}
```
