# 背景流光

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-visual-effect-background-streamer_

@State controller: hdsEffect.ShaderEffectController = new hdsEffect.ShaderEffectController();


  build() {
    Stack() {
    }
    .visualEffect(new hdsEffect.HdsEffectBuilder()
      .shaderEffect({
        effectType: hdsEffect.EffectType.UV_BACKGROUND_FLOW_LIGHT,
        animation: {
          duration: 10000,
          iterations: -1,
          autoPlay: true,
          onFinish: ()=> {
            console.info('Succeeded in finishing');
          }
        },
        controller: this.controller
      })
      .buildEffect())
    .width('100%')
    .height('100%')
  }
}

双边边缘流光
自带背景的双边流光
