# @typescript-eslint/no-for-in-array

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-for-in-array_

禁止使用 for-in 循环来遍历数组元素。

该规则仅支持对.js/.ts文件进行检查。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-for-in-array": "error"
  }
}

选项

该规则无需配置额外选项。

正例

declare const array: string[];

for (const value of array) {
  console.log(value);
}

array.forEach((value) => {
  console.log(value);
});

反例

declare const array: string[];

for (const i in array) {
  console.log(array[i]);
}

for (const i in array) {
  console.log(i, array[i]);
}

规则集

plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-for-in-array": "error"
  }
}
```

### Code block 2

```
declare const array: string[];

for (const value of array) {
  console.log(value);
}

array.forEach((value) => {
  console.log(value);
});
```

### Code block 3

```
declare const array: string[];

for (const i in array) {
  console.log(array[i]);
}

for (const i in array) {
  console.log(i, array[i]);
}
```

### Code block 4

```
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```
