# ASON解析与生成

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ason-parsing-generation_

ASON工具与JS提供的JSON工具类似，JSON用于进行JS对象的序列化（stringify）、反序列化（parse）。ASON则提供了Sendable对象的序列化、反序列化能力。使用ASON.stringify方法可将对象转换为字符串，使用ASON.parse方法可将字符串转换为Sendable对象，从而实现对象在并发任务间的高性能引用传递。

ASON.stringify方法还支持将Map和Set对象转换为字符串，可转换的Map和Set类型包括：Map、Set、collections.Map、collections.Set、HashMap、HashSet。

说明

ASON.parse默认生成的对象为Sendable对象，布局不可变，不支持增删属性。如果返回的对象需要支持增删属性，可以指定返回类型为collections.Map对象。

使用示例

使用ASON提供的接口，对Sendable对象进行序列化、反序列化。

import { ArkTSUtils, collections } from '@kit.ArkTS';


ArkTSUtils.ASON.parse("{}")
ArkTSUtils.ASON.stringify(new collections.Array(1, 2, 3))


let options2: ArkTSUtils.ASON.ParseOptions = {
    bigIntMode: ArkTSUtils.ASON.BigIntMode.PARSE_AS_BIGINT,
    parseReturnType: ArkTSUtils.ASON.ParseReturnType.MAP,
}
let jsonText = '{"largeNumber":112233445566778899}';
let map = ArkTSUtils.ASON.parse(jsonText, undefined, options2);
// 执行结果为：{"largeNumber":112233445566778899}
console.info(ArkTSUtils.ASON.stringify(map));
AsonParsingGeneration.ets
异步等待
共享容器
