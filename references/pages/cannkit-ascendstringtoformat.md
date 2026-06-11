# AscendStringToFormat

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascendstringtoformat_

函数功能

将字符串转化为Format类型值。

使用该接口需要包含type_utils.h头文件。

#include "graph/utils/type_utils.h"

函数原型

static Format AscendStringToFormat(const AscendString &str);

参数说明

参数	输入/输出	说明
str	输入	待转换的Format字符串形式，AscendString类型。

返回值

输入合法时，返回转换后的Format enum值，枚举定义请参考Format；输入不合法时，返回FORMAT_RESERVED，并打印报错信息。

约束说明

无

调用示例

ge::AscendString format_str("NHWC");
auto format = AscendStringToFormat(format_str); // 1

## Code blocks

### Code block 1

```
#include "graph/utils/type_utils.h"
```

### Code block 2

```
static Format AscendStringToFormat(const AscendString &str);
```

### Code block 3

```
ge::AscendString format_str("NHWC");
auto format = AscendStringToFormat(format_str); // 1
```
