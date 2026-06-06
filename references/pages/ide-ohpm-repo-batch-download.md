# ohpm

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-batch-download_

ohpm
|       @ohos+test-two@1.0.0.har
|       @ohos+test@1.0.0.har
|       pkgInfo.json
|
+---one
|       @ohos+test-four@1.0.0.har
|       @ohos+test-three@1.0.0.har
|       pkgInfo.json
|
+---two
|       @ohos+test-five@1.0.0.har
|       @ohos+test-six@1.0.0.har
|       pkgInfo.json
batch_download_1754735610304.zip中ohpm目录中pkgInfo.json结构
{
  "packageArray": [
    {
      "packageFile": "@ohos+test@1.0.0.har",
      "packageName": "@ohos/test@1.0.0",
      "user": "admin",
      "userId": "",
      "group": "ohos",
      "distTags": []
    },
    {
      "packageFile": "@ohos+test-two@1.0.0.har",
      "packageName": "@ohos/test-two@1.0.0",
      "user": "admin",
      "userId": "",
      "group": "ohos",
      "distTags": []
    }
  ]
}

执行以下命令从OpenHarmony三方库中心仓中批量下载包文件：

ohpm-repo batch_download <pkgInfo_xxxx.json地址> --public-registry <OpenHarmony三方库中心仓registry地址> --http-proxy <配置代理地址> --not-use-proxy <配置不使用代理>

结果示例：

PS D:\> ohpm-repo batch_download D:\pkgInfo_1754734313921.json --public-registry https://ohpm.openharmony.cn/ohpm/
...
[2025-08-09T18:49:38.833] [INFO] default - A total of 95 package(s) successfully obtain download url.
[2025-08-09T18:49:38.834] [INFO] default - A total of 95 package(s) are successfully downloaded.
[2025-08-09T18:49:38.834] [INFO] default - A total of 95 package(s) are converted successfully.
[2025-08-09T18:49:38.834] [INFO] default - Packing the .zip file. . .
[2025-08-09T18:49:39.820] [INFO] default - save the .zip file to : "D:\batch_download_1754736519129.zip".
[2025-08-09T18:49:39.820] [INFO] default - Clear the cache.
说明
如果ohpm-repo实例的数据存储类型为filedb，请执行ohpm-repo restart命令重启ohpm-repo服务，以便刷新ohpm-repo网站页面中的数据。该操作会影响正在使用ohpm-repo服务的用户，请提前告知。
生成的zip文件中以仓库名作为目录，每个仓库目录中存在pkgInfo.json文件，其中记录了每个包的文件名、包名、组织、上传者和Tag标签，用于在批量上传时准确指定ohpm-repo的数据库中某个用户为某个包的真实上传用户，同时将包的Tag标签一起上传。
当执行batch_download命令时，某个中心仓包的组织为A，若为其指定ohpm-repo的数据库中某用户为其真实上传用户，ohpm-repo实例中不存在A组织，则该包的真实上传用户将设定为空，并且提醒用户手动创建A组织。之后执行批量上传时同样会提醒该包的A组织在ohpm-repo实例中不存在，需要先手动创建A组织。如果需要自动添加组织，使用batch_publish命令的可选参数--force，将会选取一个管理员用户作为A组织负责人，自动创建A组织后进行该包的上传。
ohpm-repo export_pkginfo
ohpm-repo batch_publish
