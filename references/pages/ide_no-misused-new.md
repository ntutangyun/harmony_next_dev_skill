# @typescript-eslint/no-misused-new

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-misused-new_

要求正确地定义“new”和“constructor”。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-misused-new": "error"
  }
}

选项

该规则无需配置额外选项。

正例

export declare class C {
  public name: string;

  public constructor();
}

反例

export declare class C {
  // 应该定义为constructor(): C
  public new(): C;
}

export interface I {
  // 不应该定义constructor
  constructor(): void;
}

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-misused-new": "error"
  }
}
```

### Code block 2

```
export declare class C {
  public name: string;

  public constructor();
}
```

### Code block 3

```
export declare class C {
  // 应该定义为constructor(): C
  public new(): C;
}

export interface I {
  // 不应该定义constructor
  constructor(): void;
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
