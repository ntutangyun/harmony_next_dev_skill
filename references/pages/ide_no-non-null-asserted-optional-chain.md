# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-non-null-asserted-optional-chain_

"@typescript-eslint/no-non-null-asserted-optional-chain": "error"
  }
}
选项

该规则无需配置额外选项。

正例
class CC {
  public bar = 'hello';


  public foo(): void {
    console.info('foo');
  }
}
function getInstance(): CC | undefined {
  return new CC();
}


const instance = getInstance();
console.info(`${instance?.bar}`);
instance?.foo();
反例
class CC {
  public bar: string = 'hello';


  public foo() {
    console.info('foo');
  }
}


function getInstance(): CC | undefined {
  return new CC();
}


const instance = getInstance();
console.info(`${instance?.bar!}`);
instance?.foo()!;
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-namespace
@typescript-eslint/no-non-null-assertion
