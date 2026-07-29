# 删除车钥匙

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-carkey-scene-delete_

用户手动或系统自动删除车钥匙，从设备安全芯片中移除车钥匙数据。

交互流程

服务端开发

[h2]删除车钥匙

删除车钥匙的场景主要包括：用户手动触发删除、DK服务器管理台触发删除、车钥匙使用权限到期后的系统自动触发删除以及用户在钱包App执行车钥匙迁移成功之后触发删除。

其中用户在钱包App执行车钥匙迁移成功之后触发删除的具体实现，请参照迁移车钥匙章节。

其他删除场景的服务端开发参考更新车钥匙，采用PATCH方式进行局部更新，请求体如下：

{
  "fields": {
    "status": {
      "state": "expired"
   }
  }
}

[h2]删除成功回调

当车钥匙删除成功之后，钱包App携带删除成功回调请求钱包服务器，钱包服务器通过NFC相关事件回调通知接口通知DK服务器，请求体中包含账号+设备的唯一值标识pushToken（pushToken需要使用原值，非sha256签名值）。

DK服务器需要对原有的车钥匙唯一标识organizationPassId和账号+设备的唯一标识pushToken（pushToken需要使用sha256签名值）的关联关系进行删除。

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
