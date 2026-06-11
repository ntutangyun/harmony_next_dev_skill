# prefer-const

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-const_

推荐声明后未修改值的变量用const关键字来声明。

规则配置

// code-linter.json5
{
  "rules": {
    "prefer-const": "error"
  }
}

选项

详情请参考eslint/prefer-const选项。

正例

const a = 'hello';
console.log(a);

反例

// 变量a声明以后未重新赋值，建议用const关键字来声明
let a = 'hello';
console.log(a);

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "prefer-const": "error"
  }
}
```

### Code block 2

```
const a = 'hello';
console.log(a);
```

### Code block 3

```
// 变量a声明以后未重新赋值，建议用const关键字来声明
let a = 'hello';
console.log(a);
```

### Code block 4

```
plugin:@typescript-eslint/all
```
