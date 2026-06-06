# 白平衡设置(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-whitebalance_

从API version 20开始，支持设置白平衡效果。白平衡是相机的色彩校正技术，通过设置白平衡，使照片产生不同的效果。目前白平衡效果支持：拍照（PhotoSession）、录像（VideoSession）和安全相机模式（SecureSession）。

开发步骤

详细的API说明请参考Camera。

导入camera接口，接口中提供相机相关的属性和方法。

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';

白平衡的设置提供两种方法。

方法一：通过isWhiteBalanceModeSupported判断是否支持该白平衡模式。再通过setWhiteBalanceMode和getWhiteBalanceMode分别设置和查看白平衡模式（只能查看当前已设置的白平衡模式）。该接口提供白平衡模式设置，目前包括：自动，手动，阴天、白炽光、荧光和日光。当同时设置白平衡模式和设置白平衡值时，仅可生效一种，默认白平衡模式优先生效。

function isWhiteBalanceModeSupported(session: camera.PhotoSession | camera.VideoSession): boolean {
   let status: boolean = false;
   let whiteBalanceMode: camera.WhiteBalanceMode | undefined = undefined;
   try {
      let mode: camera.WhiteBalanceMode = camera.WhiteBalanceMode.DAYLIGHT;
      status = session.isWhiteBalanceModeSupported(mode);
      if(status){
         session.setWhiteBalanceMode(mode);
      }
      whiteBalanceMode = session.getWhiteBalanceMode();
   } catch (error) {
      let err = error as BusinessError;
      console.error(`The isWhiteBalanceModeSupported call failed. error code: ${err.code}`);
   }
   return status;
}

方法二：通过getWhiteBalanceRange接口，获取当前设备支持的白平衡值范围。再通过setWhiteBalance和getWhiteBalance分别设置和查看白平衡值（只能查看当前已设置的白平衡值）。

function getWhiteBalanceRange(session: camera.PhotoSession | camera.VideoSession): Array<number> {
   let range: Array<number> = [];
   try {
      range = session.getWhiteBalanceRange();
      let whiteBalance: number = 3000;
      if(whiteBalance >= range[0] && whiteBalance <= range[1]) {
         session.setWhiteBalance(whiteBalance);
      }
      whiteBalance = session.getWhiteBalance();
   } catch (error) {
     let err = error as BusinessError;
     console.error(`The getWhiteBalanceRange call failed. error code: ${err.code}`);
   }
   return range;
}
自动切换摄像头实践(ArkTS)
压力管控(ArkTS)
