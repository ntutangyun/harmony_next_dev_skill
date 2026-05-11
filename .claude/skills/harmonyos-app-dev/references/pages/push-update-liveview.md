# 推送实况窗消息

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-update-liveview_

****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 7


// Request Body
{
  "payload": {
    "activityId": 1,
    "operation": 0,
    "event": "TAXI",
    "status": "DRIVER_ON_THE_WAY", // 司机正在赶来
    "activityData": {
      "notificationData": {
        "type": 3,
        "contentTitle": "{{status}}", // 司机正在赶来
        "contentText": [
          {
            "text": "距您"
          },
          {
            "text": "1.2公里",
            "foregroundColor": "#FF317AF7"
          },
          {
            "text": " | "
          },
          {
            "text": "5分钟",
            "foregroundColor": "#FF317AF7"
          }
        ],
        "clickAction": {
          "actionType": 1, // 打开应用自定义页面
          "action": "xxxxxx" // 应用内置页面ability对应的action
        },
        "richProgress": {
          "type": 0,
          "nodeIcons": ["icon1.png", "icon2.png", "icon3.png"], // 取值为“/resources/rawfile”路径下的文件名
          "indicatorIcon": "taxi.png", // 取值为“/resources/rawfile”路径下的文件名
          "progress": 40,
          "indicatorType": 1,
          "color": "#FF317AF7",
          "bgColor": "#19000000"
        },
        "extend": {
          "type": 3,
          "pic": "phone.png", // 取值为“/resources/rawfile”路径下的文件名
          "clickAction": {
            "actionType": 0 // 点击辅助区打开应用首页
          }
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
        "bgColor": "#FF317AF7",
        "remind": "EXPAND",
        "title": "接驾中",
        "content": "预计5分钟"
      }
    }
  },
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "target": {
    "token": [
      "MAAALgE4G98BAAAAst************jq"
    ]
  }
}
[projectId]：项目ID，登录AppGallery Connect网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
Authorization：JWT格式字符串，可参见Authorization获取。
push-type：7表示实况窗消息场景。
activityId：实况活动ID。详情请参见activityId。
operation：实况窗通知操作类型，0表示创建实况窗。详情请参见operation。
event：实况窗消息具体场景类型，需要与应用实际申请通过的场景一致。例如：TAXI（出行打车）、FLIGHT（航班）等。通过Push Kit创建实况窗仅支持FLIGHT、TAXI、TRAIN、EXPRESS、CHECK_IN五种场景。详情请参见创建实况窗约束。
status：表示实况窗消息状态。operation为0时必填，取值范围根据场景类型而定，详情见Status取值范围，并且需要在支持携带占位符的字段填入至少一次status的占位符{{status}}，Push Kit将替换占位符{{status}}为Status取值范围中对应的值。
activityData：填写您项目中的实况窗数据。详情请参见activityData。
type：实况窗布局类型，有进度可视化类、强调文本类等。创建实况窗时每种event仅可使用特定的布局类型，详情请参见创建实况窗约束。
token：Push Token，可参见获取Push Token获取。

当用户的服务订单状态发生变化时，开发者可以调用Push Kit服务端开放的REST API服务接口，更新或者结束实况窗。

消息详情可参见场景化消息API接口功能介绍。（若开发者更新的实况窗为通过Push Kit远程创建的实况窗，更新时请遵守创建实况窗约束）

// Request URL
POST "https://push-api.cloud.huawei.com/v3/[projectId]/messages:send"
 
// Request Header
Content-Type: application/json
Authorization: Bearer eyJr*****OiIx---****.eyJh*****iJodHR--***.QRod*****4Gp---****
push-type: 7
 
// Request Body
{
  "payload": {
    "activityId": 1,
    "operation": 1,
    "event": "TAXI",
    "status": "HEADING_TO_DESTINATION", // 正在去往目的地
    "version": 1,
    "activityData": {
      "notificationData": {
        "type": 3,
        "contentTitle": "{{status}}", // 正在去往目的地
        "contentText": [
          {
            "text": "距目的地"
          },
          {
            "text": "7.2公里",
            "foregroundColor": "#FF317AF7"
          },
          {
            "text": " | 预计"
          },
          {
            "text": "27分钟",
            "foregroundColor": "#FF317AF7"
          }
        ],
        "clickAction": {
          "actionType": 1, // 打开应用自定义页面
          "action": "xxxxxx" // 应用内置页面ability对应的action
        },
        "richProgress": {
          "type": 0,
          "nodeIcons": ["icon1.png", "icon2.png", "icon3.png"], // 取值为“/resources/rawfile”路径下的文件名
          "indicatorIcon": "taxi.png", // 取值为“/resources/rawfile”路径下的文件名
          "progress": 70,
          "indicatorType": 1,
          "color": "#FF317AF7",
          "bgColor": "#19000000"
        },
        "extend": {
          "type": 0
        }
      },
      "capsuleData": {
        "type": 1,
        "status": 1,
        "icon": "icon.svg", // 取值为“/resources/rawfile”路径下的文件名
        "bgColor": "#FF317AF7",
        "title": "27分钟",
        "content": "距目的地7.2公里"
      }
    }
  },
  "pushOptions": {
    "ttl": 1000,
    "biTag": "biTag"
  },
  "target": {
    "token": [
      "MAMzLg**********lPW"
    ]
  }
}
[projectId]：项目ID，登录AppGallery Connect网站，选择“开发与服务”，在项目列表中选择对应的项目，左侧导航栏选择“项目设置”，在该页面获取。
Authorization：JWT格式字符串，可参见Authorization获取。
push-type：7表示实况窗消息场景。
activityId：实况活动ID。详情请参见activityId。
operation：实况窗通知操作类型，0表示创建实况窗，1表示更新实况窗，2表示结束实况窗。详情请参见operation。
event：实况窗通知具体场景类型，需要与应用实际申请通过的场景一致。例如：TAXI（出行打车）、FLIGHT（航班）等。详情请参见event。
status：表示实况窗消息状态。operation为1且更新的实况窗为通过Push Kit远程创建的实况窗时必填，取值范围根据场景类型而定，详情见Status取值范围，并且需要在支持携带占位符的字段填入至少一次status的占位符{{status}}，Push Kit将替换占位符{{status}}为Status取值范围中对应的值。
version：更新实况窗通知的版本号。详情请参见version。
activityData：填写您项目中的实况窗数据。详情请参见activityData。
type：实况窗布局类型，有进度可视化类、强调文本类等。详情请参见type。
token：Push Token，可参见获取Push Token获取。
说明

若发送的activityId对应的实况窗不存在（更新或结束实况窗的场景中），将限制使用该activityId发送实况窗消息24小时。

推送后台消息
推送应用内通话消息
