# 自定义声明式节点 (BuilderNode)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode_

bgColor change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
  }
  build() {
    NodeContainer(new TextNodeController(this.message))
  }
}


@ComponentV2({ freezeWhenInactive: true })
struct BuildNodeChild {
  // 使用Params实例作为storage属性。
  storage: Params = Params.instance();
  @Param message: string = '';


  // 使用@Monitor装饰器监听storage.message的变化。
  @Monitor('storage.bgColor')
  onMessageChange(monitor: IMonitor) {
    console.info(`FreezeBuildNode buildNodeChild message callback func ${this.message}`);
  }


  build() {
    Text(`[a]: ${this.message}`)
      .fontSize(25)
      .backgroundColor(this.storage.bgColor)
      .margin(2)
  }
}

在上面的示例中：

点击Reduce length to 5后，被移除的两个组件会进入Repeat缓存池，然后点击Change bgColor更改bgColor的值触发节点刷新。

开启组件冻结（freezeWhenInactive: true）和BuilderNode节点开启冻结（即inheritFreezeOptions: true），只有剩余节点中@Monitor装饰的方法onMessageChange被触发，如示例中屏上的5个节点会刷新并打印BuilderNode子组件monitor的5条日志，缓存池中的节点则不会。

Repeat和TabContent混用

BuilderNode节点开启冻结功能（即通过设置inheritFreezeOptions为true）后，支持与Repeat、TabContent等不同组件混合使用，示例如下：

import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';


// 定义一个Params类，用于传递参数。
@ObservedV2
class Params {
  // 单例模式，确保只有一个Params实例。
  static singleton_: Params;


  // 获取Params实例的方法。
  static instance() {
    if (!Params.singleton_) {
      Params.singleton_ = new Params(0);
    }
    return Params.singleton_;
  }


  // 使用@Trace装饰器装饰message属性，以便跟踪其变化。
  @Trace message: string = "Hello";
  index: number = 0;


  constructor(index: number) {
    this.index = index;
  }
}


// 定义一个buildNodeChild组件。
@ComponentV2({ freezeWhenInactive: true }) // BuilderNode下面的子组件开启冻结。
struct buildNodeChild {
  // 使用Params实例作为storage属性。
  storage: Params = Params.instance();
  @Param index: number = 0;


  // 使用@Monitor装饰器监听storage.message的变化。
  @Monitor("storage.message")
  onMessageChange(monitor: IMonitor) {
    console.info(`FreezeBuildNode buildNodeChild message callback func ${this.storage.message}, index:${this.index}`);
  }


  build() {
    Text(`buildNode Child message: ` +`\n` + `${this.storage.message}`).fontSize(30)
  }
}


// 定义一个buildText函数。
@Builder
function buildText(params: Params) {
  Column() {
    buildNodeChild({ index: params.index })
  }
}


class TextNodeController extends NodeController {
  private textNode: BuilderNode<[Params]> | null = null;
  private index: number = 0;


  // 构造函数接收一个index参数。
  constructor(index: number) {
    super();
    this.index = index;
  }


  // 创建并返回一个FrameNode。
  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.index));
    this.textNode.inheritFreezeOptions(true); // BuilderNode开启冻结。
    return this.textNode.getFrameNode();
  }
}


// 定义一个Index组件。
@Entry
@ComponentV2
export struct RepeatTab {
  // 使用Params实例作为storage属性。
  storage: Params = Params.instance();
  private data: number[] = [0, 1];


  build() {
    Row() {
      Column() {
        Button("change").width('80%').height(40).fontSize(30)
          .onClick(() => {
            this.storage.message += 'a';
          })


        Tabs() {
          // 使用Repeat重复渲染TabContent组件。
          Repeat<number>(this.data)
            .each((obj: RepeatItem<number>) => {
              TabContent() {
                FreezeBuildNode({ index: obj.item })
                  .margin({ top:20,bottom:5,left:5,right:5 })
              }.tabBar(`tab${obj.item}`)
            })
            .key((item: number) => item.toString())
        }
      }
    }
    .width('100%')
    .height('100%')
  }
}


// 定义一个FreezeBuildNode组件。
@ComponentV2({ freezeWhenInactive: true })
struct FreezeBuildNode {
  // 使用Params实例作为storage属性。
  storage: Params = Params.instance();
  @Param index: number = 0;


  // 使用@Monitor装饰器监听storage.message的变化。
  @Monitor("storage.message")
  onMessageChange(monitor: IMonitor) {
    console.info(`FreezeBuildNode message callback func ${this.storage.message}, index: ${this.index}`);
  }


  build() {
    NodeContainer(new TextNodeController(this.index))
      .width('100%')
      .height('100%')
  }
}

在上面的示例中：

1.点击change更改message的值，当前正在显示的BuilderNode下面的子组件buildNodeChild组件中@Monitor注册的方法onMessageUpdated被触发。

2.点击tab1切换到另外的TabContent，该TabContent的状态由inactive变为active，对应的BuilderNode下面的子组件buildNodeChild组件中@Monitor注册的方法onMessageUpdated被触发。

3.再次点击change更改message的值，仅当前显示的TabContent子组件中@Monitor注册的方法onMessageUpdated被触发。其他inactive的TabContent组件不会触发@Monitor。

设置BuilderNode支持内部@Consume接收外部的@Provide数据（状态管理V1）

从API version 20开始，通过配置BuildOptions参数，BuilderNode内部自定义组件的@Consume支持接收所在页面的@Provide数据。

参见示例代码。

设置BuilderNode支持内部@Consumer接收外部的@Provider数据（状态管理V2）

从API version 23开始，通过配置BuildOptions参数，BuilderNode内部自定义组件的@Consumer支持接收所在页面的@Provider数据。

参见示例代码。

BuilderNode结合ArkWeb组件实现预渲染页面

预渲染适用于Web页面启动与跳转等场景。通过结合BuilderNode，可以将ArkWeb组件提前进行离线预渲染，组件不会即时挂载至页面，而是在需要时通过NodeController动态挂载与显示。此举能够提高页面切换的流畅度及用户体验。

说明

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考声明权限。

创建载体Ability，并创建Web组件。

import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { createNWeb } from '../Common/CommonIndex';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';


const DOMAIN = 0x0000;


export default class EntryAbility extends UIAbility {
  // ···


  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');


    windowStage.loadContent('pages/Index', (err) => {
      createNWeb('', windowStage.getMainWindowSync().getUIContext());
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }


  // ···
}
EntryAbility.ets

创建NodeContainer和对应的NodeController，渲染后台Web组件。

import { UIContext } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, Size, FrameNode } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';


// @Builder中为动态组件的具体组件内容。
// Data为入参封装类。
class Data {
  public url: string = '';
  public controller: WebviewController = new webview.WebviewController();
}


// 通过布尔变量shouldInactive控制网页在后台完成预渲染后停止渲染。
let shouldInactive: boolean = true;


@Builder
function webBuilder(data: Data) {
  Column() {
    Web({ src: data.url, controller: data.controller })
      .onPageBegin(() => {
        // 调用onActive，开启渲染。
        data.controller.onActive();
      })
      .onFirstMeaningfulPaint(() => {
        if (!shouldInactive) {
          return;
        }
        // 在预渲染完成时触发，停止渲染。
        data.controller.onInactive();
        shouldInactive = false;
      })
      .width('100%')
      .height('100%')
  }
}


let wrap = wrapBuilder<Data[]>(webBuilder);


// 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。
export class MyNodeController2 extends NodeController {
  private rootnode: BuilderNode<Data[]> | null = null;


  // 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContainer中。
  // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
  makeNode(uiContext: UIContext): FrameNode | null {
    hilog.info(0xF811, 'testTag', '%{public}s', ' uicontext is undefined :' + (uiContext === undefined));
    if (this.rootnode != null) {
      // 返回FrameNode节点。
      return this.rootnode.getFrameNode();
    }
    // 返回null控制动态组件脱离绑定节点。
    return null;
  }


  // 当布局大小发生变化时进行回调。
  aboutToResize(size: Size) {
    hilog.info(0xF811, 'testTag', '%{public}s', 'aboutToResize   width   : ' + size.width + ' height : ' + size.height);
  }


  // 当controller对应的NodeContainer在Appear的时候进行回调。
  aboutToAppear() {
    hilog.info(0xF811, 'testTag', '%{public}s', 'aboutToAppear');
    // 切换到前台后，不需要停止渲染。
    shouldInactive = false;
  }


  // 当controller对应的NodeContainer在Disappear的时候进行回调。
  aboutToDisappear() {
    hilog.info(0xF811, 'testTag', '%{public}s', 'aboutToDisappear');
  }


  // 此函数为自定义函数，可作为初始化函数使用。
  // 通过UIContext初始化BuilderNode，再通过BuilderNode中的build接口初始化@Builder中的内容。
  initWeb(url: string, uiContext: UIContext, control: WebviewController) {
    if (this.rootnode != null) {
      return;
    }
    // 创建节点，需要uiContext。
    this.rootnode = new BuilderNode(uiContext);
    // 创建动态Web组件。
    this.rootnode.build(wrap, { url: url, controller: control });
  }
}


// 创建Map保存所需要的NodeController。
let nodeMap: Map<string, MyNodeController2 | undefined> = new Map();
// 创建Map保存所需要的WebViewController。
let controllerMap: Map<string, WebviewController | undefined> = new Map();


// 初始化需要UIContext 需在Ability获取。
export const createNWeb = (url: string, uiContext: UIContext) => {
  // 创建NodeController。
  let baseNode = new MyNodeController2();
  let controller = new webview.WebviewController();
  // 初始化自定义Web组件。
  baseNode.initWeb(url, uiContext, controller);
  controllerMap.set(url, controller);
  nodeMap.set(url, baseNode);
}


// 自定义获取NodeController接口。
export const getNWeb = (url: string): MyNodeController2 | undefined => {
  return nodeMap.get(url);
}
CommonIndex.ets

通过NodeContainer使用已经预渲染的页面。

// 使用NodeController的Page页。
// pages/ArkWebPage.ets
import { createNWeb, getNWeb } from '../Common/CommonIndex';


@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        // NodeContainer用于与NodeController节点绑定，rebuild会触发makeNode。
        // Page页通过NodeContainer接口绑定NodeController，实现动态组件页面显示。
        NodeContainer(getNWeb(''))
          .height('90%')
          .width('100%')
          .id('ArkWebPage')
      }
      .width('100%')
    }
    .height('100%')
  }
}
ArkWebPage.ets
自定义渲染节点 (RenderNode)
设置自定义节点跨语言属性
