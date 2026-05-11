# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-abouttoreuse_

"@performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse": "suggestion",
  }
}
选项

该规则无需配置额外选项。

正例
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';


// 此处为复用的自定义组件
@Reusable
@Component
struct ItemComponent {
  @State desc: string = '';
  @State sum: number = 0;
  @State avg: number = 0;


  aboutToReuse(params: Record<string, Object>): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
    this.avg = params.avg as number;
  }


  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
      Text('结果' + this.sum)
        .fontSize(30)
        .fontWeight(30)
      Text('平均值' + this.avg)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}


@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();


  aboutToAppear(): void {
    for (let index = 0; index < 20; index++) {
      this.data.pushData(index.toString())
    }
  }


  build() {
    Column() {
      List() {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            ItemComponent({ desc: item, sum: 0, avg: 0 })
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
反例
// 源码文件，请以工程实际为准
import { MyDataSource } from './MyDataSource';


// 此处为复用的自定义组件
@Reusable
@Component
struct ItemComponent {
  @State desc: string = '';
  @State sum: number = 0;
  @Link avg: number;


  aboutToReuse(params: Record<string, Object>): void {
    this.desc = params.desc as string;
    this.sum = params.sum as number;
    this.avg = params.avg as number;
  }


  build() {
    Column() {
      Text('子组件' + this.desc)
        .fontSize(30)
        .fontWeight(30)
      Text('结果' + this.sum)
        .fontSize(30)
        .fontWeight(30)
      Text('平均值' + this.avg)
        .fontSize(30)
        .fontWeight(30)
    }
  }
}


@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();


  aboutToAppear(): void {
    for (let index = 0; index < 20; index++) {
      this.data.pushData(index.toString())
    }
  }


  build() {
    Column() {
      List() {
        LazyForEach(this.data, (item: string) => {
          ListItem() {
            ItemComponent({ desc: item, sum: 0, avg: 0 })
          }
          .width('100%')
          .height(100)
        }, (item: string) => item)
      }
      .width('100%')
      .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
规则集
plugin:@performance/recommended
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/gif-hardware-decoding-check
@performance/hp-arkui-avoid-empty-callback
