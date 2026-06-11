# @typescript-eslint/no-restricted-syntax

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-restricted-syntax_

不允许使用指定的（即用户在规则中定义的）语法。

规则配置

// code-linter.json5
{
  "rules": {
      "@typescript-eslint/no-restricted-syntax": [
         "error",
         {
             "selector": "FunctionExpression",
             "message": "Function expressions are not allowed."
         },
         {
             "selector": "CallExpression[callee.name='setTimeout'][arguments.length!=2]",
             "message": "setTimeout must always be invoked with two arguments."
         }
     ]
  }
}

选项

详情请参考@typescript-eslint/no-restricted-syntax选项。

正例

/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export function doSomething() {
  console.info('doSomething');
}

反例

/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export class CC {
  public name: string;

  public constructor(name: string) {
    this.name = name;
  }
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
      "@typescript-eslint/no-restricted-syntax": [
         "error",
         {
             "selector": "FunctionExpression",
             "message": "Function expressions are not allowed."
         },
         {
             "selector": "CallExpression[callee.name='setTimeout'][arguments.length!=2]",
             "message": "setTimeout must always be invoked with two arguments."
         }
     ]
  }
}
```

### Code block 2

```
/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export function doSomething() {
  console.info('doSomething');
}
```

### Code block 3

```
/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export class CC {
  public name: string;

  public constructor(name: string) {
    this.name = name;
  }
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
