# @typescript-eslint/prefer-regexp-exec

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-regexp-exec_

如果未提供全局标志（/g），推荐使用“RegExp#exec”，而不是“String#match”。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-regexp-exec": "error"
  }
}

选项

该规则无需配置额外选项。

正例

/thing/.exec('something');

'some things are just things'.match(/thing/g);

const text = 'something';
const search = /thing/;
search.exec(text);

反例

'something'.match(/thing/);

'some things are just things'.match(/thing/);

const text = 'something';
const search = /thing/;
text.match(search);

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-regexp-exec": "error"
  }
}
```

### Code block 2

```
/thing/.exec('something');

'some things are just things'.match(/thing/g);

const text = 'something';
const search = /thing/;
search.exec(text);
```

### Code block 3

```
'something'.match(/thing/);

'some things are just things'.match(/thing/);

const text = 'something';
const search = /thing/;
text.match(search);
```

### Code block 4

```
plugin:@typescript-eslint/all
```
