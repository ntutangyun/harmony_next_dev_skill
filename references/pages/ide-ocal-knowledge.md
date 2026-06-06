# 本地知识库配置

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ocal-knowledge_

从DevEco Studio 6.0.0 Beta5开始，CodeGenie允许用户导入设计文档和代码等文件形成文档集，多个文档集组合成本地知识库。智能问答时，根据用户输入内容检索本地知识库以提升AI生成的能力。

点击File > Settings（macOS为DevEco Studio > Preferences/Settings） > CodeGenie > Knowledge > Docs，或在DevEco Studio右侧边栏点击CodeGenie（或输入快捷键Alt/Option+U） > @Add Context > Docs > Set Local Knowledge Base，进入配置页面。

首次打开时，点击按钮，填写相关信息，创建文档集。

Knowledge Base Path：知识库保存路径。在同一个路径下保存的文档集，会形成一个知识库。
Document set name：文档集名称。
Description：可选，文档集描述。

点击按钮，添加文档集中的文件，添加成功的文件在下方展示。

说明
支持的文件格式：txt、md、json、html、cpp、ets、ts、js。
单个文档集中文件个数：不超过1000个。
单个文件大小：不超过10M。
单个知识库中文档集个数：不超过20个。
单个知识库大小：不超过50M。

点击“OK”，完成本地知识库配置和同步，在DevEco Studio页面下方Storing document set可查看同步进度。

同步完成后，在对话框中输入@符号选择Docs ，或点击上方@Add Context > Docs ，选择需要的文档集。

选择代码文件进行问答，具体请参考智能问答
自定义提示词库（Prompts）配置
