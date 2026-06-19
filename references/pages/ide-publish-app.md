# 发布应用

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-publish-app_

HarmonyOS通过数字证书与Profile文件等签名信息来保证应用/元服务的完整性，应用/元服务上架到AppGallery Connect（AGC）必须通过签名校验。因此，您需要使用发布证书和Profile文件对应用/元服务进行签名后才能发布。

26.0.0 Beta1以下的版本，开发者需要准备签名所需的密钥、证书请求文件、发布证书、Profile文件等，对应用进行手动签名和编译构建后，将软件包上传到AGC。

从26.0.0 Beta1版本开始，开发者只需将应用进行编译构建后上传到AGC。在上传的过程中，无论应用之前是否已签名，DevEco Studio都会对应用重新进行签名，支持使用AGC自动生成的云管理证书，也支持使用开发者创建的证书。

26.0.0 Beta1及以上版本

[h2]编译构建.app文件

须知

应用上架时，要求应用包类型为Release类型。

说明

构建模式是<Default>时，构建APP包，默认Release模式；构建HAP/HSP/HAR包，默认Debug模式。更多说明请参考构建模式。

[h2]上传软件包

约束与限制

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

该功能将会把您的应用包传至AppGallery Connect用于测试或上架。为了您的信息安全，请勿上传带有个人敏感信息的数据（如密码、源代码、私钥、调试安装包、业务日志等信息）。

仅支持上传工程build/outputs目录下的软件包，上传前请确保工程已构建App包。

操作步骤

AppGallery Connect：使用云管理证书和Profile，对应用重新签名；将软件包上传到AGC用于测试和发布，同时上传符号表信息。

Testing Only：使用云管理证书和Profile，对应用重新签名；将软件包上传到AGC用于测试，同时上传符号表信息。

Custom：自定义上传配置。

Project：项目名称，可创建新项目或选择团队已有项目。

App type：应用类型，从软件包中获取。

App name：应用名称。

App package name：应用包名，从软件包中获取。

App category：应用分类。

Device Type：设备类型。

Language：默认语言。

各选项更多说明请参考为HarmonyOS应用创建APP ID。

各选项更多说明请参考为APP ID关联创建待发布的HarmonyOS应用。

应用已在AGC注册并且已关联创建待发布的应用，选择AppGallery Connect或Testing Only的上传类型，会跳转至步骤8查看软件包上传结果；选择Custom上传类型，进入下一步配置软件包的使用场景。

Upload to AppGallery Connect for test and publish：上传的软件包用于测试和发布。

Upload to AppGallery Connect for test：上传的软件包用于测试。

Upload Symbol table：上传符号表。

Manage Build Version：自动管理构建版本，Build Version值由AGC计算后更新。

Automatically manage signing：自动管理签名，使用云管理证书和Profile，对应用重新签名。

Manually manage signing：手动管理签名，开发者自行配置签名信息。

创建证书，操作界面如下，各选项含义和填写要求请参考生成密钥和证书请求文件。创建完成后，在AGC申请发布Profile。

导入证书，则需要导入本地已有的密钥库文件（.p12的密钥库文件）和证书（.cer文件）。

导入Profile，在本地选择与证书匹配的.p7b文件，或在AGC下载Profile后导入。

下载Profile，开发者可以选择.p7b文件，选择后会从AGC下载到本地。

[h2]发布.app文件到应用市场

将HarmonyOS应用/元服务打包成.app文件后上架到应用市场，发布详细操作指导请参考发布HarmonyOS应用或发布元服务。

26.0.0 Beta1以下版本

[h2]发布流程

开发者完成HarmonyOS应用/元服务开发后，需要将应用/元服务打包成App Pack（.app文件），用于上架到AppGallery Connect。发布应用/元服务的流程如下图所示：

[h2]生成密钥和证书请求文件

HarmonyOS应用/元服务通过数字证书（.cer文件）和Profile文件（.p7b文件）来保证应用/元服务的完整性。在申请数字证书和Profile文件前，需要提前生成密钥（存储在格式为.p12的密钥库文件中）和证书请求文件（.csr文件）。

密钥：包含非对称加密中使用的公钥和私钥，存储在密钥库文件中，格式为.p12，公钥和私钥对用于数字签名和验证。

证书请求文件：格式为.csr，全称为Certificate Signing Request，包含密钥对中的公钥和公共名称、组织名称、组织单位等信息，用于向AppGallery Connect申请数字证书。

数字证书：格式为.cer，由AppGallery Connect颁发。

Profile文件：格式为.p7b，包含HarmonyOS应用/元服务的包名、数字证书信息、描述应用/元服务允许申请的证书权限列表，以及允许应用/元服务调试的设备列表（如果应用/元服务类型为Release类型，则设备列表为空）等内容，每个应用/元服务包中均必须包含一个Profile文件。

当前支持通过DevEco Studio和CertificateTool两种方式生成密钥和证书请求文件。

说明

CertificateTool生成密钥和证书请求文件的操作界面与DevEco Studio 6.1.0 Beta2及以上版本一致，文档以DevEco Studio进行说明。

使用CertificateTool生成时，操作界面中各选项的含义和填写要求请参考DevEco Studio 6.1.0 Beta2及以上版本。

DevEco Studio 6.1.0 Beta2及以上版本

说明

如果本地已有对应的密钥，无需新生成密钥，可以在Generate Key界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。

Keystore Name：填写p12文件名称，仅允许包含字母、数字、下划线（_）、中划线（-）、句点（．）。

Select file save path：设置密钥库文件存储路径。

Key store Password：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。

Confirm password：再次输入密钥库密码。

Alias：密钥别名。请记住该别名，后续签名配置需要使用。

Validity(years)：选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。

First and last name：选填，通用名称，可填写应用名称或开发者姓名等。

Organizational unit：选填，组织单位，可填写部门名称或个人开发等。

Organization：选填，组织名称，可填写公司全称或开发者姓名等。

City or locality：选填，城市或地区。

State or province：选填，州或省。

Country code(XX)：选填，国家码。

说明

First and last name、Organizational unit、Organization、City or locality、State or province填写要求小于64个字符，不可使用双引号（"）、单引号（`）、斜杠（\）。

CSR File Name：填写CSR文件名称，仅允许包含字母、数字、下划线（_）、中划线（-）、句点（．）。

Select file save path：设置CSR文件存储路径。

DevEco Studio 6.1.0 Beta2以下版本

说明

如果本地已有对应的密钥，无需新生成密钥，可以在Generate Key界面中单击下方的Skip跳过密钥生成过程，直接使用已有密钥生成证书请求文件。

Key Store File：设置密钥库文件存储路径，并填写p12文件名。

Password：设置密钥库密码，必须由大写字母、小写字母、数字和特殊符号中的两种以上字符的组合，长度至少为8位。请记住该密码，后续签名配置需要使用。

Confirm Password：再次输入密钥库密码。

Alias：必填，别名，用于标识密钥名称。请记住该别名，后续签名配置需要使用。

Password：必填，密码，与密钥库密码保持一致，无需手动输入。

Validity(years)：选填，证书有效期，建议设置为25年及以上，覆盖应用/元服务的完整生命周期。

First and last name：选填，通用名称，可填写应用名称或开发者姓名等。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。

Organizational unit：选填，组织单位，可填写部门名称或个人开发等。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。

Organization：选填，组织名称，可填写公司全称或开发者姓名等。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。

City or locality：选填，城市或地区。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。

State or province：选填，州或省。字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。

Country code(XX)：选填，国家码。

说明

First and last name、Organizational unit、Organization、City or locality、State or province要求：字符长度为（0，64），且不可使用（双引号）"、（斜杠）\、（反引号）`。

[h2]申请发布证书和发布Profile文件

创建HarmonyOS应用/元服务。在AGC中创建一个HarmonyOS应用/元服务，用于申请发布证书和Profile文件，具体请参考创建HarmonyOS应用和创建元服务。

申请发布证书和发布Profile文件。在AGC中申请、下载发布证书和Profile文件，具体请参考申请发布证书和申请发布Profile。

说明

如果申请元服务的签名证书，在“创建应用”操作时，“是否元服务”选项请选择“是”。

使用发布证书和发布Profile文件进行手动签名，只能用来打包应用上架，不能用来运行调试工程。

[h2]配置签名信息

使用制作的私钥（.p12）文件、在AppGallery Connect中申请的证书（.cer）文件和Profile（.p7b）文件，在DevEco Studio配置工程的签名信息，构建携带发布签名信息的APP。

Store File：选择密钥库文件，文件后缀为.p12。

Store Password：输入密钥库密码。

Key Alias：输入密钥的别名信息。

Key Password：输入密钥的密码。

Sign Alg：签名算法，固定为SHA256withECDSA。

Profile File：选择申请的发布Profile文件，文件后缀为.p7b。

Certpath File：选择申请的发布数字证书文件，文件后缀为.cer。

设置完签名信息后，单击OK进行保存，然后使用DevEco Studio生成APP，请参考编译构建.app文件。

[h2]编译构建.app文件

须知

应用上架时，要求应用包类型为Release类型。

说明

当未指定构建模式时，构建APP包，默认Release模式；构建HAP/HSP/HAR包，默认Debug模式。

即Build APP(s)时，默认构建的APP包为Release类型，符合上架要求，开发者无需进行另外设置。

[h2]上传软件包

DevEco Studio 5.0.5.200版本开始，支持在DevEco Studio内上传应用软件包。上传软件包前，请先创建应用。

约束与限制

该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

该功能将会把您的应用包传至AppGallery Connect用于测试或上架。为了您的信息安全，请勿上传带有个人敏感信息的数据（如密码、源代码、私钥、调试安装包、业务日志等信息）。

仅Build Mode为Release的应用支持上传软件包，且确保软件包已配置Release签名。

同时支持通过AppGallery Connect上传软件包。

操作步骤

若当前上传的软件包仅做测试发布，请选择Generate app package and upload it to AppGallery Connect for test。

若软件包需要在全网正式发布，请选择Generate app package and upload it to AppGallery Connect for test and publish。

说明

如需上传符号表信息，请勾选Upload your app's symbols选项。

上传的product可以通过点击DevEco Studio编辑区域右上方图标进行查看及切换。

可通过app.json5中bundleName/versionName字段修改当前product对应的包名/版本号信息。必须使用当前开发者账号下已在AppGallery注册且真实存在的包名。

Build Version值由AGC计算后回传填入。

[h2]发布.app文件到应用市场

将HarmonyOS应用/元服务打包成.app文件后上架到应用市场，发布详细操作指导请参考发布HarmonyOS应用或发布元服务。

附录

[h2]CertificateTool下载

平台	包名	版本号	SHA256校验码	更新时间
Windows(64-bit)	certificate-tool-windows-x64-1.0.0.1.zip	1.0.0.1	dee6c2ae3b300fd7450bbeb2aadd96f1099ee5235ae627afcfad9b3ed3ded7da	2026/04/20
Mac(64-bit)	certificate-tool-mac-x64-1.0.0.1.zip	1.0.0.1	8afc53e6714cb7e8840114065012b5f706c265c056491c240e5433be311bf084	2026/04/20
Mac(ARM64)	certificate-tool-mac-arm64-1.0.0.1.zip	1.0.0.1	07283684624b11c2db0c2ce2654729b5114b3085df68736a43967eda247a7b4e	2026/04/20
