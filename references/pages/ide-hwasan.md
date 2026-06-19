# 使用HWASan检测内存错误

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hwasan_

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于ASan的内存错误检测工具。与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的检测。关于HWASan的检测原理请参考HWASan检测原理。

约束条件

HWASan检测仅适用于AArch64架构的硬件。

ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

开启HWASan

DevEco Studio 6.1.0 Beta1之前的版本，仅支持对C++源码开启HWASan。

从DevEco Studio 6.1.0 Beta1版本开始，同时支持对C++编译生成的无源码so文件进行二进制插桩，进而开启HWASan功能。

[h2]方式一

从DevEco Studio 6.1.0 Beta1版本开始，可以同时勾选BinXO check，开启无源码的so文件的HWASan检测插桩。

"buildOption": {
  "nativeLib": {
    "excludeSoFromBinXO": ["**/liblibrary.so"]
  }
}

[h2]方式二

"hwasanEnabled": true

// DevEco Studio 6.1.0 Beta1以下版本
"buildOption": {
  "externalNativeOptions": {
    "arguments": ["-DOHOS_ENABLE_HWASAN=ON"]
  }
// DevEco Studio 6.1.0 Beta1及以上版本，同时开启有源码和无源码的C++的HWASan检测插桩
"buildOption": {
  "externalNativeOptions": {
    "arguments": ["-DOHOS_ENABLE_HWASAN=ON", "-DOHOS_ENABLE_BINXO=ON"]
  }

"buildOption": {
  "nativeLib": {
    "excludeSoFromBinXO": ["**/liblibrary.so"]
  }
}

使用HWASan

运行或调试当前应用。

## Code blocks

### Code block 1

```
"buildOption": {
  "nativeLib": {
    "excludeSoFromBinXO": ["**/liblibrary.so"]
  }
}
```

### Code block 2

```
"hwasanEnabled": true
```

### Code block 3

```
// DevEco Studio 6.1.0 Beta1以下版本
"buildOption": {
  "externalNativeOptions": {
    "arguments": ["-DOHOS_ENABLE_HWASAN=ON"]
  }
// DevEco Studio 6.1.0 Beta1及以上版本，同时开启有源码和无源码的C++的HWASan检测插桩
"buildOption": {
  "externalNativeOptions": {
    "arguments": ["-DOHOS_ENABLE_HWASAN=ON", "-DOHOS_ENABLE_BINXO=ON"]
  }
```

### Code block 4

```
"buildOption": {
  "nativeLib": {
    "excludeSoFromBinXO": ["**/liblibrary.so"]
  }
}
```
