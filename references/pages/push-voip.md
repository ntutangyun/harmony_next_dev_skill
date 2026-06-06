# 推送应用内通话消息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-voip_

****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 10


// Request Body
{
  "pushOptions": {
    "ttl": 30
  },
  "payload": {
    "extraData": "{\"scene\": \"voice\"}"
  },
  "target": {
    "token": ["MAMzLg**********aZW"]
  }
}
[projectId]：项目ID，登录AppGallery Connect网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
Authorization：JWT格式字符串，可参见基于服务账号生成鉴权令牌进行获取。
push-type：10表示应用内通话消息场景。
token：Push Token，可参见获取Push Token章节获取。
extraData：携带的额外数据，字符串类型。详情参见VoIPCallPayload 应用内通话消息中extraData参数用法。extraData数据获取请参考示例代码。
ttl：消息缓存时间，建议设置为30~60秒，详见pushOptions.ttl。
说明

应用内通话消息只能用于音视频通话场景唤醒应用，完成呼叫，不要通过此种类型消息来挂断来电或者和应用通信，应用应该使用自己建立的网络连接和应用通信。相比应用服务器推送Push消息，使用现有的网络连接和应用通信通常会更快，在网络不佳的情况下，推送的Push消息可能无法到达应用。

应用无论是否在前台，自己的网络连接存在时，建议您通过Push推送应用内通话消息，再通过自己的网络连接发送通话消息，保证该呼叫能够到达应用。

未接来电通知

如果您需要给被叫方发送未接来电通知，应用服务器可以调用REST API推送通知消息。以通知消息为例，请求示例如下：

// Request URL
POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"
   
// Request Header
Content-Type: application/json
Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 0
   
// Request Body
{
  "pushOptions": {
    "ttl":86400
  },
  "payload": {
    "notification": {
      "category": "MISS_CALL",
      "title": "通知标题",
      "body": "通知内容",
      "clickAction": {
        "actionType": 0
      },
      "appMessageId": "12345"
    }
   },
   "target": {
     "token": ["MAMzLg**********aZW"]
   }
 }
push-type：0表示通知消息场景。
category：消息自分类类别，设置为MISS_CALL，请参见参数说明，发送消息前请确保您已申请通知消息自分类权益。
appMessageId：应用消息的唯一标识。被叫挂断，被叫方VoIP应用在前台时应用可以通过调用Notification Kit（用户通知服务）发送未接来电通知。被叫方VoIP应用在后台时，可以通过Push推送未接来电通知。应用可能存在前后台状态判断不准确，同一电话会产生两条未接来电，建议您通过Notification Kit和Push Kit推送的未接来电通知使用相同的appMessageId，系统会进行通知去重。
其他参数说明可参见通知消息请求体参数说明。
推送实况窗消息
端云调试
