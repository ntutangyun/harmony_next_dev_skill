# 跳转规则

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/redirection-rules_

应用可通过在config.json中设置"abilities"中的"visible"属性设置Ability是否可由其他应用的组件启动，"visible"属性的具体参数和意义如下表所示。

表1 visible属性说明

属性名称	描述	是否可缺省
visible	

表示Ability是否可以被其他应用调用。

true：该Ability可以被任何应用调用。

false：该Ability只能被同一应用的其他组件调用。

	可缺省，缺省时默认属性值为"false"。

如果需设置当前Ability可由任何应用访问，对应config.json文件的示例代码如下所示：

{
  "module": {
    ...
    "abilities": [
      {
        "visible": "true",
        ...
      }
    ]
  }
}

如果应用中的Ability包含skills过滤器，建议此属性设置为"true"，以允许其他应用通过隐式调用启动该Ability。如果此属性设为"false"，其他应用尝试启动该Ability时系统会返回PERMISSION_DENIED。这种情况下系统应用可以通过申请START_INVISIBLE_ABILITY权限启动visible为false的组件，例如系统桌面、语音助手、搜索助手等。

申请授权
ServiceAbility组件开发指导
