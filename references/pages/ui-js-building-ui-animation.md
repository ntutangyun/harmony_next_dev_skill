# 动画

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-animation_

连续动画的核心是animation样式，它定义了动画的开始状态、结束状态以及时间和速度的变化曲线。通过animation样式可以实现的效果有：

animation-name：设置动画执行后应用到组件上的背景颜色、透明度、宽高和变换类型。

animation-delay和animation-duration：分别设置动画执行后元素延迟和持续的时间。

animation-timing-function：描述动画执行的速度曲线，使动画更加平滑。

animation-iteration-count：定义动画播放的次数。

animation-fill-mode：指定动画执行结束后是否恢复初始状态。

animation样式需要在css文件中先定义keyframe，在keyframe中设置动画的过渡效果，并通过一个样式类型在hml文件中调用。animation-name的使用示例如下：

<!-- xxx.hml -->
<div class="item-container">
    <div class="item {{colorParam}}">
        <text class="txt">color</text>
    </div>
    <div class="item {{opacityParam}}">
        <text class="txt">opacity</text>
    </div>
    <input class="button" type="button" name="" value="show" onclick="showAnimation"/>
</div>
/* xxx.css */
.item-container {
  margin: 60px;
  flex-direction: column;
}
.item {
  width: 80%;
  background-color: #f76160;
}
.txt {
  text-align: center;
  width: 200px;
  height: 100px;
}
.button {
  width: 200px;
  margin: 10px;
  font-size: 30px;
  background-color: #09ba07;
}
.color {
  animation-name: Color;
  animation-duration: 8000ms;
}
.opacity {
  animation-name: Opacity;
  animation-duration: 8000ms;
}
@keyframes Color {
  from {
    background-color: #f76160;
  }
  to {
    background-color: #09ba07;
  }
}
@keyframes Opacity {
  from {
    opacity: 0.9;
  }
  to {
    opacity: 0.1;
  }
}
// xxx.js
export default {
  data: {
    colorParam: '',
    opacityParam: '',
  },
  showAnimation: function () {
    this.colorParam = '';
    this.opacityParam = '';
    this.colorParam = 'color';
    this.opacityParam = 'opacity';
  }
}

图2 连续动画效果图

添加交互
手势事件
