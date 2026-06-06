# 跨设备文件拷贝

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-copy-across-devices_

. `);
    console.info(`src: ${srcUri} dest: ${destUri}`);
  }).catch((error: BusinessError)=>{
    let err: BusinessError = error as BusinessError;
    console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
  })
} catch (error) {
  console.error(`Catch err. Failed to copy. Code: ${error.code}, message: ${error.message}`);
}
Index.ets

B设备在获取A设备沙箱文件时，从B设备的分布式目录下将对应的文件拷贝走，以此完成跨设备拷贝。

import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileUri } from '@kit.CoreFileKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit';
// ···
let pathDir: string = context.filesDir;
let distributedPathDir: string = context.distributedFilesDir;
// 待拷贝文件的目标路径(沙箱路径)
let destPath: string = pathDir + '/dest.txt';
// 获取目标路径uri
let destUri = fileUri.getUriFromPath(destPath);


// 拷贝源文件路径(分布式目录)
let srcPath = distributedPathDir + '/src.txt';
// 获取源路径uri
let srcUri: string = fileUri.getUriFromPath(srcPath);


// 定义拷贝回调
let progressListener: fileIo.ProgressListener = (progress: fileIo.Progress) => {
  console.info(`progressSize: ${progress.processedSize}, totalSize: ${progress.totalSize}`);
};
let options: fileIo.CopyOptions = {
  'progressListener' : progressListener
};
// 通过分布式设备管理的接口获取设备A的networkId信息
let dmInstance = distributedDeviceManager.createDeviceManager('com.example.hap');
let deviceInfoList: distributedDeviceManager.DeviceBasicInfo[] = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`success to get available device list`);
  let networkId = deviceInfoList[0].networkId; // 这里只是两个设备连接，列表中首个即为A设备的networkId
  // 定义访问分布式目录的回调
  let listeners : fileIo.DfsListeners = {
    onStatus: (networkId: string, status: number): void => {
      console.error(`Failed to access public directory，${status}`);
    }
  };
  // 开始跨设备文件拷贝
  fileIo.connectDfs(networkId, listeners).then(()=>{
    try {
      // 将分布式目录下的文件拷贝到其他沙箱路径下
      fileIo.copy(srcUri, destUri, options).then(()=>{
        console.info(`Succeeded in copying from distributed path`);
        console.info(`src: ${srcUri} dest: ${destUri}`);
        fileIo.unlinkSync(srcPath); // 拷贝完成后清理分布式目录下的临时文件
      }).catch((error: BusinessError)=>{
        let err: BusinessError = error as BusinessError;
        console.error(`Failed to copy. Code: ${err.code}, message: ${err.message}`);
      })
    } catch (error) {
      console.error(`Catch err. Failed to copy. Code: ${error.code}, message: ${error.message}`);
    }
  }).catch((error: BusinessError) => {
    let err: BusinessError = error as BusinessError;
    console.error(`Failed to connect dfs. Code: ${err.code}, message: ${err.message}`);
  });
}
Index.ets

跨设备文件拷贝完成，断开链路。

import { BusinessError } from '@kit.BasicServicesKit';
import { distributedDeviceManager } from '@kit.DistributedServiceKit'
import { fileIo } from '@kit.CoreFileKit';
// 获取设备A的networkId
// ···
let dmInstance = distributedDeviceManager.createDeviceManager('com.example.hap');
let deviceInfoList: distributedDeviceManager.DeviceBasicInfo[] = dmInstance.getAvailableDeviceListSync();
if (deviceInfoList && deviceInfoList.length > 0) {
  console.info(`Success to get available device list`);
  let networkId = deviceInfoList[0].networkId;
  // 关闭跨设备文件访问
  fileIo.disconnectDfs(networkId).then(() => {
    console.info(`Success to disconnect dfs`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to disconnect dfs. Code: ${err.code}, message: ${err.message}`);
  })
}
Index.ets
跨设备文件共享和访问
端云文件协同
