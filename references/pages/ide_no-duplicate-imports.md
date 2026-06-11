# @typescript-eslint/no-duplicate-imports

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-duplicate-imports_

禁止重复的模块导入。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-duplicate-imports": "error"
  }
}

选项

详情请参考eslint/no-duplicate-imports选项。

正例

// foo和bar代表两个文件
import { foo } from './foo';
import bar from './bar';

反例

// foo代表文件
import { foo } from './foo';
import { bar } from './foo';

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-duplicate-imports": "error"
  }
}
```

### Code block 2

```
// foo和bar代表两个文件
import { foo } from './foo';
import bar from './bar';
```

### Code block 3

```
// foo代表文件
import { foo } from './foo';
import { bar } from './foo';
```

### Code block 4

```
plugin:@typescript-eslint/all
```
