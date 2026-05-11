# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_prefer-readonly_

// Private parameter properties can also be marked as readonly
  private neverModifiedParameter: string;


  public constructor(
    onlyModifiedInConstructor: number,
    // Private parameter properties can also be marked as readonly
    neverModifiedParameter: string,
  ) {
    this.neverModifiedParameter = neverModifiedParameter;
    this.onlyModifiedInConstructor = onlyModifiedInConstructor;
  }
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/prefer-optional-chain
@typescript-eslint/prefer-readonly-parameter-types
