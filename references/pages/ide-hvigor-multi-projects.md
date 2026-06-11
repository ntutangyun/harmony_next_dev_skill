# 多工程构建

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-multi-projects_

为降低大型应用多个团队协作开发的复杂度，提供多工程开发模式，提高协作开发效率。多工程开发能力支持将大型应用拆分为多个模块，每个模块对应一个单独工程。在每个工程分别编译生成HAP后，需统一打包生成一个APP，用于上架应用市场。

{
  "app": {
    "multiProjects": true,
  }
}

准备好HAP打包工具app_packing_tool.jar（在 $DevEco Studio安装目录/sdk/default/openharmony/toolchains/lib下）。

java -jar app_packing_tool.jar --mode multiApp --hap-list D:\project\MyApplication\1.hap,D:\project\MyApplication1\2.hap --out-path D:\project\final.app

hap-list：多个HAP文件路径，用逗号隔开。

out-path：生成的APP文件路径，如"D:\project\final.app"。

## Code blocks

### Code block 1

```
{
  "app": {
    "multiProjects": true,
  }
}
```

### Code block 2

```
java -jar app_packing_tool.jar --mode multiApp --hap-list D:\project\MyApplication\1.hap,D:\project\MyApplication1\2.hap --out-path D:\project\final.app
```
