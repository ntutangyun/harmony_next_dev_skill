# 使用隐私模式

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-incognito-mode_

开发者在创建Web组件时，可以将可选参数incognitoMode设置为true，来开启Web组件的隐私模式。使用隐私模式浏览网页时，Cookie、缓存等数据不会写入本地持久化存储；隐私模式的Web组件销毁后，这些数据将被清除，不会保留。

创建隐私模式的Web组件。

import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
    }
  }
}
IncognitoMode_one.ets

通过isIncognitoMode 判断当前Web组件是否是隐私模式。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('isIncognitoMode')
        .onClick(() => {
          try {
            let result = this.controller.isIncognitoMode();
            console.info('isIncognitoMode' + result);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller });
    }
  }
}
IncognitoMode_two.ets

隐私模式提供了一系列接口，用于操作地理位置、Cookie以及Cache Data。

通过allowGeolocation设置隐私模式下的Web组件允许指定来源使用地理位置。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = 'file:///';


  build() {
    Column() {
      Button('allowGeolocation')
        .onClick(() => {
          try {
            // allowGeolocation第二个参数表示隐私模式（true）或非隐私模式（false）下，允许指定来源使用地理位置。
            webview.GeolocationPermissions.allowGeolocation(this.origin, true);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
    }
  }
}
AllowGeolocation.ets

通过deleteGeolocation清除隐私模式下指定来源的地理位置权限状态。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = 'file:///';


  build() {
    Column() {
      Button('deleteGeolocation')
        .onClick(() => {
          try {
            // deleteGeolocation第二个参数表示隐私模式（true）或非隐私模式（false）下，清除指定来源的地理位置权限状态。
            webview.GeolocationPermissions.deleteGeolocation(this.origin, true);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
    }
  }
}
DeleteGeolocation.ets

通过getAccessibleGeolocation以回调方式异步获取隐私模式下指定源的地理位置权限状态。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  origin: string = 'file:///';


  build() {
    Column() {
      Button('getAccessibleGeolocation')
        .onClick(() => {
          try {
            // getAccessibleGeolocation第三个参数表示隐私模式（true）或非隐私模式（false）下
            // 以回调方式异步获取指定源的地理位置权限状态。
            webview.GeolocationPermissions.getAccessibleGeolocation(this.origin, (error, result) => {
              if (error) {
                console.error(`getAccessibleGeolocationAsync error: + Code: ${error.code}, message: ${error.message}`);
                return;
              }
              console.info('getAccessibleGeolocationAsync result: ' + result);
            }, true);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
    }
  }
}
GetAccessibleGeolocation.ets

通过deleteAllData清除隐私模式下Web SQL当前使用的所有存储。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('deleteAllData')
        .onClick(() => {
          try {
            // deleteAllData参数表示删除所有隐私模式（true）或非隐私模式（false）下，内存中的web数据。
            webview.WebStorage.deleteAllData(true);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller, incognitoMode: true })
        .databaseAccess(true)
    }
  }
}
DeleteAllData.ets

加载的html文件。

<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>test</title>
  <script type="text/javascript">
    var db = openDatabase('mydb','1.0','Test DB',2 * 1024 * 1024);
    var msg;
    db.transaction(function(tx){
      tx.executeSql('INSERT INTO LOGS (id,log) VALUES(1,"test1")');
      tx.executeSql('INSERT INTO LOGS (id,log) VALUES(2,"test2")');
      msg = '<p>数据表已创建,且插入了两条数据。</p>';
      document.querySelector('#status').innerHTML = msg;
    });
    db.transaction(function(tx){
      tx.executeSql('SELECT * FROM LOGS', [], function (tx, results) {
        var len = results.rows.length,i;
        msg = "<p>查询记录条数：" + len + "</p>";
        document.querySelector('#status').innerHTML += msg;
            for(i = 0; i < len; i++){
              msg = "<p><b>" + results.rows.item(i).log + "</b></p>";
        document.querySelector('#status').innerHTML += msg;
        }
      },null);
    });
    </script>
</head>
<body>
<div id="status" name="status">状态信息</div>
</body>
</html>

通过fetchCookieSync获取隐私模式下指定url对应cookie的值。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('fetchCookieSync')
        .onClick(() => {
          try {
            // fetchCookieSync第二个参数表示获取隐私模式（true）或非隐私模式（false）下，webview的内存cookies。
            let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com', true);
            console.info('fetchCookieSync cookie = ' + value);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
    }
  }
}
FetchCookieSync.ets

通过configCookieSync设置隐私模式下指定url的单个cookie的值。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('configCookieSync')
        .onClick(() => {
          try {
            // configCookieSync第三个参数表示设置隐私模式（true）或非隐私模式（false）下，对应url的cookies。
            webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b', true);
          } catch (error) {
            console.error(
              `ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
    }
  }
}
ConfigCookieSync.ets

通过existCookie查询隐私模式下是否存在cookie。

import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('existCookie')
        .onClick(() => {
          // existCookie参数表示隐私模式（true）或非隐私模式（false）下，查询是否存在cookies。
          let result = webview.WebCookieManager.existCookie(true);
          console.info('result: ' + result);
        })
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
    }
  }
}
ExistCookie.ets

通过clearAllCookiesSync清除隐私模式下所有cookie。

import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('clearAllCookiesSync')
        .onClick(() => {
          // clearAllCookiesSync参数表示清除隐私模式（true）或非隐私模式（false）下，webview的所有内存cookies。
          webview.WebCookieManager.clearAllCookiesSync(true);
        })
      Web({ src: 'www.example.com', controller: this.controller, incognitoMode: true });
    }
  }
}
ClearAllCookiesSync.ets
管理位置权限
使用运动和方向传感器监测设备状态
