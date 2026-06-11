# @typescript-eslint/array-type

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_array-type_

定义数组类型时，建议使用相同的样式。比如都使用T[]或者都使用Array<T>。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/array-type": "error"
  }
}

选项

详情请参考typescript/array-type 选项。

正例

const x: string[] = ['a', 'b'];
const y: readonly string[] = ['a', 'b'];

export { x, y };

反例

const x: Array<string> = ['a', 'b'];
const y: ReadonlyArray<string> = ['a', 'b'];

export { x, y };

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/array-type": "error"
  }
}
```

### Code block 2

```
const x: string[] = ['a', 'b'];
const y: readonly string[] = ['a', 'b'];

export { x, y };
```

### Code block 3

```
const x: Array<string> = ['a', 'b'];
const y: ReadonlyArray<string> = ['a', 'b'];

export { x, y };
```

### Code block 4

```
plugin:@typescript-eslint/all
```
