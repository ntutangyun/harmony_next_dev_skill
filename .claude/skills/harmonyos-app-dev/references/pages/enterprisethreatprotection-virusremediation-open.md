# 打开文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisethreatprotection-virusremediation-open_

当安全防护类应用（如病毒扫描、恶意软件检测等）需要对设备上的文件进行安全扫描时，可能会遇到目标文件位于应用沙箱外且应用没有直接读取权限的情况。此时，可通过文件打开接口获取目标文件的文件描述符（fd），使安全防护应用能够绕过权限限制，正常访问和扫描这些文件，确保设备整体安全性。

接口说明

详细接口说明可参考接口文档。

接口	描述
openFile(path: string): Promise<number>	获取指定路径文件的文件描述符fd。
开发步骤

导入模块。

// 导入企业威胁防护能力模块，用于调用openFile接口
import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';

通过调用接口openFile，获取目标文件的文件描述符（fd）。path参数为目标文件的绝对路径。

import { BusinessError } from '@kit.BasicServicesKit';


// 获取文件fd，查看打印结果
function openFilePromise() {
  // 目标文件路径，此处为示例路径，实际使用时需替换为用户指定的真实路径或通过参数传入
  let targetFilePath: string = '/example/path/to/file.txt';
  virusRemediation.openFile(targetFilePath).then((fd: number) => {
    console.info(`Succeeded in opening file. Path: ${targetFilePath}, FD: ${fd}.`);
    // 使用完fd后应记得关闭
  }).catch((err: BusinessError) => {
    // 根据错误码进行不同的业务处理
    if (err.code === 1023803001) {
      console.error('Access denied, please check if the file belongs to current user.');
    } else {
      console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
    }
  });
}
启动应用目录文件扫描任务
文件隔离
