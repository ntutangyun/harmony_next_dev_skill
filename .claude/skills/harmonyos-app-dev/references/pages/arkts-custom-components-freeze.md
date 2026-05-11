# 自定义组件冻结功能（V1）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-freeze_

- called by content ${this.index}`);
    this.logNumber++;
  }


  build() {
    Column() {
      Text('msg:' + `${this.message}`)
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
      Text('log number:' + `${this.logNumber}`)
        .fontSize(30)
        .fontWeight(FontWeight.Bold)
    }
  }
}
MyNavigationTestStack.ets

在上面的示例中：

1.点击change message更改message的值，当前正在显示的MyNavigationTestStack组件中的@Watch注册的方法info被触发。

2.点击Next Page切换到PageOne，创建PageOneStack节点。

3.再次点击change message更改message的值，仅PageOneStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

4.再次点击Next Page切换到PageTwo，创建PageTwoStack节点。

5.再次点击change message更改message的值，仅PageTwoStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

6.再次点击Next Page切换到PageThree，创建PageThreeStack节点。

7.再次点击change message更改message的值，仅PageThreeStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

8.点击Back Page回到PageTwo，此时，仅PageTwoStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

9.再次点击Back Page回到PageOne，此时，仅PageOneStack中的NavigationContentMsgStack子组件中@Watch注册的方法info被触发。

10.再次点击Back Page回到初始页，此时，无任何触发。

组件复用

组件复用通过重利用缓存池中已存在的节点，而非创建新节点，来优化UI性能并提升应用流畅度。复用池中的节点尽管未在UI组件树上展示，但是状态变量的更改仍会触发UI刷新。为了解决复用池中组件异常刷新问题，可以使用组件冻结避免复用池中的组件刷新。

组件复用、if和组件冻结混用场景

下面是组件复用、if组件和组件冻结混合使用场景的例子，if组件绑定的状态变量变化成false时，触发子组件ChildComponent的下树，由于ChildComponent被标记了组件复用，所以不会被销毁，而是进入复用池，这个时候如果同时开启了组件冻结，则可以使在复用池里不再刷新。

import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
const TAG = 'FreezeChild';


@Reusable
@Component({ freezeWhenInactive: true })
struct ChildComponent {
  @Link @Watch('descChange') desc: string;
  @State count: number = 0;


  descChange() {
    hilog.info(DOMAIN, TAG, `ChildComponent messageChange ${this.desc}`);
  }


  aboutToReuse(params: Record<string, ESObject>): void {
    this.count = params.count as number;
  }


  aboutToRecycle(): void {
    // 输出recycled提示，确认组件进入复用池
    hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
  }


  build() {
    Column() {
      Text(`ChildComponent desc: ${this.desc}`)
        .fontSize(20)
      Text(`ChildComponent count ${this.count}`)
        .fontSize(20)
    }.border({ width: 2, color: Color.Pink })
  }
}


@Entry
@Component
struct Page {
  @State desc: string = 'Hello World';
  @State flag: boolean = true;
  @State count: number = 0;


  build() {
    Column() {
      Button(`change desc`).onClick(() => {
        this.desc += '!';
      })
      Button(`change flag`).onClick(() => {
        this.count++;
        this.flag = !this.flag;
      })
      if (this.flag) {
        ChildComponent({ desc: this.desc, count: this.count })
      }
    }
    .height('100%')
  }
}
ComponentReuse.ets

在上面的示例中：

点击change flag，改变flag为false：
被标记@Reusable的ChildComponent组件在下树时，不会被销毁，而是进入复用池，触发aboutToRecycle生命周期，同时设置状态为inactive。
ChildComponent同时也开启了组件冻结，当其状态为inactive时，不会响应任何状态变量变化带来的UI刷新。
点击change desc，触发Page的成员变量desc的变化：
desc是@State装饰的，其变化会通知给其子组件ChildComponent@Link装饰的desc。
但因为ChildComponent是inactive状态，且开启了组件冻结，所以这次变化并不会触发@Watch('descChange')的回调和ChildComponentUI刷新。如果没有开启组件冻结，当前@Watch('descChange')会立即回调，且复用池内的ChildComponent组件也会对应刷新。
再次点击change flag，改变flag为true：
ChildComponent从复用池中重新加入到组件树上。
回调aboutToReuse生命周期，将当前最新的count值同步给子组件。desc是通过@State到@Link同步的，所以无需开发者手动在aboutToReuse中赋值。
设置ChildComponent为active状态，并且刷新在inactive时没有刷新的组件，在当前例子中，就是Text(ChildComponent desc: ${this.desc})。

LazyForEach、组件复用和组件冻结混用场景

在数据很多的长列表滑动场景下，开发者会使用LazyForEach来按需创建组件，同时配合组件复用降低在滑动过程中因创建和销毁组件带来的开销。但是开发者如果根据其复用类型不同，设置了reuseId，或者为了保证滑动性能设置了较大的cacheCount，这就可能使复用池或者LazyForEach缓存较多的节点。在这种情况下，如果开发者触发List下所有子节点的刷新，就会带来节点刷新数量过多的问题，这个时候，可以考虑搭配组件冻结使用。

import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
const TAG = 'FreezeChild';


// 用于处理数据监听的IDataSource的基本实现
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];


  public totalCount(): number {
    return 0;
  }


  public getData(index: number): string {
    return this.originDataArray[index];
  }


  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      hilog.info(DOMAIN, TAG, 'add listener');
      this.listeners.push(listener);
    }
  }


  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      hilog.info(DOMAIN, TAG, 'remove listener');
      this.listeners.splice(pos, 1);
    }
  }


  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }


  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }


  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }


  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }


  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    });
  }
}


class MyDataSource extends BasicDataSource {
  private dataArray: string[] = [];


  public totalCount(): number {
    return this.dataArray.length;
  }


  public getData(index: number): string {
    return this.dataArray[index];
  }


  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }


  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}


@Reusable
@Component({freezeWhenInactive: true})
struct ChildComponent {
  @Link @Watch('descChange') desc: string;
  @State item: string = '';
  @State index: number = 0;


  descChange() {
    hilog.info(DOMAIN, TAG, `ChildComponent messageChange ${this.desc}`);
  }


  aboutToReuse(params: Record<string, ESObject>): void {
    this.item = params.item;
    this.index = params.index;
  }


  aboutToRecycle(): void {
    hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
  }


  build() {
    Column() {
      Text(`ChildComponent index: ${this.index} item: ${this.item}`)
        .fontSize(20)
      Text(`desc: ${this.desc}`)
        .fontSize(20)
    }.border({width: 2, color: Color.Pink})
  }
}


@Entry
@Component
struct Page {
  @State desc: string = 'Hello World';
  private data: MyDataSource = new MyDataSource();


  aboutToAppear() {
    for (let i = 0; i < 50; i++) {
      this.data.pushData(`Hello ${i}`);
    }
  }


  build() {
    Column() {
      Button(`change desc`).onClick(() => {
        hiTraceMeter.startTrace('change desc', 1);
        this.desc += '!';
        hiTraceMeter.finishTrace('change desc', 1);
      })
      List({ space: 3 }) {
        LazyForEach(this.data, (item: string, index: number) => {
          ListItem() {
            ChildComponent({index: index, item: item, desc: this.desc}).reuseId(index % 10 < 5 ? '1': '0')
          }
        }, (item: string) => item)
      }.cachedCount(5)
    }
    .height('100%')
  }
}
ComponentReuse1.ets

在上面的示例中：

滑动到index为14的位置，当前屏幕上可见区域内有15个ChildComponent。
在滑动过程中：
列表上端的ChildComponent滑出可视区域外，此时先进入LazyForEach的缓存区域内，被设置inactive。在滑出LazyForEach缓存区域外后，因为标记了组件复用，所以并不会被析构，而是会进入复用池，此时再次被设置inactive。
列表下端LazyForEach的缓存节点会进入List范围内，此时会试图请求创建新的节点进入LazyForEach的缓存，发现有可复用的节点时，从复用池中拿出已有节点，触发aboutToReuse生命周期回调，此时因为节点进入的是LazyForEach的缓存区域，所以其状态依旧是inactive。
点击change desc，触发Page的成员变量desc的变化：
desc是@State装饰的，其变化会通知给其子组件ChildComponent@Link装饰的desc。
非可视区域内的ChildComponent是inactive状态，且开启了组件冻结，所以这次变化只触发可视区域内的15个节点的@Watch('descChange')回调，并只刷新对应可视区域内的15个节点。LazyForEach和复用池中的节点并不会刷新，也不会触发@Watch回调。

图示如下：

可通过trace观察，仅触发了15个ChildComponent节点的刷新。

LazyForEach、if、组件复用和组件冻结混用场景

下面的场景中展示了LazyForEach、if、组件复用和组件冻结混用场景。在同一个父自定义组件下，可复用的节点可能通过不同的方式进入复用池，比如：

通过滑动从LazyForEach的缓存区域下树，进入复用池。
if条件切换通知子节点下树，进入复用池。
import { hilog, hiTraceMeter } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
const TAG = 'FreezeChild';


class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];


  public totalCount(): number {
    return 0;
  }


  public getData(index: number): string {
    return this.originDataArray[index];
  }


  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      hilog.info(DOMAIN, TAG, 'add listener');
      this.listeners.push(listener);
    }
  }


  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      hilog.info(DOMAIN, TAG, 'remove listener');
      this.listeners.splice(pos, 1);
    }
  }


  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }


  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }


  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }


  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }


  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    });
  }
}


class MyDataSource extends BasicDataSource {
  private dataArray: string[] = [];


  public totalCount(): number {
    return this.dataArray.length;
  }


  public getData(index: number): string {
    return this.dataArray[index];
  }


  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }


  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}


@Reusable
@Component({ freezeWhenInactive: true })
struct ChildComponent {
  @Link @Watch('descChange') desc: string;
  @State item: string = '';
  @State index: number = 0;


  descChange() {
    hilog.info(DOMAIN, TAG, `ChildComponent messageChange ${this.desc}`);
  }


  aboutToReuse(params: Record<string, ESObject>): void {
    this.item = params.item;
    this.index = params.index;
  }


  aboutToRecycle(): void {
    hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
  }


  build() {
    Column() {
      Text(`ChildComponent index: ${this.index} item: ${this.item}`)
        .fontSize(20)
      Text(`desc: ${this.desc}`)
        .fontSize(20)
    }.border({ width: 2, color: Color.Pink })
  }
}


@Entry
@Component
struct Page {
  @State desc: string = 'Hello World';
  @State flag: boolean = true;
  private data: MyDataSource = new MyDataSource();


  aboutToAppear() {
    for (let i = 0; i < 50; i++) {
      this.data.pushData(`Hello ${i}`);
    }
  }


  build() {
    Column() {
      Button(`change desc`).onClick(() => {
        hiTraceMeter.startTrace('change desc', 1);
        this.desc += '!';
        hiTraceMeter.finishTrace('change desc', 1);
      })
      Button(`change flag`).onClick(() => {
        hiTraceMeter.startTrace('change flag', 1);
        this.flag = !this.flag;
        hiTraceMeter.finishTrace('change flag', 1);
      })
      List({ space: 3 }) {
        LazyForEach(this.data, (item: string, index: number) => {
          ListItem() {
            ChildComponent({ index: index, item: item, desc: this.desc }).reuseId(index % 10 < 5 ? '1' : '0')
          }
        }, (item: string) => item)
      }
      .cachedCount(5)
      .height('60%')
      if (this.flag) {
        ChildComponent({ index: -1, item: 'Hello', desc: this.desc }).reuseId('1')
      }
    }
    .height('100%')
  }
}

在上面的示例中：

当滑动到index为14的位置，屏幕上可见区域内有10个ChildComponent，9个是LazyForEach的子节点，1个是if的子节点。
点击change flag，if的条件变成false，其子节点ChildComponent进入复用池。当前屏幕显示9个节点。
此时不管是通过LazyForEach还是if下树的节点都会进入Page节点下的复用池。
点击change desc，仅更新屏幕上的9个ChildComponent节点，具体可参考下面的trace。
再次点击change flag，if的条件变成true，ChildComponent从复用池中重新加入到组件树上，其状态变成active。
再次点击change desc，从复用池中通过if和LazyForEach上树的节点都可正常刷新。

开启组件冻结trace：

没有开启组件冻结trace：

组件混用

当支持组件冻结的场景彼此之间组合使用时，对于不同的API版本，冻结行为会有不同。给父组件设置组件冻结标志，在API version 17及以下，当父组件解冻时，会解冻自己子组件所有的节点；从API version 18开始，父组件解冻时，只会解冻子组件的屏上节点。

Navigation和TabContent的混用

代码示例如下：

// index.ets
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
const TAG = 'FreezeChild';
const TAB_STATE_INITIAL_VALUE = 47;


@Component
struct ChildOfParamComponent {
  @Prop @Watch('onChange') childVal: number;


  onChange() {
    hilog.info(DOMAIN, TAG, `Appmonitor ChildOfParamComponent: childVal changed:${this.childVal}`);
  }


  build() {
    Column() {
      Text(`Child Param: ${this.childVal}`)
    }
  }
}


@Component
struct ParamComponent {
  @Prop @Watch('onChange') paramVal: number;


  onChange() {
    hilog.info(DOMAIN, TAG, `Appmonitor ParamComponent: paramVal changed:${this.paramVal}`);
  }


  build() {
    Column() {
      Text(`val: ${this.paramVal}`)
      ChildOfParamComponent({ childVal: this.paramVal })
    }
  }
}


@Component
struct DelayComponent {
  @Prop @Watch('onChange') delayVal: number;


  onChange() {
    hilog.info(DOMAIN, TAG, `Appmonitor ParamComponent: delayVal changed:${this.delayVal}`);
  }


  build() {
    Column() {
      Text(`Delay Param: ${this.delayVal}`)
    }
  }
}


@Component({ freezeWhenInactive: true })
struct TabsComponent {
  private controller: TabsController = new TabsController();
  @State @Watch('onChange') tabState: number = TAB_STATE_INITIAL_VALUE;


  onChange() {
    hilog.info(DOMAIN, TAG, `Appmonitor TabsComponent: tabState changed:${this.tabState}`);
  }


  build() {
    Column({ space: 10 }) {
      Button(`Incr state ${this.tabState}`)
        .fontSize(25)
        .onClick(() => {
          hilog.info(DOMAIN, TAG, 'Button increment state value');
          this.tabState = this.tabState + 1;
        })
      Tabs({ barPosition: BarPosition.Start, index: 0, controller: this.controller }) {
        TabContent() {
          ParamComponent({ paramVal: this.tabState })
        }.tabBar('Update')
        TabContent() {
          DelayComponent({ delayVal: this.tabState })
        }.tabBar('DelayUpdate')
      }
      .vertical(false)
      .scrollable(true)
      .barMode(BarMode.Fixed)
      .barWidth(400)
      .barHeight(150)
      .animationDuration(400)
      .width('100%')
      .height(200)
      .backgroundColor(0xF5F5F5)
    }
  }
}


@Entry
@Component
struct MyNavigationTestStack {
  @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();


  @Builder
  PageMap(name: string) {
    if (name === 'pageOne') {
      PageOneStack()
    } else if (name === 'pageTwo') {
      PageTwoStack()
    }
  }


  build() {
    Column() {
      Navigation(this.pageInfo) {
        Column() {
          Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
            })
        }
      }.title('NavIndex')
      .navDestination(this.PageMap)
      .mode(NavigationMode.Stack)
    }
  }
}


@Component
struct PageOneStack {
  @Consume('pageInfo') pageInfo: NavPathStack;


  build() {
    NavDestination() {
      Column() {
        TabsComponent()
        Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pushPathByName('pageTwo', null);
          })
      }.width('100%').height('100%')
    }.title('pageOne')
    .onBackPressed(() => {
      this.pageInfo.pop();
      return true;
    })
  }
}


@Component
struct PageTwoStack {
  @Consume('pageInfo') pageInfo: NavPathStack;


  build() {
    NavDestination() {
      Column() {
        Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            this.pageInfo.pop();
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .onBackPressed(() => {
      this.pageInfo.pop();
      return true;
    })
  }
}
ComponentMixing.ets

代码运行结果图如下：

点击Next Page，进入pageOne页面，页面中存在两个tab标签，默认在Update标签，开启组件冻结功能，Tabcontent的标签如果未被选中，状态变量不会刷新，如以下操作。

点击Incr state，日志中查询Appmonitor，存在3个打印。

切换到DelayUpdate标签，点击Incr state，日志中查询Appmonitor，存在2个打印。DelayUpdate中状态变量不会刷新与Update标签中相关的状态变量。

在API version 17及以下：

点击Next page进入下一个页面并返回，标签默认在DelayUpdate，再次点击Incr state，日志中查询Appmonitor，存在4个打印，页面路由返回时，会解冻Tabcontent所有的标签。

在API version 18及以上：

点击Next page进入下一个页面并返回，标签默认在DelayUpdate，再次点击Incr state，日志中查询Appmonitor，存在2个打印，页面路由返回时，只会解冻对应标签的节点。

页面和LazyForEach

Navigation和TabContent混用时，之所以会解锁TabContent标签的子节点，是因为回到前一个页面时会从父组件开始递归解冻子组件，与此行为类似的还有页面生命周期：OnPageShow。OnPageShow会将当前Page中的根节点设置为active状态，TabContent作为页面的子节点，也会被设置为active状态。在屏幕灭屏和屏幕亮屏时会分别触发页面的生命周期：OnPageHide和OnPageShow，因此页面中使用LazyForEach时，手动灭屏和亮屏也能实现页面路由一样的效果，如以下示例代码：

import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
const TAG = 'FreezeChild';


// 用于处理数据监听的IDataSource的基本实现
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: string[] = [];


  public totalCount(): number {
    return 0;
  }


  public getData(index: number): string {
    return this.originDataArray[index];
  }


  // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      hilog.info(DOMAIN, TAG, 'add listener');
      this.listeners.push(listener);
    }
  }


  // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      hilog.info(DOMAIN, TAG, 'remove listener');
      this.listeners.splice(pos, 1);
    }
  }


  // 通知LazyForEach组件需要重载所有子组件
  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded();
    });
  }


  // 通知LazyForEach组件需要在index对应索引处添加子组件
  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }


  // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    });
  }


  // 通知LazyForEach组件需要在index对应索引处删除该子组件
  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index);
    });
  }


  // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to);
    });
  }
}


class MyDataSource extends BasicDataSource {
  private dataArray: string[] = [];


  public totalCount(): number {
    return this.dataArray.length;
  }


  public getData(index: number): string {
    return this.dataArray[index];
  }


  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data);
    this.notifyDataAdd(index);
  }


  public pushData(data: string): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}


@Reusable
@Component({ freezeWhenInactive: true })
struct ChildComponent {
  @State desc: string = '';
  @Link @Watch('sumChange') sum: number;


  sumChange() {
    hilog.info(DOMAIN, TAG, `sum: Change ${this.sum}`);
  }


  aboutToReuse(params: Record<string, Object>): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
  }


  aboutToRecycle(): void {
    hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
  }


  build() {
    Column() {
      Divider()
        .color('#ff11acb8')
      Text(`subcomponent: ${this.desc}`)
        .fontSize(30)
        .fontWeight(30)
      Text(`${this.sum}`)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}


@Entry
@Component({ freezeWhenInactive: true })
struct Page {
  private data: MyDataSource = new MyDataSource();
  @State sum: number = 0;
  @State desc: string = '';


  aboutToAppear() {
    for (let index = 0; index < 20; index++) {
      this.data.pushData(index.toString());
    }
  }


  build() {
    Column() {
      Button(`add sum`).onClick(() => {
        this.sum++;
      })
        .fontSize(30)
        .margin(20)
      List() {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            ChildComponent({ desc: item, sum: this.sum })
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }.cachedCount(5)
    }
    .height('100%')
    .width('100%')
  }
}
ComponentMixing1.ets

在组件复用场景中，已经对LazyForEach的节点进行了详细说明，分为屏上节点和cachedCount节点。

向下滑动LazyForEach，让cachedCount补充节点，点击add sum，搜索打印日志：sum: Change，出现了8条打印。

在API version 17及以下：

灭屏之后亮屏，触发OnPageShow，点击add sum，打印数量为屏上节点与cachedCount数量的总和。

从API version 18开始：

灭屏之后亮屏，触发OnPageShow，点击add sum，只会打印屏上节点数量，不会再解冻cachedCount中的节点。

限制条件
BuilderNode无法继承父组件冻结

在API version 20之前，BuilderNode无法继承父组件冻结。如下面的例子所示，FreezeBuildNode中使用了自定义节点BuilderNode。BuilderNode可以通过命令式动态挂载组件，而组件冻结又是强依赖父子关系来通知是否开启组件冻结。如果父组件使用组件冻结，且组件树的中间层级上又启用了BuilderNode，则BuilderNode的子组件将无法被冻结。

在API version 20及以后，开发者可以通过配置BuilderNode的inheritFreezeOptions接口为true，实现BuilderNode继承冻结的能力。具体示例见BuilderNode对象继承组件冻结。

import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
const DOMAIN = 0x0001;
const TAG = 'FreezeChild';


// 定义一个Params类，用于传递参数
class Params {
  public index: number = 0;


  constructor(index: number) {
    this.index = index;
  }
}


// 定义一个BuildNodeChild组件，它包含一个message属性和一个index属性
@Component
struct BuildNodeChild {
  @StorageProp('buildNodeTest') @Watch('onMessageUpdated') message: string = 'hello world';
  @State index: number = 0;


  // 当message更新时，调用此方法
  onMessageUpdated() {
    hilog.info(DOMAIN, TAG, `FreezeBuildNode builderNodeChild message callback func ${this.message},index:${this.index}`);
  }


  build() {
    Text(`buildNode Child message: ${this.message}`).fontSize(30)
  }
}


// 定义一个buildText函数，它接收一个Params参数并构建一个Column组件
@Builder
function buildText(params: Params) {
  Column() {
    BuildNodeChild({ index: params.index })
  }
}


// 定义一个TextNodeController类，继承自NodeController
class TextNodeController extends NodeController {
  private textNode: BuilderNode<[Params]> | null = null;
  private index: number = 0;


  // 构造函数接收一个index参数
  constructor(index: number) {
    super();
    this.index = index;
  }


  // 创建并返回一个FrameNode
  makeNode(context: UIContext): FrameNode | null {
    this.textNode = new BuilderNode(context);
    this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.index));
    return this.textNode.getFrameNode();
  }
}


// 定义一个Index组件，它包含一个message属性和一个data数组
@Entry
@Component
struct Index {
  @StorageLink('buildNodeTest') message: string = 'hello';
  private data: number[] = [0, 1];


  build() {
    Row() {
      Column() {
        Button('change').fontSize(30)
          .onClick(() => {
            this.message += 'a';
          })
        Tabs() {
          ForEach(this.data, (item: number) => {
            TabContent() {
              FreezeBuildNode({ index: item })
            }.tabBar(`tab${item}`)
          }, (item: number) => item.toString())
        }
      }
    }
    .width('100%')
    .height('100%')
  }
}


// 定义一个FreezeBuildNode组件，它包含一个message属性和一个index属性
@Component({ freezeWhenInactive: true })
struct FreezeBuildNode {
  @StorageProp('buildNodeTest') @Watch('onMessageUpdated') message: string = '1111';
  @State index: number = 0;


  // 当message更新时，调用此方法
  onMessageUpdated() {
    hilog.info(DOMAIN, TAG, `FreezeBuildNode message callback func ${this.message}, index: ${this.index}`);
  }


  build() {
    NodeContainer(new TextNodeController(this.index))
      .width('100%')
      .height('100%')
      .backgroundColor('#FFF0F0F0')
  }
}
Constraints.ets

在上面的示例中：

点击change，改变message的值，当前正在显示的TabContent组件中@Watch注册的方法onMessageUpdated被触发。未显示的TabContent中的BuilderNode节点下组件的@Watch方法onMessageUpdated也被触发，并没有被冻结。

组件冻结与组件复用混用时解冻不会触发Watch

在以下示例中，子组件ChildComponent开启了组件冻结且被标记了组件复用，当if组件绑定的状态变量condition修改为false时，子组件ChildComponent下树并进入复用池。由于子组件开启了组件冻结，所以进入复用池时，该组件也会被冻结。在复用池内，若修改状态变量count，该组件因处于inactive状态，即不会刷新也不会触发Watch回调。

当if组件绑定的状态变量condition修改为true时，子组件ChildComponent出复用池并被标记为active状态，但不会触发状态变量count绑定的Watch回调。这是因为组件复用的执行逻辑早于组件解冻的执行逻辑。子组件被复用时会将脏节点刷新（包括在冻结期间需要延迟刷新的变量绑定的系统组件），并清空脏节点列表。在子组件被复用后，重新被标记为active状态，此时子组件执行解冻逻辑，由于复用时清空了脏节点列表，所以此时判断冻结期间无变量改变，不会触发Watch回调。

import { hilog } from '@kit.PerformanceAnalysisKit';


const DOMAIN = 0x0001;
const TAG = 'FreezeChild';


@Reusable
@Component({ freezeWhenInactive: true })
struct ChildComponent {
  @Link @Watch('onChange') count: number;


  onChange() {
    hilog.info(DOMAIN, TAG, `ChildComponent messageChange ${this.count}`);
  }


  aboutToReuse(params: Record<string, ESObject>): void {
    // 在aboutToReuse中改值，解冻时同样不会触发Watch回调
    this.count++;
    hilog.info(DOMAIN, TAG, `ChildComponent has been reused`);
  }


  aboutToRecycle(): void {
    hilog.info(DOMAIN, TAG, `ChildComponent has been recycled`);
  }


  build() {
    Column() {
      Text(`ChildComponent count: ${this.count}`)
        .fontSize(20)
    }
  }
}


@Entry
@Component
struct Index {
  @State flag: boolean = true;
  @State count: number = 0;


  build() {
    Column() {
      Button(`change flag`)
        .onClick(() => {
          this.flag = !this.flag;
        })
        .margin(10)
        .width('50%')
      Button(`change count`)
        .onClick(() => {
          this.count++;
        })
        .margin(10)
        .width('50%')
      if (this.flag) {
        ChildComponent({ count: this.count })
      }
    }
    .height('100%')
  }
}
FreezeReuse.ets
自定义组件冻结
自定义组件冻结功能（V2）
