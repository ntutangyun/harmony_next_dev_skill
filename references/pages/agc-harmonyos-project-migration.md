# 历史工程转换为端云一体化开发工程

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-project-migration_

如您此前已经创建了非端云一体化开发工程，希望直接转换为端云一体化开发工程，可执行如下操作：

创建一个端云一体化开发工程，其中工程的类型（HarmonyOS应用或元服务）必须与您历史工程类型一致，同时Bundle name必须指定为您历史工程的Bundle name。在创建端云一体化开发工程过程中，该Bundle name会关联到AGC应用、项目等云端资源。

将历史工程目录（如“MyApplication30”）拷贝至步骤3的端云一体化开发工程目录下，并改名为“Application”。

重新打开端云一体化开发工程，可发现历史工程的端侧代码已迁移至端云一体化开发工程。
