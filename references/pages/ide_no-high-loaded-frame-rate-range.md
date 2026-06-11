# @performance/no-high-loaded-frame-rate-range

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-high-loaded-frame-rate-range_

不允许锁定最高帧率运行。

规则配置

// code-linter.json5
{
  "rules": {
    "@performance/no-high-loaded-frame-rate-range": "warn",
  }
}

选项

该规则无需配置额外选项。

正例

import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 60,
  min: 45,
  max: 60,
});

反例

import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 120,
  min: 120,
  max: 120,
});

规则集

plugin:@performance/all
plugin:@performance/recommended

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@performance/no-high-loaded-frame-rate-range": "warn",
  }
}
```

### Code block 2

```
import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 60,
  min: 45,
  max: 60,
});
```

### Code block 3

```
import { displaySync } from '@kit.ArkGraphics2D';
let sync = displaySync.create();
sync.setExpectedFrameRateRange({
  expected: 120,
  min: 120,
  max: 120,
});
```

### Code block 4

```
plugin:@performance/all
plugin:@performance/recommended
```
