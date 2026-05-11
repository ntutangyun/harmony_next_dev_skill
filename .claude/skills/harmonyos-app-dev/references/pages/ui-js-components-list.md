# list开发指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-list_

{{listgroup.value}}</text>
        </div>
      </list-item>
      <list-item type="item" style="background-color: #87CEFA;height:145px;" primary="true">
        <div class="item-group-child">
          <text>Primary---{{listgroup.value}}</text>
        </div>
      </list-item>
    </list-item-group>
  </list>
</div>
/* xxx.css */
.doc-page {
  flex-direction: column;
  background-color: #F1F3F5;
}
.list-item {
  margin-top:30px;
}
.top-list-item {
  width:100%;
  background-color:#D4F2E7;
}
.item-group-child {
  justify-content: center;
  align-items: center;
  width:100%;
}
// xxx.js
import promptAction from '@ohos.promptAction';
export default {
  data: {
    direction: 'column',
    list: []
  },
  onInit() {
    this.list = []
    this.listAdd = []
    for (var i = 1; i <= 2; i++) {
      var dataItem = {
        value: 'GROUP' + i,
      };
        this.list.push(dataItem);
    }
  },
  collapse(e) {
    promptAction.showToast({
      message: 'Close ' + e.groupid
    })
  },
  expand(e) {
    promptAction.showToast({
    message: 'Open ' + e.groupid
    })
  }
}

说明
groupcollapse和groupexpand事件仅支持list-item-group组件使用。
场景示例

在本场景中，开发者可以根据字母索引表查找对应联系人。

<!-- xxx.hml -->
<div class="doc-page"> 
  <text style="font-size: 35px; font-weight: 500; text-align: center; margin-top: 20px; margin-bottom: 20px;"> 
      <span>Contacts</span> 
  </text> 
  <list class="list" indexer="true"> 
    <list-item class="item" for="{{namelist}}" type="{{$item.section}}" section="{{$item.section}}"> 
      <div class="container"> 
        <div class="in-container"> 
          <text class="name">{{$item.name}}</text> 
          <text class="number">18888888888</text> 
        </div> 
      </div> 
    </list-item> 
    <list-item type="end" class="item"> 
      <div style="align-items:center;justify-content:center;width:750px;"> 
        <text style="text-align: center;">Total: 10</text> 
      </div> 
    </list-item> 
  </list> 
</div>
/* xxx.css */
.doc-page {
  width: 100%;
  height: 100%;
  flex-direction: column;
  background-color: #F1F3F5;
}
.list {
  width: 100%;
  height: 90%;
  flex-grow: 1;
}
.item {
  height: 120px;
  padding-left: 10%;
  border-top: 1px solid #dcdcdc;
}
.name {
  color: #000000;
  font-size: 39px;
}
.number {
  color: black;
  font-size: 25px;
}
.container {
  flex-direction: row;
  align-items: center;
}
.in-container {
  flex-direction: column;
  justify-content: space-around;
}
// xxx.js
export default {
   data: {
     namelist:[{
       name: 'Zoey',
       section:'Z'
     },{
       name: 'Quin',
       section:'Q'
     },{
       name:'Sam',
       section:'S'
     },{
       name:'Leo',
       section:'L'
     },{
       name:'Zach',
       section:'Z'
     },{
       name:'Wade',
       section:'W'
     },{
       name:'Zoe',
       section:'Z'
     },{
        name:'Warren',
        section:'W'
     },{
        name:'Kyle',
        section:'K'
     },{
       name:'Zaneta',
       section:'Z'
     }]
   },
   onInit() {
   }
 }

容器组件
dialog开发指导
