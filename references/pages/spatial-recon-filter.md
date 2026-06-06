# 添加滤镜效果

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-filter_

首先从项目根目录进入/src/main/ets/entryability/EntryAbility.ets文件，导入空间建模模块。

import { Scene, RenderContext } from '@kit.ArkGraphics3D';
import { spatialRender } from '@kit.SpatialReconKit';
import { RenderingPipelineType } from '@ohos.graphics.scene'

加载当前场景的上下文。

let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

调用滤镜接口。

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  Scene.load().then(async (scene: Scene) => {
    let rf = scene.getResourceFactory();
    let effect : spatialRender.RetroEffect =
      await rf.createEffect({ effectId: spatialRender.GSPlugin.RETRO_EFFECT_ID }) as spatialRender.RetroEffect;
    let camera = await rf.createCamera({ name: "gsCam", path: "//gsCam" }, { renderingPipeline: RenderingPipelineType.FORWARD });
    camera.effects.append(effect)
  });
}
加载3DGS模型
重建三维场景（C/C++）
