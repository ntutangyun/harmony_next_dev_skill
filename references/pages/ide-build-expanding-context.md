# 插件上下文

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-expanding-context_

import { appTasks, OhosAppContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';


hvigor.nodesEvaluated(() => {
    const appContext = hvigor.getRootNode().getContext(OhosPluginId.OHOS_APP_PLUGIN) as OhosAppContext;
    const buildProfileOpt = appContext.getBuildProfileOpt();
    // 添加一个工程外的模块
    const newModule = {
        "name": "har",
        "srcPath": "./../MyApplication40/har",// 确保该源码模块存在
    }
    buildProfileOpt.modules.push(newModule);
    appContext.setBuildProfileOpt(buildProfileOpt);
    console.log(buildProfileOpt.modules.map(module => {
        return module.name;
    }));
});


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}

示例：

// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';


// 自定义插件代码
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const ohpmInfo = rootNodeContext.getOhpmDependencyInfo();
            console.log(ohpmInfo)
        }
    };
}


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}

示例：

// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';


// 自定义插件代码
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const DependenciesInfo = rootNodeContext.getDependenciesOpt();
            console.log(DependenciesInfo)
        }
    };
}


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
示例：
// 工程级hvigorfile.ts文件
import { HvigorNode, HvigorPlugin } from '@ohos/hvigor';
import { appTasks } from '@ohos/hvigor-ohos-plugin';
import { OhosPluginId } from '@ohos/hvigor-ohos-plugin';


// 自定义插件代码
export function customPlugin(): HvigorPlugin {
    return {
        pluginId: 'customPlugin',
        async apply(currentNode: HvigorNode): Promise<void> {
            const rootNodeContext = currentNode.getContext(OhosPluginId.OHOS_APP_PLUGIN);
            if (!rootNodeContext) {
                return;
            }
            const dynamicDependenciesInfo = rootNodeContext.getDynamicDependenciesOpt()
            dynamicDependenciesInfo["har"] = "./har";  // 确保依赖存在
            rootNodeContext.setDynamicDependenciesOpt(dynamicDependenciesInfo);   
      }
    };
}


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[customPlugin()]         /* Custom plugin to extend the functionality of Hvigor. */
}
// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';


hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // 获得所有子节点
        const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext; // 仅对hap模块生效，hsp和har需要使用模块对应接口
        const moduleJsonOpt = hapContext?.getModuleJsonOpt();
        moduleJsonOpt.module.deviceTypes = ["phone", "tablet"]; // 修改 module.json 中的 deviceTypes 字段
        hapContext?.setModuleJsonOpt(moduleJsonOpt); // 更新 module.json
        console.log(`Module Json Opt: ${JSON.stringify(moduleJsonOpt)}`);
    });
})


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
说明

setBuildProfileOpt会进行schema校验，如果传入的对象不符合校验规则会抛出异常。

示例：

// 工程级hvigorfile.ts文件
import { appTasks, OhosHapContext, OhosPluginId } from '@ohos/hvigor-ohos-plugin';
import { hvigor, HvigorNode } from '@ohos/hvigor';


hvigor.nodesEvaluated(() => {
    const rootNode = hvigor.getRootNode();
    rootNode.subNodes((node: HvigorNode) => {
        // 获得所有子节点
        const hapContext = node.getContext(OhosPluginId.OHOS_HAP_PLUGIN) as OhosHapContext;
        const buildProfileOpt = hapContext?.getBuildProfileOpt();
        // 可以对buildProfileOpt进行修改
        buildProfileOpt?.targets?.push({
            "name": "default1",
        })
        hapContext?.setBuildProfileOpt(buildProfileOpt); // 更新 build profile
        console.log(`Build Profile Opt: ${JSON.stringify(buildProfileOpt)}`);
    });
})


export default {
    system: appTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
基础构建能力
API使用示例
