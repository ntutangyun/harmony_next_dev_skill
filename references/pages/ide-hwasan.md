# 使用HWASan检测内存错误

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hwasan_

HWASan（Hardware-Assisted Address Sanitizer）是一款类似于ASan的内存错误检测工具。与ASan相比，HWASan使用的内存减少很多，因而更适合用于整个系统的检测。关于HWASan的检测原理请参考HWASan检测原理。

在适配过程中，若遇到应用崩溃等问题，可参考适配常见问题。

使用约束

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

从26.0.0版本开始，支持解析错误堆栈对应的伪代码、方法入参及变量的名称、值。仅解析前三行堆栈（#0~#2），其中#0行会解析入参、变量的名称和值，另外两行（#1、#2）仅解析入参和变量名称。

为确保正确解析堆栈，需保留代码中的调试信息，具体请参考注意事项。

注意事项

为确保正确解析堆栈，需保留代码中的调试信息，请遵循以下配置。

"nativeLib": {
  "debugSymbol": {
    "strip": false
  }
}

set_source_files_properties(
    filename.cpp
    PROPERTIES COMPILE_FLAGS "-O0"
)
string(REPLACE "-O2" "-O0"
    CMAKE_CXX_FLAGS_RELEASE
    "${CMAKE_CXX_FLAGS_RELEASE}"
)
string(REPLACE "-O2" "-O0"
    CMAKE_C_FLAGS_RELEASE
    "${CMAKE_C_FLAGS_RELEASE}"
)

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

### Code block 5

```
"nativeLib": {
  "debugSymbol": {
    "strip": false
  }
}
```

### Code block 6

```
set_source_files_properties(
    filename.cpp
    PROPERTIES COMPILE_FLAGS "-O0"
)
string(REPLACE "-O2" "-O0"
    CMAKE_CXX_FLAGS_RELEASE
    "${CMAKE_CXX_FLAGS_RELEASE}"
)
string(REPLACE "-O2" "-O0"
    CMAKE_C_FLAGS_RELEASE
    "${CMAKE_C_FLAGS_RELEASE}"
)
```
