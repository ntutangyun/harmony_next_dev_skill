# @typescript-eslint/triple-slash-reference

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_triple-slash-reference_

不允许某些三斜杠引用，推荐使用ES6风格的导入声明。

支持以下三种三斜杠引用方式的检查

/// <reference lib="..." />
/// <reference path="..." />
/// <reference types="..." />

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/triple-slash-reference": "error"
  }
}

选项

详情请参考@typescript-eslint/triple-slash-reference选项。

正例

import { value } from 'code';
export { value };

反例

/// <reference path="code" />

globalThis.value;

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
/// <reference lib="..." />
/// <reference path="..." />
/// <reference types="..." />
```

### Code block 2

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/triple-slash-reference": "error"
  }
}
```

### Code block 3

```
import { value } from 'code';
export { value };
```

### Code block 4

```
/// <reference path="code" />

globalThis.value;
```

### Code block 5

```
plugin:@typescript-eslint/all
```
