# js标签配置

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-js-tag_

指定designWidth（屏幕逻辑宽度），所有与大小相关的样式（例如width、font-size）均以designWidth和实际屏幕宽度的比例进行缩放，例如在designWidth为720时，如果设置width为100px时，在实际宽度为1440物理像素的屏幕上，width实际渲染像素为200物理像素。

设置autoDesignWidth为true，此时designWidth字段将会被忽略，渲染组件和布局时按屏幕密度进行缩放。屏幕逻辑宽度由设备宽度和屏幕密度自动计算得出，在不同设备上可能不同，请使用相对布局来适配多种设备。例如：在466*466分辨率，320dpi的设备上，屏幕密度为2（以160dpi为基准），1px等于渲染出的2物理像素。

说明

组件样式中<length>类型的默认值，基于屏幕密度进行计算和绘制。例如：在屏幕密度为2（以160dpi为基准）的设备上，默认<length>为1px时，设备上实际渲染出2物理像素。

autoDesignWidth、designWidth的设置不影响默认值计算方式和绘制结果。

属性	类型	必填	缺省值	描述
designWidth	number	否	

720

	页面显示设计时的参考值，实际显示效果基于设备宽度与参考值之间的比例进行缩放。
autoDesignWidth	boolean	否	false	

页面设计基准宽度是否自动计算。

true表示页面设计基准宽度自动计算，false表示页面设计基准宽度不自动计算。

当设为true时，designWidth将会被忽略，设计基准宽度由设备宽度与屏幕密度计算得出。

示例如下：

{
    // ...
    "window": {
        "designWidth": 720,
        "autoDesignWidth": false
    }
    // ...
}
示例
{
  "app": {
    "bundleName": "com.example.player",
    "version": {
        "code": 1,
        "name": "1.0"
    },
    "vendor": "example"
  },
  "module": {
      // ...
      "js": [
      {
          "name": "default",
          "pages": [
              "pages/index/index",
              "pages/detail/detail"
          ],
          "window": {
              "designWidth": 720,
              "autoDesignWidth": false
          }
      }
      ],
      "abilities": [
      {
          // ...
      }
    ]
  }
}
文件组织
app.js
