# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-parameter-properties_

"@typescript-eslint/no-parameter-properties": ["error", {"allows": ["readonly"]}]
  }
}
正例
export class Foo {
  public name: string;


  public constructor(name: string) {
    this.name = name;
  }
}
反例
export class Foo {
  // 默认配置下，参数不允许使用readonly
  public constructor(public readonly name: string) {}
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-non-null-assertion
@typescript-eslint/no-redeclare
