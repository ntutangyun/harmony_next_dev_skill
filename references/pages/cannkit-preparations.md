# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparations_

推荐使用Ubuntu 22.04及以上版本、MacOS 10.14及以上版本、Windows 10及以上版本安装应用开发环境DevEco Studio。

准备训练好的tools_omg模型转换工具生成的离线模型或者从Model Zoo中选择合适的模型。

Tools下载
Tools名称	Tools说明	Tools下载	SHA256校验码


轻量化工具

包名：tools_dopt

	对原始模型进行轻量化，以减少模型体积及加快模型推理速度。	DDK-tools-6.0.1.0	1b2822fb9e5fe7443782915c6f34b4a2ce5c028207e7782514bd93970ff8e48a


OMG工具

包名：tools_omg

	模型转换工具。	DDK-tools-6.0.1.0	1b2822fb9e5fe7443782915c6f34b4a2ce5c028207e7782514bd93970ff8e48a


AscendC工具

包名：tools_ascendc

	为AscendC算子开发提供的算子功能、性能调测集成工具。	DDK-tools-6.0.1.0	1b2822fb9e5fe7443782915c6f34b4a2ce5c028207e7782514bd93970ff8e48a


平台插件包

包名：

kirin9020

	AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。	kirin9020-plugin-6.0.1.0	b0657b18d30d59fff6d6a64eb7af93e63668a921936e66a48e692ab943eb2687


平台插件包

包名：

kirinx90

	AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。	kirinx90-plugin-6.0.1.0	a3bd6872367ca370d20d392840ae5dd19c517206c48a459b531b96e0f18000a7


平台插件包

包名：

kirin9030

	AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。	kirin9030-plugin-6.0.1.0	3b32effc5af9804628cb9287e88cc28ed381877adb15dd85bf8d66e3be805251

开源软件声明：CANN Kit 6.0.1.0 Open Source Software Notice.doc。

CANN Kit简介
模型优化
