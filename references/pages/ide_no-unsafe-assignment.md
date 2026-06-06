# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-assignment_

export const a2: Map<string, string> = new Map<string, string>();
export const a3: Set<string[]> = new Set<string[]>();
export const a4: Set<Set<Set<string>>> = new Set<Set<Set<string>>>();
反例
let [x] = ['1'];
[x] = ['1'] as [any];
[x] = '1' as any;
console.info([x].toString());


// generic position examples
export const a1: Set<string> = new Set<any>();
export const a2: Map<string, string> = new Map<any, string>();
export const a3: Set<string[]> = new Set<any[]>();
export const a4: Set<Set<Set<string>>> = new Set<Set<Set<any>>>();
规则集
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-unsafe-argument
@typescript-eslint/no-unsafe-call
