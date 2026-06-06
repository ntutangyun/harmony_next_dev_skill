# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-explicit-any_

export function greet6(param: readonly string[]): string[] {
  return [...param];
}
反例
export const age1: any = 17;
export const age2: any = [age1];
export const age3: any = [age1];


export function greet1(): any {
  return 'greet';
}


export function greet2(): any[] {
  return ['greet'];
}


export function greet4(): any[][] {
  return [['greet']];
}


export function greet5(param: readonly any[]): any {
  return param[age1];
}


export function greet6(param: readonly any[]): any[] {
  return [...param];
}
规则集
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-empty-interface
@typescript-eslint/no-extraneous-class
