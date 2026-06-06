# 使用AppServiceExtensionAbility组件实现后台服务

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-service-extension-ability_

-------- terminateSelf succeed -----------');
    }).catch((error: BusinessError) => {
      hilog.error(0x0000, TAG, `terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
    });
  }


// ···
};
MyAppServiceExtAbility.ets
连接一个后台服务
客户端连接服务端

客户端可以通过connectAppServiceExtensionAbility()连接服务端（在Want对象中指定连接的目标服务），服务端的onConnect()就会被调用，并在该回调方法中接收到客户端传递过来的Want对象。

服务端的AppServiceExtensionAbility组件会在onConnect()中返回IRemoteObject对象给客户端ConnectOptions的onConnect()方法。开发者通过该IRemoteObject定义通信接口，实现客户端与服务端的RPC交互。多个客户端可以同时连接到同一个后台服务，客户端完成与服务端的交互后，客户端需要通过调用disconnectAppServiceExtensionAbility()来断开连接。如果所有连接到某个后台服务的客户端均已断开连接，则系统会销毁该服务。

使用connectAppServiceExtensionAbility()建立与后台服务的连接。示例中的context的获取方式请参见获取UIAbility的上下文信息。

import { common, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';


const TAG: string = '[ConnectAppServiceExt]';
const DOMAIN_NUMBER: number = 0xFF00;


let connectionId: number;
let want: Want = {
  deviceId: '',
  bundleName: 'com.samples.appserviceextensionability',
  abilityName: 'MyAppServiceExtAbility'
};


let options: common.ConnectOptions = {
  onConnect(elementName, remote: rpc.IRemoteObject): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onConnect callback');
    if (remote === null) {
      hilog.info(DOMAIN_NUMBER, TAG, `onConnect remote is null`);
      return;
    }
    // 通过remote进行通信
  },
  onDisconnect(elementName): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onDisconnect callback');
  },
  onFailed(code: number): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onFailed callback', JSON.stringify(code));
  }
};


@Entry
@Component
struct ConnectAppServiceExt {
  build() {
    Column() {
    // ···
      List({ initialIndex: 0 }) {
        ListItem() {
          Row() {
            // ···
          }
        // ···
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
            // 建立连接后返回的Id需要保存下来，在解绑服务时需要作为参数传入
            connectionId = context.connectAppServiceExtensionAbility(want, options);
            // 成功连接后台服务
            this.getUIContext().getPromptAction().showToast({
              message: 'SuccessfullyConnectBackendService'
            });
            hilog.info(DOMAIN_NUMBER, TAG, `connectionId is : ${connectionId}`);
          })
        }


        // ···
      }


    // ···
    }


    // ···
  }
}
ConnectAppServiceExt.ets

使用disconnectAppServiceExtensionAbility()断开与后台服务的连接。

import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';


const TAG: string = '[DisConnectAppServiceExt]';
const DOMAIN_NUMBER: number = 0xFF00;


let connectionId: number;


@Entry
@Component
struct DisConnectAppServiceExt {
  build() {
    Column() {
    // ···
      List({ initialIndex: 0 }) {
        ListItem() {
          Row() {
            // ···
          }
        // ···
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
            // connectionId为调用connectServiceExtensionAbility接口时的返回值，需开发者自行维护
            context.disconnectAppServiceExtensionAbility(connectionId).then(() => {
              hilog.info(DOMAIN_NUMBER, TAG, 'disconnectAppServiceExtensionAbility success');
              // 成功断连后台服务
              this.getUIContext().getPromptAction().showToast({
                message: 'SuccessfullyDisconnectBackendService'
              });
            }).catch((error: BusinessError) => {
              hilog.error(DOMAIN_NUMBER, TAG, 'disconnectAppServiceExtensionAbility failed');
            });
          })
        }


        // ···
      }


    // ···
    }


    // ···
  }
}
DisConnectAppServiceExt.ets
客户端与服务端通信

客户端在onConnect()中获取到rpc.IRemoteObject对象后便可与服务端进行通信。

客户端：使用sendMessageRequest接口向服务端发送消息。

import { common, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';


const TAG: string = '[ClientServerExt]';
const DOMAIN_NUMBER: number = 0xFF00;
const REQUEST_CODE = 1;
let connectionId: number;
let want: Want = {
  deviceId: '',
  bundleName: 'com.samples.appserviceextensionability',
  abilityName: 'MyAppServiceExtAbility'
};
let options: common.ConnectOptions = {
  onConnect(elementName, remote): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onConnect callback');
    if (remote === null) {
      hilog.info(DOMAIN_NUMBER, TAG, `onConnect remote is null`);
      return;
    }
    let option = new rpc.MessageOption();
    let data = new rpc.MessageSequence();
    let reply = new rpc.MessageSequence();


    // 写入请求数据
    data.writeInt(1);
    data.writeInt(2);


    remote.sendMessageRequest(REQUEST_CODE, data, reply, option).then((ret: rpc.RequestResult) => {
      if (ret.errCode === 0) {
        hilog.info(DOMAIN_NUMBER, TAG, `sendRequest got result`);
        let sum = ret.reply.readInt();
        hilog.info(DOMAIN_NUMBER, TAG, `sendRequest success, sum:${sum}`);
      } else {
        hilog.error(DOMAIN_NUMBER, TAG, `sendRequest failed`);
      }
    }).catch((error: BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, `sendRequest failed, ${JSON.stringify(error)}`);
    });
  },
  onDisconnect(elementName): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onDisconnect callback');
  },
  onFailed(code): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'onFailed callback');
  }
};


// 调用connectAppServiceExtensionAbility相关代码


@Entry
@Component
struct ClientServerExt {
  build() {
    Column() {
    // ···
      List({ initialIndex: 0 }) {
        ListItem() {
          Row() {
            // ···
          }
        // ···
          .onClick(() => {
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext; // UIAbilityContext
            connectionId = context.connectAppServiceExtensionAbility(want, options);
            hilog.info(DOMAIN_NUMBER, TAG, `connectionId is : ${connectionId}`);
          })
        }
      }
    // ···
    }
  }
}
ClientServerExt.ets

服务端：使用onRemoteMessageRequest接口接收客户端发送的消息。

import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';


const TAG: string = '[MyAppServiceExtAbility]';
const DOMAIN_NUMBER: number = 0xFF00;


// 开发者需要在这个类型里对接口进行实现
class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(code: number,
    data: rpc.MessageSequence,
    reply: rpc.MessageSequence,
    options: rpc.MessageOption): boolean | Promise<boolean> {
    hilog.info(DOMAIN_NUMBER, TAG, 'onRemoteMessageRequest');
    let sum = data.readInt() + data.readInt();
    reply.writeInt(sum);
    return true;
  }
}


// 服务端实现
export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
  onCreate(want: Want): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onCreate');
  }


  onDestroy(): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onDestroy');
  }


  onConnect(want: Want): rpc.RemoteObject {
    hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onConnect');
    return new Stub('test');
  }


  onDisconnect(): void {
    hilog.info(DOMAIN_NUMBER, TAG, 'MyAppServiceExtAbility onDisconnect');
  }
}
MyAppServiceExtAbility.ets
服务端对客户端身份校验

部分开发者需要使用AppServiceExtensionAbility组件提供一些较为敏感的服务，可以通过如下方式对客户端身份进行校验。

通过callerTokenId对客户端进行鉴权

通过调用getCallingTokenId()接口获取客户端的tokenID，再调用verifyAccessTokenSync()接口判断客户端是否有某个具体权限，由于当前不支持自定义权限，因此只能校验当前系统所定义的权限。示例代码如下：

import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
import { abilityAccessCtrl, bundleManager } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';


const TAG: string = '[AppServiceExtImpl]';
const DOMAIN_NUMBER: number = 0xFF00;


// 开发者需要在这个类里进行实现


class Stub extends rpc.RemoteObject {
  onRemoteMessageRequest(
    code: number,
    data: rpc.MessageSequence,
    reply: rpc.MessageSequence,
    options: rpc.MessageOption): boolean | Promise<boolean> {
    // 开发者自行实现业务逻辑
    hilog.info(DOMAIN_NUMBER, TAG, `onRemoteMessageRequest: ${data}`);
    let callerUid = rpc.IPCSkeleton.getCallingUid();
    bundleManager.getBundleNameByUid(callerUid).then((callerBundleName) => {
      hilog.info(DOMAIN_NUMBER, TAG, 'getBundleNameByUid: ' + callerBundleName);
      // 对客户端包名进行识别
      if (callerBundleName !== 'com.samples.stagemodelabilitydevelop') { // 识别不通过
        hilog.info(DOMAIN_NUMBER, TAG, 'The caller bundle is not in trustlist, reject');
        return;
      }
      // 识别通过，执行正常业务逻辑
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN_NUMBER, TAG, 'getBundleNameByUid failed: ' + err.message);
    });


    let callerTokenId = rpc.IPCSkeleton.getCallingTokenId();
    let accessManager = abilityAccessCtrl.createAtManager();
    // 所校验的具体权限由开发者自行选择，此处ohos.permission.GET_BUNDLE_INFO_PRIVILEGED只作为示例
    let grantStatus = accessManager.verifyAccessTokenSync(callerTokenId, 'ohos.permission.GET_BUNDLE_INFO_PRIVILEGED');
    if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION_DENIED) {
      hilog.error(DOMAIN_NUMBER, TAG, 'PERMISSION_DENIED');
      return false;
    }
    hilog.info(DOMAIN_NUMBER, TAG, 'verify access token success.');
    return true;
  }
}


export default class MyAppServiceExtAbility extends AppServiceExtensionAbility {
  onConnect(want: Want): rpc.RemoteObject {
    return new Stub('test');
  }
  // 其他生命周期
}
MyAppServiceExtAbility.ets
EmbeddedUIExtensionAbility
使用AgentExtensionAbility组件实现智能体服务
