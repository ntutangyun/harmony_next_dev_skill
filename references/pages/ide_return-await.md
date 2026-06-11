# @typescript-eslint/return-await

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_return-await_

要求异步函数返回“await”。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/return-await": "error"
  }
}

选项

详情请参考@typescript-eslint/return-await选项。

正例

export async function validInTryCatch1() {
  try {
    return await Promise.resolve('try');
  } catch (e) {
    return await Promise.resolve('catch');
  }
}

反例

export async function validInTryCatch1() {
  try {
    return Promise.resolve('try');
  } catch (e) {
    return Promise.resolve('catch');
  }
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
    "@typescript-eslint/return-await": "error"
  }
}
```

### Code block 2

```
export async function validInTryCatch1() {
  try {
    return await Promise.resolve('try');
  } catch (e) {
    return await Promise.resolve('catch');
  }
}
```

### Code block 3

```
export async function validInTryCatch1() {
  try {
    return Promise.resolve('try');
  } catch (e) {
    return Promise.resolve('catch');
  }
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
