# 性能/内存优化：多目标编译优化实践

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-product-target-practice_

概述

在多目标工程中，targets配置和依赖链路是影响编译效率的两个关键因素：

HAP/HSP模块target默认编译行为：在HAP/HSP模块级build-profile.json5中配置targets时，如果没有在工程级build-profile.json5的modules下显式声明这些targets的applyToProducts（ohosTest除外），它们会默认应用到name为default的product。这可能导致构建default产物时，编译出冗余的包，详细可参考target显式配置applyToProducts。

HAR模块的target由依赖方决定：HAR模块的target由依赖它的模块决定，当HAR被不同target的模块依赖时，可能会产生冗余的编译任务，详细可参考HAR模块与依赖方配置相同的target。

这两种情况都会导致不必要的编译任务被执行，增加耗时和内存占用，推荐按照以下方式优化。

target显式配置applyToProducts

[h2]错误示例

执行构建命令时，如果不指定模块的target，参与编译的target由product决定。

例如在entry模块的build-profile.json5中配置default和test两个target，并且在工程级build-profile.json5没有配置test target的applyToProducts。

{
  "targets": [
    { "name": "default" },
    { "name": "test" },
  ]
}

执行以下命令，不指定target：

hvigorw assembleHap -p product=default

由于default target会被默认应用到default product，并且工程级build-profile.json5中没有显式指定test target的applyToProducts，test也被默认应用到default product，导致两个target都被编译。

[h2]优化方案

新增target时，建议显式声明applyToProducts。

{
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        {
          "name": "default",
          "applyToProducts": ["default"]
        },
        {
          "name": "test",
          "applyToProducts": ["test"]   // 显式指定应用到test product
        }
      ]
    }
  ]
}

{
  "app": {
    "products": [
      { "name": "default", },
      { "name": "test", }  // 新增test product
    ]
  }
}

这样执行`hvigorw assembleHap -p product=default`时，只有default target参与编译，test target不会参与。

HAR模块与依赖方配置相同的target

[h2]错误示例

当HAR模块被多个不同target的模块依赖时，可能会产生冗余的编译任务。

例如存在如下依赖关系：

entry(default、default2) → har1(default) → har2(default、default2)   // har1的target和entry不完全相同
entry(default、default2) → har2(default、default2)

当执行以下命令时：

hvigorw assembleHap -p product=default -p module=entry@default2

由于HAR模块的target由依赖它的模块决定，实际参与构建的target为：

entry(default2) → har1(default) → har2(default)
entry(default2) → har2(default2)

可以看到，har2有2个target(default、default2)参与构建，但是由于entry(default2)直接依赖的是har2(default2)，因此最终是har2(default2)参与打包，har2(default)并不会被打包。但是在打包前，har2(default)相关的任务（如:har2:default@PreBuild）也会被执行，这些任务属于冗余任务，会导致不必要的耗时。

[h2]优化方案

建议HAR模块与依赖方配置相同的target。例如以上示例，要给har1新增default2 target。

entry(default、default2) → har1(default、default2) → har2(default、default2)
entry(default、default2) → har2(default、default2)

这样无论依赖方使用哪个target，HAR模块都能提供对应的target，避免产生冗余的编译任务。

## Code blocks

### Code block 1

```
{
  "targets": [
    { "name": "default" },
    { "name": "test" },
  ]
}
```

### Code block 2

```
hvigorw assembleHap -p product=default
```

### Code block 3

```
{
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        {
          "name": "default",
          "applyToProducts": ["default"]
        },
        {
          "name": "test",
          "applyToProducts": ["test"]   // 显式指定应用到test product
        }
      ]
    }
  ]
}
```

### Code block 4

```
{
  "app": {
    "products": [
      { "name": "default", },
      { "name": "test", }  // 新增test product
    ]
  }
}
```

### Code block 5

```
entry(default、default2) → har1(default) → har2(default、default2)   // har1的target和entry不完全相同
entry(default、default2) → har2(default、default2)
```

### Code block 6

```
hvigorw assembleHap -p product=default -p module=entry@default2
```

### Code block 7

```
entry(default2) → har1(default) → har2(default)
entry(default2) → har2(default2)
```

### Code block 8

```
entry(default、default2) → har1(default、default2) → har2(default、default2)
entry(default、default2) → har2(default、default2)
```
