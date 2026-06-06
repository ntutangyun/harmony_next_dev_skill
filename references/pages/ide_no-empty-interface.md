# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-empty-interface_

// in this case the interface can be used as a replacement of an intersection type.
export interface Baz extends Foo, Bar {}
反例
// an empty interface
interface Foo {}


// an interface with only one supertype (Bar === Foo)
export interface Bar extends Foo {}


// an interface with an empty list of supertypes
export interface Baz {}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-empty-function
@typescript-eslint/no-explicit-any
