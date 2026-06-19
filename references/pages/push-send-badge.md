# 推送角标消息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-send-badge_

场景介绍

角标场景化消息仅适用于应用已开通category=IM（即时聊天）通知消息自分类权益的多端角标同步场景。该功能主要用于设置应用角标上的数字，终端仅展示应用桌面的角标，从而提醒用户查看应用内的消息更新。

约束与限制

推送角标消息能力支持Phone、Tablet、PC/2in1设备。

开通权益

推送角标消息需要应用开通即时聊天通知消息自分类权益。请参见申请通知消息自分类权益。

频控规则

调测阶段，每个项目每日全网最多可推送1000条测试消息。发送测试消息需设置testMessage为true。

正式发布阶段，单设备单应用下每日推送消息总条数受设备消息频控限制，系统会根据现网使用场景和流量进行管控，不合理的使用场景系统会进行频控。

开发步骤

参见指导获取Push Token。

应用服务端调用REST API推送角标消息，消息详情可参见场景化消息API接口功能介绍。

说明

发送角标消息时，payload.notification中不可携带title和body字段。

应用开通category=IM的通知消息自分类权益即可发送角标消息，发消息时无需携带category参数，未申请category=IM自分类权益的应用不可以发送角标消息。

请使用V3版本的请求URL（https://push-api.cloud.huawei.com/v3/[projectId]/messages:send）进行消息推送。

请求示例如下：

// Request URL
POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 0

// Request Body
{
  "payload": {
    "notification": {
      "badge" :
      {
        "setNum" : 99
      }
    }
  },
  "target": {
    "token": ["MAMzLg**********lPW"]
  },
  "pushOptions": {
    "testMessage": true
  }
}

[projectId]：项目ID，登录AppGallery Connect网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。

Authorization：JWT格式字符串，可参见Authorization获取。

push-type：0表示角标消息场景。

setNum：表示应用要显示的角标数量，取值为大于等于0小于100的整数。

token：Push Token，可参见获取Push Token获取。

testMessage：（选填）测试消息标识，true表示测试消息。每个项目每天限制发送1000条测试消息，单次推送可发送Token数不超过10个。详情请参见testMessage。

通过观察应用的角标数字是否更新为预期值，以验证设备是否收到角标消息。

## Code blocks

### Code block 1

```
// Request URL
POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"

// Request Header
Content-Type: application/json
Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 0

// Request Body
{
  "payload": {
    "notification": {
      "badge" :
      {
        "setNum" : 99
      }
    }
  },
  "target": {
    "token": ["MAMzLg**********lPW"]
  },
  "pushOptions": {
    "testMessage": true
  }
}
```
