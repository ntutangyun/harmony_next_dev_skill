# @typescript-eslint/naming-convention

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_naming-convention_

强制标识符使用一致的命名风格。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/naming-convention": "error"
  }
}

选项

详情请参考@typescript-eslint/naming-convention选项。

正例

// 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
export class Bar {
  public meth() {
    console.info('method');
  }
}

export function foo() {
  console.info('function');
}

反例

// 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
export class bar {
  public Meth() {
    console.info('method');
  }
}

export function Foo() {
  console.info('function');
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
    "@typescript-eslint/naming-convention": "error"
  }
}
```

### Code block 2

```
// 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
export class Bar {
  public meth() {
    console.info('method');
  }
}

export function foo() {
  console.info('function');
}
```

### Code block 3

```
// 默认类名为大驼峰的命名风格，函数名为小驼峰的命名风格
export class bar {
  public Meth() {
    console.info('method');
  }
}

export function Foo() {
  console.info('function');
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
