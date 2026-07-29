# 应用接入快捷栏

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/desktop-quickbar-extension-guide_

应用接入快捷栏之后，可自定义应用的右键菜单分组、应用的窗口分组、应用的图标和进度条。

从API版本26.0.0开始，支持查询是否支持接入快捷栏和自定义快捷栏应用的图标和进度条。

从API版本6.1.1(23)开始，支持自定义快捷栏应用的窗口分组。

从API版本6.0.2(22)开始，支持自定义快捷栏应用的菜单分组。

场景介绍

快捷栏指的是PC/2in1设备的屏幕底部的图标区域，具体如下图。

应用接入快捷栏之后，快捷栏的应用图标菜单会显示应用自定义的菜单项，应用可以添加、删除、更新、查询菜单项，具体效果如下图。

接口说明

以下列出应用接入快捷栏菜单的相关API，具体API说明详见接口文档。

说明

Desktop Extension Kit相关API仅在PC/2in1设备上生效。

表1 应用接入快捷栏菜单相关功能接口介绍

接口名	描述
getCustomCategories(context: common.Context): Promise<CustomCategory[]>	获取所有在快捷栏菜单定义的分组。
addCustomCategory(context: common.Context, categoryName: string): Promise<CustomCategory>	添加快捷栏菜单分组。
updateCustomCategory(context: common.Context, category: CustomCategory): Promise<void>	更新快捷栏菜单分组。
deleteCustomCategory(context: common.Context, categoryId: number): Promise<void>	删除快捷栏菜单分组。
getTasksFromCategory(context: common.Context, categoryId: number): Promise<QuickTask[]>	获取某个快捷栏菜单的分组下的所有任务。
addQuickTask(context: common.Context, categoryId: number, taskInfo: QuickTaskInfo): Promise<QuickTask>	添加快捷栏菜单任务。
updateQuickTask(context: common.Context, task: QuickTask): Promise<void>	更新快捷栏菜单任务。
deleteQuickTask(context: common.Context, taskId: number): Promise<void>	删除快捷栏菜单任务。
addQuickBarGroup(context: common.Context, group: QuickBarGroup): Promise<void>	增加快捷栏分组。
deleteQuickBarGroup(context: common.Context, groupKey: string): Promise<void>	删除快捷栏分组。
getQuickBarGroups(context: common.Context): Promise<QuickBarGroup[]>	获取所有分组信息。
setWindowToGroup(context: common.Context, windowid:string, groupKey?: string): Promise<void>	给分组增加窗口。
setQuickBarCombineIcon(context: common.Context, combineIcon: image.PixelMap): Promise<void>	设置快捷栏融合图标。
setQuickBarLayeredIcon(context: common.Context, foregroundIcon: image.PixelMap, backgroundIcon: image.PixelMap): Promise<void>	设置快捷栏分层图标。
setProgressState(context: common.Context, state: ProgressState): Promise<void>	设置快捷栏进度条状态。
setProgressValue(context: common.Context, completed: number, total: number): Promise<void>	设置快捷栏图标的进度条。
isQuickBarCapabilitySupported(context: common.Context): Promise<boolean>	检查是否支持快捷栏功能。

检查是否支持快捷栏功能

导入相关模块。

import { quickBarManager } from '@kit.DeskTopExtensionKit';

调用isQuickBarCapabilitySupported判断当前设备是否支持接入快捷栏。仅当返回值isSupport为true时，方可进行自定义快捷栏的菜单分组、窗口分组、图标及进度条。

let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}

try {
  const isSupport = await quickBarManager.isQuickBarCapabilitySupported(context);
  console.info(`isQuickBarCapabilitySupported: ${isSupport}`);
} catch (error) {
  console.error(`isQuickBarCapabilitySupported failed. error code: ${error.code}, error message: ${error.message}`);
}

快捷栏自定义菜单分组

导入相关模块。

import quickBarManager from '@hms.pcService.quickBarManager';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

新建一个TestAbility.ets文件（例如在entry/src/main/ets/entryability文件夹下），同时新建一个TestIndex的页面（例如在entry/src/main/ets/pages目录下），点击图标菜单任务后可跳转到该页面。

let TAG = 'TestAbility';

export default class TestAbility extends UIAbility {
  onCreate() {
    console.info(TAG, `onCreate`);
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    // 加载页面
    windowStage.loadContent('pages/TestIndex');
  }

  onForeground() {
    console.info(TAG, `onForeground`);
  }

  onBackground() {
    console.info(TAG, `onBackground`);
  }

  onWindowStageDestroy(): void {
    console.info(TAG, `onWindowStageDestroy`);
  }

  onDestroy() {
    console.info(TAG, `onDestroy`);
  }
}

在TestAbility所在模块下的module.json5文件中配置的Ability的信息。

{
    "name": "TestAbility",
    "srcEntry": "./ets/entryability/TestAbility.ets",
    "description": "$string:EntryAbility_desc",
    "icon": "$media:layered_image",
    "label": "$string:EntryAbility_label",
    "startWindowIcon": "$media:startIcon",
    "startWindowBackground": "$color:start_window_background",
    "exported": true,
    "skills": [
        {
            "entities": [
                "entity.system.home"
            ],
            "actions": [
                "action.system.home"
            ]
        }
    ],
}

在页面组件内(如：TestIndex.ets)中调用接口完成如下步骤。调用addCustomCategory接口添加一个快捷栏菜单分组，添加分组后才可以往分组里添加任务。

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addCustomCategory(context: Context) {
  if (context === undefined) {
   return;
  }
  try {
    const res = await quickBarManager.addCustomCategory(context, 'recent tasks')
    console.info(`customCategory info: ${JSON.stringify(res)}`)
  } catch (error) {
    console.error(`addCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}

添加分组后可以调用addQuickTask接口在分组中添加快捷栏菜单任务。打开应用图标在快捷栏的右键菜单，即可看到添加后对应的菜单项。

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addQuickTask(context: Context) {
  if (context === undefined) {
   return
  }

  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建white pixelMap，需在资源rawfile文件夹中预置taskImage.png图片，图片大小为24vp * 24vp
  const fileData = resourceMgr.getRawFileContentSync('taskImage.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();

  // 构建parameters
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  let task: quickBarManager.QuickTaskInfo = {
    taskName: 'test task name',
    abilityName: 'TestAbility',
    // 参数可选
    moduleName: 'entry',
    // 参数可选
    taskIcon: imagePixelMap,
    // 参数可选
    taskDetail: 'description of the task',
    // 参数可选
    parameters: [parameters]
  }
  try {
    // 获取所有的分组信息，将任务添加到想要的分组中
    const categoryList = await quickBarManager.getCustomCategories(context);
    // 选择添加任务到第一个分组中
    let res = await quickBarManager.addQuickTask(context, categoryList[0].categoryId, task);
    console.info(`quickTask info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`addQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}

调用getCustomCategories接口获取定义所有分组信息。

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function getCustomCategories(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    const res = await quickBarManager.getCustomCategories(context);
    console.info(`customCategoryList info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`getCustomCategories failed. error code: ${error.code}, error message: ${error.message}`);
  }
}

调用getTasksFromCategory接口获取分组下的所有任务信息，此处获取了第一个分组下的所有任务。

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function getTasksFromCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 获取所有的分组信息，用于获取分组下所有的任务
    const category = await quickBarManager.getCustomCategories(context);
    // 选择获取第一个分组下的所有任务
    const res = await quickBarManager.getTasksFromCategory(context, category[0].categoryId)
    console.info(`quickTaskList info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`getTasksFromCategory failed. error code: ${error.code}, error message: ${error.message}`);
 }
}

调用updateCustomCategory接口更新快捷栏菜单分组信息，此处更新了分组的名称。

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  const category: quickBarManager.CustomCategory = {
    categoryId: 1,
    categoryName: 'demo'
  }
  try {
    await quickBarManager.updateCustomCategory(context, category);
  } catch (error) {
    console.error(`updateCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}

调用updateQuickTask接口更新快捷栏菜单任务信息。以下示例代码以更新任务的图标信息为例。

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建任务的pixelMap，需在资源rawfile文件夹中预置testUpdateImage.png图片
  const fileData = resourceMgr.getRawFileContentSync('testUpdateImage.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();
  // 构建parameters
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  let taskInfo: quickBarManager.QuickTaskInfo = {
    taskName: 'newTaskName',
    abilityName: 'newEntryAbility',
    // 参数可选
    moduleName: 'newModuleName',
    // 参数可选
    taskIcon: imagePixelMap,
    // 参数可选
    taskDetail: '任务的描述',
    // 参数可选
    parameters: [parameters]
  }

  const task: quickBarManager.QuickTask = {
    taskId: 1,
    categoryId: 1,
    taskInfo: taskInfo
  }

  try {
    await quickBarManager.updateQuickTask(context, task);
  } catch (error) {
    console.error(`updateQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}

调用deleteQuickTask接口删除不需要的快捷栏菜单任务，此处删除了taskId为1的任务。

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function deleteQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 删除任务id为1的任务
    await quickBarManager.deleteQuickTask(context, 1);
  } catch (error) {
    console.error(`deleteQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}

调用deleteCustomCategory接口删除不需要的快捷栏菜单分组，此处删除了categoryId为1的分组，它的所有任务也会被一起删除。

/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function deleteCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 删除分组id为1的分组
    await quickBarManager.deleteCustomCategory(context, 3);
  } catch (error) {
    console.error(`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}

快捷栏自定义窗口分组

导入相关模块。

import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';

在entry/src/main/ets/pages目录下创建一个空页面文件，并增加一个按钮控件。 在按钮控件的onClick方法中调用addQuickBarGroup接口，增加快捷栏分组。

// 获取资源管理器
const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}
const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

// 从rawfile目录中获取图片
const whiteFileData = resourceMgr.getRawFileContentSync('icon.png');
const whiteImageSource = image.createImageSource(whiteFileData.buffer);
const imagePixelMap = await whiteImageSource.createPixelMap();

try {
  // 增加分组
  await quickBarManager.addQuickBarGroup(context, {
    groupKey: 'group_one', // 分组名
    groupIcon: imagePixelMap // 分组图标
  });
} catch (error) {
  console.error(`error code: ${error.code}, error message: ${error.message}`);
}

新增加一个按钮控件，并在onClick方法中调用getQuickBarGroups接口，获取所有分组信息。

const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 获取所有分组
  const groups = await quickBarManager.getQuickBarGroups(context);
  console.info(`groups: ${JSON.stringify(groups)}`);
} catch (error) {
  console.error(`error code: ${error.code}, error message: ${error.message}`);
}

新增加一个按钮控件，并在onClick方法中调用setWindowToGroup接口，给分组增加窗口信息。

const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 将id为80的窗口，增加到分组名为 group_one 的分组
  await quickBarManager.setWindowToGroup(context, '80', 'group_one');
} catch (error) {
  console.error(`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
}

新增加一个按钮控件，并在onClick方法中调用deleteQuickBarGroup接口，删除快捷栏分组。

const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 删除分组名为group_one的分组
  await quickBarManager.deleteQuickBarGroup(context, 'group_one');
} catch (error) {
  console.error(`error code: ${error?.code}, error message: ${error?.message}`);
}

快捷栏自定义图标和进度条

导入相关模块。

import { quickBarManager }  from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';

调用setQuickBarCombineIcon设置快捷栏融合图标。

let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}
try {
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建图标的pixelMap，需在资源rawfile文件夹中预置icon.png图片
  const fileData = resourceMgr.getRawFileContentSync('icon.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();

  await quickBarManager.setQuickBarCombineIcon(context, imagePixelMap);
  console.info('setQuickBarCombineIcon success');
} catch (error) {
  console.error(`setQuickBarCombineIcon failed. error code: ${error.code}, error message: ${error.message}`);
}

调用setQuickBarLayeredIcon设置快捷栏分层图标。

let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}
try {
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建前景图的pixelMap，需在资源rawfile文件夹中预置foreground.png图片
  const foregroundFileData = resourceMgr.getRawFileContentSync('foreground.png');
  const foregroundImageSource = image.createImageSource(foregroundFileData.buffer);
  const foregroundPixelMap = await foregroundImageSource.createPixelMap();

  // 创建背景图的pixelMap，需在资源rawfile文件夹中预置background.png图片
  const backgroundFileData = resourceMgr.getRawFileContentSync('background.png');
  const backgroundImageSource = image.createImageSource(backgroundFileData.buffer);
  const backgroundPixelMap = await backgroundImageSource.createPixelMap();

  await quickBarManager.setQuickBarLayeredIcon(context, foregroundPixelMap, backgroundPixelMap);
  console.info('setQuickBarLayeredIcon success');
} catch (error) {
  console.error(`setQuickBarLayeredIcon failed. error code: ${error.code}, error message: ${error.message}`);
}

调用setProgressValue设置快捷栏进度条，如果调用该接口前未设置进度条状态，默认状态为NORMAL。

let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}
const completed: number = 50;
const total: number = 100;

try {
  await quickBarManager.setProgressValue(context, completed, total);
  console.info('setProgressValue success');
} catch (error) {
  console.error(`setProgressValue failed. error code: ${error.code}, error message: ${error.message}`);
}

调用setProgressState设置快捷栏进度条状态。

let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}

try {
  // 设置进度状态为PAUSED，暂停状态
  await quickBarManager.setProgressState(context, quickBarManager.ProgressState.PAUSED);
  console.info('setProgressState success');
} catch (error) {
  console.error(`setProgressState failed. error code: ${error.code}, error message: ${error.message}`);
}

## Code blocks

### Code block 1

```
import { quickBarManager } from '@kit.DeskTopExtensionKit';
```

### Code block 2

```
let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}

try {
  const isSupport = await quickBarManager.isQuickBarCapabilitySupported(context);
  console.info(`isQuickBarCapabilitySupported: ${isSupport}`);
} catch (error) {
  console.error(`isQuickBarCapabilitySupported failed. error code: ${error.code}, error message: ${error.message}`);
}
```

### Code block 3

```
import quickBarManager from '@hms.pcService.quickBarManager';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
```

### Code block 4

```
let TAG = 'TestAbility';

export default class TestAbility extends UIAbility {
  onCreate() {
    console.info(TAG, `onCreate`);
  }

  onWindowStageCreate(windowStage: window.WindowStage) {
    // 加载页面
    windowStage.loadContent('pages/TestIndex');
  }

  onForeground() {
    console.info(TAG, `onForeground`);
  }

  onBackground() {
    console.info(TAG, `onBackground`);
  }

  onWindowStageDestroy(): void {
    console.info(TAG, `onWindowStageDestroy`);
  }

  onDestroy() {
    console.info(TAG, `onDestroy`);
  }
}
```

### Code block 5

```
{
    "name": "TestAbility",
    "srcEntry": "./ets/entryability/TestAbility.ets",
    "description": "$string:EntryAbility_desc",
    "icon": "$media:layered_image",
    "label": "$string:EntryAbility_label",
    "startWindowIcon": "$media:startIcon",
    "startWindowBackground": "$color:start_window_background",
    "exported": true,
    "skills": [
        {
            "entities": [
                "entity.system.home"
            ],
            "actions": [
                "action.system.home"
            ]
        }
    ],
}
```

### Code block 6

```
/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addCustomCategory(context: Context) {
  if (context === undefined) {
   return;
  }
  try {
    const res = await quickBarManager.addCustomCategory(context, 'recent tasks')
    console.info(`customCategory info: ${JSON.stringify(res)}`)
  } catch (error) {
    console.error(`addCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

### Code block 7

```
/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function addQuickTask(context: Context) {
  if (context === undefined) {
   return
  }

  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建white pixelMap，需在资源rawfile文件夹中预置taskImage.png图片，图片大小为24vp * 24vp
  const fileData = resourceMgr.getRawFileContentSync('taskImage.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();

  // 构建parameters
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  let task: quickBarManager.QuickTaskInfo = {
    taskName: 'test task name',
    abilityName: 'TestAbility',
    // 参数可选
    moduleName: 'entry',
    // 参数可选
    taskIcon: imagePixelMap,
    // 参数可选
    taskDetail: 'description of the task',
    // 参数可选
    parameters: [parameters]
  }
  try {
    // 获取所有的分组信息，将任务添加到想要的分组中
    const categoryList = await quickBarManager.getCustomCategories(context);
    // 选择添加任务到第一个分组中
    let res = await quickBarManager.addQuickTask(context, categoryList[0].categoryId, task);
    console.info(`quickTask info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`addQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

### Code block 8

```
/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function getCustomCategories(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    const res = await quickBarManager.getCustomCategories(context);
    console.info(`customCategoryList info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`getCustomCategories failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

### Code block 9

```
/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function getTasksFromCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 获取所有的分组信息，用于获取分组下所有的任务
    const category = await quickBarManager.getCustomCategories(context);
    // 选择获取第一个分组下的所有任务
    const res = await quickBarManager.getTasksFromCategory(context, category[0].categoryId)
    console.info(`quickTaskList info: ${JSON.stringify(res)}`);
  } catch (error) {
    console.error(`getTasksFromCategory failed. error code: ${error.code}, error message: ${error.message}`);
 }
}
```

### Code block 10

```
/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  const category: quickBarManager.CustomCategory = {
    categoryId: 1,
    categoryName: 'demo'
  }
  try {
    await quickBarManager.updateCustomCategory(context, category);
  } catch (error) {
    console.error(`updateCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

### Code block 11

```
/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function updateQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建任务的pixelMap，需在资源rawfile文件夹中预置testUpdateImage.png图片
  const fileData = resourceMgr.getRawFileContentSync('testUpdateImage.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();
  // 构建parameters
  let parameters: quickBarManager.ParameterItem = {
    key: 'testKey',
    value: 'testValue'
  }
  let taskInfo: quickBarManager.QuickTaskInfo = {
    taskName: 'newTaskName',
    abilityName: 'newEntryAbility',
    // 参数可选
    moduleName: 'newModuleName',
    // 参数可选
    taskIcon: imagePixelMap,
    // 参数可选
    taskDetail: '任务的描述',
    // 参数可选
    parameters: [parameters]
  }

  const task: quickBarManager.QuickTask = {
    taskId: 1,
    categoryId: 1,
    taskInfo: taskInfo
  }

  try {
    await quickBarManager.updateQuickTask(context, task);
  } catch (error) {
    console.error(`updateQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

### Code block 12

```
/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function deleteQuickTask(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 删除任务id为1的任务
    await quickBarManager.deleteQuickTask(context, 1);
  } catch (error) {
    console.error(`deleteQuickTask failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

### Code block 13

```
/**
 * 可以通过自定义组件的内置方法获取Context信息
 * 具体方法：this.getUIContext().getHostContext();
 */
async function deleteCustomCategory(context: Context) {
  if (context === undefined) {
    return;
  }
  try {
    // 删除分组id为1的分组
    await quickBarManager.deleteCustomCategory(context, 3);
  } catch (error) {
    console.error(`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
  }
}
```

### Code block 14

```
import { quickBarManager } from '@kit.DeskTopExtensionKit';
import { image } from '@kit.ImageKit';
import { resourceManager } from '@kit.LocalizationKit';
```

### Code block 15

```
// 获取资源管理器
const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}
const resourceMgr: resourceManager.ResourceManager = context.resourceManager;

// 从rawfile目录中获取图片
const whiteFileData = resourceMgr.getRawFileContentSync('icon.png');
const whiteImageSource = image.createImageSource(whiteFileData.buffer);
const imagePixelMap = await whiteImageSource.createPixelMap();

try {
  // 增加分组
  await quickBarManager.addQuickBarGroup(context, {
    groupKey: 'group_one', // 分组名
    groupIcon: imagePixelMap // 分组图标
  });
} catch (error) {
  console.error(`error code: ${error.code}, error message: ${error.message}`);
}
```

### Code block 16

```
const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 获取所有分组
  const groups = await quickBarManager.getQuickBarGroups(context);
  console.info(`groups: ${JSON.stringify(groups)}`);
} catch (error) {
  console.error(`error code: ${error.code}, error message: ${error.message}`);
}
```

### Code block 17

```
const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 将id为80的窗口，增加到分组名为 group_one 的分组
  await quickBarManager.setWindowToGroup(context, '80', 'group_one');
} catch (error) {
  console.error(`deleteCustomCategory failed. error code: ${error.code}, error message: ${error.message}`);
}
```

### Code block 18

```
const context: Context | undefined = this.getUIContext().getHostContext();
if (!context) {
  console.error('context is null');
  return;
}

try {
  // 删除分组名为group_one的分组
  await quickBarManager.deleteQuickBarGroup(context, 'group_one');
} catch (error) {
  console.error(`error code: ${error?.code}, error message: ${error?.message}`);
}
```

### Code block 19

```
import { quickBarManager }  from '@kit.DeskTopExtensionKit';
import { resourceManager } from '@kit.LocalizationKit';
import { image } from '@kit.ImageKit';
```

### Code block 20

```
let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}
try {
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建图标的pixelMap，需在资源rawfile文件夹中预置icon.png图片
  const fileData = resourceMgr.getRawFileContentSync('icon.png');
  const imageSource = image.createImageSource(fileData.buffer);
  const imagePixelMap = await imageSource.createPixelMap();

  await quickBarManager.setQuickBarCombineIcon(context, imagePixelMap);
  console.info('setQuickBarCombineIcon success');
} catch (error) {
  console.error(`setQuickBarCombineIcon failed. error code: ${error.code}, error message: ${error.message}`);
}
```

### Code block 21

```
let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}
try {
  // 获取resourceManager资源管理器
  const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
  // 创建前景图的pixelMap，需在资源rawfile文件夹中预置foreground.png图片
  const foregroundFileData = resourceMgr.getRawFileContentSync('foreground.png');
  const foregroundImageSource = image.createImageSource(foregroundFileData.buffer);
  const foregroundPixelMap = await foregroundImageSource.createPixelMap();

  // 创建背景图的pixelMap，需在资源rawfile文件夹中预置background.png图片
  const backgroundFileData = resourceMgr.getRawFileContentSync('background.png');
  const backgroundImageSource = image.createImageSource(backgroundFileData.buffer);
  const backgroundPixelMap = await backgroundImageSource.createPixelMap();

  await quickBarManager.setQuickBarLayeredIcon(context, foregroundPixelMap, backgroundPixelMap);
  console.info('setQuickBarLayeredIcon success');
} catch (error) {
  console.error(`setQuickBarLayeredIcon failed. error code: ${error.code}, error message: ${error.message}`);
}
```

### Code block 22

```
let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}
const completed: number = 50;
const total: number = 100;

try {
  await quickBarManager.setProgressValue(context, completed, total);
  console.info('setProgressValue success');
} catch (error) {
  console.error(`setProgressValue failed. error code: ${error.code}, error message: ${error.message}`);
}
```

### Code block 23

```
let context: Context | undefined = this.getUIContext().getHostContext();
if (context === undefined) {
  return;
}

try {
  // 设置进度状态为PAUSED，暂停状态
  await quickBarManager.setProgressState(context, quickBarManager.ProgressState.PAUSED);
  console.info('setProgressState success');
} catch (error) {
  console.error(`setProgressState failed. error code: ${error.code}, error message: ${error.message}`);
}
```
