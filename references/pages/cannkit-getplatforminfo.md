# GetPlatformInfo

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplatforminfo_

函数功能

获取fe::PlatFormInfos指针。

函数原型

fe::PlatFormInfos *GetPlatformInfo() const

参数说明

无

返回值

fe::PlatFormInfos指针。

约束说明

无

调用示例

ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto platform_info = context->GetPlatformInfo();
  // ...
}

## Code blocks

### Code block 1

```
fe::PlatFormInfos *GetPlatformInfo() const
```

### Code block 2

```
ge::graphStatus Tiling4XXX(TilingContext* context) {
  auto platform_info = context->GetPlatformInfo();
  // ...
}
```
