# @Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink_

-----this.per.name in Child is still: ${this.per.name}`); // 4
  };
}
ObjectLinkDataSourceUpdate.ets

@ObjectLink的数据源更新依赖其父组件，当父组件中数据源改变引起父组件刷新时，会重新设置子组件@ObjectLink的数据源。这个过程不是在父组件数据源变化后立刻发生的，而是在父组件实际刷新时才会进行。上述示例中，Parent包含Child，Parent传递箭头函数给Child，在点击时，日志打印顺序是1-2-3-4-5，打印到日志4时，点击事件流程结束，此时仅仅是将子组件Child标记为需要父组件更新的节点，因此日志4打印的this.per.name的值仍为Bob，等到父组件真正更新时，才会更新Child的数据源。

当@ObjectLink @Watch('onChange02') per: Person的@Watch函数执行时，说明@ObjectLink的数据源已被父组件更新，此时日志5打印的值为更新后的Jack。

日志的含义为：

日志1：对Parent @State @Watch('onChange01') info: Info = new Info(new Person('Bob', 10)) 赋值前。

日志2：对Parent @State @Watch('onChange01') info: Info = new Info(new Person('Bob', 10)) 赋值，执行其@Watch函数，同步执行。

日志3：对Parent @State @Watch('onChange01') info: Info = new Info(new Person('Bob', 10)) 赋值完成。

日志4：onClickType方法内clickEvent执行完，此时只是将子组件Child标记为需要父组件更新的节点，未将最新的值更新给Child @ObjectLink @Watch('onChange02') per: Person，所以日志4打印的this.per.name的值仍然是Bob。

日志5：下一次vsync信号触发Child更新，@ObjectLink @Watch('onChange02') per: Person被更新，触发其@Watch方法，此时@ObjectLink @Watch('onChange02') per: Person为新值Jack。

@Prop父子同步原理与@ObjectLink一致。

当clickEvent中更改this.info.person.name时，修改会立刻生效，此时日志4打印的值是Jack。

Child({
  per: this.info.person, clickEvent: () => {
    hilog.info(DOMAIN, TAG, `:::clickEvent before ${this.info.person.name}`); // 1
    this.info.person.name = 'Jack';
    hilog.info(DOMAIN, TAG, `:::clickEvent after ${this.info.person.name}`); // 3
  }
})
ClickEventJack.ets

此时Parent中Text组件不会刷新，因为this.info.person.name属于两层嵌套。

@Observed装饰的类，在构造函数中使用this赋值属性，不触发UI更新

@Observed类的构造函数中对成员变量进行赋值或者修改时，此修改不会经过代理，无法被观测到。

【反例】

@Observed
class DataDownloader {
  state: number;
  constructor() {
    this.state = 0;
    setInterval(() => {
      // 从构造函数修改成员变量，不触发UI更新
      this.state += 1;
    }, 2000);
  }
}


@Entry
@Component
struct Index {
  @State dataDownloader: DataDownloader = new DataDownloader();
  build() {
    Column() {
      Text(`Download state is ${this.dataDownloader.state}`)
    }
  }
}

【正例】

@Observed
class DataDownloader {
  public state: number;


  constructor() {
    this.state = 0;
  }


  startIntervalUpdate() {
    setInterval(() => {
      this.state += 1;
    }, 2000);
  }
}


@Entry
@Component
struct Index {
  @State dataDownloader: DataDownloader = new DataDownloader();


  aboutToAppear() {
    this.dataDownloader.startIntervalUpdate(); // @Observed装饰的类构建后再修改属性可以触发更新UI
  }


  build() {
    Column() {
      Text(`Download state is ${this.dataDownloader.state}`)
    }
  }
}
ChangePropertyInConstructor.ets

LazyForEach和@ObjectLink一起使用时，替换数组数据后UI不刷新

@Observed装饰的类的数组，用LazyForEach展开显示的时候，可能会出现替换数组数据后，修改数组数据不刷新UI的问题。改变数组数据后，需要调用onDataChange通知LazyForEach组件重新绑定状态变量，否则就会出现上述问题。

【反例】

// LazyForEach遍历数据基类
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: StringData[] = [];


  public totalCount(): number {
    return this.originDataArray.length;
  }


  public getData(index: number): StringData {
    return this.originDataArray[index];
  }


  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }


  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }


  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }
}


// LazyForEach遍历数据类型
class MyDataSource extends BasicDataSource {
  public dataArray: StringData[] = [];


  public totalCount(): number {
    return this.dataArray.length;
  }


  public getData(index: number): StringData {
    return this.dataArray[index];
  }


  public pushData(data: StringData): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}


@Observed
class StringData {
  message: string;


  constructor(message: string) {
    this.message = message;
  }
}


@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();
  helloCount: number = 4;


  aboutToAppear() {
    for (let i = 0; i <= 3; i++) {
      this.data.pushData(new StringData(`Hello ${i}`));
    }
  }


  build() {
    Column() {
      List({ space: 3 }) {
        // 使用LazyForEach懒加载遍历数据
        LazyForEach(this.data, (item: StringData, index: number) => {
          ListItem() {
            ChildComponent({ data: item })
          }
        }, (item: StringData, index: number) => index.toString() + item.message)
      }.cachedCount(3)
      Button('替换第一个元素')
        .onClick(() => {
          // 替换数组元素不刷新UI，此时新替换的值还未绑定到LazyForEach组件上。
          this.data.dataArray[0] = new StringData('Hello ' + this.helloCount++)
        })
      Button('修改第一个元素的数据')
        .onClick(() => {
          // 替换数组元素后修改元素值也不会刷新UI。
          this.data.dataArray[0].message += '1';
        })
    }
  }
}


// 使用@Reusable实现组件复用
@Reusable
@Component
struct ChildComponent {
  // 使用@ObjectLink接收@Observed装饰的类的数据
  @ObjectLink data: StringData;


  aboutToAppear(): void {
    console.info(`aboutToAppear: ${this.data.message}`);
  }


  aboutToRecycle(): void {
    console.info(`aboutToRecycle: ${this.data.message}`);
  }


  // 对复用的组件进行数据更新
  aboutToReuse(params: Record<string, ESObject>): void {
    this.data.message = (params.data as StringData).message;
    console.info(`aboutToReuse: ${this.data.message}`);
  }


  build() {
    Row() {
      Text(this.data.message)
        .fontSize(50)
        .onAppear(() => {
          console.info(`appear: ${this.data.message}`);
        })
    }.margin({ left: 10, right: 10 })
  }
}

【正例】

// LazyForEach遍历数据基类
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: StringData[] = [];


  public totalCount(): number {
    return this.originDataArray.length;
  }


  public getData(index: number): StringData {
    return this.originDataArray[index];
  }


  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }


  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }


  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }


  // 通知LazyForEach处理数据替换
  notifyDataChanged(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }
}


// LazyForEach遍历数据类型
class MyDataSource extends BasicDataSource {
  public dataArray: StringData[] = [];


  public totalCount(): number {
    return this.dataArray.length;
  }


  public getData(index: number): StringData {
    return this.dataArray[index];
  }


  public pushData(data: StringData): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}


@Observed
class StringData {
  public message: string;


  constructor(message: string) {
    this.message = message;
  }
}


@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();
  helloCount: number = 4;


  aboutToAppear() {
    for (let i = 0; i <= 2; i++) {
      this.data.pushData(new StringData(`Hello ${i}`));
    }
  }


  build() {
    Column({ space: 3 }) {
      List({ space: 3 }) {
        // 使用LazyForEach懒加载遍历数据
        LazyForEach(this.data, (item: StringData, index: number) => {
          ListItem() {
            ChildComponent({ data: item })
          }.width('100%')
          // LazyForEach的key从index和message构建，每次替换元素时，需要修改key才能触发UI刷新。
        }, (item: StringData, index: number) => index.toString() + item.message)
      }.cachedCount(3)
      Button('替换第一个元素')
        .onClick(() => {
          this.data.dataArray[0] = new StringData('Hello ' + this.helloCount++);
          // 替换元素后通知LazyForEach，可以刷新UI。
          this.data.notifyDataChanged(0);
        })
      Button('修改第一个元素的数据')
        .onClick(() => {
          // 替换元素后由于重新建立绑定，后续修改元素值也能刷新UI。
          this.data.dataArray[0].message += '1';
        })
    }
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }
}


// 使用Reusable使能组件复用
@Reusable
@Component
struct ChildComponent {
  // 使用@ObjectLink接受@Observed类数据
  @ObjectLink data: StringData;


  aboutToAppear(): void {
    console.info(`aboutToAppear: ${this.data.message}`);
  }


  aboutToRecycle(): void {
    console.info(`aboutToRecycle: ${this.data.message}`);
  }


  // 对复用的组件进行数据更新
  aboutToReuse(params: Record<string, ESObject>): void {
    this.data.message = (params.data as StringData).message;
    console.info(`aboutToReuse: ${this.data.message}`);
  }


  build() {
    Row() {
      Text(this.data.message)
        .fontSize(50)
        .onAppear(() => {
          console.info(`appear: ${this.data.message}`);
        })
    }.margin({ left: 10, right: 10 })
  }
}
UseWithLazyForEach.ets

@Provide装饰器和@Consume装饰器：与后代组件双向同步
@Watch装饰器：状态变量更改通知

## Code blocks

### Code block 1

```
// 允许@ObjectLink装饰的数据属性赋值
this.objLink.a= ...
// 不允许@ObjectLink装饰的数据自身赋值
this.objLink= ...
```

### Code block 2

```
@Observed
class DateClass extends Date {
  constructor(args: number | string) {
    super(args);
  }
}


@Observed
class NewDate {
  public data: DateClass;


  constructor(data: DateClass) {
    this.data = data;
  }
}


@Component
struct Child {
  label: string = 'date';
  @ObjectLink data: DateClass;


  build() {
    Column() {
      // data被@Observed和@ObjectLink装饰，可以被观察到Date整体的赋值以及调用Date接口带来的变化
      Button('child increase the day by 1')
        .onClick(() => {
          this.data.setDate(this.data.getDate() + 1);
        })
      DatePicker({
        start: new Date('1970-1-1'),
        end: new Date('2100-1-1'),
        selected: this.data
      })
    }
  }
}


@Entry
@Component
struct Parent {
  @State newData: NewDate = new NewDate(new DateClass('2023-1-1'));


  build() {
    Column() {
      Child({ label: 'date', data: this.newData.data })


      Button('parent update the new date')
        .onClick(() => {
          this.newData.data = new DateClass('2023-07-07');
        })
      Button(`ViewB: this.newData = new NewDate(new DateClass('2023-08-20'))`)
        .onClick(() => {
          this.newData = new NewDate(new DateClass('2023-08-20'));
        })
    }
  }
}
```

### Code block 3

```
class Test {
  msg: number;


  constructor(msg: number) {
    this.msg = msg;
  }
}
// 错误写法，count未指定类型，编译报错
@ObjectLink count;
// 错误写法，Test未被@Observed装饰，编译报错
@ObjectLink test: Test;
```

### Code block 4

```
@Observed
class Info {
  public count: number;


  constructor(count: number) {
    this.count = count;
  }
}
// ...
// 正确写法
@ObjectLink count: Info;
```

### Code block 5

```
// 错误写法，编译报错
@ObjectLink count: CountInfo = new CountInfo(10);
```

### Code block 6

```
@Observed
class CountInfo {
  public count: number;


  constructor(count: number) {
    this.count = count;
  }
}
// ...
// 正确写法
@ObjectLink count: CountInfo;
```

### Code block 7

```
@Observed
class Info {
  count: number;


  constructor(count: number) {
    this.count = count;
  }
}


@Component
struct Child {
  @ObjectLink num: Info;


  build() {
    Column() {
      Text(`num的值: ${this.num.count}`)
        .onClick(() => {
          // 错误写法，@ObjectLink装饰的变量不能被赋值，运行时报错
          this.num = new Info(10);
        })
    }
  }
}


@Entry
@Component
struct Parent {
  @State num: Info = new Info(10);


  build() {
    Column() {
      Text(`count的值: ${this.num.count}`)
      Child({num: this.num})
    }
  }
}
```

### Code block 8

```
@Observed
class Info {
  public count: number;


  constructor(count: number) {
    this.count = count;
  }
}


@Component
struct Child {
  @ObjectLink num: Info;


  build() {
    Column() {
      Text(`num value: ${this.num.count}`)
        .onClick(() => {
          // 正确写法，可以更改@ObjectLink装饰变量的成员属性
          this.num.count = 20;
        })
    }
  }
}


@Entry
@Component
struct Parent {
  @State num: Info = new Info(10);


  build() {
    Column() {
      Text(`count value: ${this.num.count}`)
      Button('click')
        .onClick(() => {
          // 可以在父组件做整体替换
          this.num = new Info(30);
        })
      Child({ num: this.num })
    }
  }
}
```

### Code block 9

```
class Book {
  public name: string;


  constructor(name: string) {
    this.name = name;
  }
}


@Component
struct BookCard {
  @ObjectLink book: Book;


  build() {
    Column() {
      Text(`BookCard: ${this.book.name}`) // 可以观察到name的变化
        .width(320)
        .margin(10)
        .textAlign(TextAlign.Center)


      Button('change book.name')
        .width(320)
        .margin(10)
        .onClick(() => {
          this.book.name = 'C++';
        })
    }
  }
}


@Entry
@Component
struct Index {
  @State book: Book = new Book('JS');


  build() {
    Column() {
      BookCard({ book: this.book })
    }
  }
}
```

### Code block 10

```
@Observed
class Book {
  public name: string;


  constructor(name: string) {
    this.name = name;
  }
}


@Observed
class Bag {
  public book: Book;


  constructor(book: Book) {
    this.book = book;
  }
}


@Component
struct BookCard {
  @ObjectLink book: Book;


  build() {
    Column() {
      Text(`BookCard: ${this.book.name}`) // 可以观察到name的变化
        .width(320)
        .margin(10)
        .textAlign(TextAlign.Center)


      Button('change book.name')
        .width(320)
        .margin(10)
        .onClick(() => {
          this.book.name = 'C++';
        })
    }
  }
}


@Entry
@Component
struct Index {
  @State bag: Bag = new Bag(new Book('JS'));


  build() {
    Column() {
      Text(`Index: ${this.bag.book.name}`) // 无法观察到name的变化
        .width(320)
        .margin(10)
        .textAlign(TextAlign.Center)


      Button('change bag.book.name')
        .width(320)
        .margin(10)
        .onClick(() => {
          this.bag.book.name = 'TS';
        })


      BookCard({ book: this.bag.book })
    }
  }
}
```

### Code block 11

```
import { hilog } from '@kit.PerformanceAnalysisKit';


const DOMAIN = 0x0001;
const TAG = 'ArkTSObservedAndObjectlink';
let nextID: number = 1;


@Observed
class Info {
  public id: number;
  public info: number;


  constructor(info: number) {
    this.id = nextID++;
    this.info = info;
  }
}


@Component
struct Child {
  // 子组件Child的@ObjectLink的类型是Info
  @ObjectLink info: Info;
  label: string = 'ViewChild';


  build() {
    Row() {
      Button(`ViewChild [${this.label}] this.info.info = ${this.info ? this.info.info : 'undefined'}`)
        .width(320)
        .margin(10)
        .onClick(() => {
          this.info.info += 1;
        })
    }
  }
}


@Entry
@Component
struct Parent {
  // Parent中有@State装饰的Info[]
  @State arrA: Info[] = [new Info(0), new Info(0)];


  build() {
    Column() {
      ForEach(this.arrA,
        (item: Info) => {
          Child({ label: `#${item.id}`, info: item })
        },
        (item: Info): string => item.id.toString()
      )
      // 使用@State装饰的数组的数组项初始化@ObjectLink，其中数组项是被@Observed装饰的Info的实例
      Child({ label: 'ViewChild this.arrA[first]', info: this.arrA[0] })
      Child({ label: 'ViewChild this.arrA[last]', info: this.arrA[this.arrA.length-1] })


      Button('ViewParent: reset array')
        .width(320)
        .margin(10)
        .onClick(() => {
          this.arrA = [new Info(0), new Info(0)];
        })
      Button('ViewParent: push')
        .width(320)
        .margin(10)
        .onClick(() => {
          this.arrA.push(new Info(0));
        })
      Button('ViewParent: shift')
        .width(320)
        .margin(10)
        .onClick(() => {
          if (this.arrA.length > 0) {
            this.arrA.shift();
          } else {
            hilog.info(DOMAIN, TAG, 'length <= 0');
          }
        })
      Button('ViewParent: item property in middle')
        .width(320)
        .margin(10)
        .onClick(() => {
          this.arrA[Math.floor(this.arrA.length / 2)].info = 10;
        })
      Button('ViewParent: item property in middle')
        .width(320)
        .margin(10)
        .onClick(() => {
          this.arrA[Math.floor(this.arrA.length / 2)] = new Info(11);
        })
    }
  }
}
```

### Code block 12

```
@Observed
class ObservedArray<T> extends Array<T> {
}
```

### Code block 13

```
@Observed
class ObservedArray<T> extends Array<T> {
}


@Component
struct Item {
  @ObjectLink itemArr: ObservedArray<string>;


  build() {
    Row() {
      ForEach(this.itemArr, (item: string, index: number) => {
        Text(`${index}: ${item}`)
          .width(100)
          .height(100)
      }, (item: string) => item)
    }
  }
}


@Entry
@Component
struct IndexPage {
  // new操作符创建的ObservedArray<string>的实例可以观察到属性变化
  @State arr: Array<ObservedArray<string>> = [
    new ObservedArray<string>('apple'),
    new ObservedArray<string>('banana'),
    new ObservedArray<string>('orange')
  ];


  build() {
    Column() {
      ForEach(this.arr, (itemArr: ObservedArray<string>) => {
        Item({ itemArr: itemArr })
      })


      Divider()


      Button('push two-dimensional array item')
        .margin(10)
        .onClick(() => {
          this.arr[0].push('strawberry');
        })


      Button('push array item')
        .margin(10)
        .onClick(() => {
          this.arr.push(new ObservedArray<string>('pear'));
        })


      Button('change two-dimensional array first item')
        .margin(10)
        .onClick(() => {
          this.arr[0][0] = 'APPLE';
        })


      Button('change array first item')
        .margin(10)
        .onClick(() => {
          this.arr[0] = new ObservedArray<string>('watermelon');
        })
    }
  }
}
```

### Code block 14

```
import { UIUtils } from '@kit.ArkUI';


@Component
struct Item {
  @ObjectLink itemArr: Array<string>;


  build() {
    Row() {
      ForEach(this.itemArr, (item: string, index: number) => {
        Text(`${index}: ${item}`)
          .width(100)
          .height(100)
      }, (item: string) => item)
    }
  }
}


@Entry
@Component
struct IndexPage {
  // 利用makeV1Observed观察二维数组的变化
  @State arr: Array<Array<string>> =
    [UIUtils.makeV1Observed(['apple']), UIUtils.makeV1Observed(['banana']), UIUtils.makeV1Observed(['orange'])];


  build() {
    Column() {
      ForEach(this.arr, (itemArr: Array<string>) => {
        Item({ itemArr: itemArr })
      })


      Divider()


      Button('push two-dimensional array item')
        .margin(10)
        .onClick(() => {
          this.arr[0].push('strawberry');
        })


      Button('push array item')
        .margin(10)
        .onClick(() => {
          this.arr.push(UIUtils.makeV1Observed(['pear']));
        })


      Button('change two-dimensional array first item')
        .margin(10)
        .onClick(() => {
          this.arr[0][0] = 'APPLE';
        })


      Button('change array first item')
        .margin(10)
        .onClick(() => {
          this.arr[0] = UIUtils.makeV1Observed(['watermelon']);
        })
    }
  }
}
```

### Code block 15

```
@Observed
class Info {
  public info: MyMap<number, string>;


  constructor(info: MyMap<number, string>) {
    this.info = info;
  }
}


@Observed
export class MyMap<K, V> extends Map<K, V> {
  public name: string;


  constructor(name?: string, args?: [K, V][]) {
    super(args);
    this.name = name ? name : 'My Map';
  }


  getName() {
    return this.name;
  }
}


@Entry
@Component
struct MapSampleNested {
  @State message: Info = new Info(new MyMap('myMap', [[0, 'a'], [1, 'b'], [3, 'c']]));


  build() {
    Row() {
      Column() {
        MapSampleNestedChild({ myMap: this.message.info })
      }
      .width('100%')
    }
    .height('100%')
  }
}


@Component
struct MapSampleNestedChild {
  @ObjectLink myMap: MyMap<number, string>;


  build() {
    Row() {
      Column() {
        ForEach(Array.from(this.myMap.entries()), (item: [number, string]) => {
          Text(`${item[0]}`).fontSize(30)
          Text(`${item[1]}`).fontSize(30)
          Divider().strokeWidth(5)
        })


        // myMap被@Observed和@ObjectLink装饰，可以被观察到Map整体的赋值以及调用Map接口带来的变化
        Button('set new one')
          .width(200)
          .margin(10)
          .onClick(() => {
            this.myMap.set(4, 'd');
          })
        Button('clear')
          .width(200)
          .margin(10)
          .onClick(() => {
            this.myMap.clear();
          })
        Button('replace the first one')
          .width(200)
          .margin(10)
          .onClick(() => {
            this.myMap.set(0, 'aa');
          })
        Button('delete the first one')
          .width(200)
          .margin(10)
          .onClick(() => {
            this.myMap.delete(0);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### Code block 16

```
@Observed
class Info {
  public info: MySet<number>;


  constructor(info: MySet<number>) {
    this.info = info;
  }
}


@Observed
export class MySet<T> extends Set<T> {
  public name: string;


  constructor(name?: string, args?: T[]) {
    super(args);
    this.name = name ? name : 'My Set';
  }


  getName() {
    return this.name;
  }
}


@Entry
@Component
struct SetSampleNested {
  @State message: Info = new Info(new MySet('Set', [0, 1, 2, 3, 4]));


  build() {
    Row() {
      Column() {
        SetSampleNestedChild({ mySet: this.message.info })
      }
      .width('100%')
    }
    .height('100%')
  }
}


@Component
struct SetSampleNestedChild {
  @ObjectLink mySet: MySet<number>;


  build() {
    Row() {
      Column() {
        ForEach(Array.from(this.mySet.entries()), (item: [number, number]) => {
          Text(`${item}`).fontSize(30)
          Divider()
        })
        // mySet被@Observed和@ObjectLink装饰，可以被观察到Set整体的赋值以及调用Set接口带来的变化
        Button('set new one')
          .width(200)
          .margin(10)
          .onClick(() => {
            this.mySet.add(5);
          })
        Button('clear')
          .width(200)
          .margin(10)
          .onClick(() => {
            this.mySet.clear();
          })
        Button('delete the first one')
          .width(200)
          .margin(10)
          .onClick(() => {
            this.mySet.delete(0);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### Code block 17

```
import { hilog } from '@kit.PerformanceAnalysisKit';


const DOMAIN = 0x0001;
const TAG = 'ArkTSObservedAndObjectlink';


@Observed
class Source {
  public source: number;


  constructor(source: number) {
    this.source = source;
  }
}


@Observed
class Data {
  public data: number;


  constructor(data: number) {
    this.data = data;
  }
}


@Entry
@Component
struct Parent {
  @State count: Source | Data | undefined = new Source(10);


  build() {
    Column() {
      Child({ count: this.count })


      Button('change count property')
        .margin(10)
        .onClick(() => {
          // 判断count的类型，做属性的更新
          if (this.count instanceof Source) {
            this.count.source += 1;
          } else if (this.count instanceof Data) {
            this.count.data += 1;
          } else {
            hilog.info(DOMAIN, TAG, `count is undefined, cannot change property`);
          }
        })


      Button('change count to Source')
        .margin(10)
        .onClick(() => {
          // 赋值为Source的实例
          this.count = new Source(100);
        })


      Button('change count to Data')
        .margin(10)
        .onClick(() => {
          // 赋值为Data的实例
          this.count = new Data(100);
        })


      Button('change count to undefined')
        .margin(10)
        .onClick(() => {
          // 赋值为undefined
          this.count = undefined;
        })
    }.width('100%')
  }
}


@Component
struct Child {
  @ObjectLink count: Source | Data | undefined;


  build() {
    Column() {
      Text(`count is instanceof ${this.count instanceof Source ? 'Source' :
        this.count instanceof Data ? 'Data' : 'undefined'}`)
        .fontSize(30)
        .margin(10)


      Text(`count's property is  ${this.count instanceof Source ? this.count.source : this.count?.data}`).fontSize(15)


    }.width('100%')
  }
}
```

### Code block 18

```
class Parent {
  parentId: number;


  constructor(parentId: number) {
    this.parentId = parentId;
  }


  getParentId(): number {
    return this.parentId;
  }


  setParentId(parentId: number): void {
    this.parentId = parentId;
  }
}


class Child {
  childId: number;


  constructor(childId: number) {
    this.childId = childId;
  }


  getChildId(): number {
    return this.childId;
  }


  setChildId(childId: number): void {
    this.childId = childId;
  }
}


class Cousin extends Parent {
  cousinId: number = 47;
  child: Child;


  constructor(parentId: number, cousinId: number, childId: number) {
    super(parentId);
    this.cousinId = cousinId;
    this.child = new Child(childId);
  }


  getCousinId(): number {
    return this.cousinId;
  }


  setCousinId(cousinId: number): void {
    this.cousinId = cousinId;
  }


  getChild(): number {
    return this.child.getChildId();
  }


  setChild(childId: number): void {
    this.child.setChildId(childId);
  }
}


@Entry
@Component
struct MyView {
  @State cousin: Cousin = new Cousin(10, 20, 30);


  build() {
    Column({ space: 10 }) {
      Text(`parentId: ${this.cousin.parentId}`)
      Button('Change Parent.parent')
        .onClick(() => {
          this.cousin.parentId += 1;
        })


      Text(`cousinId: ${this.cousin.cousinId}`)
      Button('Change Cousin.cousinId')
        .onClick(() => {
          this.cousin.cousinId += 1;
        })


      Text(`childId: ${this.cousin.child.childId}`)
      Button('Change Cousin.Child.childId')
        .onClick(() => {
          // 点击时上面的Text组件不会刷新
          this.cousin.child.childId += 1;
        })
    }
  }
}
```

### Code block 19

```
class Parent {
  public parentId: number;


  constructor(parentId: number) {
    this.parentId = parentId;
  }


  getParentId(): number {
    return this.parentId;
  }


  setParentId(parentId: number): void {
    this.parentId = parentId;
  }
}


@Observed
class Child {
  public childId: number;


  constructor(childId: number) {
    this.childId = childId;
  }


  getChildId(): number {
    return this.childId;
  }


  setChildId(childId: number): void {
    this.childId = childId;
  }
}


class Cousin extends Parent {
  public cousinId: number = 47;
  public child: Child;


  constructor(parentId: number, cousinId: number, childId: number) {
    super(parentId);
    this.cousinId = cousinId;
    this.child = new Child(childId);
  }


  getCousinId(): number {
    return this.cousinId;
  }


  setCousinId(cousinId: number): void {
    this.cousinId = cousinId;
  }


  getChild(): number {
    return this.child.getChildId();
  }


  setChild(childId: number): void {
    this.child.setChildId(childId);
  }
}


@Component
struct ViewChild {
  @ObjectLink child: Child;


  build() {
    Column({ space: 10 }) {
      Text(`childId: ${this.child.getChildId()}`)
      Button('Change childId')
        .onClick(() => {
          this.child.setChildId(this.child.getChildId() + 1);
        })
    }
  }
}


@Entry
@Component
struct MyView {
  @State cousin: Cousin = new Cousin(10, 20, 30);


  build() {
    Column({ space: 10 }) {
      Text(`parentId: ${this.cousin.parentId}`)
      Button('Change Parent.parentId')
        .onClick(() => {
          this.cousin.parentId += 1;
        })


      Text(`cousinId: ${this.cousin.cousinId}`)
      Button('Change Cousin.cousinId')
        .onClick(() => {
          this.cousin.cousinId += 1;
        })


      ViewChild({ child: this.cousin.child }) // Text(`childId: ${this.cousin.child.childId}`)的替代写法
      Button('Change Cousin.Child.childId')
        .onClick(() => {
          this.cousin.child.childId += 1;
        })
    }
  }
}
```

### Code block 20

```
let nextId = 1;
@Observed
class SubCounter {
  counter: number;
  constructor(c: number) {
    this.counter = c;
  }
}
@Observed
class ParentCounter {
  id: number;
  counter: number;
  subCounter: SubCounter;
  incrCounter() {
    this.counter++;
  }
  incrSubCounter(c: number) {
    this.subCounter.counter += c;
  }
  setSubCounter(c: number): void {
    this.subCounter.counter = c;
  }
  constructor(c: number) {
    this.id = nextId++;
    this.counter = c;
    this.subCounter = new SubCounter(c);
  }
}
@Component
struct CounterComp {
  @ObjectLink value: ParentCounter;
  build() {
    Column({ space: 10 }) {
      Text(`${this.value.counter}`)
        .fontSize(25)
        .onClick(() => {
          this.value.incrCounter();
        })
      Text(`${this.value.subCounter.counter}`)
        .onClick(() => {
          this.value.incrSubCounter(1);
        })
      Divider().height(2)
    }
  }
}
@Entry
@Component
struct ParentComp {
  @State counter: ParentCounter[] = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];
  build() {
    Row() {
      Column() {
        CounterComp({ value: this.counter[0] })
        CounterComp({ value: this.counter[1] })
        CounterComp({ value: this.counter[2] })
        Divider().height(5)
        ForEach(this.counter,
          (item: ParentCounter) => {
            CounterComp({ value: item })
          },
          (item: ParentCounter) => item.id.toString()
        )
        Divider().height(5)
        // 第一个点击事件
        Text('Parent: incr counter[0].counter')
          .fontSize(20).height(50)
          .onClick(() => {
            this.counter[0].incrCounter();
            // 每次触发时自增10
            this.counter[0].incrSubCounter(10);
          })
        // 第二个点击事件
        Text('Parent: set.counter to 10')
          .fontSize(20).height(50)
          .onClick(() => {
            // 无法将value设置为10，UI不会刷新
            this.counter[0].setSubCounter(10);
          })
        Text('Parent: reset entire counter')
          .fontSize(20).height(50)
          .onClick(() => {
            this.counter = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];
          })
      }
    }
  }
}
```

### Code block 21

```
let nextId = 1;


@Observed
class SubCounter {
  public counter: number;


  constructor(c: number) {
    this.counter = c;
  }
}


@Observed
class ParentCounter {
  public id: number;
  public counter: number;
  public subCounter: SubCounter;


  incrCounter() {
    this.counter++;
  }


  incrSubCounter(c: number) {
    this.subCounter.counter += c;
  }


  setSubCounter(c: number): void {
    this.subCounter.counter = c;
  }


  constructor(c: number) {
    this.id = nextId++;
    this.counter = c;
    this.subCounter = new SubCounter(c);
  }
}




@Entry
@Component
struct ParentComp {
  @State counter: ParentCounter[] = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];
  build() {
    Row() {
        CounterComp({ value: this.counter[0] }) // ParentComp组件传递 ParentCounter 给 CounterComp 组件
    }
  }
}


@Component
struct CounterComp {
  @ObjectLink value: ParentCounter; // @ObjectLink 接收 ParentCounter
  build() {
      // CounterChild 是 CounterComp 的子组件，CounterComp 传递 this.value.subCounter 给 CounterChild 组件
      CounterChild({ subValue: this.value.subCounter })
  }
}


@Component
struct CounterChild {
  @ObjectLink subValue: SubCounter; // @ObjectLink 接收 SubCounter
  build() {
    Text(`${this.subValue.counter}`)
      .onClick(() => {
        this.subValue.counter += 1;
      })
  }
}
```

### Code block 22

```
let nextId = 1;


@Observed
class SubCounter {
  public counter: number;


  constructor(c: number) {
    this.counter = c;
  }
}


@Observed
class ParentCounter {
  public id: number;
  public counter: number;
  public subCounter: SubCounter;


  incrCounter() {
    this.counter++;
  }


  incrSubCounter(c: number) {
    this.subCounter.counter += c;
  }


  setSubCounter(c: number): void {
    this.subCounter.counter = c;
  }


  constructor(c: number) {
    this.id = nextId++;
    this.counter = c;
    this.subCounter = new SubCounter(c);
  }
}


@Component
struct CounterComp {
  @ObjectLink value: ParentCounter;


  build() {
    Column({ space: 10 }) {
      Text(`${this.value.counter}`)
        .fontSize(25)
        .onClick(() => {
          this.value.incrCounter();
        })
      CounterChild({ subValue: this.value.subCounter })
      Divider().height(2)
    }
  }
}


@Component
struct CounterChild {
  @ObjectLink subValue: SubCounter;


  build() {
    Text(`${this.subValue.counter}`)
      .onClick(() => {
        this.subValue.counter += 1;
      })
  }
}


@Entry
@Component
struct ParentComp {
  // @ObjectLink分别代理了ParentCounter和SubCounter的属性，这两个类的属性的变化都可以观察到
  @State counter: ParentCounter[] = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];


  build() {
    Row() {
      Column() {
        CounterComp({ value: this.counter[0] })
        CounterComp({ value: this.counter[1] })
        CounterComp({ value: this.counter[2] })
        Divider().height(5)
        ForEach(this.counter,
          (item: ParentCounter) => {
            CounterComp({ value: item })
          },
          (item: ParentCounter) => item.id.toString()
        )
        Divider().height(5)
        Text('Parent: reset entire counter')
          .fontSize(20).height(50)
          .onClick(() => {
            this.counter = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];
          })
        Text('Parent: incr counter[0].counter')
          .fontSize(20).height(50)
          .onClick(() => {
            this.counter[0].incrCounter();
            this.counter[0].incrSubCounter(10);
          })
        Text('Parent: set.counter to 10')
          .fontSize(20).height(50)
          .onClick(() => {
            this.counter[0].setSubCounter(10);
          })
      }
    }
  }
}
```

### Code block 23

```
let nextId = 0;


@Observed
class User {
  public id: number;


  constructor() {
    this.id = nextId++;
  }
}


@Entry
@Component
struct Index {
  @State users: User[] = [new User(), new User(), new User()];


  build() {
    Column() {
      UserChild({ firstUserByObjectLink: this.users[0], firstUserByProp: this.users[0] })
    }
  }
}


@Component
struct UserChild {
  @ObjectLink firstUserByObjectLink: User;
  @Prop firstUserByProp: User;


  build() {
    Column() {
      // 比较结果为false说明@Prop经过深拷贝后得到的对象与原对象已不是同一个对象
      Text(`firstUserByObjectLink equals firstUserByProp? : ${this.firstUserByObjectLink === this.firstUserByProp}`)
      Text(`UserChild firstUserByObjectLink.id: ${this.firstUserByObjectLink.id}`) // Text1
      Text(`UserChild firstUserByProp.id: ${this.firstUserByProp.id}`) // Text2
      Button('change @ObjectLink value')
        .onClick(() => {
          this.firstUserByObjectLink.id++;
        })
      Button('change @Prop value')
        .onClick(() => {
          this.firstUserByProp.id++;
        })
    }
  }
}
```

### Code block 24

```
@Observed
class RenderClass {
  waitToRender: boolean = false;


  constructor() {
    setTimeout(() => {
      this.waitToRender = true;
      console.info('更改waitToRender的值为：' + this.waitToRender);
    }, 1000)
  }
}


@Entry
@Component
struct Index {
  @State @Watch('renderClassChange') renderClass: RenderClass = new RenderClass();
  @State textColor: Color = Color.Black;


  renderClassChange() {
    console.info('renderClass的值被更改为：' + this.renderClass.waitToRender);
  }


  build() {
    Row() {
      Column() {
        Text('renderClass的值为：' + this.renderClass.waitToRender)
          .fontSize(20)
          .fontColor(this.textColor)
        Button('Show')
          .onClick(() => {
            // 使用其他状态变量强行刷新UI的做法并不推荐，此处仅用来检测waitToRender的值是否更新
            this.textColor = Color.Red;
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### Code block 25

```
import { hilog } from '@kit.PerformanceAnalysisKit';


const DOMAIN = 0x0001;
const TAG = 'ArkTSObservedAndObjectlink';


@Observed
class RenderClass {
  public waitToRender: boolean = false;


  constructor() {
  }
}


@Entry
@Component
struct DelayedChangeIndex {
  @State @Watch('renderClassChange') renderClass: RenderClass = new RenderClass();


  renderClassChange() {
    hilog.info(DOMAIN, TAG, `The value of renderClass is changed to: ${this.renderClass.waitToRender}`);
  }


  onPageShow() {
    setTimeout(() => {
      this.renderClass.waitToRender = true;
    }, 1000);
  }


  build() {
    Row() {
      Column() {
        Text(`The value of renderClass is: ${this.renderClass.waitToRender}`)
          .fontSize(20)
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

### Code block 26

```
import { hilog } from '@kit.PerformanceAnalysisKit';


const DOMAIN = 0x0001;
const TAG = 'ArkTSObservedAndObjectlink';


@Observed
class Person {
  public name: string = '';
  public age: number = 0;


  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }
}


@Observed
class Info {
  public person: Person;


  constructor(person: Person) {
    this.person = person;
  }
}


@Entry
@Component
struct Parent {
  @State @Watch('onChange01') info: Info =
    new Info(
      new Person('Bob', 10)
    );


  onChange01() {
    hilog.info(DOMAIN, TAG, `:::onChange01: + ${this.info.person.name}`); // 2
  }


  build() {
    Column() {
      Text(this.info.person.name).height(40)
      Child({
        per: this.info.person, clickEvent: () => {
          hilog.info(DOMAIN, TAG, `:::clickEvent before ${this.info.person.name}`); // 1
          this.info.person = new Person('Jack', 12);
          hilog.info(DOMAIN, TAG, `:::clickEvent after ${this.info.person.name}`); // 3
        }
      })
    }
  }
}


@Component
struct Child {
  @ObjectLink @Watch('onChange02') per: Person;
  clickEvent?: () => void;


  onChange02() {
    hilog.info(DOMAIN, TAG, `:::onChange02:${this.per.name}`); // 5
  }


  build() {
    Column() {
      Button(this.per.name)
        .height(40)
        .onClick(() => {
          this.onClickType();
        })
    }
  }


  private onClickType() {
    if (this.clickEvent) {
      this.clickEvent();
    }
    hilog.info(DOMAIN, TAG, `:::--------this.per.name in Child is still: ${this.per.name}`); // 4
  };
}
```

### Code block 27

```
Child({
  per: this.info.person, clickEvent: () => {
    hilog.info(DOMAIN, TAG, `:::clickEvent before ${this.info.person.name}`); // 1
    this.info.person.name = 'Jack';
    hilog.info(DOMAIN, TAG, `:::clickEvent after ${this.info.person.name}`); // 3
  }
})
```

### Code block 28

```
@Observed
class DataDownloader {
  state: number;
  constructor() {
    this.state = 0;
    setInterval(() => {
      // 从构造函数修改成员变量，不触发UI更新
      this.state += 1;
    }, 2000);
  }
}


@Entry
@Component
struct Index {
  @State dataDownloader: DataDownloader = new DataDownloader();
  build() {
    Column() {
      Text(`Download state is ${this.dataDownloader.state}`)
    }
  }
}
```

### Code block 29

```
@Observed
class DataDownloader {
  public state: number;


  constructor() {
    this.state = 0;
  }


  startIntervalUpdate() {
    setInterval(() => {
      this.state += 1;
    }, 2000);
  }
}


@Entry
@Component
struct Index {
  @State dataDownloader: DataDownloader = new DataDownloader();


  aboutToAppear() {
    this.dataDownloader.startIntervalUpdate(); // @Observed装饰的类构建后再修改属性可以触发更新UI
  }


  build() {
    Column() {
      Text(`Download state is ${this.dataDownloader.state}`)
    }
  }
}
```

### Code block 30

```
// LazyForEach遍历数据基类
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: StringData[] = [];


  public totalCount(): number {
    return this.originDataArray.length;
  }


  public getData(index: number): StringData {
    return this.originDataArray[index];
  }


  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }


  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }


  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }
}


// LazyForEach遍历数据类型
class MyDataSource extends BasicDataSource {
  public dataArray: StringData[] = [];


  public totalCount(): number {
    return this.dataArray.length;
  }


  public getData(index: number): StringData {
    return this.dataArray[index];
  }


  public pushData(data: StringData): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}


@Observed
class StringData {
  message: string;


  constructor(message: string) {
    this.message = message;
  }
}


@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();
  helloCount: number = 4;


  aboutToAppear() {
    for (let i = 0; i <= 3; i++) {
      this.data.pushData(new StringData(`Hello ${i}`));
    }
  }


  build() {
    Column() {
      List({ space: 3 }) {
        // 使用LazyForEach懒加载遍历数据
        LazyForEach(this.data, (item: StringData, index: number) => {
          ListItem() {
            ChildComponent({ data: item })
          }
        }, (item: StringData, index: number) => index.toString() + item.message)
      }.cachedCount(3)
      Button('替换第一个元素')
        .onClick(() => {
          // 替换数组元素不刷新UI，此时新替换的值还未绑定到LazyForEach组件上。
          this.data.dataArray[0] = new StringData('Hello ' + this.helloCount++)
        })
      Button('修改第一个元素的数据')
        .onClick(() => {
          // 替换数组元素后修改元素值也不会刷新UI。
          this.data.dataArray[0].message += '1';
        })
    }
  }
}


// 使用@Reusable实现组件复用
@Reusable
@Component
struct ChildComponent {
  // 使用@ObjectLink接收@Observed装饰的类的数据
  @ObjectLink data: StringData;


  aboutToAppear(): void {
    console.info(`aboutToAppear: ${this.data.message}`);
  }


  aboutToRecycle(): void {
    console.info(`aboutToRecycle: ${this.data.message}`);
  }


  // 对复用的组件进行数据更新
  aboutToReuse(params: Record<string, ESObject>): void {
    this.data.message = (params.data as StringData).message;
    console.info(`aboutToReuse: ${this.data.message}`);
  }


  build() {
    Row() {
      Text(this.data.message)
        .fontSize(50)
        .onAppear(() => {
          console.info(`appear: ${this.data.message}`);
        })
    }.margin({ left: 10, right: 10 })
  }
}
```

### Code block 31

```
// LazyForEach遍历数据基类
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = [];
  private originDataArray: StringData[] = [];


  public totalCount(): number {
    return this.originDataArray.length;
  }


  public getData(index: number): StringData {
    return this.originDataArray[index];
  }


  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener');
      this.listeners.push(listener);
    }
  }


  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener');
      this.listeners.splice(pos, 1);
    }
  }


  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index);
    });
  }


  // 通知LazyForEach处理数据替换
  notifyDataChanged(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index);
    })
  }
}


// LazyForEach遍历数据类型
class MyDataSource extends BasicDataSource {
  public dataArray: StringData[] = [];


  public totalCount(): number {
    return this.dataArray.length;
  }


  public getData(index: number): StringData {
    return this.dataArray[index];
  }


  public pushData(data: StringData): void {
    this.dataArray.push(data);
    this.notifyDataAdd(this.dataArray.length - 1);
  }
}


@Observed
class StringData {
  public message: string;


  constructor(message: string) {
    this.message = message;
  }
}


@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();
  helloCount: number = 4;


  aboutToAppear() {
    for (let i = 0; i <= 2; i++) {
      this.data.pushData(new StringData(`Hello ${i}`));
    }
  }


  build() {
    Column({ space: 3 }) {
      List({ space: 3 }) {
        // 使用LazyForEach懒加载遍历数据
        LazyForEach(this.data, (item: StringData, index: number) => {
          ListItem() {
            ChildComponent({ data: item })
          }.width('100%')
          // LazyForEach的key从index和message构建，每次替换元素时，需要修改key才能触发UI刷新。
        }, (item: StringData, index: number) => index.toString() + item.message)
      }.cachedCount(3)
      Button('替换第一个元素')
        .onClick(() => {
          this.data.dataArray[0] = new StringData('Hello ' + this.helloCount++);
          // 替换元素后通知LazyForEach，可以刷新UI。
          this.data.notifyDataChanged(0);
        })
      Button('修改第一个元素的数据')
        .onClick(() => {
          // 替换元素后由于重新建立绑定，后续修改元素值也能刷新UI。
          this.data.dataArray[0].message += '1';
        })
    }
    .width('100%')
    .alignItems(HorizontalAlign.Center)
  }
}


// 使用Reusable使能组件复用
@Reusable
@Component
struct ChildComponent {
  // 使用@ObjectLink接受@Observed类数据
  @ObjectLink data: StringData;


  aboutToAppear(): void {
    console.info(`aboutToAppear: ${this.data.message}`);
  }


  aboutToRecycle(): void {
    console.info(`aboutToRecycle: ${this.data.message}`);
  }


  // 对复用的组件进行数据更新
  aboutToReuse(params: Record<string, ESObject>): void {
    this.data.message = (params.data as StringData).message;
    console.info(`aboutToReuse: ${this.data.message}`);
  }


  build() {
    Row() {
      Text(this.data.message)
        .fontSize(50)
        .onAppear(() => {
          console.info(`appear: ${this.data.message}`);
        })
    }.margin({ left: 10, right: 10 })
  }
}
```
