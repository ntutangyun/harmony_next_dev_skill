# 如何解析华为CDN场景下manifestUrl对应的xml文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-5_

To use as package dependency $ ohpm install @ifbear/fast-xml-parser

示例代码：

const { XMLParser, XMLBuilder, XMLValidator} = require("fast-xml-parser");


const parser = new XMLParser();
let jObj = parser.parse(XMLdata);
游戏资源加速ExtensionAbility方法中使用static静态变量为什么不生效
是否可以仅接入下载ExtensionAbility，而不改写原先在游戏引擎内部的下载逻辑或下载中间件
