# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unnecessary-boolean-literal-compare_

"@typescript-eslint/no-unnecessary-boolean-literal-compare": "error"
  }
}
选项

详情请参考@typescript-eslint/no-unnecessary-boolean-literal-compare选项。

正例
declare const someCondition: boolean;
if (someCondition) {
}


declare const someObjectBoolean: boolean | Record<string, object>;
if (someObjectBoolean === true) {
}


declare const someStringBoolean: boolean | string;
if (someStringBoolean === true) {
}
反例
declare const someCondition: boolean;
// 禁止将布尔变量和布尔字面量直接比较，直接使用someCondition判断即可
if (someCondition === true) {
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/no-type-alias
@typescript-eslint/no-unnecessary-condition
