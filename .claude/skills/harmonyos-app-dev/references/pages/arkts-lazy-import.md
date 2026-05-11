# 延迟加载（lazy import）

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-lazy-import_

-Summary----> Total file number: 13, total time: 2ms, including used file:12, cost time: 1ms, and unused file: 1, cost time: 1ms

上述信息表示应用当前线程在冷启动抓取时间段内加载了13个文件，共耗时2ms。其中，12个文件导出内容被其他文件加载使用，执行这12个文件共耗时1ms；1个文件执行完成，但是其导出内容没有被其他文件在冷启阶段用到，耗时1ms。

被使用文件

在冷启动阶段，导出内容被其他文件使用的文件称为used file。

场景1：通过静态加载所加载的文件，其父文件（parentModule）代表该文件的引入方。

used file 1: &entry/src/main/ets/pages/1&, cost time: 0.248ms
    parentModule 1: &entry/src/main/ets/pages/outer& a

对应写法示例：

// entry/src/main/ets/pages/outer.ets
import { a } from './1' // outer文件从1文件中加载了a变量
console.info("example ", a); // a变量在outer文件执行时就被使用


// entry/src/main/ets/pages/1.ets
export let a = "a";

场景2：通过静态加载所加载的文件，存在多个父文件。

// 说明：显示顺序不代表父文件的加载顺序。
used file 1: &entry/src/main/ets/pages/1&, cost time: 0.248ms
   parentModule 1: &entry/src/main/ets/pages/outer& a
   parentModule 2: &entry/src/main/ets/pages/innerinner& a

对应写法示例：

// entry/src/main/ets/pages/outer.ets
import { a } from './1' // outer文件从1文件中加载了a变量
console.info("example ", a); // a变量在outer文件执行时就被使用


// entry/src/main/ets/pages/innerinner.ets
import { a } from './1' // innerinner文件从1文件中加载了a变量
console.info("example ", a); // a变量在innerinner文件执行时就被使用


// entry/src/main/ets/pages/1.ets
export let a = "a";

场景3：通过静态加载所加载的文件，存在多个导出，但是只显示了一部分。

used file 1: &entry/src/main/ets/pages/1&, cost time: 0.248ms
   parentModule 1: &entry/src/main/ets/pages/outer& a

对应写法示例：

// entry/src/main/ets/pages/outer.ets
import { a , b } from './1' // 加载1文件的多个变量
console.info("example ", a); // a被使用
export function myFunc() {
 return b; // b未被使用
}


// entry/src/main/ets/pages/1.ets
export let a = 10;
export let b = 100;

场景4：动态加载或使用napi接口加载时，暂未支持父文件打印，因此不会显示父文件。

unused file 1: &entry/src/main/ets/pages/1&, cost time: 0.07ms

对应写法示例：

// entry/src/main/ets/pages/outer.ets
import("./1").then((ns:ESObject) => {
    console.info('import file 1 success');
});


// entry/src/main/ets/pages/1.ets
export let a = "a";

场景5：通过loadContent、pushUrl等接口加载的文件，其父文件（parentModule）统一显示为EntryPoint。

used file 1: &entry/src/main/ets/pages/Index&, cost time: 0.545ms
parentModule 1: EntryPoint
未被使用文件

在冷启动阶段，导出内容没有被其他文件使用的文件称为未使用的文件，代表可以延迟加载。

场景与被使用文件场景一致，但未被使用文件没有变量被使用的信息。

场景：文件被这些父文件引用，但变量未被使用。可在引入未使用文件处（父文件）使用延迟加载方式加载该文件。

unused file 1: &entry/src/main/ets/pages/under1&, cost time: 0.001ms
    parentModule 1: &entry/src/main/ets/pages/1&

对应写法示例：

// entry/src/main/ets/pages/1.ets
import { a } from './under1' // 加载under1文件的变量
export function myFunc() {
    return a; // a未被使用
}


// entry/src/main/ets/pages/under1.ets
export let a = "a";

可使用延迟加载：

// entry/src/main/ets/pages/1.ets
import lazy { a } from './under1' // 不在此处触发under1文件的加载
export function myFunc() {
    return a; // 此时触发under1文件的加载
}
使用示例

使用场景

下述例子中A文件被引用，在应用启动到点击按钮的这段时间里，A文件并没有被实际执行，在冷启动阶段加载A文件的行为属于冗余。

// A.ets
export let A = "A";


// Index.ets
import { A } from "./A";


@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('点击执行A文件')
        .onClick(() => {
          // 点击后触发A文件的执行
          console.info("执行A文件", A);
        })
    }
    // ...
  }
}

通过抓取Trace图查看调用栈，可以发现应用在冷启动时加载了A文件。

使用工具分析

连接设备，在终端直接输入下方命令执行。

hdc shell param set persist.ark.properties 0x200105c

启动应用，启动结束后关闭应用。

下载文件到本地，其中${bundleName}为应用名。

hdc file recv data/app/el2/100/base/${bundleName}/files/${bundleName}_redundant_file.txt D:\

对上述示例代码获取到的文件进行分析。

修改方式

工具筛选出冗余文件后，开发者可在引入时添加lazy关键字，标记文件可延迟加载。

// A.ets
export let A = "A";


// Index.ets
import lazy { A } from "./A"; // 此处添加lazy关键字，标记该文件可延迟加载


@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('点击执行A文件')
        .onClick(() => {
          // 点击后触发A文件的执行
          console.info("执行A文件", A);
        })
    }
    // ...
  }
}

通过抓取Trace图查看调用栈可以发现，使用lazy-import标识后，应用在冷启动时不再加载A文件。

优化效果

优化效果	加载文件耗时（微秒μs）
优化前	412us
优化后	350us

根据上述优化前后案例Trace图对比分析，使用延迟加载后应用冷启动时不再加载A文件，在资源加载阶段减少因加载冗余文件产生的耗时约15%，提高了应用冷启动性能。（由于案例仅演示场景，优化数据仅做参考，在实际业务中随着引用文件的复杂度提高，引用文件数量增多，优化效果也会随之提升。）

动态加载
同步方式动态加载Native模块
