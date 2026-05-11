# @performance/reasonable

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reasonable-gps-use-check_

'priority': geoLocationManager.LocationRequestPriority.ACCURACY,
      'timeInterval': 0,
      'distanceInterval': 0,
      'maxAccuracy': 0
    };
    let locationChange = (location: geoLocationManager.Location): void => {
      console.log('locationChanger:data:' + JSON.stringify(location));
    };
    //监听位置的变化
    geoLocationManager.on('locationChange', requestInfo, locationChange);
  }


  onBackground(): void {
    //退后台取消监听
    geoLocationManager.off('locationChange');
  }
}
反例
import { UIAbility } from '@kit.AbilityKit';
import { geoLocationManager } from '@kit.LocationKit';


export default class EntryAbility extends UIAbility {
  onForeground(): void {
    //在前台时按业务所需创建定位请求
    let requestInfo: geoLocationManager.LocationRequest = {
      'priority': geoLocationManager.LocationRequestPriority.ACCURACY,
      'timeInterval': 0,
      'distanceInterval': 0,
      'maxAccuracy': 0
    };
    let locationChange = (location: geoLocationManager.Location): void => {
      console.log('locationChanger:data:' + JSON.stringify(location));
    };
    //监听位置的变化
    geoLocationManager.on('locationChange', requestInfo, locationChange);
  }


  onBackground(): void {
  }
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/reasonable-audio-use-check
@performance/reuse-date-instances-check
