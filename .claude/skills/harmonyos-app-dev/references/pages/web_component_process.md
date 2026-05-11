# ArkWeb进程

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web_component_process_

移动设备默认为单进程渲染，而2in1设备则默认采用多进程渲染。通过调用getRenderProcessMode可查询当前的渲染子进程模式，其中枚举值0表示单进程模式，枚举值1对应多进程模式。若setRenderProcessMode接口传入的值不在RenderProcessMode枚举值范围内，系统将自动采用多进程渲染模式作为默认设置。

import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('getRenderProcessMode')
        .onClick(() => {
          let mode = webview.WebviewController.getRenderProcessMode();
          console.info('getRenderProcessMode: ' + mode);
        })
      Button('setRenderProcessMode')
        .onClick(() => {
          try {
            webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as     BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
SetRenderProcessMode.ets

可通过terminateRenderProcess来主动关闭渲染进程。若渲染进程尚未启动或已销毁，此操作将不会产生任何影响。此外，销毁渲染进程将同时影响所有与之关联的其他实例。

import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Button('terminateRenderProcess')
        .onClick(() => {
          let result = this.controller.terminateRenderProcess();
          console.info('terminateRenderProcess result: ' + result);
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
TerminateRenderProcess.ets

可通过onRenderExited来监听渲染进程的退出事件，从而获知退出的具体原因（如内存OOM、crash或正常退出等）。由于多个Web组件可能共用同一个渲染进程，因此，每当渲染进程退出时，每个受此影响的Web组件均会触发相应的回调。

import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Web({ src: 'chrome://crash/', controller: this.controller })
        .onRenderExited((event) => {
          if (event) {
            console.info('reason:' + event.renderExitReason);
          }
        })
    }
  }
}
OnRenderExited.ets

可通过onRenderProcessNotResponding、onRenderProcessResponding来监听渲染进程的无响应状态。

当Web组件无法处理输入事件，或未能在预期时间内导航至新URL时，系统会判定网页进程为无响应状态，并触发onRenderProcessNotResponding回调。在网页进程持续无响应期间，该回调可能反复触发，直至进程恢复至正常运行状态，此时将触发onRenderProcessResponding回调。

import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRenderProcessNotResponding((data) => {
          console.info('onRenderProcessNotResponding: [jsStack]= ' + data.jsStack +
            ', [process]=' + data.pid + ', [reason]=' + data.reason);
        })
    }
  }
}
OnRenderProcessNotResponding.ets
import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRenderProcessResponding(() => {
          console.info('onRenderProcessResponding again');
        })
    }
  }
}
OnRenderProcessResponding.ets

Web组件创建参数涵盖了多进程模型的运用。其中，sharedRenderProcessToken标识了当前Web组件所指定的共享渲染进程的token。在多渲染进程模式下，拥有相同token的Web组件将优先尝试重用与该token绑定的渲染进程。token与渲染进程的绑定关系，在渲染进程的初始化阶段形成。一旦渲染进程不再关联任何Web组件，它与token的绑定关系将被解除。

import { webview } from '@kit.ArkWeb';


@Entry
@Component
struct WebComponent {
  controller1: webview.WebviewController = new webview.WebviewController();
  controller2: webview.WebviewController = new webview.WebviewController();


  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller1, sharedRenderProcessToken: '111' })
      Web({ src: 'www.w3.org', controller: this.controller2, sharedRenderProcessToken: '111' })
    }
  }
}
WebComponentCreat.ets
ArkWeb简介
Web组件的生命周期
