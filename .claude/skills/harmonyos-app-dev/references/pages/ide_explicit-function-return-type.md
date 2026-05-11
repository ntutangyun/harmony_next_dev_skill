# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-function-return-type_

"@typescript-eslint/explicit-function-return-type": ["error", { "allowArkTS": true }]
  }
}

其余配置详情请参考@typescript-eslint/explicit-function-return-type选项。

正例
// No return value should be expected (void)
function test(): void {
  return;
}


// A return value of type number
const fn = function (): number {
  return Number.MAX_VALUE;
};


// A return value of type string
const arrowFn = (): string => 'test';


class Test {
  // No return value should be expected (void)
  public method(): void {
    return;
  }
}


export { test, fn, arrowFn, Test };
反例
// Should indicate that no value is returned (void)
function test() {
  return;
}


// Should indicate that a number is returned
const fn = function () {
  return Number.MAX_VALUE;
};


// Should indicate that a string is returned
const arrowFn = () => 'test';


class Test {
  // Should indicate that no value is returned (void)
  public method() {
    return;
  }
}


export { test, fn, arrowFn, Test };
规则集
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/dot-notation
@typescript-eslint/explicit-member-accessibility
