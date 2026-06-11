# @typescript-eslint/semi

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_semi_

要求或不允许使用分号。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/semi": "error"
  }
}

选项

详情请参考@typescript-eslint/semi选项。

正例

export const name = 'ESLint';

export class Foo {
  public bar = '1';
}

反例

// 默认在语句末尾需要加分号
export const name = 'ESLint'

export class Foo {
  // 默认在语句末尾需要加分号
  public bar = '1'
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
    "@typescript-eslint/semi": "error"
  }
}
```

### Code block 2

```
export const name = 'ESLint';

export class Foo {
  public bar = '1';
}
```

### Code block 3

```
// 默认在语句末尾需要加分号
export const name = 'ESLint'

export class Foo {
  // 默认在语句末尾需要加分号
  public bar = '1'
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
