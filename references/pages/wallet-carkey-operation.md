# 钥匙开通

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-operation_

如果queryPass接口返回1010220501 查询卡券不存在，则调用canAddPass接口检查当前设备是否支持添加车钥匙。

如果queryPass接口或是canAddPass接口返回1010200003 访问钱包的前置环境没有准备好，则调用initWalletEnvironment接口初始化钱包开通车钥匙的同意协议或是登录账号等必要条件，引导用户跳转钱包App完成应用初始化。

车主APP调用queryPassDeviceInfo接口查询设备类型，指定目标设备标识，提升安全性。

车主服务器预置模板后申请钥匙卡片以及JWE数据，参考车主服务器开发。

用户主动发起开卡时，车主APP跳转钱包应用，调用addPass接口携带上述流程中生成的编码后的JWE数据，开通车钥匙到钱包。

卡片激活的过程中钱包服务器需要和DK业务管理服务进行交互的包括：设备的认证（和车钥匙管理台交换证书信息）、获取请求个人化数据时的token（用于向车钥匙管理台请求Applet个人化数据）、以及最后的请求Applet个人化数据，最后写入安全芯片，参考车主服务器激活卡片。

车主APP可通过viewPass接口跳转钱包查看已开通的车钥匙详情页。

开发步骤

车主APP使用创建Wallet Kit服务时注册的服务号和申请钥匙卡片时定义的卡券唯一标识，车主APP调用queryPass接口检查当前设备车钥匙的开通情况。

import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建Wallet Kit服务时注册的服务号
  private passType: string = '';
  // 申请钥匙卡片时定义的卡券唯一标识
  private serialNumber: string = '';


  async queryPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    this.walletPassClient.queryPass(passStr).then((result: string) => {
      console.info(`Succeeded in querying pass, result: ${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to query pass, code:${err.code}, message:${err.message}`);
    })
  }


  build() {
    // your application UI
  }
}

如果queryPass接口返回1010220501 查询卡券不存在，则调用canAddPass接口检查当前设备是否支持添加车钥匙。

import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建Wallet Kit服务时注册的服务号
  private passType: string = '';
  // 目标设备类型 phone: 手机
  private targetDeviceType: string = '';


  async canAddPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.canAddPass(passStr).then((result: string) => {
      console.info(`Succeeded in checking addPass, result:${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to check addPass, code:${err.code}, message:${err.message}`);
    })
  }


  build() {
    // your application UI
  }
}

如果queryPass接口或是canAddPass接口返回1010200003 访问钱包的前置环境没有准备好，则调用initWalletEnvironment接口初始化钱包开通车钥匙的同意协议或是登录账号等必要条件，引导用户跳转钱包App完成应用初始化。

import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 目标设备类型 phone: 手机
  private targetDeviceType: string = '';


  async initWalletEnvironment() {
    let passStr = JSON.stringify({
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.initWalletEnvironment(passStr).then(() => {
      console.info(`Succeeded in initiating walletEnvironment`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to initiate walletEnvironment, code:${err.code}, message:${err.message}`);
    })
  }


  build() {
    // your application UI
  }
}

车主APP调用queryPassDeviceInfo接口查询设备类型，指定目标设备标识。

import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建Wallet Kit服务时注册的服务号
  private passType: string = '';
  // 目标设备类型 phone: 手机
  private targetDeviceType: string = '';


  async queryPassDeviceInfo() {
    let passStr = JSON.stringify({
      passType: this.passType,
      targetDeviceType: this.targetDeviceType
    });
    this.walletPassClient.queryPassDeviceInfo(passStr).then((result: string) => {
      console.info(`Succeeded in querying passDeviceInfo, result:${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to query passDeviceInfo, code:${err.code}, message:${err.message}`);
    })
  }


  build() {
    // your application UI
  }
}

车主服务器预置模板后申请钥匙卡片以及JWE数据，参考车主服务器开发。

用户主动发起开卡时，车主APP跳转钱包应用，调用addPass接口携带上述流程中生成的编码后的JWE数据，开通车钥匙到钱包。

import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 参考车主服务器开发生成的JWE数据
  private jweContent: string = '';


  async addPass() {
    let passStr = JSON.stringify({
      jweContent: this.jweContent
    });
    this.walletPassClient.addPass(passStr).then((result: string) => {
      console.info(`Succeeded in adding pass, result:${result}`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to add pass, code:${err.code}, message:${err.message}`);
    })
  }


  build() {
    // your application UI
  }
}

卡片激活的过程中钱包服务器需要和DK业务管理服务进行交互的包括：设备的认证（和车钥匙管理台交换证书信息）、获取请求个人化数据时的token（用于向车钥匙管理台请求Applet个人化数据）、以及最后的请求Applet个人化数据，最后写入安全芯片，参考车主服务器激活卡片。

车主APP可通过viewPass接口跳转钱包查看已开通的车钥匙详情页。

import { common } from '@kit.AbilityKit';
import { walletPass } from '@kit.WalletKit';


@Entry
@Component
struct Index {
  private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
  // 创建Wallet Kit服务时注册的服务号
  private passType: string = '';
  // 申请钥匙卡片时定义的卡券唯一标识
  private serialNumber: string = '';


  async viewPass() {
    let passStr = JSON.stringify({
      passType: this.passType,
      serialNumber: this.serialNumber
    });
    try {
      await this.walletPassClient.viewPass(passStr);
      console.info(`Succeeded in viewing pass`);
    } catch (err) {
      console.error(`Failed to view pass, code:${err.code}, message:${err.message}`);
    }
  }


  build() {
    // your application UI
  }
}
车主服务器开发

使用Intellij IDEA打开钱包服务-服务端卡片开通的示例代码，没有请先下载Intellij IDEA的当前最新版本。示例代码和工具下载完成后，目录结构如下，我们需要关注下图框出来几个文件：

打开resources/release.config.properties文件，替换真实的应用数据。

需替换的参数	参数说明
gw.appid	


gw.appid.secret	AppGallery Connect平台申请的Client ID和Client Secret分别填入gw.appid和gw.appid.secret
walletServerBaseUrl	固定填入服务器基地址：https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass
servicePrivateKey	创建Wallet Kit服务步骤5生成的私钥

打开resources/data/StdCarKeyModel.json文件，替换真实的应用数据，详细见预置模板的请求参数。

打开stdcarkey/StdCarKeyModelTest.java文件，运行createStdCarKeyModel方法，可看到控制台如下输出，详细见预置模板的响应参数。

打开resources/data/StdCarKeyInstance.json文件，替换真实的应用数据，详细见申请钥匙卡片的请求参数。

打开stdcarkey/StdCarKeyInstanceTest.java文件，运行addStdCarKeyInstance方法，可看到控制台如下输出，详细见申请钥匙卡片的响应参数。

车主服务器激活卡片

使用 Intellij IDEA打开钱包服务-服务端卡片激活的示例代码。示例代码和工具下载完成后，解决工程配置等问题后，Constants类中替换SERVER_PUBLIC_KEY和SERVER_SECRET_KEY为您在创建Wallet Kit服务步骤5生成的公钥和私钥，直接打开PassesController这个类。

设备认证对应类中的register方法，通过此方法进行设备认证。

获取个人化数据Token对应类中的requestToken方法，通过此方法获取个人化数据Token。

获取个人化数据对应类中的getPersonalInfo方法，重点看dealWithPersonalizeDataRequest中的getDevicePassData这个方法，查看ICCECarKeyDevicePassUnit的generatePassData方法，通过这些方法获取个人化数据。再深入打开里面的getPersonalizeData方法，根据此接口的说明进行生成。

云侧开发准备
车控
