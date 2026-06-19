# 剪贴板粘贴框遮挡智能填充选择框

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-faq-3_

现象描述

解决措施

在代码文件中设置.selectionMenuHidden(true)，使剪贴板粘贴框隐藏。

Row() {
  Text('姓名：').textAlign(TextAlign.End).width('25%')
  TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
}

## Code blocks

### Code block 1

```
Row() {
  Text('姓名：').textAlign(TextAlign.End).width('25%')
  TextInput().width('75%').contentType(ContentType.PERSON_FULL_NAME).selectionMenuHidden(true)
}
```
