# 混淆加固

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-obfuscation_

-混淆选项
--------扫描任务：扫描出来推荐配置白名单字段的数量

选中一个扫描任务，在页面下方会按照以下的树状结构，显示推荐的保留选项和白名单字段。

保留选项
----关键代码
--------白名单字段 --> 字段所在文件:代码行
关键代码：点击关键代码，可以跳转到代码所在的文件和代码行。

白名单字段：点击白名单字段，可以跳转到字段所在的文件和代码行。

如果需要将白名单文件生成到工程中，可以点击生成推荐白名单按钮，ObfuscationHelper会在对应模块下生成推荐白名单文件Hm-recommend-keep-list.txt/Hm-recommend-consumer-keep-list.txt，并提示对应的文件路径。同时在工程根目录下生成对应的白名单Excel表格obfuscation-helper-xxx.xlsx。

点击OK，会关闭提示框，停留在推荐白名单场景。
点击跳转待排查，会关闭提示框，进入到待排查白名单场景。

如果勾选合并白名单文件，点击OK或者跳转待排查时，会在工程根目录下生成合并后的白名单文件Hm-merge-recommend-keep-list.txt，该文件会合并entry模块的Hm-recommend-keep-list.txt和所有模块的Hm-recommend-consumer-keep-list.txt。

如以下模块下生成推荐白名单文件：

在混淆配置中添加白名单文件，有两种方式。
在各模块的build-profile.json5中，将Hm-recommend-keep-list.txt加入到混淆配置files字段下，将Hm-recommend-consumer-keep-list.txt加入到consumerFiles字段下。关于字段的介绍请参考字段说明。
将合并后的文件Hm-merge-recommend-keep-list.txt配置在entry模块build-profile.json5的files字段下。

使用DevEco Studio 6.0.0 Beta1以下版本，按以下步骤操作：
在页面上方，按照以下的树状结构呈现扫描结果。
模块名
----混淆选项
--------扫描任务：扫描出来推荐配置白名单字段的数量

选中一个扫描任务，在页面下方会按照以下的树状结构，显示推荐的保留选项和白名单字段。

保留选项
----关键代码
--------白名单字段 --> 字段所在文件:代码行
关键代码：点击关键代码，可以跳转到代码所在的文件和代码行。

白名单字段：点击白名单字段，可以跳转到字段所在的文件和代码行。

如果需要将白名单文件生成到工程中，可以点击生成推荐白名单按钮，ObfuscationHelper会在对应模块下生成Hm-recommend-keep-list.txt文件，并提示对应的文件路径。同时在工程根目录下生成对应的白名单Excel表格obfuscation-helper-xxx.xlsx。

点击OK，会关闭提示框，停留在推荐白名单场景。
点击跳转待排查，会关闭提示框，进入到待排查白名单场景。

如以下模块下生成推荐白名单文件：

在模块下的build-profile.json5中，将模块下生成的推荐白名单文件Hm-recommend-keep-list.txt加入到混淆配置files或consumerFiles字段下。关于字段的介绍请参考字段说明。

配置待排查白名单

在待排查白名单配置页面，可以查看扫描出来的关键代码，需要开发者根据业务进一步排查，识别白名单字段并配置到文件中。

使用DevEco Studio 6.0.0 Beta1及以上版本，按以下步骤操作：
在页面上方，按照以下的树状结构呈现扫描结果。
模块名
----混淆选项
--------扫描任务：扫描出来待排查的关键代码的数量

选中一个扫描任务，在页面下方会显示待排查的代码。点击关键代码，可以跳转到代码所在的文件和代码行。

跳转到关键代码后，根据具体场景识别是否需要配置白名单字段，排查方式请参考扫描任务。
如果排查后不需要配置白名单，点击待排查，选择已排查，标记该项已经排查。
如果排查后需要配置白名单，点击添加白名单，在输入框中输入保留选项和白名单字段，点击保存白名单。保存后该排查项会被标记为已排查。

被标记为已排查的排查项，后续再次扫描该模块和场景时，如果关联本次的排查记录，将不再需要重复排查。

排查完成后，点击生成排查白名单按钮，ObfuscationHelper会在对应模块下生成排查白名单文件Hm-manual-keep-list.txt/Hm-manual-consumer-keep-list.txt，并提示对应的文件路径。同时在工程根目录下生成对应的白名单Excel表格obfuscation-helper-xxx.xlsx。

如果勾选合并白名单文件，点击OK，会在工程根目录下生成合并后的白名单文件Hm-merge-manual-keep-list.txt，该文件会合并entry模块的Hm-manual-keep-list.txt和所有模块的Hm-manual-consumer-keep-list.txt。

如以下模块下生成排查白名单文件：

在混淆配置中添加白名单文件，有两种方式。
在各模块的build-profile.json5中，将Hm-manual-keep-list.txt加入到混淆配置files字段下，将Hm-manual-consumer-keep-list.txt加入到consumerFiles字段下。关于字段的介绍请参考字段说明。
将合并后的文件Hm-merge-manual-keep-list.txt配置在entry模块build-profile.json5的files字段下。

使用DevEco Studio 6.0.0 Beta1以下版本，按以下步骤操作：
在页面上方，按照以下的树状结构呈现扫描结果。
模块名
----混淆选项
--------扫描任务：扫描出来待排查的关键代码的数量

选中一个扫描任务，在页面下方会按照“关键代码 --> 代码所在文件: 代码行”的结构，显示待排查的代码。点击关键代码，可以跳转到代码所在的文件和代码行。

跳转到关键代码后，根据具体场景识别是否需要配置白名单字段，排查方式请参考扫描任务。如果存在需要配置的字段，在上方的输入框中，输入保留选项和对应的白名单字段。

排查完成后，点击生成排查白名单按钮，ObfuscationHelper会在对应模块下生成Hm-manual-keep-list.txt文件，并提示对应的文件路径。同时在工程根目录下生成对应的白名单Excel表格obfuscation-helper-xxx.xlsx。

如以下模块下生成排查白名单文件：

在模块下的build-profile.json5中，将模块下生成的排查白名单文件Hm-manual-keep-list.txt加入到混淆配置files或consumerFiles字段下。关于字段的介绍请参考字段说明。

查看历史记录

点击生成推荐白名单或者待排查白名单后，会生成一条历史记录，方便开发者后续查看和继续排查白名单。

在ObfuscationHelper的首页，点击底部的历史记录按钮，可查看所有的历史记录。

保存路径是历史记录的缓存文件，鼠标悬停在保存路径上，可以查看白名单文件和Excel表格保存的路径。
点击查看详情图标，可以跳转到对应的白名单场景配置页面。
点击删除图标，可以删除指定的历史记录，以及对应的缓存文件和Excel表格，但是不会删除白名单文件。
扫描任务

以下是ObfuscationHelper的扫描任务，关于保留选项的原理介绍和排查场景请参考混淆规则。

属性混淆

JSON数据解析及对象序列化

在使用JSON/ArkTSUtils.ASON进行转换时，对象类型中的属性需要被保留。

// JSON.parse
class JSONTest {
  prop1: string = ""
  prop2: number = 0
}
// 示例JSON文件test.json
/*
{
  "prop1": "value",
  "prop2": 10
}
*/
const jsonData = buffer.from(this.context.resourceManager.getRawFileContentSync("test.json")).toString();
let demo: JSONTest = JSON.parse(jsonData)       // JSONTest加入keep-property-name
let demo = JSON.parse(jsonData) as JSONTest     // JSONTest加入keep-property-name
let demo = JSON.parse(jsonData) as ESObject as JSONTest      // JSONTest加入keep-property-name
let demo: ESObject = JSON.parse(jsonData)       // 没有明确类型的，包括(ESObject、Object、object)加入待排查白名单中，需要将jsonData中所有的key，如prop1/prop2加入keep-property-name


// ArkTSUtils.ASON.parse
let demo: JSONTest = ArkTSUtils.ASON.parse(jsonData)      // JSONTest加入keep-property-name
let demo = ArkTSUtils.ASON.parse(jsonData) as JSONTest    // JSONTest加入keep-property-name
let demo = ArkTSUtils.ASON.parse(jsonData) as ESObject as ESObject as JSONTest    // JSONTest加入keep-property-name
let demo: ESObject = ArkTSUtils.ASON.parse(jsonData)      // 没有明确类型的，包括(ESObject、Object、object)加入待排查白名单中，需要将jsonData中所有的key，如prop1/prop2加入keep-property-name


// JSON.stringify
let type = new JSONTest()
let str = JSON.stringify(type)    // JSON.stringify加入待排查白名单，需要将JSONTest中的所有属性加入-keep-property-name


// ArkTSUtils.ASON.stringify
let type = new JSONTest()
let str = ArkTSUtils.ASON.stringify(type)  // ArkTSUtils.ASON.stringify加入待排查白名单，需要将JSONTest中的所有属性加入-keep-property-name
通过字符串访问的对象属性

通过中括号形式访问的对象属性，以及Object.defineProperty/Object.defineProperties/Object.getOwnPropertyDescriptor接口中的属性需要被保留。

// 通过中括号形式访问的属性如obj['name']，如果name是变量，加入待排查白名单，需要将name对应的内容加入-keep-property-name
Object.defineProperty(obj, 'y', {})   // 如果y是变量，加入待排查白名单，需要将y对应的内容加入-keep-property-name
Object.defineProperties(obj, {        // 属性prop1/prop2加入推荐白名单-keep-property-name
  prop1: {
    value: 'Hello',
    writable: true,
    enumerable: true,
    configurable: true
  },
  prop2: {
    value: 'Hello',
    writable: true,
    enumerable: true,
    configurable: true
  } 
});
Object.getOwnPropertyDescriptor(obj, 'bbb');    // 如果bbb是变量，加入待排查白名单，需要将bbb对应的内容加入-keep-property-name
obj.s=0; let key='s'; obj[key]    // key是变量，加入待排查白名单，需要将key对应的内容s加入keep-property-name
C++侧访问/操作ArkTS对象属性

开发者需要根据C++接口来排查与其相关的ArkTS中的属性字符串，并手动加入白名单中，涉及的C++接口参考使用Node-API接口设置ArkTS对象的属性。

//index.ets
func() {
  let obj: NapiTestClassObj = { napiTestClassObjData: 0, napiTestClassObjMessage: "hello world" };
  let result: ESObject = testNapi.setProperty(obj, "napiTestClassObjMessage", "100");    // 根据napi_set_property接口排查到ArkTS中的属性napiTestClassObjMessage被修改，需要将napiTestClassObjMessage加入-keep-property-name白名单
  if (obj.napiTestClassObjMessage === "100") {
    console.log("setProperty success");
    return true;
  }
  return false;
}
//napi_init.cpp
static napi_value SetProperty(napi_env env, napi_callback_info info) {
    size_t argc = 3;
    napi_value args[3];
    napi_status status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
    if (status != napi_ok) {
        napi_throw_error(env, nullptr, "Node-API napi_get_cb_info fail");
    }
    status = napi_set_property(env, args[0], args[1], args[2]);    // 扫描napi_set_property关键API
    if (status != napi_ok) {
        napi_throw_error(env, nullptr, "Node-API napi_set_property fail");
        return nullptr;
    }
    return args[0];
}
数据库键值对类型（ValuesBucket）中的属性

数据库键值对类型（ValuesBucket）中的属性需要被保留。

const valueBucket: ValuesBucket = {
  'ID1': ID1,    // ID1、NAME1、AGE1、SALARY1加入到-keep-property-name
  'NAME1': name,
  'AGE1': age,
  'SALARY1': salary
};
自定义装饰器修饰的成员变量、方法、参数

自定义装饰器修饰的成员变量、方法、参数，需要排查是否加入白名单。

function logClass(target: any) {
  console.log('类被创建：', target);    // MyClass未参与混淆，因此被@logClass修饰的类名不需要加入白名单
  return target;
}
export function logMethod(target: any, methodName: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;
  descriptor.value = function (...args: any[]) {
   if(methodName === 'myMethod'){    // methodName会被混淆，与'myMethod'作比较不符合预期，因此被@logMethod修饰的方法名myMethod需要加入白名单
      console.log('调用myMethod方法')
    }
    console.log(`方法 ${methodName} 即将被调用，参数为：`, args);
    const result = originalMethod.apply(this, args);
    console.log(`方法 ${methodName} 调用完毕，结果为：`, result);
    return result;
  };
  return descriptor;
}
function logProperty(target: any, propertyName: string) {
  let value;
  const getter = function () {
    console.log(`正在获取属性 ${propertyName}`);   // propertyName会被混淆，但不影响运行结果，不需要加入白名单
    return value;
  };
  const setter = function (newValue: any) {
    console.log(`正在设置属性 ${propertyName}，新值为：${newValue}`);
    value = newValue;
  };
  Object.defineProperty(target, propertyName, {
    get: getter,
    set: setter,
    enumerable: true,
    configurable: true
  });
  return;
}
@logClass
class MyClass {    // 自定义装饰器修饰的类名，需要排查MyClass是否加入白名单
  @logProperty
  myProperty: number;    // 自定义装饰器修饰的属性，需要排查myProperty是否加入白名单
  constructor() {
    this.myProperty = 10;
  }
  @abcd
  @logMethod
  myMethod(arg1: number, arg2: number) {    // 自定义装饰器修饰的方法，需要排查myMethod是否加入白名单
    return arg1 + arg2;
  }
}
Record类型对象的属性

Record类型对象的属性需要被保留。该场景从DevEco Studio 6.0.1 Beta1版本开始支持。

// 支持扫描的场景
export function hello() {
  const person: Record<string, Object> = {
    ddName: 'zhangsan',    // Record类型对象person的属性ddName、ggAge、isWfStudent，加入到-keep-property-name
    ggAge: 25,
    isWfStudent: true
  }
  person.wwArea = '112';     // 通过点语法新增的属性wwArea，加入到-keep-property-name
  return person;
}
// 不支持扫描的场景
// 1、调用该方法获取Record类型对象，通过点语法添加sssd属性不支持扫描，该属性会被混淆
let ret = hello();
ret.sssd = '1111';
// 2、隐式Record类型的对象parameters的属性a123、b123不支持扫描，会被混淆
export function sendPost3() {
  const want: Want = {
    action: 'ohos.want.action.viewData',
    entities: ['entity.system.browsable'],
    uri: '123',
    parameters: {
      a123: 1,
      b123: 2
    }
  };
}

顶层作用域名称混淆

namespace中导出的名称

namespace中导出的名称、嵌套namespace中导出的名称都需要被保留。

export namespace namespace1 {
  export class namespace1Class1 {      // namespace1Class1加入推荐白名单-keep-global-name
  }
  export namespace namespace1_1 {      // namespace1_1加入推荐白名单-keep-global-name
    export let namespace1Property1_1: string = '111';      // namespace1Property1_1加入推荐白名单-keep-global-name
    export function namespace1Func1_1() {      // namespace1Func1_1加入推荐白名单-keep-global-name
      console.log('namespace1Func1_1 execute success');
    }
    export class namespaceClass1_1{      // namespaceClass1_1加入推荐白名单-keep-global-name
      func(){
        console.log(""namespaceClass1_1 success"")
      }
    }
  }
}
动态导入的名称

动态导入的接口名、属性名和类名，需要被保留。该场景从DevEco Studio 6.0.0 Beta2版本开始支持。

// 导入模块后，使用的类名TestClass加入推荐白名单keep-global-name
try {
  let test = (await import('../model/TestClass')).TestClass
  console.warn(TAG, 'test = ', test);
  // console.warn(TAG, 'test TestClass = ', test.);
  console.warn(TAG, 'test staticGlsAdd = ', test.staticGlsAdd(5, 6));
} catch (e) {
  console.warn(TAG, `error = ${e}`);
}
// 导入模块后，使用的方法名componentClass加入推荐白名单keep-global-name
let util = await import('harlibrary/src/main/ets/utils/Util');
try {
    console.warn(TAG, 'util = ', util);
    console.warn(TAG, 'call util function = ', await util.componentClass());
} catch (e) {
    console.warn(TAG, `error = ${e}`);
}
// 导入模块后，使用default后调用的方法warn加入推荐白名单keep-global-name
import('hsplibrary/src/main/ets/utils/Logger').then(logger => {
    try {
    console.warn(TAG, 'import Logger success.');
    logger.default.warn('this is logger warn')
    } catch (e) {
    console.warn(TAG, `error = ${e}`);
    }
})
// 将动态导入封装为方法，导出的类实例如果是变量，加入待排查白名单，需要排查后将变量对应的值加入keep-global-name
public static importFile<T>(modulePath: string, resultClassName: string) {
    return import(modulePath).then((ns: ESObject) => {
      let res: T = new ns[resultClassName]();   // 该行加入待排查白名单，排查后将resultClassName对应的值TestClass加入keep-global-name
      return res;
    }).catch((err: Error) => {
      console.warn('chisj debug: importFile error = ', err);
      return undefined;
    });
  }
// Index.ets
let modulePath = '../model/TestClass';
let className = 'TestClass';
ImportUtil.importFile<ESObject>(modulePath, className).then((ns:ESObject) => {
    try {
    console.warn(TAG, 'import importFile success')
    console.warn(TAG, 'ns = ', ns)
    console.warn(TAG, 'calcAdd = ', ns?.calcAdd(1, 2));
    } catch (e) {
    console.warn(TAG, `error = ${e}`);
    }
})
// 将动态导入封装为方法，导出的模块myModule调用的方法Calc加入推荐白名单
// ImportUtil.ts
export function dynamicImport<T>(modulePath: string): Promise<T> {
  return import(modulePath).then(module => {
    // 有些模块可能有默认导出，这里处理一下
    return module.default || module as T;
  });
}
// Index.ets
const myModule = await dynamicImport<typeof import('harlibrary')>('harlibrary');
console.warn(TAG, '1 calc = ', myModule.Calc(1, 2))

文件名名称混淆

动态导入的路径名

模块下build-profile.json5文件中，sources字段对应的路径名需要被保留。

// 模块级build-profile.json5
{
  "apiType": "stageMode",
  "buildOption": {
    "arkOptions": {"runtimeOnly": {"sources": ["./aaa/bbb", "./ccc/dddd"]}}  //./aaa/bbb和./ccc/dddd加入keep-file-name
  },
  "buildOptionSet": [
    {
      "name": "release",
      "arkOptions": {
        "runtimeOnly": {"sources": ["./e/f", "./g/h"]},  // ./e/f和./g/h加入keep-file-name
        "obfuscation": {
          "ruleOptions": {
            "enable": true,
            "files": [
              "./obfuscation-rules.txt"
            ]
          }
        }
      },
    },
  ],
......
}
传递给动态路由的路径名

模块下resources/base/profile/route_map.json中，pageSourceFile字段对应的路径名需要被保留。

// 模块下resources/base/profile/route_map.json文件
{
  "routerMap": [
    {
      "name": "PageOne",
      "pageSourceFile": "src/main/ets/pages/directory/PageOne.ets",  // src/main/ets/pages/directory/PageOne.ets加入keep-file-name
      "buildFunction": "PageOneBuilder",
      "data": {
        "description" : "this is PageOne"
      }
    }
  ]
}

导入/导出名称混淆

从so库导入的接口

从so库中导入的接口及其点式调用的属性，需要被保留。

import testNapi from "xxxx.so"    // testNapi加入keep-global-name
import {testNapi} from "xxxx.so"  // testNapi加入keep-global-name
import {testNapi as napi} from "xxxx.so"    // testNapi加入keep-global-name
testNapi.add()    // add加入-keep-property-name
hsp对外暴露的接口
hsp的入口文件(一般为index.ets)中导出的接口名及其属性名，需要被保留。
// 导出的常量
export const LOCAL_NUM = 100  // LOCAL_NUM加入keep-global-name
// 导出的方法
export function harFun() {    // harFun加入keep-global-name
}
// 导出的类名及其属性(包括该类的父类和属性)，如果属性也是一个类，该类也需要以同样的方式保留。
class FatherClass {
  prop4: string = "bbb"
}
class SubClass {
  prop3: string = "bbb"
}
export class HSPClass extends FatherClass{    // 类名称HSPClass加入到-keep-global-name
  prop1: string = "aaa" 
  prop2: SubClass = new SubClass()    // 属性prop1,prop2,prop3,prop4加入到-keep-property-name
}


// 导出的namespace，包括其中的方法、常量、类(保留方式同上)、子namespace
export namespace NmSpace {
  export const NUM_NAME_SPACE = 100   // 常量NUM_NAME_SPACE加入-keep-global-name
  export class classNameSpace {       // 类名称classNameSpace加入-keep-global-name
     prop: string = "bbb"             // 类属性prop加入-keep-property-name
  }
  export function funNameSpace() {    // 方法funNameSpace加入-keep-global-name
  }
}
// 将入口文件相对路径,如 ./index.ets加入keep保留选项。
// 将入口文件名如index.ets加入keep-file-name保留选项。
从hsp导入的接口

从hsp中导入的接口及其点式调用的属性，需要被保留。

import MyClass1 from "xxxx"     // MyClass1加入keep-global-name
import {MyClass2} from "xxxx"   // MyClass2加入keep-global-name
import {MyClass3 as MyClass} from "xxxx"    // MyClass3加入keep-global-name
MyClass1.add()    // add加入keep-property-name
har对外暴露的接口

参考hsp对外暴露的接口。

仅当hap->hsp->har，同时hap->har时，该har会被扫描，其中->表示依赖关系。

任务可视化与执行
构建报错排查
