# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_adjacent-overload-signatures_

export declare function foo(a: number, b: string, c?: string): void;
反例
export declare function foo(a: string): void;
export declare function bar(): void;
export declare function foo(a: number, b: number): void;
export declare function foo(a: number, b: string, c?: string): void;
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

通用规则@typescript-eslint
@typescript-eslint/array-type
