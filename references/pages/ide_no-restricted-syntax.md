# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-restricted-syntax_

"selector": "CallExpression[callee.name='setTimeout'][arguments.length!=2]",
             "message": "setTimeout must always be invoked with two arguments."
         }
     ]
  }
}
选项

详情请参考@typescript-eslint/no-restricted-syntax选项。

正例
/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export function doSomething() {
  console.info('doSomething');
}
反例
/* eslint no-restricted-syntax: ["error", "ClassDeclaration"] */
export class CC {
  public name: string;


  public constructor(name: string) {
    this.name = name;
  }
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-require-imports
@typescript-eslint/no-shadow
