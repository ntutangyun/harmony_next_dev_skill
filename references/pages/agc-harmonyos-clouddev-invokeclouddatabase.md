# 在端侧访问云数据库

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-invokeclouddatabase_

前提条件

请确保云数据库已正确开发并部署。

注意

云数据库部署成功后，DevEco Studio将自动从云侧下载云数据库的schema文件至“AppScope/resources/rawfile/schema.json”路径，该文件是云数据库端侧API必须引入的配置文件。

如果后续又在本地工程修改了对象类型，请重新部署云数据库，DevEco Studio将自动更新schema.json文件；如果后续在AGC云侧修改了对象类型，您需手动从AGC控制台导出schema.json文件，拷贝至本地工程的“AppScope/resources/rawfile”目录下。否则，可能导致schema.json文件中的对象类型和代码中的对象类型不一致，端侧访问云数据库时提示1008230002错误。

检查您的角色拥有的对象类型操作权限。如果未配置AccessToken，需要给World角色添加Upsert和Delete权限。

生成Client Model

在端侧通过Cloud Foundation Kit访问云数据库，需先引入对应云数据库对象类型的Client Model。

参考生成Client Model生成云数据库对象类型的端侧模型，如下图初始化代码中的Client Model示例“ets/pages/CloudDb/Post.ts”。

访问数据库

接下来您便可参考初始化数据库访问、查询数据、写入数据、删除数据等访问数据库。

“src/main/ets/pages/CloudDb”目录下提供了部分示例代码，更完整的接口信息请参考Cloud Foundation Kit API参考-云数据库模块。
