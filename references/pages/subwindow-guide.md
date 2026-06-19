# 子窗口开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subwindow-guide_

场景介绍

子窗口是最基础的辅助窗口类型，用于提供辅助性的功能或展示额外的信息。

说明

在非自由窗口状态下，子窗只会在应用主窗口范围显示。

在自由窗口状态下，子窗可超出应用主窗口范围显示。

开发步骤

通过createSubWindow()接口或createSubWindowWithOptions()创建应用子窗口。子窗口创建后默认为沉浸式布局。

API版本26.0.0开始，支持在使用createSubWindowWithOptions()创建子窗时设置SubWindowOptions中的zLevelAboveParentLoosened为true，此时创建的子窗称为独立子窗。

独立子窗在自由窗口状态下，不跟随主窗前后台的切换，仅跟随主窗一起销毁，独立子窗与主窗可通过点击调整层级。

let windowStage_: window.WindowStage | undefined = undefined;
let subWindowClass: window.Window | undefined = undefined;
// ...
      // 获取windowStage
      windowStage_ = AppStorage.get('windowStage');
      // 创建应用子窗口。
      if (windowStage_ == null) {
        console.error('Failed to create the subwindow. Cause: windowStage_ is null');
      } else {
        // 1.使用createSubWindow接口创建子窗
        windowStage_.createSubWindow('SubWindow', (err, data) => {
          if (err?.code) {
            console.error('Failed to create the subwindow. Cause: ' + JSON.stringify(err));
          }
          subWindowClass = data;
          if (!subWindowClass) {
            console.error('sub_windowClass is null');
            return;
          }
          console.info('Succeeded in creating the subwindow. Data: ' + JSON.stringify(data));
          // ...
        })

let independentWindowClass: window.Window | undefined = undefined;
// ...
    // 获取windowStage
    windowStage_ = AppStorage.get('windowStage');
    // 1.创建独立子窗口。
    // ...
        let options : window.SubWindowOptions = {
          title: 'IndependentSubWindow',
          decorEnabled: true,
          zLevelAboveParentLoosened: true  // 独立子窗需将zLevelAboveParentLoosened置为true
        };
        let promise = windowStage_.createSubWindowWithOptions('IndependentSubWindow', options);
        promise.then((data: window.Window | undefined) => {
          independentWindowClass = data;
          if (!independentWindowClass) {
            console.error('independent_sub_windowClass is null');
            return;
          }
          console.info(`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
          // ...
          });

设置子窗口属性。

子窗口创建成功后，可以改变其大小、位置等，还可以根据应用需要设置窗口背景色、亮度等属性。

在调用showWindow()之前，建议设置子窗口的大小和位置。

如果没有设置子窗口的大小，调用showWindow()后有如下表现：

自由窗口状态下，默认子窗口大小为当前物理屏幕的大小。

非自由窗口状态下，默认子窗口大小为主窗口大小。

此处以设置独立子窗的属性为例。示例代码如下：

// 2.子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
independentWindowClass.moveWindowTo(100, 100, (err) => {
  if (err?.code) {
    console.error('Failed to move the window. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in moving the window.');
  if (!independentWindowClass) {
    console.error('independent_windowClass is null');
    return;
  }
  independentWindowClass.resize(1000, 500, (err) => {
    if (err?.code) {
      console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in changing the window size.');
  });
});

加载显示子窗口的具体内容。

通过setUIContent()和showWindow()接口加载和显示子窗口的具体内容。

此处以加载显示独立子窗的具体内容为例。示例代码如下：

// 3.为子窗口加载对应的目标页面。
independentWindowClass.setUIContent('pages/IndependentSubWindow', (err) => {
  if (err?.code) {
    console.error('Failed to load the content. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in loading the content.');
  if (!independentWindowClass) {
    console.error('independent_windowClass is null');
    return;
  }
  // 显示子窗口。
  independentWindowClass.showWindow((err) => {
    if (err?.code) {
      console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in showing the window.');
  });

销毁子窗口。

当不再需要某些子窗口时，可根据具体实现逻辑，使用destroyWindow()接口销毁子窗口。

此处以销毁独立子窗为例。示例代码如下：

// 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
independentWindowClass.destroyWindow((err) => {
  if (err?.code) {
    console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in destroying the window.');
});

## Code blocks

### Code block 1

```
let windowStage_: window.WindowStage | undefined = undefined;
let subWindowClass: window.Window | undefined = undefined;
// ...
      // 获取windowStage
      windowStage_ = AppStorage.get('windowStage');
      // 创建应用子窗口。
      if (windowStage_ == null) {
        console.error('Failed to create the subwindow. Cause: windowStage_ is null');
      } else {
        // 1.使用createSubWindow接口创建子窗
        windowStage_.createSubWindow('SubWindow', (err, data) => {
          if (err?.code) {
            console.error('Failed to create the subwindow. Cause: ' + JSON.stringify(err));
          }
          subWindowClass = data;
          if (!subWindowClass) {
            console.error('sub_windowClass is null');
            return;
          }
          console.info('Succeeded in creating the subwindow. Data: ' + JSON.stringify(data));
          // ...
        })
```

### Code block 2

```
let independentWindowClass: window.Window | undefined = undefined;
// ...
    // 获取windowStage
    windowStage_ = AppStorage.get('windowStage');
    // 1.创建独立子窗口。
    // ...
        let options : window.SubWindowOptions = {
          title: 'IndependentSubWindow',
          decorEnabled: true,
          zLevelAboveParentLoosened: true  // 独立子窗需将zLevelAboveParentLoosened置为true
        };
        let promise = windowStage_.createSubWindowWithOptions('IndependentSubWindow', options);
        promise.then((data: window.Window | undefined) => {
          independentWindowClass = data;
          if (!independentWindowClass) {
            console.error('independent_sub_windowClass is null');
            return;
          }
          console.info(`Succeeded in creating the subwindow. Data: ${JSON.stringify(data)}`);
          // ...
          });
```

### Code block 3

```
// 2.子窗口创建成功后，设置子窗口的位置、大小及相关属性等。
independentWindowClass.moveWindowTo(100, 100, (err) => {
  if (err?.code) {
    console.error('Failed to move the window. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in moving the window.');
  if (!independentWindowClass) {
    console.error('independent_windowClass is null');
    return;
  }
  independentWindowClass.resize(1000, 500, (err) => {
    if (err?.code) {
      console.error('Failed to change the window size. Cause:' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in changing the window size.');
  });
});
```

### Code block 4

```
// 3.为子窗口加载对应的目标页面。
independentWindowClass.setUIContent('pages/IndependentSubWindow', (err) => {
  if (err?.code) {
    console.error('Failed to load the content. Cause:' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in loading the content.');
  if (!independentWindowClass) {
    console.error('independent_windowClass is null');
    return;
  }
  // 显示子窗口。
  independentWindowClass.showWindow((err) => {
    if (err?.code) {
      console.error('Failed to show the window. Cause: ' + JSON.stringify(err));
      return;
    }
    console.info('Succeeded in showing the window.');
  });
```

### Code block 5

```
// 4.销毁子窗口。当不再需要子窗口时，可根据具体实现逻辑，使用destroy对其进行销毁。
independentWindowClass.destroyWindow((err) => {
  if (err?.code) {
    console.error('Failed to destroy the window. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Succeeded in destroying the window.');
});
```
