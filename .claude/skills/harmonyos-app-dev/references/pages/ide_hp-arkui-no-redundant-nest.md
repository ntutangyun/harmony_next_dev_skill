# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-redundant-nest_

"@performance/hp-arkui-remove-redundant-nest-container": "suggestion",
  }
}
选项

该规则无需配置额外选项。

正例
@Entry  
@Component  
struct MyComponent {  
  @State children: number[] = Array.from(Array<number>(900), (v, k) => k);  
  
  build() {  
    Scroll() {  
      Grid() {  
        ForEach(this.children, (item: Number[]) => {  
          GridItem() {  
            Text(item.toString())  
          }.backgroundColor(Color.Yellow)  
        }, (item: string) => item)  
      }  
      .columnsTemplate('1fr 1fr 1fr 1fr')  
      .columnsGap(0)  
      .rowsGap(0)  
      .size({ width: "100%", height: "100%" })  
    }  
  }  
}
反例
@Entry
@Component
struct MyComponent {
    @State children: number[] = Array.from(Array<number>(900), (v, k) => k);
    
    build() {
      Scroll() {
      Grid() {
        ForEach(this.children, (item: Number[]) => {
          GridItem() {
            // 冗余Stack
            Stack() {  
              Stack() {  
                Stack() {  
                  Text(item.toString())  
                }.size({ width: "100%"})  
              }.backgroundColor(Color.Yellow)  
            }.backgroundColor(Color.Pink)  
          }  
        }, (item: string) => item)  
      }  
      .columnsTemplate('1fr 1fr 1fr 1fr')  
      .columnsGap(0)  
      .rowsGap(0)  
      .size({ width: "100%", height: "100%" })  
    }  
  }  
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-reduce-pangesture-distance
@performance/hp-arkui-remove-redundant-state-var
