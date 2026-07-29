# 删除出行凭证

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-travel-scene-delete_

用户主动删除，将出行凭证从钱包中移除。

交互流程

服务端开发

删除出行凭证的场景主要分为如下两个场景：

钱包侧触发删除

用户在钱包App中手动删除（包括恢复出厂、退出账号等场景）。

开发者客户端侧触发删除

用户在开发者客户端中手动删除，开发者客户端请求开发者服务器触发删除。

服务端开发参考出行凭证更新，采用PATCH方式进行局部更新，请求体如下：

{
  "fields": {
    "status": {
      "state": "expired"
   }
  }
}

删除成功回调

当出行凭证删除成功之后，钱包App携带删除成功回调请求钱包服务器，钱包服务器通过NFC相关事件回调通知接口通知开发者服务器。

## Code blocks

### Code block 1

```
{
  "fields": {
    "status": {
      "state": "expired"
   }
  }
}
```
