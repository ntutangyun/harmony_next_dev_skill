# 使用TSan检测线程错误

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan_

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考TSan。

使用约束

ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。

TSan不支持静态链接libc或libc++库。

开启TSan

可通过以下两种方式开启TSan。

[h2]方式一

[h2]方式二

 "tsanEnabled": true

在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

"arguments": "-DOHOS_ENABLE_TSAN=ON"

使用TSan

运行或调试当前应用。

## Code blocks

### Code block 1

```
 "tsanEnabled": true
```

### Code block 2

```
"arguments": "-DOHOS_ENABLE_TSAN=ON"
```
