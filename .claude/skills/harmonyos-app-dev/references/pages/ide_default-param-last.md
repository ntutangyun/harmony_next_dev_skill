# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_default-param-last_

export function f4(a: number, b?: number, c = defaultValue) {
  return b !== undefined ? a + b + c : a + c;
}
export function f5(a: number, b = defaultValue, c?: number) {
  return c !== undefined ? a + c : a + b;
}
反例
const defaultValue = 0;
export function f2(b = defaultValue, a: number) {
  return a + b;
}
export function f3(b?: number, a: number) {
  return b !== undefined ? a + b : a;
}
export function f4(b?: number, a: number, c = defaultValue) {
  return b !== undefined ? a + b + c : a + c;
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/consistent-type-imports
@typescript-eslint/dot-notation
