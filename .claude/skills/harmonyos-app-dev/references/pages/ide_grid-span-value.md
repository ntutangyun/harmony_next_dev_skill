# @cross

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_grid-span-value_

span: { sm: 4, md: 4, lg: 4 }, offset: { sm: 0, md: 2, lg: 4 }
        }) {
          Row().backgroundColor($r('sys.color.ohos_id_color_palette_aux1'))
        }
      }
    }
  }
}
反例
@Entry
@Component
struct Index {
  build() {
    GridRow({
      columns: { sm: 4, md: 8, lg: 12 }
    }) {
      GridCol({
        span: { sm: 2.5, md: 4, lg: 4 }, offset: { sm: 0, md: 2.5, lg: 4 }
      }) {
        Row().backgroundColor($r('sys.color.ohos_id_color_palette_aux1'))
      }
    }
  }
}
规则集
plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@cross-device-app-dev/grid-columns-span
@cross-device-app-dev/one-multi-breakpoint-check
