# 生命周期

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-lifecycle_

通过以下示例，详细说明生命周期函数的调用顺序。首先创建两个页面，分别为pageA和pageB，并在config.json中配置页面路由信息：

{
    // ...
    "pages": [
        "pages/pageA/pageA",
        "pages/pageB/pageB"
    ],
    // ...
}

pageA实现代码如下：

<!-- pageA.hml -->
<div class="container">
  <text class="title">This is PageA</text>
  <input type="button" value="Go to the PageB" onclick="launch"></input>
</div>
/* pageA.css */
.container {
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}
.title {
  font-size: 38px;
  text-align: center;
  width: 100%;
  height: 40%;
}
// pageA.js
import router from '@ohos.router';
export default {
  launch() {
    router.push ({
      url: 'pages/pageB/pageB'
    });
  },
  onInit() {
    console.info('PageA onInit');
  },
  onReady() {
    console.info('PageA onReady');
  },
  onShow() {
    console.info('PageA onShow');
  },
  onHide() {
    console.info('PageA onHide');
  },
  onDestroy() {
    console.info('PageA onDestroy');
  },
  onBackPress() {
    console.info('PageA onBackPress');
  },
  onActive() {
    console.info('PageA onActive');
  },
  onInactive() {
    console.info('PageA onInactive');
  },
  onNewRequest() {
    console.info('PageA onNewRequest');
  }
}

pageB实现代码如下：

<!-- pageB.hml -->
<div class="container">
  <text class="title">This is PageB</text>
</div>
/* pageB.css */
.container {
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}
.title {
  font-size: 38px;
  text-align: center;
  width: 100%;
  height: 40%;
}
// pageB.js
export default {
  onInit() {
    console.info('PageB onInit');
  },
  onReady() {
    console.info('PageB onReady');
  },
  onShow() {
    console.info('PageB onShow');
  },
  onHide() {
    console.info('PageB onHide');
  },
  onDestroy() {
    console.info('PageB onDestroy');
  },
  onBackPress() {
    console.info('PageB onBackPress');
  },
  onActive() {
    console.info('PageB onActive');
  },
  onInactive() {
    console.info('PageB onInactive');
  },
  onNewRequest() {
    console.info('PageB onNewRequest');
  }
}

运行程序，通过日志观察生命周期函数的调用顺序。其中pageA的生命周期函数的调用顺序为：

打开应用进入页面A：onInit() -> onReady() -> onActive() -> onShow()

在页面A打开页面B：onHide()

从页面B返回页面A：onShow()

退出页面A：onBackPress() -> onInactive() -> onHide()

页面A隐藏到后台运行：onInactive() -> onHide()

页面A从后台运行恢复到前台：onNewRequest() -> onShow() -> onActive()

pageB的生命周期函数的调用顺序为：

在页面A打开页面B：onInit() -> onReady() -> onShow()

从页面B返回页面A：onBackPress() -> onHide() -> onDestroy()

页面B隐藏到后台运行：onInactive() -> onHide()

页面B从后台运行恢复到前台：onNewRequest() -> onShow() -> onActive()

JS语法参考
资源限定与访问
