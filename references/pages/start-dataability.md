# 启动DataAbility

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-dataability_

启动DataAbility会获取一个工具接口类对象（DataAbilityHelper）。启动DataAbility的示例代码如下：

import featureAbility from '@ohos.ability.featureAbility';
import ability from '@ohos.ability.ability';


let uri: string = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(uri);
创建DataAbility
访问DataAbility
