# 全局配置项功能场景

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/global-configuration-guide_

public lock: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock;
  public isLogin: boolean = false;
  public loginUser?: string;
  public wifiOn: boolean = false;


  async login(user: string) {
    return this.lock.lockAsync(() => {
      this.isLogin = true;
      this.loginUser = user;
    }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
  }


  async logout(user?: string) {
    return this.lock.lockAsync(() => {
      this.isLogin = false;
      this.loginUser = '';
    }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
  }


  async getIsLogin(): Promise<boolean> {
    return this.lock.lockAsync(() => {
      return this.isLogin;
    }, ArkTSUtils.locks.AsyncLockMode.SHARED)
  }


  async getUser(): Promise<string> {
    return this.lock.lockAsync(() => {
      return this.loginUser!;
    }, ArkTSUtils.locks.AsyncLockMode.SHARED)
  }


  async setWifiState(state: boolean) {
    return this.lock.lockAsync(() => {
      this.wifiOn = state;
    }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
  }


  async isWifiOn() {
    return this.lock.lockAsync(() => {
      return this.wifiOn;
    }, ArkTSUtils.locks.AsyncLockMode.SHARED)
  }
}


export let config = new Config();
Config.ets

UI主线程及子线程访问全局配置项。

import { config } from './Config';
import { taskpool } from '@kit.ArkTS';


@Concurrent
async function download() {
  if (!await config.isWifiOn()) {
    console.info('wifi is off');
    return false;
  }
  if (!await config.getIsLogin()) {
    console.info('not login');
    return false;
  }
  console.info(`User[${await config.getUser()}] start download ...`);
  return true;
}


@Entry
@Component
struct Index {
  @State message: string = 'not login';
  @State wifiState: string = 'wifi off';
  @State downloadResult: string = '';
  input: string = '';


  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
        TextInput({ placeholder: '请输入用户名' })
          .id('textInput')
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onChange((value) => {
            this.input = value;
          })
        Text('login')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(async () => {
            if (!await config.getIsLogin() && this.input) {
              this.message = 'login: ' + this.input;
              try {
                config.login(this.input);
              } catch (e) {
                console.error('login failed');
              }
            }
          })
          .backgroundColor(0xcccccc)
        Text('logout')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(async () => {
            if (await config.getIsLogin()) {
              this.message = 'not login';
              try {
                config.logout();
              } catch (e) {
                console.error('logout failed');
              }
            }
          })
          .backgroundColor(0xcccccc)
        Text(this.wifiState)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
        Toggle({ type: ToggleType.Switch })
          .onChange(async (isOn: boolean) => {
            await config.setWifiState(isOn)
            this.wifiState = isOn ? 'wifi on' : 'wifi off';
          })
        Text('download')
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(async () => {
            let ret = await taskpool.execute(download);
            this.downloadResult = ret ? 'download success' : 'download fail';
          })
        Text(this.downloadResult)
          .fontSize(20)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
GlobalConfigurationGuide.ets
业务模块并发加载场景
ArkUI数据更新场景
