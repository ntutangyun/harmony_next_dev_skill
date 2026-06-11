# TensorDescInfo

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordescinfo_

struct TensorDescInfo {
    Format format_ = FORMAT_RESERVED;        /* tbe op注册支持的格式 */
    DataType dataType_ = DT_UNDEFINED;       /* tbe op注册支持的数据类型 */
    };

Format为枚举类型，定义请参考Format。

DataType为枚举类型，定义请参考DataType。

## Code blocks

### Code block 1

```
struct TensorDescInfo {
    Format format_ = FORMAT_RESERVED;        /* tbe op注册支持的格式 */
    DataType dataType_ = DT_UNDEFINED;       /* tbe op注册支持的数据类型 */
    };
```
