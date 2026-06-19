# 使用滑动选择器 (Picker)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-picker_

概述

从API version 23开始，ArkUI开发框架在NDK接口提供了Picker容器组件。Picker容器组件用于实现用户自定义选项的选择操作，支持滚动选择、触感反馈、循环滚动等功能。Picker组件通过设置选择指示器样式，可以自定义选中项的显示效果，适用于日期选择、时间选择、文本选择等场景。

创建Picker后，可以设置Picker属性，并监听Picker事件。

使用NDK接口构建UI界面以及NDK基本使用，可以参考接入ArkTS页面。

创建Picker

通过调用createNode()得到组件对象指针，节点类型为ARKUI_NODE_PICKER，并设置ArkUI_NodeAttributeType中的相关属性，创建一个Picker容器组件。

[h2]基本创建方式

以下示例展示了创建Picker组件并设置基本属性的方法。

static ArkUI_NodeHandle CreatePicker(ArkUI_NativeNodeAPI_1 *api)
{
    ArkUI_NodeHandle picker = api->createNode(ARKUI_NODE_PICKER);
    if (picker == nullptr) {
        return nullptr;
    }
    if (g_state) {
        g_state->pickerNode = picker;
    }
    ArkUI_NumberValue widthValue = {.f32 = K_PICKER_WIDTH_RATIO};
    ArkUI_AttributeItem widthItem = {&widthValue, sizeof(widthValue) / sizeof(ArkUI_NumberValue)};
    api->setAttribute(picker, NODE_WIDTH_PERCENT, &widthItem);
    UpdatePickerSelectedIndex();
    api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_CHANGE, K_ON_CHANGE_EVENT_ID, nullptr);
    api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_SCROLL_STOP, K_ON_SCROLL_STOP_EVENT_ID, nullptr);
    if (g_state) {
        for (const auto &item : g_state->dataArray) {
            ArkUI_NodeHandle optionNode = CreatePickerOption(api, item);
            if (optionNode != nullptr) {
                api->addChild(picker, optionNode);
            }
        }
    }
    return picker;
}

[h2]封装为工具类

参考示例中列表组件的实现方式，可以将Picker组件常用的属性设置封装到自定义的工具类中方便后续使用。

class ContainerPickerCanLoopMaker : public BaseNode {
public:
    static ArkUI_NodeHandle CreateNativeNode();

    ContainerPickerCanLoopMaker()
        : BaseNode(NodeApiInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI_NODE_PICKER)),
          nodeApi_(NodeApiInstance::GetInstance()->GetNativeNodeAPI())
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
    }

    ~ContainerPickerCanLoopMaker() override = default;

    // ========================================
    // 基础尺寸设置接口
    // ========================================
    void SetPickerSize(float width, float height) { SetSize(width, height); }

    void SetPickerSizePercent(float widthPercent, float heightPercent) { SetSizePercent(widthPercent, heightPercent); }

    void SetPickerWidthPercent(float widthPercent)
    {
        SetAttributeFloat32(nodeApi_, GetHandle(), NODE_WIDTH_PERCENT, widthPercent);
    }

    void SetPickerHeightPercent(float heightPercent)
    {
        SetAttributeFloat32(nodeApi_, GetHandle(), NODE_HEIGHT_PERCENT, heightPercent);
    }

    // ========================================
    // Picker特有属性设置接口
    // ========================================
    void SetSelectedIndex(uint32_t index)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue selectedIndexValue = {.u32 = index};
        ArkUI_AttributeItem selectedIndexItem = {&selectedIndexValue,
                                                 sizeof(selectedIndexValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_OPTION_SELECTED_INDEX, &selectedIndexItem);
    }

    void SetCanLoop(bool canLoop)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue canLoopValue = {.i32 = canLoop ? 1 : 0};
        ArkUI_AttributeItem canLoopItem = {&canLoopValue, sizeof(canLoopValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_CAN_LOOP, &canLoopItem);
    }

    void SetHapticFeedback(bool enabled)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue enableHapticFeedbackValue = {.i32 = enabled ? 1 : 0};
        ArkUI_AttributeItem enableHapticFeedbackItem = {&enableHapticFeedbackValue,
                                                        sizeof(enableHapticFeedbackValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_ENABLE_HAPTIC_FEEDBACK, &enableHapticFeedbackItem);
    }

    void SetSelectionIndicatorBackground(uint32_t backgroundColor, float cornerRadius = 10.0f)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_PickerIndicatorStyle *indicatorStyle =
            OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_BACKGROUND);
        if (indicatorStyle == nullptr) {
            return;
        }
        ArkUI_PickerIndicatorBackground background = {.backgroundColor = backgroundColor,
                                                      .topLeftRadius = cornerRadius,
                                                      .topRightRadius = cornerRadius,
                                                      .bottomLeftRadius = cornerRadius,
                                                      .bottomRightRadius = cornerRadius};
        OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(indicatorStyle, &background);
        ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
    }

    void SetSelectionIndicatorDivider(uint32_t dividerColor, float strokeWidth = 2.0f, float startMargin = 20.0f,
                                      float endMargin = 20.0f)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_PickerIndicatorStyle *indicatorStyle =
            OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_DIVIDER);
        if (indicatorStyle == nullptr) {
            return;
        }
        ArkUI_PickerIndicatorDivider divider = {.strokeWidth = strokeWidth,
                                                .dividerColor = dividerColor,
                                                .startMargin = startMargin,
                                                .endMargin = endMargin};
        OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(indicatorStyle, &divider);
        ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
    }

    // ========================================
    // 公共辅助方法
    // ========================================
    ArkUI_NativeNodeAPI_1 *GetNodeAPI() const { return nodeApi_; }

protected:
    void OnNodeEvent(ArkUI_NodeEvent *event) override { BaseNode::OnNodeEvent(event); }

private:
    ArkUI_NativeNodeAPI_1 *nodeApi_ = nullptr;
};

设置Picker属性

[h2]设置默认选中项

通过设置ArkUI_NodeAttributeType中的NODE_PICKER_OPTION_SELECTED_INDEX属性，可以设置Picker组件的默认选中项索引。

ArkUI_NumberValue selectedIndexValue = {.u32 = index};
ArkUI_AttributeItem selectedIndexItem = {&selectedIndexValue,
                                         sizeof(selectedIndexValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_OPTION_SELECTED_INDEX, &selectedIndexItem);

[h2]设置触感反馈

通过设置NODE_PICKER_ENABLE_HAPTIC_FEEDBACK属性，可以控制Picker组件是否启用触感反馈。开启后，当用户滚动选择器时，如果系统硬件支持，会产生触感反馈。

使用ArkUI_NativeNodeAPI_1时可直接调用setAttribute。

ArkUI_NumberValue enableHapticFeedbackValue = {.i32 = enabled ? 1 : 0};
ArkUI_AttributeItem enableHapticFeedbackItem = {&enableHapticFeedbackValue,
                                                sizeof(enableHapticFeedbackValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_ENABLE_HAPTIC_FEEDBACK, &enableHapticFeedbackItem);

若使用上文封装的ContainerPickerCanLoopMaker，可调用已封装的接口。

picker->SetHapticFeedback(K_HAPTIC_FEEDBACK);

[h2]设置循环滚动

通过设置NODE_PICKER_CAN_LOOP属性，可以控制Picker组件是否支持循环滚动。设置为true时，选择器可以无限循环滚动；设置为false时，滚动到首尾时会停止。

说明

如果子组件的个数小于8个，无论设置为true还是false，都不会循环滚动。

使用ArkUI_NativeNodeAPI_1时可直接调用setAttribute。

ArkUI_NumberValue canLoopValue = {.i32 = canLoop ? 1 : 0};
ArkUI_AttributeItem canLoopItem = {&canLoopValue, sizeof(canLoopValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_CAN_LOOP, &canLoopItem);

若使用上文封装的ContainerPickerCanLoopMaker，可调用已封装的接口。

picker->SetCanLoop(K_CAN_LOOP);

[h2]设置选择指示器样式

通过设置NODE_PICKER_SELECTION_INDICATOR属性，可以自定义Picker组件的选择指示器样式。选择指示器包括背景样式和分割线样式两部分。

背景样式指示器通过ArkUI_PickerIndicatorBackground结构体设置，包括背景颜色和圆角半径。

void SetSelectionIndicatorBackground(uint32_t backgroundColor, float cornerRadius = 10.0f)
{
    if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
        return;
    }
    ArkUI_PickerIndicatorStyle *indicatorStyle =
        OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_BACKGROUND);
    if (indicatorStyle == nullptr) {
        return;
    }
    ArkUI_PickerIndicatorBackground background = {.backgroundColor = backgroundColor,
                                                  .topLeftRadius = cornerRadius,
                                                  .topRightRadius = cornerRadius,
                                                  .bottomLeftRadius = cornerRadius,
                                                  .bottomRightRadius = cornerRadius};
    OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(indicatorStyle, &background);
    ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
    nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
}

分割线样式指示器通过ArkUI_PickerIndicatorDivider结构体设置，包括线宽、颜色和边距。

void SetSelectionIndicatorDivider(uint32_t dividerColor, float strokeWidth = 2.0f, float startMargin = 20.0f,
                                  float endMargin = 20.0f)
{
    if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
        return;
    }
    ArkUI_PickerIndicatorStyle *indicatorStyle =
        OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_DIVIDER);
    if (indicatorStyle == nullptr) {
        return;
    }
    ArkUI_PickerIndicatorDivider divider = {.strokeWidth = strokeWidth,
                                            .dividerColor = dividerColor,
                                            .startMargin = startMargin,
                                            .endMargin = endMargin};
    OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(indicatorStyle, &divider);
    ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
    nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
}

将背景样式或分割线样式组合到ArkUI_PickerIndicatorStyle结构体中，并设置给Picker组件。

若使用上文封装的ContainerPickerMonthMaker，可调用已封装的接口。

picker->SetSelectionIndicatorDivider(0xFF0000FF, 2.0f, 20.0f, 20.0f);

监听Picker事件

本示例通过registerNodeEvent注册Picker组件的事件类型ArkUI_NodeEventType，使用ArkUI_NodeEventItem结构体为每个事件指定独立的回调函数。开发者无需额外注册全局回调函数，每个事件项直接绑定回调函数。Picker组件支持的事件如下：

枚举	说明	起始版本
NODE_PICKER_EVENT_ON_CHANGE	Picker组件中选择某项时触发的事件。	23
NODE_PICKER_EVENT_ON_SCROLL_STOP	Picker组件中选择某项且滚动停止时触发的事件。	23

[h2]监听选择变化事件

通过registerNodeEvent注册NODE_PICKER_EVENT_ON_CHANGE事件，使用ArkUI_NodeEventItem结构体指定回调函数，可以监听Picker组件的选择变化。事件回调中会返回选中项的索引值。

api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_CHANGE, K_ON_CHANGE_EVENT_ID, nullptr);

[h2]监听滚动停止事件

通过registerNodeEvent注册NODE_PICKER_EVENT_ON_SCROLL_STOP事件，使用ArkUI_NodeEventItem结构体指定回调函数，可以监听Picker组件滚动停止时的选择变化。与NODE_PICKER_EVENT_ON_CHANGE事件相比，该事件只在滚动停止时触发，适合需要在滚动完成后再处理选择的场景。

api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_SCROLL_STOP, K_ON_SCROLL_STOP_EVENT_ID, nullptr);

完整示例

Native_Type_Sample

## Code blocks

### Code block 1

```
static ArkUI_NodeHandle CreatePicker(ArkUI_NativeNodeAPI_1 *api)
{
    ArkUI_NodeHandle picker = api->createNode(ARKUI_NODE_PICKER);
    if (picker == nullptr) {
        return nullptr;
    }
    if (g_state) {
        g_state->pickerNode = picker;
    }
    ArkUI_NumberValue widthValue = {.f32 = K_PICKER_WIDTH_RATIO};
    ArkUI_AttributeItem widthItem = {&widthValue, sizeof(widthValue) / sizeof(ArkUI_NumberValue)};
    api->setAttribute(picker, NODE_WIDTH_PERCENT, &widthItem);
    UpdatePickerSelectedIndex();
    api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_CHANGE, K_ON_CHANGE_EVENT_ID, nullptr);
    api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_SCROLL_STOP, K_ON_SCROLL_STOP_EVENT_ID, nullptr);
    if (g_state) {
        for (const auto &item : g_state->dataArray) {
            ArkUI_NodeHandle optionNode = CreatePickerOption(api, item);
            if (optionNode != nullptr) {
                api->addChild(picker, optionNode);
            }
        }
    }
    return picker;
}
```

### Code block 2

```
class ContainerPickerCanLoopMaker : public BaseNode {
public:
    static ArkUI_NodeHandle CreateNativeNode();

    ContainerPickerCanLoopMaker()
        : BaseNode(NodeApiInstance::GetInstance()->GetNativeNodeAPI()->createNode(ARKUI_NODE_PICKER)),
          nodeApi_(NodeApiInstance::GetInstance()->GetNativeNodeAPI())
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
    }

    ~ContainerPickerCanLoopMaker() override = default;

    // ========================================
    // 基础尺寸设置接口
    // ========================================
    void SetPickerSize(float width, float height) { SetSize(width, height); }

    void SetPickerSizePercent(float widthPercent, float heightPercent) { SetSizePercent(widthPercent, heightPercent); }

    void SetPickerWidthPercent(float widthPercent)
    {
        SetAttributeFloat32(nodeApi_, GetHandle(), NODE_WIDTH_PERCENT, widthPercent);
    }

    void SetPickerHeightPercent(float heightPercent)
    {
        SetAttributeFloat32(nodeApi_, GetHandle(), NODE_HEIGHT_PERCENT, heightPercent);
    }

    // ========================================
    // Picker特有属性设置接口
    // ========================================
    void SetSelectedIndex(uint32_t index)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue selectedIndexValue = {.u32 = index};
        ArkUI_AttributeItem selectedIndexItem = {&selectedIndexValue,
                                                 sizeof(selectedIndexValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_OPTION_SELECTED_INDEX, &selectedIndexItem);
    }

    void SetCanLoop(bool canLoop)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue canLoopValue = {.i32 = canLoop ? 1 : 0};
        ArkUI_AttributeItem canLoopItem = {&canLoopValue, sizeof(canLoopValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_CAN_LOOP, &canLoopItem);
    }

    void SetHapticFeedback(bool enabled)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_NumberValue enableHapticFeedbackValue = {.i32 = enabled ? 1 : 0};
        ArkUI_AttributeItem enableHapticFeedbackItem = {&enableHapticFeedbackValue,
                                                        sizeof(enableHapticFeedbackValue) / sizeof(ArkUI_NumberValue)};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_ENABLE_HAPTIC_FEEDBACK, &enableHapticFeedbackItem);
    }

    void SetSelectionIndicatorBackground(uint32_t backgroundColor, float cornerRadius = 10.0f)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_PickerIndicatorStyle *indicatorStyle =
            OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_BACKGROUND);
        if (indicatorStyle == nullptr) {
            return;
        }
        ArkUI_PickerIndicatorBackground background = {.backgroundColor = backgroundColor,
                                                      .topLeftRadius = cornerRadius,
                                                      .topRightRadius = cornerRadius,
                                                      .bottomLeftRadius = cornerRadius,
                                                      .bottomRightRadius = cornerRadius};
        OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(indicatorStyle, &background);
        ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
    }

    void SetSelectionIndicatorDivider(uint32_t dividerColor, float strokeWidth = 2.0f, float startMargin = 20.0f,
                                      float endMargin = 20.0f)
    {
        if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
            return;
        }
        ArkUI_PickerIndicatorStyle *indicatorStyle =
            OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_DIVIDER);
        if (indicatorStyle == nullptr) {
            return;
        }
        ArkUI_PickerIndicatorDivider divider = {.strokeWidth = strokeWidth,
                                                .dividerColor = dividerColor,
                                                .startMargin = startMargin,
                                                .endMargin = endMargin};
        OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(indicatorStyle, &divider);
        ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
        nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
    }

    // ========================================
    // 公共辅助方法
    // ========================================
    ArkUI_NativeNodeAPI_1 *GetNodeAPI() const { return nodeApi_; }

protected:
    void OnNodeEvent(ArkUI_NodeEvent *event) override { BaseNode::OnNodeEvent(event); }

private:
    ArkUI_NativeNodeAPI_1 *nodeApi_ = nullptr;
};
```

### Code block 3

```
ArkUI_NumberValue selectedIndexValue = {.u32 = index};
ArkUI_AttributeItem selectedIndexItem = {&selectedIndexValue,
                                         sizeof(selectedIndexValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_OPTION_SELECTED_INDEX, &selectedIndexItem);
```

### Code block 4

```
ArkUI_NumberValue enableHapticFeedbackValue = {.i32 = enabled ? 1 : 0};
ArkUI_AttributeItem enableHapticFeedbackItem = {&enableHapticFeedbackValue,
                                                sizeof(enableHapticFeedbackValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_ENABLE_HAPTIC_FEEDBACK, &enableHapticFeedbackItem);
```

### Code block 5

```
picker->SetHapticFeedback(K_HAPTIC_FEEDBACK);
```

### Code block 6

```
ArkUI_NumberValue canLoopValue = {.i32 = canLoop ? 1 : 0};
ArkUI_AttributeItem canLoopItem = {&canLoopValue, sizeof(canLoopValue) / sizeof(ArkUI_NumberValue)};
nodeApi_->setAttribute(GetHandle(), NODE_PICKER_CAN_LOOP, &canLoopItem);
```

### Code block 7

```
picker->SetCanLoop(K_CAN_LOOP);
```

### Code block 8

```
void SetSelectionIndicatorBackground(uint32_t backgroundColor, float cornerRadius = 10.0f)
{
    if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
        return;
    }
    ArkUI_PickerIndicatorStyle *indicatorStyle =
        OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_BACKGROUND);
    if (indicatorStyle == nullptr) {
        return;
    }
    ArkUI_PickerIndicatorBackground background = {.backgroundColor = backgroundColor,
                                                  .topLeftRadius = cornerRadius,
                                                  .topRightRadius = cornerRadius,
                                                  .bottomLeftRadius = cornerRadius,
                                                  .bottomRightRadius = cornerRadius};
    OH_ArkUI_PickerIndicatorStyle_ConfigureBackground(indicatorStyle, &background);
    ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
    nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
}
```

### Code block 9

```
void SetSelectionIndicatorDivider(uint32_t dividerColor, float strokeWidth = 2.0f, float startMargin = 20.0f,
                                  float endMargin = 20.0f)
{
    if (!IsNotNull(nodeApi_) || !IsNotNull(GetHandle())) {
        return;
    }
    ArkUI_PickerIndicatorStyle *indicatorStyle =
        OH_ArkUI_PickerIndicatorStyle_Create(ARKUI_PICKER_INDICATOR_DIVIDER);
    if (indicatorStyle == nullptr) {
        return;
    }
    ArkUI_PickerIndicatorDivider divider = {.strokeWidth = strokeWidth,
                                            .dividerColor = dividerColor,
                                            .startMargin = startMargin,
                                            .endMargin = endMargin};
    OH_ArkUI_PickerIndicatorStyle_ConfigureDivider(indicatorStyle, &divider);
    ArkUI_AttributeItem selectionIndicatorItem = {.object = indicatorStyle};
    nodeApi_->setAttribute(GetHandle(), NODE_PICKER_SELECTION_INDICATOR, &selectionIndicatorItem);
}
```

### Code block 10

```
picker->SetSelectionIndicatorDivider(0xFF0000FF, 2.0f, 20.0f, 20.0f);
```

### Code block 11

```
api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_CHANGE, K_ON_CHANGE_EVENT_ID, nullptr);
```

### Code block 12

```
api->registerNodeEvent(picker, NODE_PICKER_EVENT_ON_SCROLL_STOP, K_ON_SCROLL_STOP_EVENT_ID, nullptr);
```
