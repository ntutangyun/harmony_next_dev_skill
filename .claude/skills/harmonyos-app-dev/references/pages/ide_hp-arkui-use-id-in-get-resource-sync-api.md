# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-id-in-get-resource-sync-api_

"@performance/hp-arkui-use-id-in-get-resource-sync-api": "suggestion",
  }
}
选项

该规则无需配置额外选项。

正例
import { BusinessError } from '@ohos.base';


try {
  // 本地resources中配置的color资源
  this.context.resourceManager.getColorSync($r('app.color.test').id);
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(`getColorSync failed, error code: ${code}, message: ${message}.`);
}
反例
import { BusinessError } from '@ohos.base';


try {
  // 本地resources中配置的color资源
  this.context.resourceManager.getColorSync($r('app.color.test'));
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(`getColorSync failed, error code: ${code}, message: ${message}.`);
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-use-grid-layout-options
@performance/hp-arkui-use-local-var-to-replace-state-var
