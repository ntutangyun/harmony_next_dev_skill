# @cross

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_color-value_

// 通过'app.color.xxx'引用的颜色值，需要分别在dark和light颜色模式的color.json中配置
      Text()
        .fontColor($r('app.color.text_color'));
    }
  }
}
反例
@Entry
@Component
struct Index1 {
  build() {
    RelativeContainer() {
      Text('message').fontColor('#000000')
      Text('message').fontColor('rgb(0, 0, 0)')
      Text('message').fontColor(Color.Black)
    }
  }
}
规则集
plugin:@cross-device-app-dev/recommended
plugin:@cross-device-app-dev/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@cross-device-app-dev/color-contrast
@cross-device-app-dev/font-size-unit
