# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-inferrable-types_

export function fn(a: number = num, b: boolean = true): void {
  console.info(`${a}${b}`);
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-implied-eval
@typescript-eslint/no-invalid-this
