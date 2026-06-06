# 使用Node

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-extension_

扩展能力接口进一步扩展了Node-API的功能，提供了一些额外的接口，用于在Node-API模块中与ArkTS进行更灵活的交互和定制，这些接口可以用于创建自定义ArkTS对象等场景。

Node-API接口开发流程参考使用Node-API实现跨语言交互开发流程，本文仅对接口对应C++及ArkTS相关代码进行展示。

本文cpp部分代码所需引用的头文件如下：

#include "napi/native_api.h"
#include <bits/alltypes.h>
#include <mutex>
#include <unordered_set>
#include <uv.h>
#include "hilog/log.h"

本文ArkTS侧示例代码所需的模块导入如下：

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
import { taskpool } from '@kit.ArkTS';
Node-API使用指导
使用Node-API接口进行array相关开发
