# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_consistent-indexed-object-style_

"@typescript-eslint/consistent-indexed-object-style": "error"
  }
}
选项

详情请参考@typescript-eslint/consistent-indexed-object-style选项。

正例
// 默认推荐使用Record 类型
export type Foo = Record<string, unknown>;
反例
export interface Foo1 {
  // 默认推荐使用Record 类型
  [key: string]: unknown;
}


export type Foo2 = {
  // 默认推荐使用Record 类型
  [key: string]: unknown;
};
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/comma-spacing
@typescript-eslint/consistent-type-assertions
