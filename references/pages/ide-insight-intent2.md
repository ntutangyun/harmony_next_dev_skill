# 意图装饰器生成和小艺智能体创建

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-intent2_

通过装饰类或方法可以将应用的功能定义为"意图"，然后将应用功能以"意图"形式集成至系统入口。用户通过系统入口（如语音助手、智能推荐卡片）触发意图执行，即可便捷使用应用提供的功能。

从DevEco Studio 6.0.0 Beta2开始，CodeGenie新增通过装饰器开发意图的功能，支持生成五类意图装饰器。同时，DevEco Studio新增Application Agent入口，通过该入口可完成意图插件注册、智能体创建等，提升开发效率。

使用约束

使用API 20及以上版本。

仅支持使用团队账号登录时，添加意图插件。个人加入目标团队方式具体可参考添加成员。

应用在AGC已注册，具体可参考创建HarmonyOS应用。

生成意图装饰器时使用HarmonyOS Ask智能体。

意图装饰器分类

CodeGenie提供了几类意图装饰器，开发者可根据业务场景进行选择，具体请参考意图装饰器定义：

@InsightIntentLink装饰器：在class头部或内部位置唤起意图装饰器，在class上方插入生成的代码。

@InsightIntentPage装饰器：在@Component头部/struct结构体内部/选中整个结构体区域唤起意图装饰器，在@Entry上方插入生成的代码。

@InsightIntentFunction装饰器：在类中静态方法区域唤起意图装饰器，在class上方插入@InsightIntentFunction，在class内部插入@InsightIntentFunctionMethod生成内容。

@InsightIntentForm装饰器：在继承FormExtensionAbility的class头部或内部唤起意图装饰器，在class上方插入生成的代码。

@InsightIntentEntry装饰器：在直接继承InsightIntentEntryExecutor的class头部或内部唤起意图装饰器，在class上方插入生成的代码。

[h2]@InsightIntentLink装饰器

[h2]@InsightIntentPage装饰器

基于组件导航（Navigation）的子页面使用，@Component和struct需成对出现。

[h2]@InsightIntentFunction装饰器

[h2]@InsightIntentForm装饰器

[h2]@InsightIntentEntry装饰器

生成意图插件和创建小艺智能体

说明

个人账号需要完成实名认证，具体请参考实名认证。

如下企业开发者账号为某团队账号名称，仅供参考。

在DevEco Studio菜单栏点击View > Tool Windows > Application Agent ，打开内嵌的小艺智能平台新建智能体和添加插件。小艺智能平台更多具体操作可参考鸿蒙智能体。
