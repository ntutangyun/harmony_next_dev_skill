# 本地化语言与地区名称

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/i18n-language-region-display_

功能介绍

本地化语言与地区名称是指语言和地区按照本地的语言习惯显示，确保用户可识别，主要在展示语言与地区名称的场景下使用。例如，在简体中文环境下，简体中文显示为“简体中文”，英文显示为“英文”；在英文环境下，简体中文显示为“Simplified Chinese”，英文显示为“English”。

开发步骤

接口具体说明请参考getDisplayCountry和getDisplayLanguage的API文档。

导入模块。

import { i18n } from '@kit.LocalizationKit';

使用场景。

本地化语言名称。支持获取语言名称在不同语言下的翻译，以获取德文语言名称的中文翻译为例：

let displayLanguage = i18n.System.getDisplayLanguage('de', 'zh-Hans-CN'); // displayLanguage = '德文'
// language: 语言两字母代码，如'zh'，'de'，'fr'等
// locale: 表示区域ID的字符串，如'en-GB'、'en-US'、'zh-Hans-CN'等
// sentenceCase: 返回的语言名称是否需要首字母大写，默认值：true

本地化国家/地区名称。支持获取国家/地区名称在不同语言下的翻译，以获取沙特阿拉伯国家名称的英文翻译为例：

let displayCountry = i18n.System.getDisplayCountry('SA', 'en-GB'); // displayCountry = 'Saudi Arabia'
// country: 国家/地区两字母代码，如'CN'、'DE'、'SA'等
// locale: 表示区域ID的字符串，如'en-GB'、'en-US'、'zh-Hans-CN'等
// sentenceCase: 返回的国家/地区名称是否需要首字母大写，默认值：true

## Code blocks

### Code block 1

```
import { i18n } from '@kit.LocalizationKit';
```

### Code block 2

```
let displayLanguage = i18n.System.getDisplayLanguage('de', 'zh-Hans-CN'); // displayLanguage = '德文'
// language: 语言两字母代码，如'zh'，'de'，'fr'等
// locale: 表示区域ID的字符串，如'en-GB'、'en-US'、'zh-Hans-CN'等
// sentenceCase: 返回的语言名称是否需要首字母大写，默认值：true
```

### Code block 3

```
let displayCountry = i18n.System.getDisplayCountry('SA', 'en-GB'); // displayCountry = 'Saudi Arabia'
// country: 国家/地区两字母代码，如'CN'、'DE'、'SA'等
// locale: 表示区域ID的字符串，如'en-GB'、'en-US'、'zh-Hans-CN'等
// sentenceCase: 返回的国家/地区名称是否需要首字母大写，默认值：true
```
