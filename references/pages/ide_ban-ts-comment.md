# @typescript-eslint/ban-ts-comment

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-ts-comment_

不允许使用`@ts-<directional>`格式的注释，或要求在注释后进行补充说明。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-ts-comment": "error"
  }
}

选项

详情请参考@typescript-eslint/ban-ts-comment选项。

正例

console.log('hello');

反例

// @ts-expect-error
console.log('hello');

/* @ts-expect-error */
console.log('hello');

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-ts-comment": "error"
  }
}
```

### Code block 2

```
console.log('hello');
```

### Code block 3

```
// @ts-expect-error
console.log('hello');

/* @ts-expect-error */
console.log('hello');
```

### Code block 4

```
plugin:@typescript-eslint/all
```
