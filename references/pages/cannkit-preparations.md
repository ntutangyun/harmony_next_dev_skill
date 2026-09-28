# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparations_

环境准备

使用Ubuntu 64位运行Tools下载中的tools_omg模型转换工具。

推荐使用Ubuntu 22.04及以上版本、MacOS 10.14及以上版本、Windows 10及以上版本安装应用开发环境DevEco Studio。

准备训练好的tools_omg模型转换工具生成的离线模型或者从Model Zoo中选择合适的模型。

Tools下载

Tools名称	Tools说明	Tools下载	SHA256校验码
DDK工具包	DDK工具包包含tools_dopt、tools_omg、tools_ascendc和platform。 轻量化工具（tools_dopt）：对原始模型进行轻量化，以减少模型体积及加快模型推理速度。 OMG工具（tools_omg）：模型转换工具。 AscendC工具（tools_ascendc）：为AscendC算子开发提供的算子功能、性能调测集成工具。 platform：将对应平台插件包安装到platform目录下。	DDK-tools-next-6.1.1.0	87d7e3f186ad5c527a9385cea555559ea53c63b87dc483820523bcf7bf6f87e5
平台插件包 包名： kirin9020	AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。	kirin9020-plugin-next-6.1.1.0	da4ebea4ce88889d94f96baf7bde43ff178153d68425e24d4e0db5b25089aa3f
平台插件包 包名： kirinx90	AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。	kirinx90-plugin-next-6.1.1.0	0657efdddd2267949e83af2a382603b523d30b258d72e077a6975eb87d4f10b1
平台插件包 包名： kirin9030	AscendC工具提供不同平台的差异化能力，使用AscendC工具前需要将对应的平台安装到platform目录下。	kirin9030-plugin-next-6.1.1.0	5df8110e9b494ba87216b0c195c83d7f6c1407af89613de850ed7c569e57e593

开源软件声明：CANN Kit 6.1.1.0 Open Source Software Notice。
