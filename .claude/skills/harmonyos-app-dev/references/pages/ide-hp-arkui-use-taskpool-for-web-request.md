# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-use-taskpool-for-web-request_

"@performance/hp-arkui-use-taskpool-for-web-request": "warn",
  }
}
选项

该规则无需配置额外选项。

正例
import { http } from '@kit.NetworkKit';
import { BusinessError } from '@ohos.base';
import taskpool from '@ohos.taskpool';


@Concurrent
function processRespTask(err: BusinessError, data: http.HttpResponse) {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies);
  } else {
    console.info('error:' + JSON.stringify(err));
  }
}


let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE_URL", async (err: Error, data: http.HttpResponse) => {
  let task = new taskpool.Task(processRespTask, data);
  await taskpool.execute(task);
});
反例
import { http } from '@kit.NetworkKit';


let httpRequest = http.createHttp();
httpRequest.request("EXAMPLE_URL", (err: Error, data: http.HttpResponse) => {
  if (!err) {
    console.info('Result:' + data.result);
    console.info('code:' + data.responseCode);
    console.info('type:' + JSON.stringify(data.resultType));
    console.info('header:' + JSON.stringify(data.header));
    console.info('cookies:' + data.cookies); 
  } else {
    console.info('error:' + JSON.stringify(err));
  }
});
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/hp-arkui-use-scale-to-replace-attr-animateto
@performance/hp-arkui-use-transition-to-replace-animateto
