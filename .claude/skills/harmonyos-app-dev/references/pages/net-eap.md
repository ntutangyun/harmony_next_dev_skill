# 扩展认证

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-eap_

在802.1X认证过程中，系统会将符合条件的EAP报文传递至callback函数（如示例代码中的eapData函数）中，供企业应用获取。报文传递至callback函数后，802.1X认证流程会阻塞等待，用户能够获取到完整的报文内容。

（1）若注册的是由服务器发送给客户端的报文类型（即eapCode=1），则此时可以从报文中看到由服务器加入的自定义内容。应用根据自定义内容，判断认证是否应该继续往后续步骤进行，并调用replyCustomEapData方法通知系统。

（2）若注册的报文类型是由客户端发给服务器的（即eapCode=2），则此时获取到的是原始的802.1X认证报文，应用需要在原始报文内容中加入自己的自定义内容，并将加入自定义内容后的报文内容调用replyCustomEapData方法通知系统。

（3）若注册的报文类型是服务器返回的成功（即eapCode=3）或失败（即eapCode=4）的结果，客户端可在接收到此结果之后做定制处理。

以下注册服务器发送给客户端的报文类型（即eapCode=1，eapType=25）为例，若需注册其他类型，修改eapCode值后再调用regCustomEapHandler方法即可。

let netType = 1;
let eapCode= 1; // eap request
let eapType= 25; // EAP_PEAP
let result = 1;


let eapData = (eapData:eap.EapData):void => {
  hilog.info(0x0000, 'testTag', 'rsp result',JSON.stringify(eapData));
  const newBuffer = new Uint8Array(eapData.bufferLen);
  newBuffer.set(eapData.eapBuffer, 0);
  let eapData2: eap.EapData = {
    msgId: eapData.msgId,
    eapBuffer: newBuffer,
    bufferLen: newBuffer.length
  }
  try{
    eap.replyCustomEapData(result, eapData2);
    hilog.info(0x0000, 'testTag', 'replyCustomEapData success');
  } catch (err) {
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ' , errMessage: ' + err.message);
  }
}
function serverReplyCustomEapData() {
  try{
    eap.regCustomEapHandler(netType, eapCode, eapType, eapData);
    hilog.info(0x0000, 'testTag', 'regCustomEapHandler success');
    // ...
  } catch (err) {
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + 'errMessage: ' + err.message);
    // ...
  }
}
AccreditationProcess.ets

若需取消定制化，可调用unregCustomEapHandler方法。

let netType = 1;
let eapCode= 1; // eap request
let eapType= 25; // EAP_PEAP
let result = 1;


let eapData = (eapData:eap.EapData):void => {
  hilog.info(0x0000, 'testTag', 'rsp result',JSON.stringify(eapData));
  const newBuffer = new Uint8Array(eapData.bufferLen);
  newBuffer.set(eapData.eapBuffer, 0);
  let eapData2: eap.EapData = {
    msgId: eapData.msgId,
    eapBuffer: newBuffer,
    bufferLen: newBuffer.length
  }
  // ...
}
// ...
  try {
    eap.unregCustomEapHandler(netType, eapCode, eapType, eapData);
    hilog.info(0x0000, 'testTag', 'unregCustomEapHandler success');
    // ...
  } catch (err) {
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
    // ...
  }
AccreditationProcess.ets
使用eth接口发起802.1X认证流程

设备通过硬件接口，插入网线。

从@kit.NetworkKit中导入eap命名空间。

import { eap } from '@kit.NetworkKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
EthInterface.ets

当企业管理软件需要进行认证，调用startEthEap方法时，会发起802.1X认证流程。

const netId: number = 100;
// ...
  let profile: eap.EthEapProfile = {
    eapMethod: eap.EapMethod.EAP_TTLS,
    phase2Method: eap.Phase2Method.PHASE2_AKA_PRIME,
    identity: 'identity',
    anonymousIdentity: 'anonymousIdentity',
    password: 'password',
    caCertAliases: 'caCertAliases',
    caPath: 'caPath',
    clientCertAliases: 'clientCertAliases',
    certEntry: new Uint8Array([5,6,7,8,9,10]),
    certPassword: 'certPassword',
    altSubjectMatch: 'altSubjectMatch',
    domainSuffixMatch: 'domainSuffixMatch',
    realm: 'realm',
    plmn: 'plmn',
    eapSubId: 1
  };


  try {
    eap.startEthEap(netId, profile);
    hilog.info(0x0000, 'testTag', 'startEthEap success');
    // ...
  } catch (err) {
    // ...
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
  }
EthInterface.ets

当企业管理软件需要退出认证状态，调用logOffEthEap方法，即会发起802.1X取消认证流程。

const netId: number = 100;
// ...
  try{
    eap.logOffEthEap(netId);
    hilog.error(0x0000, 'testTag', 'logOffEthEap success');
    // ...
  } catch (err) {
    // ...
    hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + ', errMessage: ' + err.message);
  }
EthInterface.ets
使用网络防火墙
Network Boost Kit（网络加速服务）
