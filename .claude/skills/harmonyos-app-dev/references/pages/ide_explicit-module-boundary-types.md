# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_explicit-module-boundary-types_

"@typescript-eslint/explicit-module-boundary-types": "error"
  }
}
选项

详情请参考@typescript-eslint/explicit-module-boundary-types选项。

正例
// A function with no return value (void)
export function test1(): void {
  return;
}


// A return value of type string
export const arrowFn1 = (): string => 'test';


// All arguments should be typed
export const arrowFn2 = (arg: string): string => `test ${arg}`;


export class Test {
  // A class method with no return value (void)
  public method(): void {
    return;
  }
}


// The function does not apply because it is not an exported function.
function test2() {
  return;
}


test2();
反例
// Should indicate that no value is returned (void)
export function test() {
  return;
}


// Should indicate that a string is returned
export const arrowFn1 = () => 'test';


// All arguments should be typed
export const arrowFn2 = (arg): string => `test ${arg}`;
export const arrowFn3 = (arg: any): string => `test ${arg}`;


export class Test {
  // Should indicate that no value is returned (void)
  public method() {
    return;
  }
}
规则集
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/explicit-member-accessibility
@typescript-eslint/func-call-spacing
