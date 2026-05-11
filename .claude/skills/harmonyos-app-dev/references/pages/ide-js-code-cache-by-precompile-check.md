# @performance/js

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-js-code-cache-by-precompile-check_

"@performance/js-code-cache-by-precompile-check": "suggestion",
  }
}
选项

该规则无需配置额外选项。

正例
import { webview } from '@kit.ArkWeb';
interface Config {
  url: string,
  localPath: string,
  options: webview.CacheOptions
}
@Entry
@Component
struct JsCodeCacheByPrecompileCheckNoReport {
  controller: webview.WebviewController = new webview.WebviewController();
  configs: Array<Config> = [
    {
      url: 'https://www.example.com/example.js',
      localPath: 'example.js',
      options: {
        responseHeaders: [
          { headerKey: 'E-Tag', headerValue: 'xxx' },
          { headerKey: 'Last-Modified', headerValue: 'Web, 21 Mar 2024 10:38:41 GMT' }
        ]
      }
    }
  ]
  build() {
    Column() {
      Web({ src: 'https://www.example.com/a.html', controller: this.controller })
        .onControllerAttached(async () => {
          for (const config of this.configs) {
            let content = getContext().resourceManager.getRawFileContentSync(config.localPath);
            try {
              this.controller.precompileJavaScript(config.url, content, config.options)
                .then((errCode: number) => {
                  console.log('precompile successfully!' );
                }).catch((errCode: number) => {
                console.error('precompile failed.' + errCode);
              })
            } catch (err) {
              console.error('precompile failed!.' + err.code + err.message);
            }
          }
        })
    }
  }
}
反例
import { webview } from '@kit.ArkWeb';
import { hiTraceMeter } from '@kit.PerformanceAnalysisKit';
@Entry
@Component
struct JsCodeCacheByPrecompileCheckReport {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Button('加载页面')
        .onClick(() => {
          hiTraceMeter.startTrace('unPrecompileJavaScript', 1);
          this.controller.loadUrl('https://www.example.com/b.html');
        })
      // warning line
      Web({ src: 'https://www.example.com/a.html', controller: this.controller })
        .fileAccess(true)
        .onPageBegin((event) => {
          console.log(`load page begin: ${event?.url}`);
        })
        .onPageEnd((event) => {
          hiTraceMeter.finishTrace('unPrecompileJavaScript', 1);
          console.log(`load page end: ${event?.url}`);
        })
    }
  }
}
规则集
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/js-code-cache-by-interception-check
@performance/lazyforeach-args-check（已下线）
