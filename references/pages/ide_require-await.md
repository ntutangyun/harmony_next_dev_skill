# @typescript-eslint/require-await

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_require-await_

异步函数必须包含“await”。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/require-await": "error"
  }
}

选项

该规则无需配置额外选项。

正例

async function doSomething(): Promise<void> {
  return Promise.resolve();
}

export async function foo() {
  await doSomething();
}

export function baz() {
  doSomething().catch(() => {
    console.info('error');
  });
}

反例

async function doSomething(): Promise<void> {
  return Promise.resolve();
}

export async function foo() {
  doSomething();
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
    "@typescript-eslint/require-await": "error"
  }
}
```

### Code block 2

```
async function doSomething(): Promise<void> {
  return Promise.resolve();
}

export async function foo() {
  await doSomething();
}

export function baz() {
  doSomething().catch(() => {
    console.info('error');
  });
}
```

### Code block 3

```
async function doSomething(): Promise<void> {
  return Promise.resolve();
}

export async function foo() {
  doSomething();
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
