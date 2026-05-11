# 撤回语音播报消息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-revoke-extend-noti_

****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 2
 
// Request Body
{
  "notifyId": 1234567,
  "token": [
    "pushToken1",
    "pushToken2",
    "pushToken3"
  ]
}
[clientId]：请替换为您应用的Client ID，可参见指导获取。
Authorization：JWT格式字符串，可参见Authorization获取。
push-type：2，表示语音播报消息场景。
notifyId：消息ID，消息的唯一标识，详情请参见notifyId。
token：Push Token，可参见获取Push Token获取。
发送语音播报消息
推送后台消息
