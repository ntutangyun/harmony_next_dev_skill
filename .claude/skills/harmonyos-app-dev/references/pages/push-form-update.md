# 推送卡片刷新消息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-form-update_

****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 1


// Request Body
{
    "payload": {
    "moduleName": "entry",
    "abilityName": "EntryFormAbility",
    "formName": "widget",
    "formId": 423434262,
    "version": 123456,
    "formData": {
      "text_key": "刷新文本内容"
    },
    "images": [
      {
        "keyName": "image_key",
        "url": "https://***.png",
        "require": 1
      }
    ]
  },
  "target": {
    "token": [
      "MAMzLg**********lPW"
    ]
  },
  "pushOptions": {
     "testMessage": true
  }
}

[projectId]：项目ID，登录AppGallery Connect网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。

Authorization：JWT格式字符串，可参见Authorization获取。

push-type：1表示服务卡片刷新场景。

moduleName：项目模块级别下的 src/main/module.json5 中的 module 标签下的name值。

abilityName：项目模块级别下的src/main/module.json5中的extensionAbilities标签下的服务卡片的ability名称。

formName：项目模块级别下的src/main/resources/base/profile/form_config.json中forms标签下服务卡片的名称。下图以卡片配置文件form_config为例：

version：当前卡片刷新消息的版本号，新的卡片刷新消息的版本号需大于当前卡片刷新消息版本号，否则会刷新失败。详情参见version。

formId：服务卡片的实例ID，当卡片的onAddForm()方法被调用时（卡片使用方添加卡片至桌面）进行获取。最大值为231-1。

formData：填写待刷新服务卡片的业务数据，该数据来源于项目模块级别下的src/main/ets/widget/pages/WidgetCard.ets文件下的声明式范式组件名称。下图以卡片页面文件WidgetCard为例：

images：待刷新服务卡片业务数据中的图片数据，其中keyName为您服务卡片中图片控件的key值，url为图片的地址，下图以卡片页面文件WidgetCard为例：

说明

Push Kit禁止推送包含敏感信息的图片。

支持图片的格式为PNG、JPG、JPEG、WEBP，图片文件最大为512KB，若超过则图片不展示。

require：图片刷新策略控制，“0”表示如果图片下载失败，仅刷新文字；“1”表示如果图片下载失败，则不进行刷新操作。

token：Push Token，可参见获取Push Token获取。

testMessage：（选填）测试消息标识，true表示测试消息。每个项目每天限制发送1000条测试消息，单次推送仅能发送一个Token。详情请参见testMessage。

撤回通知消息
推送语音播报消息
