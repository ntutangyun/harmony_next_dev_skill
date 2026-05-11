# qrcode开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-qrcode_

<option for="{{bcol_list}}" value="{{$item}}">{{$item}}</option>
  </select>
  <qrcode value="Hello" type="{{qr_type}}"></qrcode>
</div>
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
select{
  margin-top: 50px;
  margin-bottom: 50px;
}
// index.js
export default {
  data: {
    qr_type: 'rect',
    bcol_list: ['rect','circle']
  },
  settype(e) {
    this.qr_type = e.newValue
  },
}

设置样式

通过color和background-color样式为二维码设置显示颜色和背景颜色。

<!-- xxx.hml-->
<div class="container">
  <qrcode value="Hello" type="rect"></qrcode>
</div>
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
qrcode{
  width: 300px;
  height: 300px;
 color: blue;  background-color: #ffffff;
}

说明

width和height不一致时，取二者较小值作为二维码的边长，且最终生成的二维码居中显示。

width和height只设置一个时，取设置的值作为二维码的边长。都不设置时，使用200px作为默认边长。

场景示例

在本场景中将二维码与输入框绑定，通过改变输入框的内容改变二维码。

<!-- xxx.hml-->
<div class="container">
  <input style="margin-bottom: 100px;" onchange="change"></input>
  <qrcode value="{{textVal}}"></qrcode>
</div>
/* xxx.css */
.container {
  width: 100%;
  height: 100%;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #F1F3F5;
}
qrcode{
  width: 400px;
  height: 400px;
}
// index.js
export default{
  data: {
    textVal: ''
  },
  change(e){
    this.textVal = e.value
  }
}

marquee开发指导
search开发指导
