# @typescript-eslint/restrict-template-expressions

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_restrict-template-expressions_

要求模板表达式中的变量为“string”类型。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/restrict-template-expressions": "error"
  }
}

选项

详情请参考@typescript-eslint/restrict-template-expressions选项。

正例

const arg: string | undefined = 'foo';
export const msg1 = `arg = ${arg}`;
export const msg2 = `arg = ${arg || 'default'}`;

反例

const arg1 = ['1', '2'];
export const msg1 = `arg1 = ${arg1}`;

interface GeneratedObjectLiteralInterface {
  name: string;
}

const arg2: GeneratedObjectLiteralInterface = { name: 'Foo' };
export const msg2 = `arg2 = ${arg2 || null}`;

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/restrict-template-expressions": "error"
  }
}
```

### Code block 2

```
const arg: string | undefined = 'foo';
export const msg1 = `arg = ${arg}`;
export const msg2 = `arg = ${arg || 'default'}`;
```

### Code block 3

```
const arg1 = ['1', '2'];
export const msg1 = `arg1 = ${arg1}`;

interface GeneratedObjectLiteralInterface {
  name: string;
}

const arg2: GeneratedObjectLiteralInterface = { name: 'Foo' };
export const msg2 = `arg2 = ${arg2 || null}`;
```

### Code block 4

```
plugin:@typescript-eslint/all
```
