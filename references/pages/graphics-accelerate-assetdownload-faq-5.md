# 如何解析华为CDN场景下manifestUrl对应的xml文件

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-5_

推荐使用@ifbear/fast-xml-parser。

执行如下命令行，安装依赖。

To use as package dependency $ ohpm install @ifbear/fast-xml-parser

示例代码：

const { XMLParser, XMLBuilder, XMLValidator} = require("fast-xml-parser");

const parser = new XMLParser();
let jObj = parser.parse(XMLdata);

## Code blocks

### Code block 1

```
To use as package dependency $ ohpm install @ifbear/fast-xml-parser
```

### Code block 2

```
const { XMLParser, XMLBuilder, XMLValidator} = require("fast-xml-parser");

const parser = new XMLParser();
let jObj = parser.parse(XMLdata);
```
