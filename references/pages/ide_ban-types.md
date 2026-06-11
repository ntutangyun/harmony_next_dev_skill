# @typescript-eslint/ban-types

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_ban-types_

不允许使用某些类型。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-types": "error"
  }
}

选项

支持配置以下选项：

type Options = {
  types: {
    [key: string]: boolean | string | { message: string, fixWith: string } | null;
  };
  extendDefaults: boolean;
}

boolean：布尔值，配置为true时，表示禁用该类型，告警信息使用默认配置；配置为false时，表示不禁用该类型，通常和{ extendDefaults: true }搭配使用，表示不检查某些预置类型。

string：自定义告警信息。

{ message: string, fixWith: string } ：对象，message表示自定义的告警信息，fixWith表示自动修复时将禁用类型替换为新类型。

null：使用默认的告警信息。

extendDefaults：布尔类型，默认为true，表示需要检查ts语法中内置的原始类包装器，包括String、Boolean、Number、Symbol、BigInt、Function和Object；配置为false时，表示不需要检查。

示例：

"@typescript-eslint/ban-types": [
  "error",
  {
    "types": {
      "String": true,
      "Number": false,
      "MyType": "Do not use 'MyType'",
      "MyTypeWithFix": {
        "message": "Do not use 'MyTypeWithFix', use 'MyType' instead",
        "fixWith": "MyType"
      }
    },
    "extendDefaults": true
  },
]

正例

// 类型小写保持一致
const str: string = 'foo';
const bool: boolean = true;
const num: number = 1;
const bigInt: bigint = 1n;

// 使用正确的函数类型
const func: () => string = () => 'hello';

export { str, bool, num, bigInt, func };

反例

// 类型小写保持一致
const str: String = 'foo';
const bool: Boolean = true;
const num: Number = 1;
const bigInt: BigInt = 1n;

// 使用正确的函数类型
const func: Function = () => 'hello';

export { str, bool, num, bigInt, func };

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/ban-types": "error"
  }
}
```

### Code block 2

```
type Options = {
  types: {
    [key: string]: boolean | string | { message: string, fixWith: string } | null;
  };
  extendDefaults: boolean;
}
```

### Code block 3

```
"@typescript-eslint/ban-types": [
  "error",
  {
    "types": {
      "String": true,
      "Number": false,
      "MyType": "Do not use 'MyType'",
      "MyTypeWithFix": {
        "message": "Do not use 'MyTypeWithFix', use 'MyType' instead",
        "fixWith": "MyType"
      }
    },
    "extendDefaults": true
  },
]
```

### Code block 4

```
// 类型小写保持一致
const str: string = 'foo';
const bool: boolean = true;
const num: number = 1;
const bigInt: bigint = 1n;

// 使用正确的函数类型
const func: () => string = () => 'hello';

export { str, bool, num, bigInt, func };
```

### Code block 5

```
// 类型小写保持一致
const str: String = 'foo';
const bool: Boolean = true;
const num: Number = 1;
const bigInt: BigInt = 1n;

// 使用正确的函数类型
const func: Function = () => 'hello';

export { str, bool, num, bigInt, func };
```

### Code block 6

```
plugin:@typescript-eslint/all
```
