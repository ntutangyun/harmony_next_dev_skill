# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-dynamic-delete_

// Can be replaced with the constant equivalents, such as container.aaa
delete container['aaa'];
// 'Infinity' may be a string constant
delete container['Infinity'];


// Dynamic, difficult-to-reason-about lookups
const name = 'name';
delete container[name];
delete container[name.toUpperCase()];
规则集
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-duplicate-imports
@typescript-eslint/no-empty-function
