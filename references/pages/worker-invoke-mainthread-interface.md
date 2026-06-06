# Worker同步调用宿主线程的接口

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-invoke-mainthread-interface_

const workerInstance: worker.ThreadWorker = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
               // 在Worker上注册需要调用的对象
               workerInstance.registerGlobalCallObject('testObj', TestObj.testObj);
               workerInstance.onmessage = (e: MessageEvents): void => {
                 // 接收Worker子线程的结果
                 console.info('mainThread: ' + e.data);
                 // 销毁Worker
                 workerInstance.terminate();
               }
               workerInstance.postMessage('start');
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
WorkerCallGlobalUsage.ets

然后，在Worker中通过callGlobalCallObjectMethod接口可以调用宿主线程中的getMessage()方法。

import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';


const workerPort: ThreadWorkerGlobalScope = worker.workerPort;


workerPort.onmessage = async (e: MessageEvents) => {
  if (e.data === 'start') {
    try {
      // 调用方法
      let res: string = workerPort.callGlobalCallObjectMethod('testObj', 'getMessage', 0) as string;
      if (res === 'this is a message from TestObj') {
        workerPort.postMessage('run function success.');
      }
    } catch (error) {
      // 异常处理
      console.error('worker: error code is ' + error.code + ' error message is ' + error.message);
    }
  }


  // ...
}
Worker.ets
Worker和宿主线程的即时消息通信
多级Worker间高性能消息通信
