# @performance/high

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-high-frequency-log-check_

高频函数包括：onTouch、onItemDragMove、onDragMove、onMouse、onVisibleAreaChange、onAreaChange、onScroll（已废弃）、onWillScroll。

高耗时函数处理场景下，建议优先修改。

规则配置
// code-linter.json5
{
  "rules": {
    "@performance/high-frequency-log-check": "warn",
  }
}
选项

该规则无需配置额外选项。

正例
// Test.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Scroll()
        .onWillScroll(() => {
          const TAG = 'onWillScroll';
        })
    }
  }
}
反例
// Test.ets
import hilog from '@ohos.hilog';


@Entry
@Component
struct Index {
  build() {
    Column() {
      Scroll()
        .onWillScroll(() => {
          // Avoid printing logs
          hilog.info(1001, 'Index', 'onWillScroll');
        })
    }
  }
}
规则集
plugin:@performance/recommended
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-wrap-waterflow-if-else-footer（已下线）
@performance/hp-ffrt-no-use-std
