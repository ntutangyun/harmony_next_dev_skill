# XML生成

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-generation_

XML模块提供XmlSerializer及XmlDynamicSerializer类来生成XML数据，使用XmlSerializer需传入固定长度的ArrayBuffer或DataView对象作为输出缓冲区，用于存储序列化后的XML数据。

XmlDynamicSerializer类动态扩容，程序根据实际生成的数据大小自动创建ArrayBuffer。

调用不同的方法写入不同的内容，如startElement(name: string)写入元素开始标记，setText(text: string)写入标签值。

XML模块的API接口可以参考@ohos.xml的详细描述，按需求调用相应的函数可以生成一份完整的XML数据。

使用XmlSerializer生成XML示例如下：

引入模块。

import { xml, util } from '@kit.ArkTS';
XmlSerializer.ets

创建缓冲区，构造XmlSerializer对象。可以基于ArrayBuffer构造XmlSerializer对象，也可以基于DataView构造XmlSerializer对象。

方式1：基于ArrayBuffer构造XmlSerializer对象

let arrayBuffer: ArrayBuffer = new ArrayBuffer(2048); // 创建一个2048字节的缓冲区
let serializer: xml.XmlSerializer = new xml.XmlSerializer(arrayBuffer); // 基于ArrayBuffer构造XmlSerializer对象
XmlSerializer.ets

方式2：基于DataView构造XmlSerializer对象

let arrayBuffer: ArrayBuffer = new ArrayBuffer(2048); // 创建一个2048字节的缓冲区
let dataView: DataView = new DataView(arrayBuffer); // 创建一个DataView
let serializer: xml.XmlSerializer = new xml.XmlSerializer(dataView); // 基于DataView构造XmlSerializer对象
XmlSerializer.ets

调用XML元素生成函数。

serializer.setDeclaration(); // 写入XML的声明
serializer.startElement('bookstore'); // 写入元素开始标记
serializer.startElement('book'); // 嵌套元素开始标记
serializer.setAttributes('category', 'COOKING'); // 写入属性及其属性值
serializer.startElement('title');
serializer.setAttributes('lang', 'en');
serializer.setText('Everyday'); // 写入标签值
serializer.endElement(); // 写入结束标记
serializer.startElement('author');
serializer.setText('Giana');
serializer.endElement();
serializer.startElement('year');
serializer.setText('2005');
serializer.endElement();
serializer.endElement();
serializer.endElement();
XmlSerializer.ets

使用Uint8Array操作ArrayBuffer，并调用TextDecoder对Uint8Array解码后输出。

let uint8Array: Uint8Array = new Uint8Array(arrayBuffer); // 使用Uint8Array读取arrayBuffer的数据
let textDecoder: util.TextDecoder = util.TextDecoder.create(); // 调用util模块的TextDecoder类
let result: string = textDecoder.decodeToString(uint8Array); // 对uint8Array解码
console.info(result);
XmlSerializer.ets

输出结果如下：

<?xml version="1.0" encoding="utf-8"?><bookstore>
  <book category="COOKING">
    <title lang="en">Everyday</title>
    <author>Giana</author>
    <year>2005</year>
  </book>
</bookstore>

使用XmlDynamicSerializer生成XML示例如下：

引入模块。

import { xml, util } from '@kit.ArkTS';
XmlDynamicSerializer.ets

调用XML元素生成函数。

let dySerializer = new xml.XmlDynamicSerializer('utf-8');
dySerializer.setDeclaration(); // 写入XML的声明
dySerializer.startElement('bookstore'); // 写入元素开始标记
dySerializer.startElement('book'); // 嵌套元素开始标记
dySerializer.setAttributes('category', 'COOKING'); // 写入属性及其属性值
dySerializer.startElement('title');
dySerializer.setAttributes('lang', 'en');
dySerializer.setText('Everyday'); // 写入标签值
dySerializer.endElement(); // 写入结束标记
dySerializer.startElement('author');
dySerializer.setText('Giana');
dySerializer.endElement();
dySerializer.startElement('year');
dySerializer.setText('2005');
dySerializer.endElement();
dySerializer.endElement();
dySerializer.endElement();
let arrayBuffer = dySerializer.getOutput();
XmlDynamicSerializer.ets

使用Uint8Array操作ArrayBuffer，并调用TextDecoder对Uint8Array解码后输出。

let uint8Array: Uint8Array = new Uint8Array(arrayBuffer);
let result: string = util.TextDecoder.create().decodeToString(uint8Array);
console.info(result);
XmlDynamicSerializer.ets

输出结果如下：

<?xml version="1.0" encoding="utf-8"?>
<bookstore>
  <book category="COOKING">
    <title lang="en">Everyday</title>
    <author>Giana</author>
    <year>2005</year>
  </book>
</bookstore>
XML概述
XML解析
