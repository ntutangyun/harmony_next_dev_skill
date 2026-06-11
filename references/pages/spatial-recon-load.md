# 加载3DGS模型

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/spatial-recon-load_

适用场景

支持的3DGS模块格式包括：MP4、PLY、GLB三种格式。

效果如下图所示：

接口说明

以下仅列出本指南示例代码中调用的部分主要接口：

接口名	描述
static loadGSNode(scene: Scene, params: GSImportSettings, parent?: Node): Promise<GSNode>	加载3DGS模型。

开发步骤

从entry目录进入/src/main/ets/entryability/EntryAbility.ets文件，导入空间建模模块。

import { spatialRender } from '@kit.SpatialReconKit';
import { Scene, RenderContext } from '@kit.ArkGraphics3D'

加载当前场景的上下文。

let renderContext: RenderContext | null = Scene.getDefaultRenderContext();

调用加载3DGS模型接口。

if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  let scene = Scene.load().then(async (scene: Scene) => {
    let uri = "OhosRawFile://assets/gltf/model.glb"; // 3DGS模型的uri，根据实际情况修改
    let offset = 0;
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
  });
}

## Code blocks

### Code block 1

```
import { spatialRender } from '@kit.SpatialReconKit';
import { Scene, RenderContext } from '@kit.ArkGraphics3D'
```

### Code block 2

```
let renderContext: RenderContext | null = Scene.getDefaultRenderContext();
```

### Code block 3

```
if (renderContext != null) {
  renderContext.loadPlugin(spatialRender.GSPlugin.PLUGIN_ID);
  let scene = Scene.load().then(async (scene: Scene) => {
    let uri = "OhosRawFile://assets/gltf/model.glb"; // 3DGS模型的uri，根据实际情况修改
    let offset = 0;
    let gsNodeext: spatialRender.GSNode = await spatialRender.GSPlugin.loadGSNode(scene, {uri, offset}, scene.root);
  });
}
```
