# 使用智能防跟踪功能

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-intelligent-tracking-prevention_

通过调用enableIntelligentTrackingPrevention接口启用或关闭Web组件的智能防跟踪功能。默认情况下，该功能未启用。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('enableIntelligentTrackingPrevention')
        .onClick(() => {
          try {
            this.controller.enableIntelligentTrackingPrevention(true);
            console.info('enableIntelligentTrackingPrevention: true');
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller });
    }
  }
}
EnableIntTrackPrevent.ets

调用isIntelligentTrackingPreventionEnabled接口，判断Web组件是否开启了智能防跟踪功能。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('isIntelligentTrackingPreventionEnabled')
        .onClick(() => {
          try {
            let result = this.controller.isIntelligentTrackingPreventionEnabled();
            console.info('result: ' + result);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller });
    }
  }
}
IsIntTrackPreventEnabled.ets

通过onIntelligentTrackingPreventionResult接口将被拦截的跟踪型域名及其触发网站的域名回调给应用。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      // 需要打开智能防跟踪功能，才会触发onIntelligentTrackingPreventionResult回调
      Button('enableIntelligentTrackingPrevention')
        .onClick(() => {
          try {
            this.controller.enableIntelligentTrackingPrevention(true);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onIntelligentTrackingPreventionResult((details) => {
          console.info('onIntelligentTrackingPreventionResult: [websiteHost]= ' + details.host +
            ', [trackerHost]=' + details.trackerHost);
        })
    }
  }
}
OnIntTrackPreventResult.ets

智能防跟踪功能提供了一组接口，用于设置绕过该功能的域名列表。这些接口设置的域名列表适用于整个应用，而非特定的Web组件。

调用addIntelligentTrackingPreventionBypassingList接口设置绕过域名列表。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('addIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          try {
            let hostList = ['www.test1.com', 'www.test2.com', 'www.test3.com'];
            webview.WebviewController.addIntelligentTrackingPreventionBypassingList(hostList);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller });
    }
  }
}
AddIntTrackPreventByPassList.ets

调用removeIntelligentTrackingPreventionBypassingList接口删除部分绕过域名列表。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('removeIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          try {
            let hostList = [ 'www.test1.com', 'www.test2.com' ];
            webview.WebviewController.removeIntelligentTrackingPreventionBypassingList(hostList);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
RemoveIntTrackPreventByPassList.ets

调用clearIntelligentTrackingPreventionBypassingList接口清除所有绕过域名列表。

import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('clearIntelligentTrackingPreventionBypassingList')
        .onClick(() => {
          webview.WebviewController.clearIntelligentTrackingPreventionBypassingList();
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
ClearIntTrackPreventByPassList.ets
解决Web组件本地资源跨域问题
使用Web组件的广告过滤功能
