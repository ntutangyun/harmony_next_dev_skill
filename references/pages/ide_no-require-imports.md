# @typescript-eslint/no-require-imports

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-require-imports_

禁止使用“require()”语法导入依赖。

该规则仅支持对.js/.ts文件进行检查。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-require-imports": "error"
  }
}

选项

该规则无需配置额外选项。

正例

// lib1 lib2 lib3为.js/.ts文件
import * as lib1 from './lib1';
import { lib2 } from './lib2';
import * as lib3 from './lib3';

反例

// lib3为.js/.ts文件
import lib3 = require('./lib3');

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-require-imports": "error"
  }
}
```

### Code block 2

```
// lib1 lib2 lib3为.js/.ts文件
import * as lib1 from './lib1';
import { lib2 } from './lib2';
import * as lib3 from './lib3';
```

### Code block 3

```
// lib3为.js/.ts文件
import lib3 = require('./lib3');
```

### Code block 4

```
plugin:@typescript-eslint/all
```
