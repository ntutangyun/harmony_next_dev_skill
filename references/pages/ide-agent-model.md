# 模型（Model）配置

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model_

CodeGenie支持通过Anthropic-API、Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Anthropic-API、Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。

操作步骤

Name：模型名称。

Provider：模型的提供商，可选项包括OpenAI、Gemini、Anthropic、DeepSeek、Alibaba Cloud、Z.ai。

API Key：模型的访问密钥，在提供商网站申请。

Model：模型的标识。

不同Service Provider的API Key和支持的模型如下：

Provider	API Key获取地址	Model示例
OpenAI	https://platform.openai.com/api-keys	gpt-5.3-codex、gpt-5.4、gpt-5.5、gpt-5.6
Gemini	https://aistudio.google.com/apikey	gemini-3-pro-preview、gemini-3-flash-preview、gemini-3-pro-image-preview
Anthropic	https://console.anthropic.com	claude-sonnet-4-5-20250929
DeepSeek	https://platform.deepseek.com	deepseek-v4-pro
Alibaba Cloud	https://dashscope.console.aliyun.com	qwen3-coder-plus
Z.ai	https://open.bigmodel.cn	glm-5

Name：模型名称。

Url：模型的访问地址。

Protocol：模型的协议，可选项包括OpenAI、Anthropic、Gemini、Ollama。

API Key：模型的访问密钥，在提供商网站申请。

Model：模型的标识。

说明

配置说明、URL配置示例等内容请参考通过URL添加模型。

附录

[h2]通过URL添加模型

约束与限制

暂不支持开启深度思考（Deep Thinking）功能和多模态图片处理功能。

配置说明

代理配置：为了避免代理问题造成的请求超时，将内网模型服务域名添加到HTTP代理的No proxy for中。

原URL： https://api.deepseek.com/chat/completions

填写为： https://api.deepseek.com

原API Key：Bearer sk-f9e98c******8

填写为：sk-f9e98c******8

配置示例
