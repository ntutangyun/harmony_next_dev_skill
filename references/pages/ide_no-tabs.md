# @hw-stylistic/no-tabs

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-tabs_

禁止使用tab作为缩进，推荐使用空格。该规则仅检查.ets文件类型。

规则配置

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/no-tabs": "error"
  }
}

选项

该规则无需配置额外选项。

正例

export const message: string = 'Hello World';

反例

export	const	message:	string = 'Hello World';

规则集

"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@hw-stylistic/no-tabs": "error"
  }
}
```

### Code block 2

```
export const message: string = 'Hello World';
```

### Code block 3

```
export	const	message:	string = 'Hello World';
```

### Code block 4

```
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```
