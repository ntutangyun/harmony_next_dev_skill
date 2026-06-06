# 主动获取HiCar的连接状态

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/car-check-application-start_

let awareness: smartMobilityCommon.SmartMobilityAwareness = smartMobilityCommon.getSmartMobilityAwareness();
      // 获取当前智慧出行连接状态
      let info: smartMobilityCommon.SmartMobilityInfo =
        awareness.getSmartMobilityStatus(smartMobilityCommon.SmartMobilityType.HICAR);
      const deviceDisplayId = Number(info.data["DISPLAY_ID"]);
      if (currentDisplayId === deviceDisplayId) {
        // 表示应用在对应的设备屏幕上
        hilog.info(0x0000, 'testTag', 'app in on device screen');
        return true;
      }
    } catch (e) {
      // 捕获接口调用异常时的错误码并做相应处理
      hilog.error(0x0000, 'testTag', `get smart mobility status error, error code: ${e?.code}`);
    }
    return false;
  }
}
获取HiCar连接状态
监听HiCar的连接状态
