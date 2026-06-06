# 基础构建能力

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-api_

"hvigor"对象是一个预定义的Hvigor对象，表示当前正在执行的Hvigor构建引擎的实例，通过"hvigor"对象可以获得有关构建的一些信息和操作。

不同类型的构建事件具有不同结构，以下为典型结构示例：

// report.json
{
  "version": "2.0", // 固定字段
  "ppid": 524, // process.ppid
  "events": [ // 构建事件
    ...
    {
      "head": {
        "id": "61068546-11d9-49d0-baa7-733e167af7d6", // 事件id
        "name": "Finished :entry:default@PreBuild", // 事件name
        "description": "Pre-build in the stage model.",// 描述
        "type": "log" // 类型
      },
      "body": {
        "pid": 3960, // process.pid
        "tid": "Main Thread", // thread id
        "startTime": 1280741873226000, // 开始时间
        "endTime": 1280741896325200, // 结束时间
        "totalTime": 22868300 // 总计时间
      },
      "additional": {
        "logType": "info", // log类型
        "children": [], // 子事件id列表
      }
    }
  ],
  "workLog": []
}

示例：

// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, FileUtil } from '@ohos/hvigor';


hvigor.buildFinished(buildResult => {
  // 将数据写入指定path的文件中
  const json5FilePath = FileUtil.pathResolve('D:\\', 'testJson.json5');
  FileUtil.ensureFileSync(json5FilePath);
  FileUtil.writeFileSync(json5FilePath, JSON.stringify(buildResult.getReportJson(), null, 2));
})


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}

当前节点的根目录的NormalizedFile对象。

起始版本：Hvigor 4.3.0

示例二：依赖其他模块的任务。

// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';


// 获取当前entry节点对象
const entryNode = hvigor.getNodeByName('entry');


// 逻辑放在hook-nodesEvaluated中
hvigor.nodesEvaluated(async () => {
  // 注册任务
  entryNode.registerTask({
    // 任务名称
    name: `default@CustomTask`,
    run() {
      console.log('customTask1')
    },
    // 配置前置任务依赖
    dependencies: ['har:assembleHar'], // 跨模块依赖har的assembleHar任务，确保har模块存在
    // 配置任务的后置任务依赖
    postDependencies: ['entry:default@PreBuild']  // 支持两种写法 entry:default@PreBuild  default@PreBuild
  });
});


export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: []       /* Custom plugin to extend the functionality of Hvigor. */
}

示例二：依赖其他模块的任务。

// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode, HvigorPlugin } from '@ohos/hvigor';


// 获取当前entry节点对象
const entryNode = hvigor.getNodeByName('entry');


// 逻辑放在hook-nodesEvaluated中
hvigor.nodesEvaluated(async () => {
  // 注册任务
  entryNode.registerTask({
    // 任务名称
    name: `default@CustomTask`,
    run() {
      console.log('customTask1')
    },
    // 配置前置任务依赖
    dependencies: ['entry:default@PreBuild'], // 支持两种写法 entry:default@PreBuild  default@PreBuild
    // 配置任务的后置任务依赖
    postDependencies: ['har:default@PreBuild']  // 跨模块依赖har的PreBuild任务，确保har模块存在
  });
});


export default {
  system: appTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  plugins: []       /* Custom plugin to extend the functionality of Hvigor. */
}

需要在hvigor-config.json5中添加dependencies：

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

需要在hvigor-config.json5中添加dependencies：

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

需要在hvigor-config.json5中添加dependencies：

// hvigor-config.json5
"dependencies": {
    "fs-extra": "11.2.0",
    "@types/fs-extra": "9.0.13"
},

获取任务名称。

返回值:

类型

	

说明




string

	

任务名称

示例：

// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';


hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
    if (assembleAppTask) {
        const taskName = assembleAppTask.getName();
        console.log(`taskName: ${taskName}`);
    }
});


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}

获取当前任务依赖的前置任务名称列表。

返回值:

类型

	

说明




string[]

	

当前任务依赖的前置任务名称列表

示例：

// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';


hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
    if (assembleAppTask) {
        const taskDependencies = assembleAppTask.getDependencies();
        console.log(`Task Dependencies: ${taskDependencies}`);
    }
});


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}

添加任务执行完成之后的钩子函数。钩子函数以堆结构存储，遵循先进先出原则，先添加的函数先被执行。

参数:

参数名

	

类型

	

必填

	

说明




fn

	

Function

	

是

	

回调函数

示例：

// 工程级hvigorfile.ts文件
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor, Task } from '@ohos/hvigor';


hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    const assembleAppTask: Task | undefined = rootNode.getTaskByName('assembleApp');
    if (assembleAppTask) {
        // 任务执行之后的钩子函数
        assembleAppTask.afterRun(() => {
            console.log('After Task: assembleApp');
        });
    }
});


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}

wait-job.js内容如下，和hvigorfile.ts在同一个目录下：

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}


async function wait() {
    console.log('开始等待10秒...');
    await sleep(10000);
    console.log('结束，退出程序。');
}


exports.wait = wait;
扩展构建API
插件上下文
