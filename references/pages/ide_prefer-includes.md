# @typescript-eslint/prefer-includes

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-includes_

强制使用“includes”方法而不是“indexOf”方法。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-includes": "error"
  }
}

选项

该规则无需配置额外选项。

正例

const str: string = 'hello';
const array: string[] = ['hello'];
const readonlyArray: readonly string[] = ['hello'];

str.includes('h');
array.includes('h');
readonlyArray.includes('h');

反例

const str: string = 'hello';
const array: string[] = ['hello'];
const readonlyArray: readonly string[] = ['hello'];

const num = -1;
let vv = str.indexOf('h') !== num;
vv = vv && array.indexOf('h') !== num;
vv = vv && readonlyArray.indexOf('h') !== num;
export { vv };

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/prefer-includes": "error"
  }
}
```

### Code block 2

```
const str: string = 'hello';
const array: string[] = ['hello'];
const readonlyArray: readonly string[] = ['hello'];

str.includes('h');
array.includes('h');
readonlyArray.includes('h');
```

### Code block 3

```
const str: string = 'hello';
const array: string[] = ['hello'];
const readonlyArray: readonly string[] = ['hello'];

const num = -1;
let vv = str.indexOf('h') !== num;
vv = vv && array.indexOf('h') !== num;
vv = vv && readonlyArray.indexOf('h') !== num;
export { vv };
```

### Code block 4

```
plugin:@typescript-eslint/all
```
