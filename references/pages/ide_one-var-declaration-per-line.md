# @hw-stylistic/one-var-declaration-per-line

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_one-var-declaration-per-line_

变量声明时，要求一次仅声明一个变量。该规则仅检查.ets文件类型。

规则配置

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/one-var-declaration-per-line": "error"
  }
}

选项

该规则无需配置额外选项。

正例

let a: string = 'hello';
let b: string = 'world';
a += 'my';
b += 'my';

const c: string = 'hello';
const d: string = 'world';

console.info(`a: ${a}, b: ${b}, c: ${c}, d: ${d}`);

反例

// Split 'const' declarations into multiple statements.
const a: string = 'hello', b: string = 'world';

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
    "@hw-stylistic/one-var-declaration-per-line": "error"
  }
}
```

### Code block 2

```
let a: string = 'hello';
let b: string = 'world';
a += 'my';
b += 'my';

const c: string = 'hello';
const d: string = 'world';

console.info(`a: ${a}, b: ${b}, c: ${c}, d: ${d}`);
```

### Code block 3

```
// Split 'const' declarations into multiple statements.
const a: string = 'hello', b: string = 'world';
```

### Code block 4

```
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"
```
