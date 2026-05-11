# @typescript

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_promise-function-async_

export const arrowFunctionReturnsPromise = async () => Promise.resolve('value');


export async function functionReturnsPromise() {
  return Promise.resolve('value');
}


// An explicit return type that is not Promise means this function cannot be made async, so it is ignored by the rule
export function functionReturnsUnionWithPromiseExplicitly(
  p: boolean
): string | Promise<string> {
  return p ? 'value' : Promise.resolve('value');
}


export async function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
  return p ? 'value' : Promise.resolve('value');
}
反例
export const arrowFunctionReturnsPromise = () => Promise.resolve('value');


export function functionReturnsPromise() {
  return Promise.resolve('value');
}


export function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
  return p ? 'value' : Promise.resolve('value');
}
规则集
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@typescript-eslint/prefer-ts-expect-error
@typescript-eslint/quotes
