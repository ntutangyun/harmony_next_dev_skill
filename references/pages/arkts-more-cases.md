# 适配指导案例

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-more-cases_

用class/interface为object literal标注类型，要求使用identifier作为object literal的key
使用Record类型为object literal标注类型，要求使用字符串作为object literal的key
函数参数类型包含index signature
函数实参使用了object literal
class/interface 中包含方法
export default对象
通过导入namespace获取类型
object literal传参给Object类型
arkts-no-obj-literals-as-types
arkts-no-noninferrable-arr-literals
arkts-no-method-reassignment
arkts-no-polymorphic-unops
arkts-no-type-query
arkts-no-in
使用Object.keys判断属性是否存在
arkts-no-destruct-assignment
arkts-no-types-in-catch
arkts-no-for-in
arkts-no-mapped-types
arkts-limited-throw
arkts-no-standalone-this
函数内使用this
class的静态方法内使用this
arkts-no-spread
arkts-no-ctor-signatures-funcs
arkts-no-globalthis
arkts-no-func-apply-bind-call
使用标准库中接口
bind定义方法
使用apply
arkts-limited-stdlib
Object.fromEntries()
严格模式检查(StrictModeError)
strictPropertyInitialization
Type *** | null is not assignable to type ***
严格属性初始化检查
严格函数类型检查
严格空值检查
函数返回类型不匹配
Type '*** | null' is not assignable to type '***'
Cannot invoke an object which is possibly 'undefined'
Variable '***' is used before being assigned
Function lacks ending return statement and return type does not include 'undefined'.
arkts-strict-typing-required
Importing ArkTS files to JS and TS files is not allowed
arkts-no-tsdeps
arkts-no-special-imports
arkts-no-classes-as-obj
使用class构造实例
访问静态属性
arkts-no-side-effects-imports
arkts-no-func-props
arkts-limited-esobj
拷贝
浅拷贝
深拷贝
展开章节

本文通过具体应用场景中的案例，提供在ArkTS语法规则下将TS代码适配成ArkTS代码的建议。各章以ArkTS语法规则的英文名称命名，每个案例展示适配前的TS代码和适配后的ArkTS代码。

arkts-identifiers-as-prop-names

当属性名是有效的标识符（即不包含特殊字符、空格等，并且不以数字开头），可以直接使用而无需引号。

应用代码

interface W {
  bundleName: string
  action: string
  entities: string[]
}


let wantInfo: W = {
  'bundleName': 'com.huawei.hmos.browser',
  'action': 'ohos.want.action.viewData',
  'entities': ['entity.system.browsable']
}

建议改法

interface W {
  bundleName: string
  action: string
  entities: string[]
}


let wantInfo: W = {
  bundleName: 'com.huawei.hmos.browser',
  action: 'ohos.want.action.viewData',
  entities: ['entity.system.browsable']
}
arkts-no-any-unknown
按照业务逻辑，将代码中的any, unknown改为具体的类型
function printObj(obj: any) {
  console.info(obj);
}


printObj('abc'); // abc

建议改法

function printObj(obj: string) {
  console.info(obj);
  // ...
}
// ...
          printObj('abc'); // abc
从TypeScript到ArkTS的适配规则
ArkTS高性能编程实践
