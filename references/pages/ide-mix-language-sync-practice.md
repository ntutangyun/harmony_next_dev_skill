# 性能优化：混合语言工程Sync优化实践

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-mix-language-sync-practice_

概述

在包含多个C++模块的大型HarmonyOS工程中，传统的同步（Sync）阶段往往因模块任务串行执行，多次执行ohpm install，导致构建文件生成耗时增加，进而影响开发效率。为提升开发体验，DevEco Studio提供了多项优化机制，通过调整依赖安装逻辑、同步策略、CMake配置刷新方式等，显著降低构建耗时。主要优化措施如下。

优化措施一：优化ohpm依赖安装效率

启用enable_unified_lockfile，当模块间存在重复依赖时，显著减少ohpm install的耗时，优化构建流程。

启用enable_boost_extraction_speed，ohpm将采用高性能解压与遍历算法，当工程中存在大文件依赖时，可以显著减少ohpm install耗时。

从DevEco Studio 6.0.0 Beta3版本开始，新增一个开关，开启后，Hvigor仅执行一次ohpm install，可提升构建效率。

开启方式：点击File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor，勾选Enable ohpm execution by hvigor。

优化措施二：启用C++并行同步编译

在包含C++模块的工程中，执行同步（Sync and Refresh Project）时，会针对每个C++模块单独启动compileNative任务，多个模块之间是串行编译。如果工程中包含较多C++模块时，会导致编译耗时较长。

从26.0.0版本开始，支持启用C++并行同步编译，优化Sync阶段编译速度，开启后Sync阶段会执行syncNative任务。

开启方式：点击File > Settings（macOS为DevEco Studio > Preferences/Settings） > Build, Execution, Deployment > Build Tools > Hvigor，勾选Enable C++ syncNative compilation。

开启后，根据模块之间是否有依赖关系，分为以下两种场景。

可能影响：如果在hvigorfile.ts脚本的compileNative任务阶段有自定义插件或任务，开启开关后，由于compileNative任务不会被执行，会导致自定义插件或任务未执行。

优化措施三：动态刷新C++项目配置

在包含C++模块的工程中，开发者常在CMakeLists.txt中使用FILE(GLOB)动态收集源码文件，如下所示：

#当前CMakeLists.txt文件同目录下的文件
FILE(GLOB SRC_LIST "test/*.cpp")

#将上述SRC_LIST列表合并到一个新的变量PROJECT_SOURCE中
list(APPEND PROJECT_SOURCE
     ${SRC_LIST}
     )

#创建共享库
add_library(MyProject SHARED ${PROJECT_SOURCE})

当开发者在test目录下新增或修改.cpp源码文件后，直接执行Sync或Build操作时，往往会出现编译报错。根本原因是CMake默认采用静态缓存机制。使用FILE(GLOB)时，CMake仅在配置阶段（Configure）扫描一次文件。如果源码文件发生增删改，CMake可能无法及时识别这些变更，导致构建系统仍引用旧的缓存状态。此时，清理.cxx缓存可以修复该问题，但频繁清理缓存会显著降低开发效率。

从26.0.0版本开始，新增Refresh C++ Project功能，允许开发者主动触发CMake重新配置项目，确保动态生成的源码列表与当前文件系统状态同步。

优化措施四：修改代码索引模式

在开发大型C/C++工程时，代码索引（Code Indexing）往往是影响启动速度和日常开发流畅度的关键因素。传统的全量索引虽然能提供完整的代码导航能力，但在处理代码量巨大的项目时，往往会导致索引耗时较长，并持续占用较高的CPU和内存资源，迫使开发者等待较长时间才能进入编码状态。

从26.0.0版本开始，DevEco Studio支持切换C/C++代码索引模式，可以根据当前工程的规模、硬件性能以及具体的开发需求，灵活选择最适合的索引策略，在“开发体验”与“资源消耗”之间找到最佳平衡点，具体支持的代码索引模式和切换方式请参考代码索引（clangd）。

## Code blocks

### Code block 1

```
#当前CMakeLists.txt文件同目录下的文件
FILE(GLOB SRC_LIST "test/*.cpp")

#将上述SRC_LIST列表合并到一个新的变量PROJECT_SOURCE中
list(APPEND PROJECT_SOURCE
     ${SRC_LIST}
     )

#创建共享库
add_library(MyProject SHARED ${PROJECT_SOURCE})
```
