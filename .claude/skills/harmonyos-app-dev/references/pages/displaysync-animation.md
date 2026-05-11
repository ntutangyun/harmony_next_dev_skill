# 请求动画绘制帧率

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysync-animation_

在应用开发中，属性动画和显式动画能够使用可选参数ExpectedFrameRateRange，为不同的动画配置不同的期望绘制帧率。

请求属性动画的绘制帧率

定义文本组件的属性动画，请求绘制帧率为60，范例如下：

Text('60')
  // ...
  .animation({
    duration: 1200,
    iterations: 10,
    // ...
    expectedFrameRateRange: {
      expected: 60,
      min: 0,
      max: 120,
    },
  })
PropertyAnimationDisplaySync.ets
请求显式动画的绘制帧率

定义按钮组件的显式动画，请求绘制帧率为30，范例如下：

Button('Start')
  // ...
  .onClick(() => {
    // ...


    this.uiContext?.animateTo({
      duration: 1200,
      iterations: 10,
      // ...
      expectedFrameRateRange: {
        expected: 30,
        min: 0,
        max: 120,
      },
    }, () => {
      // ...
    })


    // ...
  })
PropertyAnimationDisplaySync.ets
可变帧率简介
请求UI绘制帧率
