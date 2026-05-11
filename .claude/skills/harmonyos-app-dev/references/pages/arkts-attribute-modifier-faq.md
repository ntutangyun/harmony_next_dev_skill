# 动态属性设置常见问题

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-modifier-faq_

该示例通过Button绑定AttributeModifier，展示了AttributeModifier在设置不支持的属性时会抛出异常的场景，运行示例代码后会出现jscrash报错，参考下方的动图，跳转至具体的报错场景。在本示例中，删除reuseId相关代码即可正常运行。

// xxx.ets
// 设置Button组件属性的自定义AttributeModifier
class MyButtonModifier implements AttributeModifier<ButtonAttribute> {


  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.reuseId('String') // 删除本行可以让程序正常运行
    instance.backgroundColor(Color.Red)
  }
}


@Entry
@Component
struct attributeDemo {
  @State modifier: MyButtonModifier = new MyButtonModifier();


  build() {
    Row() {
      Column() {
        Button('Button')
          .attributeModifier(this.modifier)
      }
      .width('100%')
    }
    .height('100%')
  }
}

使用文本常见问题
命令式节点常见问题
