# 开发Hvigor插件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-plugin_

Hvigor允许开发者实现自己的插件，开发者可以定义自己的构建逻辑，并与他人共享。

Hvigor主要提供了两种方式来实现插件：基于hvigorfile脚本开发插件、基于typescript项目开发。

关于插件开发的具体实践请参考定制hvigor插件开发实践。

说明

建议使用DevEco Studio内置的Node.js，如需另行安装，推荐使用DevEco Studio配套的Node.js版本，具体配套关系请参考DevEco Studio兼容性配套关系。

基于hvigorfile脚本开发

基于hvigorfile.ts脚本开发的方式，其优点是可实现快速开发，直接编辑工程或模块下hvigorfile.ts即可编写插件代码，不足之处是在多个项目中，无法方便地进行插件代码的复用和共享分发。

从DevEco Studio 6.0.2 Beta1版本开始，在构建脚本中编写代码时，支持代码补全、代码生成、代码重构等代码编辑能力，具体使用方式请参考代码阅读、代码生成/补全、代码重构。

若开发者需要创建新的构建脚本，推荐将这些脚本统一放在工程或模块的scripts目录下，以便与应用代码进行隔离，示例如下。

以工程级hvigorfile.ts脚本为例，开发步骤如下。

// 工程级hvigorfile.ts
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { HvigorPlugin, HvigorNode } from '@ohos/hvigor';

// 工程级hvigorfile.ts
function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode) {
      // 插件主体
      console.log('hello customPlugin!');
    }
  }
}

// 工程级hvigorfile.ts
export default {
  system: appTasks,
  plugins:[
    customPlugin()  // 应用自定义Plugin
  ]
}

执行Hvigor命令时，在Hvigor生命周期配置阶段执行插件中的apply方法。

基于typescript项目开发

基于typescript项目开发较好地弥补了上一小节中使用hvigorfile脚本方式编写插件代码不易复用和共享分发的问题。因此通常情况下推荐此方式开发。

[h2]初始化typescript项目

在命令行工具中使用cd命令进入空目录下。

// 全局安装TypeScript
npm install typescript -g

// 初始化一个npm项目
npm init

// 初始化typeScript配置文件
tsc --init

检查tsconfig.json文件是否存在verbatimModuleSyntax字段，如果存在且配置为true，会导致无法使用ESM语法，编译时会报错，因此需要删除该字段。

[h2]开发插件

在工程目录下创建.npmrc文件，配置如下信息：

registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/

打开package.json添加devDependencies配置。

"devDependencies": {
    "@ohos/hvigor": "5.2.2"
}

npm install

在src/plugin目录下创建custom-plugin.ts文件，编写插件代码，更多接口请参考扩展构建API。

import type { HvigorNode, HvigorPlugin } from '@ohos/hvigor';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode) {
      console.log('hello customPlugin!');
    }
  }
}

创建index.ts文件，并在该文件中声明插件方法的导出。由于.ts最终会编译成.js文件，因此需要导出.js文件。

export { customPlugin } from './src/plugin/custom-plugin.js';

[h2]发布插件

typescript项目本质上是一种npm项目，插件发布流程遵循npm发布规范。详情请查询npm官方资料。

发布npm包流程：

打开工程目录下的.npmrc文件，配置您需要发布的镜像仓库。

registry=[npm镜像仓库地址]

执行如下命令，注册并登录npm仓库，在工程目录下.npmrc文件中自动生成token信息。

npm login

tsc

如果编译时报以下错误，请检查初始化项目时是否删除了verbatimModuleSyntax。

执行如下命令，将npm项目打包并发布至镜像仓库。

npm publish

[h2]使用插件

在工程下hvigor/hvigor-config.json5中添加自定义插件依赖，依赖项支持离线插件配置。

"dependencies": {
  "custom-plugin": "1.0.0"   // 添加自定义插件依赖
}

方式1：执行编辑区右上角Sync Now或执行菜单File -> Sync and Refresh Project进行工程Sync后，DevEco Studio将会根据hvigor-config.json5中的依赖配置自动安装。

hvigorw --sync

根据插件编写时基于的node节点，确定导入的节点所在的hvigorfile.ts文件，在hvigorfile.ts中导入插件。

import { customPlugin } from 'custom-plugin';

将自定义插件添加到export default的plugins中。

export default {
  system: appTasks,  // 以工程级hvigorfile.ts为例
  plugins:[
    customPlugin()  // 应用自定义插件
  ]
}

## Code blocks

### Code block 1

```
// 工程级hvigorfile.ts
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { HvigorPlugin, HvigorNode } from '@ohos/hvigor';
```

### Code block 2

```
// 工程级hvigorfile.ts
function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode) {
      // 插件主体
      console.log('hello customPlugin!');
    }
  }
}
```

### Code block 3

```
// 工程级hvigorfile.ts
export default {
  system: appTasks,
  plugins:[
    customPlugin()  // 应用自定义Plugin
  ]
}
```

### Code block 4

```
// 全局安装TypeScript
npm install typescript -g
```

### Code block 5

```
// 初始化一个npm项目
npm init
```

### Code block 6

```
// 初始化typeScript配置文件
tsc --init
```

### Code block 7

```
registry=https://repo.huaweicloud.com/repository/npm/
@ohos:registry=https://repo.harmonyos.com/npm/
```

### Code block 8

```
"devDependencies": {
    "@ohos/hvigor": "5.2.2"
}
```

### Code block 9

```
npm install
```

### Code block 10

```
import type { HvigorNode, HvigorPlugin } from '@ohos/hvigor';

export function customPlugin(): HvigorPlugin {
  return {
    pluginId: 'customPlugin',
    apply(node: HvigorNode) {
      console.log('hello customPlugin!');
    }
  }
}
```

### Code block 11

```
export { customPlugin } from './src/plugin/custom-plugin.js';
```

### Code block 12

```
registry=[npm镜像仓库地址]
```

### Code block 13

```
npm login
```

### Code block 14

```
tsc
```

### Code block 15

```
npm publish
```

### Code block 16

```
"dependencies": {
  "custom-plugin": "1.0.0"   // 添加自定义插件依赖
}
```

### Code block 17

```
hvigorw --sync
```

### Code block 18

```
import { customPlugin } from 'custom-plugin';
```

### Code block 19

```
export default {
  system: appTasks,  // 以工程级hvigorfile.ts为例
  plugins:[
    customPlugin()  // 应用自定义插件
  ]
}
```
