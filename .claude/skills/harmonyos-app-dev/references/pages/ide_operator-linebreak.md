# @hw

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_operator-linebreak_

export function test(n1: number, n2: number, n3: number): void {
  if (n1 > n2
    // '||' should be placed at the end of the line.
    || n1 < n3) {
    console.info('hello');
  }
}
规则集
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@hw-stylistic/one-var-declaration-per-line
@hw-stylistic/quotes
