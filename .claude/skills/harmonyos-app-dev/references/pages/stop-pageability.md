# 停止PageAbility

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stop-pageability_

terminateSelfWithResult(parameter: AbilityResult)	设置该PageAbility停止时返回给调用者的结果及数据并停止Ability。

如下示例展示了停止Ability的方法。

import featureAbility from '@ohos.ability.featureAbility';
import hilog from '@ohos.hilog';


const TAG: string = 'PagePageAbilityFirst';
const domain: number = 0xFF00;
// ...
(async (): Promise<void> => {
  try {
    hilog.info(domain, TAG, 'Begin to terminateSelf');
    await featureAbility.terminateSelf();
    hilog.info(domain, TAG, 'terminateSelf succeed');
  } catch (error) {
    hilog.error(domain, TAG, 'terminateSelf failed with ' + error);
  }
})()
// ...
启动本地PageAbility
启动指定页面
