# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-condition_

// arg is never nullable or empty string, so this is unnecessary
  if (arg) {
  }
}


export function bar(arg: string) {
  // arg can never be nullish, so ?. is unnecessary
  return arg?.length;
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-unnecessary-boolean-literal-compare
@typescript-eslint/no-unnecessary-qualifier
