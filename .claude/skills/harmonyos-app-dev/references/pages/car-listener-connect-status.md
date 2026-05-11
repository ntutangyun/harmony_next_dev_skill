# 监听HiCar的连接状态

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-listener-connect-status_

let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();


  // 业务类型
  let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.HICAR];


  // 智慧出行连接状态回调函数
  const callBack = (info: smartMobilityCommon.SmartMobilityInfo) => {
    hilog.info(0x0000, 'testTag', 'Received smart mobility info: ', JSON.stringify(info));
    if (info.status === smartMobilityCommon.SmartMobilityStatus.RUNNING) {
      // 连接成功通知
    } else if (info.status === smartMobilityCommon.SmartMobilityStatus.IDLE) {
      // 断开连接通知
    }
  };


  // 注册智慧出行连接状态的监听
  awareness.on('smartMobilityStatus', types, callBack);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `on smart mobility status listener error, error code: ${e?.code}`);
}

取消监听。

在应用退出时，需要取消之前注册的监听，减少系统不必要的资源消耗。

try {
  // 获取SmartMobilityAwareness实例
  let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
  // 业务类型
  let types: smartMobilityCommon.SmartMobilityType[] = [smartMobilityCommon.SmartMobilityType.HICAR];
  // 取消注册智慧出行连接状态的监听
  awareness.off('smartMobilityStatus', types);
} catch (e) {
  // 捕获接口调用异常时的错误码并做相应处理
  hilog.error(0x0000, 'testTag', `off smart mobility status listener error, error code: ${e?.code}`);
}
主动获取HiCar的连接状态
超级桌面应用接入分布式相机
