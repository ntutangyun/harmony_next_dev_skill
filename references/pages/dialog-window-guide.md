# 模态窗口开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dialog-window-guide_

模态窗口用于临时展示关键信息或引导用户完成特定操作（如保存信息），它会中断用户当前的操作流程，要求用户必须做出响应才能继续其他操作，通常用于需要向用户传达重要信息的场景。

开发步骤

创建模态窗口。

通过window.createWindow()接口创建模态窗口（TYPE_DIALOG）。

let dialogWindowClass: window.Window | undefined = undefined;
// ...
    // 1.创建模态窗口。
    let context1: common.UIAbilityContext | undefined = AppStorage.get<common.UIAbilityContext>('context');
    let config: window.Configuration = {
      name: 'dialogWindow', windowType: window.WindowType.TYPE_DIALOG, ctx: context1 as common.BaseContext
    };
    window.createWindow(config, (err, data) => {
      if (err?.code) {
        console.error('Failed to create the dialogWindow. Cause: ' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in creating the dialogWindow. Data: ' + JSON.stringify(data));
      dialogWindowClass = data;
      // ...
    });

设置模态窗口属性。

模态窗口创建成功后，可以改变其大小、位置等，还可以根据应用需要设置窗口背景色、亮度等属性。

在调用showWindow()之前，建议设置模态窗口的大小和位置。

// 2.模态窗口创建成功后，设置模态窗口的位置、大小及相关属性等。
dialogWindowClass.moveWindowTo(100, 100, (err) => {
  if (err?.code) {
    console.error('Failed to move the window. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in moving the window.');
  if (!dialogWindowClass) {
    console.error('dialog_windowClass is null');
    return;
  }
  dialogWindowClass.resize(500, 500, (err) => {
    if (err?.code) {
      console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in changing the window size.');
  });
});

加载显示窗口的具体内容。

通过setUIContent()和showWindow()接口加载显示模态窗口的具体内容。

// 3.为模态窗口加载对应的目标页面。
dialogWindowClass.setUIContent('pages/DialogWindow', (err) => {
  if (err?.code) {
    console.error('Failed to load the content. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in loading the content.');
  // 显示模态窗口。
  (dialogWindowClass as window.Window).showWindow((err) => {
    if (err?.code) {
      console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in showing the window.');
  });
});

销毁窗口。

当不再需要模态窗口时，可根据具体实现逻辑，使用destroyWindow()接口销毁模态窗口。

// 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
dialogWindowClass.destroyWindow((err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in destroying the window.');
});

## Code blocks

### Code block 1

```
let dialogWindowClass: window.Window | undefined = undefined;
// ...
    // 1.创建模态窗口。
    let context1: common.UIAbilityContext | undefined = AppStorage.get<common.UIAbilityContext>('context');
    let config: window.Configuration = {
      name: 'dialogWindow', windowType: window.WindowType.TYPE_DIALOG, ctx: context1 as common.BaseContext
    };
    window.createWindow(config, (err, data) => {
      if (err?.code) {
        console.error('Failed to create the dialogWindow. Cause: ' + JSON.stringify(err));
        return;
      }
      console.info('Succeeded in creating the dialogWindow. Data: ' + JSON.stringify(data));
      dialogWindowClass = data;
      // ...
    });
```

### Code block 2

```
// 2.模态窗口创建成功后，设置模态窗口的位置、大小及相关属性等。
dialogWindowClass.moveWindowTo(100, 100, (err) => {
  if (err?.code) {
    console.error('Failed to move the window. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in moving the window.');
  if (!dialogWindowClass) {
    console.error('dialog_windowClass is null');
    return;
  }
  dialogWindowClass.resize(500, 500, (err) => {
    if (err?.code) {
      console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in changing the window size.');
  });
});
```

### Code block 3

```
// 3.为模态窗口加载对应的目标页面。
dialogWindowClass.setUIContent('pages/DialogWindow', (err) => {
  if (err?.code) {
    console.error('Failed to load the content. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in loading the content.');
  // 显示模态窗口。
  (dialogWindowClass as window.Window).showWindow((err) => {
    if (err?.code) {
      console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in showing the window.');
  });
});
```

### Code block 4

```
// 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
dialogWindowClass.destroyWindow((err: BusinessError) => {
  let errCode: number = err.code;
  if (errCode) {
    console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in destroying the window.');
});
```
