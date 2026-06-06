# UI调优

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-inspector-profiler_

-----------------ViewPUInfo--------------------
[-dumpAll, viewId=4, isRecursive=true]


@Component
Page[4]


View Hierarchy:


|--Page[4]ViewPU {isViewActive: true, isDeleting_: false}
  |--Child[7]ViewPU {isViewActive: true, isDeleting_: false}
    |--GrandChild[10]ViewPU {isViewActive: true, isDeleting_: false}


State variables:
|--Page[4]
  @State 'message'[0]
  |--Owned by @Component 'Page'[4]
  |--Sync peers: {
    @Link 'message'[-1] <@Component 'Child'[7]>
  }
  dependencies: variable assignment affects elmtIds: Text[6]
  |--Dependent elements: Text[6]; @Component 'Child'[7], Text[9]; @Component 'GrandChild'[10], Text[12]


Registered Element IDs:


|--Page[4]: {
    Column[5]
    Text[6]
    Child[7]
  }[3]
  |--Child[7]: {
      Column[8]
      Text[9]
      GrandChild[10]
    }[3]
    |--GrandChild[10]: {
        Column[11]
        Text[12]
      }[2]
Total: 8


Dirty Registered Element IDs:


|--Page[4]: {
  }[0]
  |--Child[7]: {
    }[0]
    |--GrandChild[10]: {
      }[0]
Total: 0

命令2：打印指定自定义组件的状态变量信息。例如，dump组件id为7的状态变量，可执行如下命令：

hdc shell hidumper -s WindowManagerService -a '-w 90 -jsdump -dumpAll -viewId=7'

输出信息如下。

--------------------ViewPUInfo--------------------
[-dumpAll, viewId=7, isRecursive=false]


@Component
Child[7]


View Hierarchy:


|--Child[7]ViewPU {isViewActive: true, isDeleting_: false}
  |--GrandChild[10]ViewPU {isViewActive: true, isDeleting_: false}


State variables:
|--Child[7]
  @Link 'message'[-1]
  |--Owned by @Component 'Child'[7]
  |--Sync peers: {
    @Link 'message'[-2] <@Component 'GrandChild'[10]>
  }
  dependencies: variable assignment affects elmtIds: Text[9]
  |--Dependent elements: Text[9]; @Component 'GrandChild'[10], Text[12]


Registered Element IDs:


|--Child[7]: {
    Column[8]
    Text[9]
    GrandChild[10]
  }[3]


Dirty Registered Element IDs:


|--Child[7]: {
  }[0]
状态管理Profiler调优能力

DevEco Studio的Profiler工具可抓取状态变量的变化打点。在Profiler工具中选择ArkUI，则抓取ArkUI State泳道。该泳道主要展示录制期间有哪些状态变量发生变化，和其会触发哪些关联组件刷新，以便开发者根据状态变量关联组件的数量分析当前场景内的更新负载。

状态管理在Profiler工具中，会展示如下信息内容：

名称	含义
Start Time	状态变量修改的时间
Attributes	状态变量的属性名
Owned by Component	状态变量所属自定义组件名
Owned by Class	状态变量所属类名
Property Type	状态变量装饰器名称
Current Values	状态变量当前值

录制ArkUI State泳道图步骤如下：

步骤1：点击ArkUI模板创建session，并启动录制。录制过程中点击第一个Text组件，修改状态变量@State message为hello world1，通知其同步对象@Link message的变更，及其关联组件的刷新。

步骤2： 录制结束等待数据处理完成，ArkUI State泳道会记录状态变量变化的事件打点。

图1 录制ArkUI State泳道流程示意图

步骤3：选中状态变量变化的打点，将显示当前状态变量更新触发了哪些组件的刷新，以及对应组件的创建、测量和布局的耗时。

图2 ArkUI State泳道图示意图

说明

由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI State泳道。

状态管理Inspector调试能力

DevEco Studio的ArkUI Inspector可以显示当前页面自定义组件内的状态变量的详细信息，具体包括以下内容。

名称	含义
decorator	自定义组件内状态变量装饰器，如@State、@Link等。
name	自定义组件内状态变量的属性名，如@State message: string = 'hello world';中message。
value	当前状态变量值。对于超长或者嵌套多层的复杂类型会进行截断。
mode	

状态变量观察模式，包括：

Compatible Mode：状态管理V1状态变量，且其装饰变量的类型没有@Track装饰的属性。

Track Mode：状态管理V1状态变量，且其装饰的类型有@Track装饰的属性。

V2：状态管理V2状态变量。


elmtIds	

状态变量关联的组件。声明式UI语法规则中，状态会驱动UI刷新。

目前状态管理可以做到组件级别的更新，即状态变量变化后仅会触发使用该变量的组件的刷新。


syncPeers	状态变量同步对象，仅限状态管理V1的状态变量。例如@State的同步对象为@Link。

打开ArkUI Inspector展示@Component Page自定义组件状态变量相关信息如下。

图3 ArkUI Inspector显示状态变量相关信息

说明

由于隐私安全政策，已上架应用市场的应用不支持使用ArkUI Inspector。

以上主要介绍了状态管理的hidumper、调试与调优能力，这些工具方便开发者调测，有助于提升开发高性能应用的效率。

Trace调试能力

ArkUI内部针对关键的UI处理流程添加了Trace信息，帮助开发者通过Trace工具观测应用的UI耗时，辅助定位问题。详细Trace说明及案例参考：常用Trace使用指导。

Inspector调试能力

ArkUI Inspector是DevEco Studio内置的页面布局检查工具，帮助开发者查看应用的UI层级结构、组件属性和布局效果。详细Inspector使用方法及案例参考：页面布局检查器ArkUI Inspector使用指导。

UI预览
UI高性能开发
