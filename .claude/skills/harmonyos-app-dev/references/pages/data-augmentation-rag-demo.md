# 完整示例代码

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-augmentation-rag-demo_

--- 实际使用时请删除本行注释
{
  "knowledgeSource": [{
    "version": 1,
    "dbName": "testmail_store.db",
    "tables": [{
      "tableName": "email",
      "referenceFields": ["id"],
      "knowledgeFields": [{
        "columnName": "subject",
        "type": ["Text"]
      },
      {
        "columnName": "content",
        "type": ["Text"]
      },
      {
        "columnName": "image_text",
        "type": ["Text"]
      },
      {
        "columnName": "attachment_names",
        "type": ["Text"]
      },
      {
    "columnName": "inline_files",
    "type": ["Json"],
    "parser": [
      {
        "type": "File",
        "path": "$[*].uri"
      }
    ]
      },
      {
        "columnName": "sender",
        "type": ["Scalar"],
        "description": "sender"
      },
      {
        "columnName": "receivers",
        "type": ["Scalar"],
        "description": "receivers"
      },
      {
        "columnName": "received_date",
        "type": ["Scalar"],
        "description": "received_date"
      }]
    }]
  }]
}
sourceData.json

sourceData.json文件中的内容为模拟数据源，作为输入插入应用数据库表。真实情况应用数据输入途径应该是界面输入、服务器获取等。

// src/main/resources/rawfile/sourceData.json ------ 仅用于测试数据插入，请开发者根据业务需要预置数据库数据
[{
  "subject": "【请阅】手机优惠政策",
  "sender_name": "test1",
  "sender_email": "test1@example.com",
  "received_time": "2025-05-15 15:49:04.135",
  "recipients": [
    {
      "Address": "test2@example.com",
      "name": "test2",
      "Type": 1
    },
    {
      "Address": "test3@example.com",
      "name": "test3",
      "Type": 2
    },
    {
      "Address": "test4@example.com",
      "name": "test4",
      "Type": 3
    }
  ],
  "to": [
    "lisi"
  ],
  "cc": [
    "wangwu"
  ],
  "bcc": [
    "zhaoliu"
  ],
  "attachment": [],
  "body": "优惠政策：\r\n旗舰系列优惠10%！！ 非旗舰系列优惠20%！！。",
  "unread": false
}]
配置分析过程模板
智慧化数据检索-ArkTS
