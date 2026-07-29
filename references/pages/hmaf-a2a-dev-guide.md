# 通过AgentAbilityExtension实现智能体间A2A协议通信

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hmaf-a2a-dev-guide_

A2A（Agent to Agent）协议用于智能体之间的通信。A2A服务端负责接收客户端请求、触发智能体执行任务、更新任务状态和返回执行结果。

通过Agent Framework Kit，开发者可以在ArkTS应用中构建支持A2A协议的Agent服务端，实现以下能力：

接收客户端的请求消息

触发智能体执行业务逻辑

更新任务状态和返回执行结果

基本概念

Agent Card（智能体卡片）：一种JSON元数据文档，用于描述智能体的身份、能力、端点地址、技能和认证要求。客户端通过解析智能体卡片来发现智能体并了解如何安全有效地与其交互。

Task（任务）：由智能体发起的具有唯一标识和明确定义生命周期的有状态工作单元。用于跟踪长时间运行的操作和支持多轮交互与协作。

Message（消息）：客户端与智能体之间一次通信的单元，包含内容和角色（"user"或"agent"）。用于传递指令、上下文、问题、答案或状态更新。

Part（消息部件）：消息和产物中使用的基础内容容器。一个部件可以包含以下内容之一：文本内容、文件引用（URL或内联字节）或结构化数据。

Artifact（产物）：智能体在任务处理过程中生成的有形成果或具体结果（如文档、图片或结构化数据）。与通用消息不同，产物是实际的交付物，具有唯一的产物ID和名称。

Context（上下文）：由服务端生成的标识符，用于逻辑上关联多个相关的任务对象，为一系列交互提供上下文。

TaskState（任务状态）：任务可能处于的状态，包括已提交、工作中、需要用户输入、已完成、已取消、已失败、已拒绝、需要认证等。

业务功能介绍

A2A协议支持智能体之间的高效通信，其核心业务功能包括：

智能体发现：通过Agent Card元数据文档，客户端可以发现智能体并了解其能力、端点地址和认证要求。

任务管理：支持创建和管理具有明确生命周期的任务，支持长时间运行操作的跟踪和多轮交互。

消息传递：支持客户端与智能体之间的单轮通信，传递指令、上下文、问题、答案或状态更新。

产物生成：智能体在任务处理过程中可以生成有形的交付物（如文档、图片或结构化数据）。

状态更新：支持任务状态的全程跟踪，包括已提交、工作中、需要用户输入、已完成、已取消、已失败、已拒绝、需要认证等状态。

业务流程

客户端连接：客户端通过Agent Card发现智能体后，与A2A Server建立连接。

发送请求：客户端构造请求消息并发送给服务端，请求触发智能体执行任务。

处理任务：服务端接收请求后，触发智能体执行业务逻辑，处理任务并生成产物。

返回结果：服务端更新任务状态和返回执行结果，客户端收到响应后完成本次交互。

接口说明

本模块提供A2A协议的服务端API，具体接口说明请参见A2A Server模块API文档。

主要接口包括：

接口名	说明
createA2AServer	创建并获取Server实例，用于处理A2A协议通信。
Server	服务器实例接口，负责处理智能体通信和任务生命周期管理。
RequestContext	请求上下文接口，提供传入请求的上下文信息。
OnDataCallback	A2A Server收到客户端请求后，触发智能体执行的事件回调函数类型。
Message	A2A通信中的消息单元。
Task	A2A任务，包含任务状态、产物和历史消息。

开发步骤

[h2]导入所需模块

import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want, AgentExtensionAbility } from '@kit.AbilityKit';
import { RequestContext, createA2AServer, Server, AgentOperation, TaskState, Role } from '@kit.AgentFrameworkKit';

[h2]业务功能实现步骤

推荐在服务端继承AgentExtensionAbility，以实现跨App进程通信的能力。AgentExtensionAbility提供了基于IPC的请求处理回调接口。

参考以下步骤，实现每一个AgentExtensionAbility中的方法。

创建OnDataCallback，定义Agent的业务处理逻辑。

const TAG = "=====A2AServer===="
export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  private server: Server | null = null;

  // OnDataCallback函数
  private agentOnData(method: AgentOperation, context: RequestContext) {
    // 从结构化的上下文参数context中，获取AgentID等信息
    const agentId: string = context.getAgentId();
    if (!agentId) {
        hilog.error(0x0000, TAG, "Agent ID not found in request context");
        return;
    }
    const taskId: string = context.getTaskId();
    switch (method) {
      case AgentOperation.EXECUTE:
        // 使用server.updateStatus，更新任务执行状态
        this.server?.updateStatus(taskId, {
            state: TaskState.WORKING,
            message: {
                messageId: "msg1",
                role: Role.AGENT,
                parts: [{
                    mediaType: "text/plain",
                    text: "Starting work on your request..."
                }]
            }
        });

        // 等待Agent生成产物
        this.server?.addArtifact(taskId, {
            artifactId: "result-artifact",
            parts: [{
                mediaType: "text/plain",
                text: '{"action": "completed", "result": "Task finished successfully"}'
            }]
        });

        // 通知任务完成
        this.server?.updateStatus(taskId, {
            state: TaskState.COMPLETED,
            message: {
                messageId: "msg3",
                role: Role.AGENT,
                parts: [{
                    mediaType: "text/plain",
                    text: "Task completed successfully!"
                }]
            }
        });
        break;
      case AgentOperation.CANCEL:
        // 根据AgentId，通知Agent处理取消任务的请求
        hilog.info(0x0000, TAG, "Cancel called");
        break;
      case AgentOperation.CLEAR_CONTEXT:
          // 根据AgentId，通知Agent清除上下文
        hilog.info(0x0000, TAG, `Clear context called, client session id: ${context.getClientSessionId()}`);
        break;
      case AgentOperation.PERCEPTION_SUGGEST:
        hilog.info(0x0000, TAG, `Perception suggest called, metadata: ${JSON.stringify(context.getMetadata(), null, 2)}`);
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: "onChipsMsg1",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "On chips task completed successfully!"
            }]
          }
        });
      default:
        break;
    }
  }
}

实现onCreate方法，确保在首次收到请求时调用createA2AServer创建A2A Server对象。

async onCreate(want: Want) {
   try {
     const card = this.context.agentCard;
     this.server = createA2AServer(card, this.agentOnData, want=want);
   } catch (error) {
     hilog.error(0x0000, TAG, `Failed to create server: ${error}`);
   }
}

实现onConnect，客户端建连时触发，启动服务端。

onConnect(want: Want, proxy: common.AgentHostProxy) {
  // 客户端连接时触发的回调
  this.server?.start();
}

接收客户端请求时触发onData，需要调用server.onMessage传递请求体。

async onData(proxy: common.AgentHostProxy, data: string) {
  // 处理请求的回调函数
  this.server?.onMessage(data, (response: string) => {
     proxy.sendData(response);
  });
}

客户端断开连接时，在onDisconnect中关闭服务端。

onDisconnect(want: Want, proxy: common.AgentHostProxy) {
  // 客户端断开连接时触发的回调
  this.server?.stop();
}

服务对象销毁时触发onDestroy。

onDestroy() {
  // 清理资源
  this.server?.stop();
}

[h2]完整示例

import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want, AgentExtensionAbility } from '@kit.AbilityKit';
import { RequestContext, createA2AServer, Server, AgentOperation, TaskState, Role } from '@kit.AgentFrameworkKit';

const TAG = "=====A2AServer===="
export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  private server: Server | null = null;

  // OnDataCallback函数
  private agentOnData(method: AgentOperation, context: RequestContext) {
    // 从结构化的上下文参数context中，获取AgentID等信息
    const agentId: string = context.getAgentId();
    if (!agentId) {
      hilog.error(0x0000, TAG, "Agent ID not found in request context");
      return;
    }
    const taskId: string = context.getTaskId();
    switch (method) {
      case AgentOperation.EXECUTE:
        // 使用server.updateStatus，更新任务执行状态
        this.server?.updateStatus(taskId, {
          state: TaskState.WORKING,
          message: {
            messageId: "msg1",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "Starting work on your request..."
            }]
          }
        });

        // 等待Agent生成产物
        this.server?.addArtifact(taskId, {
          artifactId: "result-artifact",
          parts: [{
            mediaType: "text/plain",
            text: '{"action": "completed", "result": "Task finished successfully"}'
          }]
        });

        // 通知任务完成
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: "msg3",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "Task completed successfully!"
            }]
          }
        });
        break;
      case AgentOperation.CANCEL:
        // 根据AgentId，通知Agent处理取消任务的请求
        hilog.info(0x0000, TAG, "Cancel called");
        break;
      case AgentOperation.CLEAR_CONTEXT:
        // 根据AgentId，通知Agent清除上下文
        hilog.info(0x0000, TAG, `Clear context called, client session id: ${context.getClientSessionId()}`);
        break;
      case AgentOperation.PERCEPTION_SUGGEST:
        hilog.info(0x0000, TAG, `Perception suggest called, metadata: ${JSON.stringify(context.getMetadata(), null, 2)}`);
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: "onChipsMsg1",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "On chips task completed successfully!"
            }]
          }
        });
      default:
        break;
    }
  }

  async onCreate(want: Want) {
    try {
      const card = this.context.agentCard;
      this.server = createA2AServer(card, this.agentOnData, want=want);
    } catch (error) {
      hilog.error(0x0000, TAG, `Failed to create server: ${error}`);
    }
  }

  onConnect(want: Want, proxy: common.AgentHostProxy) {
    // 客户端连接时触发的回调
    this.server?.start();
  }

  async onData(proxy: common.AgentHostProxy, data: string) {
    // 处理请求的回调函数
    this.server?.onMessage(data, (response: string) => {
      proxy.sendData(response);
    });
  }

  onDisconnect(want: Want, proxy: common.AgentHostProxy) {
    // 客户端断开连接时触发的回调
    this.server?.stop();
  }

  onDestroy() {
    // 清理资源
    this.server?.stop();
  }
}

## Code blocks

### Code block 1

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want, AgentExtensionAbility } from '@kit.AbilityKit';
import { RequestContext, createA2AServer, Server, AgentOperation, TaskState, Role } from '@kit.AgentFrameworkKit';
```

### Code block 2

```
const TAG = "=====A2AServer===="
export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  private server: Server | null = null;

  // OnDataCallback函数
  private agentOnData(method: AgentOperation, context: RequestContext) {
    // 从结构化的上下文参数context中，获取AgentID等信息
    const agentId: string = context.getAgentId();
    if (!agentId) {
        hilog.error(0x0000, TAG, "Agent ID not found in request context");
        return;
    }
    const taskId: string = context.getTaskId();
    switch (method) {
      case AgentOperation.EXECUTE:
        // 使用server.updateStatus，更新任务执行状态
        this.server?.updateStatus(taskId, {
            state: TaskState.WORKING,
            message: {
                messageId: "msg1",
                role: Role.AGENT,
                parts: [{
                    mediaType: "text/plain",
                    text: "Starting work on your request..."
                }]
            }
        });

        // 等待Agent生成产物
        this.server?.addArtifact(taskId, {
            artifactId: "result-artifact",
            parts: [{
                mediaType: "text/plain",
                text: '{"action": "completed", "result": "Task finished successfully"}'
            }]
        });

        // 通知任务完成
        this.server?.updateStatus(taskId, {
            state: TaskState.COMPLETED,
            message: {
                messageId: "msg3",
                role: Role.AGENT,
                parts: [{
                    mediaType: "text/plain",
                    text: "Task completed successfully!"
                }]
            }
        });
        break;
      case AgentOperation.CANCEL:
        // 根据AgentId，通知Agent处理取消任务的请求
        hilog.info(0x0000, TAG, "Cancel called");
        break;
      case AgentOperation.CLEAR_CONTEXT:
          // 根据AgentId，通知Agent清除上下文
        hilog.info(0x0000, TAG, `Clear context called, client session id: ${context.getClientSessionId()}`);
        break;
      case AgentOperation.PERCEPTION_SUGGEST:
        hilog.info(0x0000, TAG, `Perception suggest called, metadata: ${JSON.stringify(context.getMetadata(), null, 2)}`);
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: "onChipsMsg1",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "On chips task completed successfully!"
            }]
          }
        });
      default:
        break;
    }
  }
}
```

### Code block 3

```
async onCreate(want: Want) {
   try {
     const card = this.context.agentCard;
     this.server = createA2AServer(card, this.agentOnData, want=want);
   } catch (error) {
     hilog.error(0x0000, TAG, `Failed to create server: ${error}`);
   }
}
```

### Code block 4

```
onConnect(want: Want, proxy: common.AgentHostProxy) {
  // 客户端连接时触发的回调
  this.server?.start();
}
```

### Code block 5

```
async onData(proxy: common.AgentHostProxy, data: string) {
  // 处理请求的回调函数
  this.server?.onMessage(data, (response: string) => {
     proxy.sendData(response);
  });
}
```

### Code block 6

```
onDisconnect(want: Want, proxy: common.AgentHostProxy) {
  // 客户端断开连接时触发的回调
  this.server?.stop();
}
```

### Code block 7

```
onDestroy() {
  // 清理资源
  this.server?.stop();
}
```

### Code block 8

```
import { hilog } from '@kit.PerformanceAnalysisKit';
import { common, Want, AgentExtensionAbility } from '@kit.AbilityKit';
import { RequestContext, createA2AServer, Server, AgentOperation, TaskState, Role } from '@kit.AgentFrameworkKit';

const TAG = "=====A2AServer===="
export default class MyAgentExtensionAbility extends AgentExtensionAbility {
  private server: Server | null = null;

  // OnDataCallback函数
  private agentOnData(method: AgentOperation, context: RequestContext) {
    // 从结构化的上下文参数context中，获取AgentID等信息
    const agentId: string = context.getAgentId();
    if (!agentId) {
      hilog.error(0x0000, TAG, "Agent ID not found in request context");
      return;
    }
    const taskId: string = context.getTaskId();
    switch (method) {
      case AgentOperation.EXECUTE:
        // 使用server.updateStatus，更新任务执行状态
        this.server?.updateStatus(taskId, {
          state: TaskState.WORKING,
          message: {
            messageId: "msg1",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "Starting work on your request..."
            }]
          }
        });

        // 等待Agent生成产物
        this.server?.addArtifact(taskId, {
          artifactId: "result-artifact",
          parts: [{
            mediaType: "text/plain",
            text: '{"action": "completed", "result": "Task finished successfully"}'
          }]
        });

        // 通知任务完成
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: "msg3",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "Task completed successfully!"
            }]
          }
        });
        break;
      case AgentOperation.CANCEL:
        // 根据AgentId，通知Agent处理取消任务的请求
        hilog.info(0x0000, TAG, "Cancel called");
        break;
      case AgentOperation.CLEAR_CONTEXT:
        // 根据AgentId，通知Agent清除上下文
        hilog.info(0x0000, TAG, `Clear context called, client session id: ${context.getClientSessionId()}`);
        break;
      case AgentOperation.PERCEPTION_SUGGEST:
        hilog.info(0x0000, TAG, `Perception suggest called, metadata: ${JSON.stringify(context.getMetadata(), null, 2)}`);
        this.server?.updateStatus(taskId, {
          state: TaskState.COMPLETED,
          message: {
            messageId: "onChipsMsg1",
            role: Role.AGENT,
            parts: [{
              mediaType: "text/plain",
              text: "On chips task completed successfully!"
            }]
          }
        });
      default:
        break;
    }
  }

  async onCreate(want: Want) {
    try {
      const card = this.context.agentCard;
      this.server = createA2AServer(card, this.agentOnData, want=want);
    } catch (error) {
      hilog.error(0x0000, TAG, `Failed to create server: ${error}`);
    }
  }

  onConnect(want: Want, proxy: common.AgentHostProxy) {
    // 客户端连接时触发的回调
    this.server?.start();
  }

  async onData(proxy: common.AgentHostProxy, data: string) {
    // 处理请求的回调函数
    this.server?.onMessage(data, (response: string) => {
      proxy.sendData(response);
    });
  }

  onDisconnect(want: Want, proxy: common.AgentHostProxy) {
    // 客户端断开连接时触发的回调
    this.server?.stop();
  }

  onDestroy() {
    // 清理资源
    this.server?.stop();
  }
}
```
