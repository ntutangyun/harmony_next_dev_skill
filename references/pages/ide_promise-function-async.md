# @typescript-eslint/promise-function-async

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_promise-function-async_

要求任何返回Promise的函数或方法标记为async。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/promise-function-async": "error"
  }
}

选项

详情请参考@typescript-eslint/promise-function-async选项。

正例

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

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/promise-function-async": "error"
  }
}
```

### Code block 2

```
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
```

### Code block 3

```
export const arrowFunctionReturnsPromise = () => Promise.resolve('value');

export function functionReturnsPromise() {
  return Promise.resolve('value');
}

export function functionReturnsUnionWithPromiseImplicitly(p: boolean) {
  return p ? 'value' : Promise.resolve('value');
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
