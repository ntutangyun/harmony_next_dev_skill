# 推送后台消息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-background_

****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 6


// Request Body
{
  "payload": {
    "extraData": "携带的额外数据",
    "proxyData": "ENABLE"
  },
  "target": {
    "token": ["MAMzLg**********lPW"]
  }
}
[projectId]：项目ID，登录AppGallery Connect网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
Authorization：JWT格式字符串，可参见Authorization获取。
push-type：6表示后台消息场景。
token：Push Token，可参见获取Push Token获取。
extraData：携带的额外数据，字符串类型。详情请参见extraData。
proxyData（选填）：进程不存在时是否开启数据代理静默写入到应用自身缓存，当前只能传全大写"ENABLE"开启代理。若您不希望开启代理写入，请不要在消息体中填写此字段。详情请参见proxyData。

当设备中的应用进程在前台时会直接拉起应用并将数据传递，您可以在receiveMessage()方法中获取消息数据。

当应用进程不在前台且proxyData为“ENABLE”时，Push Kit将后台消息写入到数据库中，建议应用进程在前台时将数据库中数据迁移到您业务数据库中（避免数据库大小无限制增长）。当应用进程不在前台且无proxyData时则为缓存消息（发送多条消息时仅缓存最新的一条），等下次应用进程在前台时调用getToken()接口，Push Kit将重新发送缓存消息，您可以在receiveMessage方法获取消息数据。

撤回语音播报消息
推送实况窗消息
