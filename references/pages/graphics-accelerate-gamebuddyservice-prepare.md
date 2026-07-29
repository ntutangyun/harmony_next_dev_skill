# 开发准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddyservice-prepare_

请先参考应用开发准备完成基本准备工作，再继续以下开发准备项。

配置游戏伴随服务权限

在“src/main/module.json5”的requestPermissions层级中配置游戏伴随服务权限。

{
    "module":
    {
        // ...
        "requestPermissions":
        [
            {
                "name": "ohos.permission.ACCESS_GAME_BUDDY_SERVICE",
                "reason": "$string:accessGameBuddyService"
            }
        ]
    }
}

## Code blocks

### Code block 1

```
{
    "module":
    {
        // ...
        "requestPermissions":
        [
            {
                "name": "ohos.permission.ACCESS_GAME_BUDDY_SERVICE",
                "reason": "$string:accessGameBuddyService"
            }
        ]
    }
}
```
