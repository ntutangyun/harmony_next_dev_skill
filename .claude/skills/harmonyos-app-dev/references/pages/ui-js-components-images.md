# image开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-images_

-image "+i+"'s height"+e.height,
      duration: 3000,
    })
  },
  imageError(i,e){
    setTimeout(()=>{
      promptAction.showToast({
        message: "Failed to load image "+i+".",
        duration: 3000,
      })
    },3000)
  }
}

场景示例

在本场景中，开发者长按图片后将慢慢隐藏图片，当完全隐藏后再重新显示原始图片。定时器setInterval每隔一段时间改变图片透明度,实现慢慢隐藏的效果，当透明度为0时清除定时器，设置透明度为1。

<!-- index.hml -->
<div class="page-container">
  <div class="content">
    <div class="image-container">
      <image class="testimage" src="{{testuri}}" style="opacity:{{imageopacity}};" onlongpress="changeopacity"> </image>
    </div>
    <div class="text-container">
      <text style="font-size: 37px;font-weight:bold;color:orange;text-align: center;width: 100%;">Touch and hold the image</text>
    </div>
  </div>
</div>
/* xxx.css */
.page-container {
  width: 100%;
  height: 100%;
  flex-direction:column;
  align-self: center;
  justify-content: center;
  background-color:#F1F3F5;
  background-color: #F1F3F5;
}
.content{
  flex-direction:column;
}
.image-container {
  width: 100%;
  height: 300px;
  align-items: center;
  justify-content: center;
}
.text-container {
  margin-top:50px;
  width: 100%;
  height: 60px;
  flex-direction: row;
  justify-content: space-between;
}
.testimage {
  width: 100%;  height: 400px;
  object-fit: scale-down;
  border-radius: 20px;
}
// index.js
import promptAction from '@ohos.promptAction';
export default {
  data: {
    testuri: 'common/images/bg-tv.jpg',
    imageopacity:1,
    timer: null
  },
  changeopacity: function () {
    promptAction.showToast({
      message: 'Touch and hold the image.'
    })
    var opval = this.imageopacity * 20
    clearInterval(this.timer);
    this.timer = setInterval(()=>{
      opval--;
      this.imageopacity = opval / 20
      if (opval===0) {
        clearInterval(this.timer)
        this.imageopacity = 1
      }
    },100);
  }
}

picker开发指导
image-animator开发指导
