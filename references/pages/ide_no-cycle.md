# @security/no-cycle

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-cycle_

该规则禁止使用循环依赖。

规则配置

// code-linter.json5
{
  "rules": {
    "@security/no-cycle": "error"
  }
}

选项

该规则无需配置额外选项。

正例

// foo.ets
import {} from './bar';

// bar.ets
import {} from './index';

反例

// foo.ets
import {} from './bar';

// bar.ets
import {} from './foo';

说明

反例中foo.ets文件依赖了bar.ets文件，bar.ets文件同时依赖了foo.ets文件，造成了循环依赖。

规则集

plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@security/no-cycle": "error"
  }
}
```

### Code block 2

```
// foo.ets
import {} from './bar';

// bar.ets
import {} from './index';
```

### Code block 3

```
// foo.ets
import {} from './bar';

// bar.ets
import {} from './foo';
```

### Code block 4

```
plugin:@security/all
```
