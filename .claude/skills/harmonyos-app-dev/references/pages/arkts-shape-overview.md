# 几何图形绘制概述

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shape-overview_

绘制几何图形有两种方法：一是通过绘制组件Shape直接绘制出几何图形；二是通过形状裁剪属性clipShape将组件裁剪成几何图形。

使用场景
绘制方式	使用场景
绘制几何图形 (Shape)	用于创建指定形状的组件，在页面上直接绘制出几何图形。
形状裁剪 (clipShape)	用于将组件裁剪为指定的几何图形。
约束限制

对绘制组件，既可用Shape组件作为父组件实现类似SVG的效果，也可单独使用各种形状的子组件进行绘制。

对形状裁剪属性，裁剪不会导致被裁剪区域无法响应绑定的手势事件。

几何图形绘制
绘制几何图形 (Shape)
