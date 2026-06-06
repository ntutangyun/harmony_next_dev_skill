# @correctness/redundant

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-redundant-dependency-check_

1. 在 entry 下的oh-package.json5文件中配置了a、b、c三个依赖，entry/src/main/ets中的文件中全部 import 导入。

2. 在工程级的oh-package.json5文件中配置了a、b、c三个依赖，整个工程全部 import 导入。

反例

1. 在 entry 下的oh-package.json5文件中配置了a、b、c三个依赖，但entry/src/main/ets中的文件中只 import 导入了a,b两个依赖。

2. 在工程级的oh-package.json5文件中配置了a、b、c三个依赖，但整个工程只 import 导入了a,b两个依赖。

规则集
plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@correctness/multimedia-use-stride-in-image-receiver
@correctness/v1-nested-object-property-change-format-check
