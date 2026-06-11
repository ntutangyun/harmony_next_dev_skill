# @deprecated

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arktsdoc-deprecated_

@deprecated标签指明一个标识在代码中已经被弃用。

语法

@deprecated [<some text>]

示例

可以单独使用@deprecated标记，也可以包含一些描述有关deprecated的详细信息的文本。

例：说明自版本2.0以来旧函数已被弃用

/**
 * @deprecated since version 2.0
 */
export function old() {}

## Code blocks

### Code block 1

```
/**
 * @deprecated since version 2.0
 */
export function old() {}
```
