# @typescript-eslint/strict-boolean-expressions

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_strict-boolean-expressions_

不允许在布尔表达式中使用非布尔类型。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/strict-boolean-expressions": "error"
  }
}

选项

详情请参考@typescript-eslint/strict-boolean-expressions选项。

正例

// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
  return undefined;
}

const num: number | undefined = getNum();
if (num !== undefined) {
  console.log('num is defined');
}

function getStr(): string | null {
  return 'null';
}

const str: string | null = getStr();
if (str !== null) {
  console.log('str is not empty');
}

反例

// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
  return undefined;
}

const num: number | undefined = getNum();
if (num) {
  console.log('num is defined');
}

function getStr(): string | null {
  return 'null';
}

const str: string | null = getStr();
if (str) {
  console.log('str is not empty');
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
    "@typescript-eslint/strict-boolean-expressions": "error"
  }
}
```

### Code block 2

```
// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
  return undefined;
}

const num: number | undefined = getNum();
if (num !== undefined) {
  console.log('num is defined');
}

function getStr(): string | null {
  return 'null';
}

const str: string | null = getStr();
if (str !== null) {
  console.log('str is not empty');
}
```

### Code block 3

```
// nullable values should be checked explicitly against null or undefined
function getNum(): number | undefined {
  return undefined;
}

const num: number | undefined = getNum();
if (num) {
  console.log('num is defined');
}

function getStr(): string | null {
  return 'null';
}

const str: string | null = getStr();
if (str) {
  console.log('str is not empty');
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
