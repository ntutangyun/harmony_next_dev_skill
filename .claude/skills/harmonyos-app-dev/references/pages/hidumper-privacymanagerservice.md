# PrivacyManagerService

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper-privacymanagerservice_

----------------------------[ability]-------------------------------




----------------------------------PrivacyManagerService----------------------------------
Privacy Dump:
Usage:
       -h: command help
       -t <TOKEN_ID>: according to specific token id dump permission used records
获取敏感权限使用记录信息

支持通过应用进程的tokenid，查看敏感权限使用记录的信息，可以通过下列命令实现。

hidumper -s PrivacyManagerService -a '-t <tokenId>'

命令所需的tokenId可以通过atm-tool进行查询。

使用样例：

hidumper -s PrivacyManagerService -a '-t 536992218'


-------------------------------[ability]-------------------------------




----------------------------------PrivacyManagerService----------------------------------
Privacy Dump:
{
  "permissionRecord": [
    {
      "bundleName": "com.ohos.camera",
      "isRemote": false,
      "permissionName": "ohos.permission.READ_IMAGEVIDEO",
      "lastAccessTime": 1508577149393,
      "lastAccessDuration": 0,
      "accessCount": 2
    }
  ]
}
hidumper
hitrace
