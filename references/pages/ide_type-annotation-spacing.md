# @typescript-eslint/type-annotation-spacing

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_type-annotation-spacing_

类型注解前后需要一致的空格风格。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/type-annotation-spacing": "error"
  }
}

选项

支持配置以下选项：

type Options = {
  before: boolean;
  after: boolean;
  overrides: {
    colon: {
      before: boolean;
      after: boolean;
    };
    arrow: {
      before: boolean;
      after: boolean;
    };
    variable: {
      before: boolean;
      after: boolean;
    };
    parameter: {
      before: boolean;
      after: boolean;
    };
    property: {
      before: boolean;
      after: boolean;
    };
    returnType: {
      before: boolean;
      after: boolean;
    };
  }
}

before/after：布尔类型，可以设置为true或者false。true表示类型注解中的冒号（:）和箭头（=>）之前/之后需要加空格，false表示类型注解中的冒号（:）和箭头（=>）之前/之后不需要加空格。

before：布尔类型，可以设置为true或者false。默认值为false，表示类型注解中的冒号（:）之前不需要加空格；true表示类型注解中的冒号（:）之前需要加空格。

after：布尔类型，可以设置为true或者false。默认值为false，表示类型注解中的冒号（:）之后不需要加空格；true表示类型注解中的冒号（:）之后需要加空格。

before：布尔类型，可以设置为true或者false。默认值为true，表示类型注解中的箭头（=>）之前需要加空格；false表示类型注解中的箭头（=>）之前不需要加空格。

after：布尔类型，可以设置为true或者false。默认值为true，表示类型注解中的箭头（=>）之后需要加空格；false表示类型注解中的箭头（=>）之后不需要加空格。

before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。

before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。

before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。

before/after：布尔类型，可以设置为true或者false，true表示类型注解中的冒号（:）之前/之后需要加空格。

示例：

"@typescript-eslint/type-annotation-spacing": [
  "error",
  {
    "before": true,
    "after": true,
    "overrides": {
      "colon": {
        "before": false,
        "after": true
      },
      "arrow": {
        "before": true,
        "after": true
      },
      "variable": {
        "before": true,
        "after": false
      },
      "parameter": {
        "before": false,
        "after": true
      },
      "property": {
        "before": true,
        "after": false
      },
      "returnType": {
        "before": true,
        "after": false
      }
    }
  }
]

说明

选项存在优先级，overrides下的配置会覆盖overrides之外的配置：overrides.variable/parameter/property/returnType > overrides.colon/arrow > before/after。

正例

// 默认冒号前无空格，冒号后有空格
export const foo1: string = 'bar';

export declare function foo2(): string;

export class Foo3 {
  public name: string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = () => void;

反例

// 默认冒号前无空格，冒号后有空格
export const foo1 :string = 'bar';

export declare function foo2() :string;

export class Foo3 {
  public name :string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = ()=>void;

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/type-annotation-spacing": "error"
  }
}
```

### Code block 2

```
type Options = {
  before: boolean;
  after: boolean;
  overrides: {
    colon: {
      before: boolean;
      after: boolean;
    };
    arrow: {
      before: boolean;
      after: boolean;
    };
    variable: {
      before: boolean;
      after: boolean;
    };
    parameter: {
      before: boolean;
      after: boolean;
    };
    property: {
      before: boolean;
      after: boolean;
    };
    returnType: {
      before: boolean;
      after: boolean;
    };
  }
}
```

### Code block 3

```
"@typescript-eslint/type-annotation-spacing": [
  "error",
  {
    "before": true,
    "after": true,
    "overrides": {
      "colon": {
        "before": false,
        "after": true
      },
      "arrow": {
        "before": true,
        "after": true
      },
      "variable": {
        "before": true,
        "after": false
      },
      "parameter": {
        "before": false,
        "after": true
      },
      "property": {
        "before": true,
        "after": false
      },
      "returnType": {
        "before": true,
        "after": false
      }
    }
  }
]
```

### Code block 4

```
// 默认冒号前无空格，冒号后有空格
export const foo1: string = 'bar';

export declare function foo2(): string;

export class Foo3 {
  public name: string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = () => void;
```

### Code block 5

```
// 默认冒号前无空格，冒号后有空格
export const foo1 :string = 'bar';

export declare function foo2() :string;

export class Foo3 {
  public name :string = 'hello';
}
// 默认箭头前后都有空格
export declare type Foo4 = ()=>void;
```

### Code block 6

```
plugin:@typescript-eslint/all
```
