# 模型上下文协议（MCP）配置

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp_

功能介绍

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置模型上下文协议（Model Context Protocol，简称MCP）。MCP是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 MCP 官方文档。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，以及支持从MCP Market添加MCP工具。

[h2]使用约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

npx：依赖于Node.js，建议使用Node.js的LTS版本。

uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

操作步骤

说明

MCP Server支持三种通信方式：Stdio 、Server-Sent Events (SSE) 和Streamable HTTP。

Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。

名称：MCP工具名称，如time。

连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。

启用状态：工具是否已启用。
