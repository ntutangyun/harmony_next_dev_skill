# @hw

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-file-naming-convention_

该规则默认检查代码文件和资源文件的命名风格，也可以接受一个对象作为参数{selector: string}，来指定只检查代码文件或者资源文件。"selector"支持配置为"resources"或者"code"。

示例：

1.以下配置只检查代码文件命名风格：

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/file-naming-convention": ["error", { "selector": "code" }]
  }
}

2.以下配置只检查资源文件命名风格：

// code-linter.json5
{
  "rules": {
    "@hw-stylistic/file-naming-convention": ["error", { "selector": "resources" }]
  }
}
正例
// 代码文件名：Index.ets、EntryAbility.ets、index.js
// 资源文件名：color.json、background.png、main_pages.json
反例
// 代码文件名：index.ets、ability.ets、Index.js
// 资源文件名：String.json、BackGround.png
规则集
"plugin:@hw-stylistic/recommended"
"plugin:@hw-stylistic/all"

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@hw-stylistic/curly
@hw-stylistic/indent
