# Taro框架+H5接入智能填充

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scenario-fusion-taro_

示例代码仅展示接入智能填充相关部分，请按照实际场景修改后使用。在Taro的Input组件（Form表单的子节点）中添加nativeProps属性，并配置nativeProps中autocomplete属性来支持智能填充，Form表单提交后，当页面导航发生变化时，满足历史表单输入保存的条件时会触发对应弹窗（建议使用HTML <button> 标签进行Form表单提交）。代码如下：

import { View, Text, Input, Form } from "@tarojs/components";
import Taro, { useLoad } from "@tarojs/taro";
import "./index.scss";


export default function Demo() {
  useLoad(() => {
    console.info("Page loaded.");
  });
  function handleSubmit(e) {
    Taro.request({
      // 将URL设置为实际的接口路径。
      url: "",
      method: "POST",
    });
  }
  return (
    <Form onSubmit={handleSubmit}>
      <View className="native-form">
        <View className="form-item">
          <Text className="col-md-4">昵称：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="nickname"
              type="text"
              nativeProps={{ autocomplete: "nickname" }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">姓名：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="name"
              type="text"
              nativeProps={{ autocomplete: "name" }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">手机号：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="tel"
              type="text"
              nativeProps={{ autocomplete: "tel-national" }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">邮箱：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="email"
              type="text"
              nativeProps={{ autocomplete: "email" }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">身份证：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="idcard"
              type="text"
              nativeProps={{ autocomplete: "id-card-number" }}
            ></Input>
          </View>
        </View>
        <View className="form-item">
          <Text className="col-md-4">带街道地址：</Text>
          <View className="col-md-6">
            <Input
              className="form-value"
              name="street-address"
              type="text"
              nativeProps={{ autocomplete: "street-address" }}
            ></Input>
          </View>
        </View>
      </View>
      <View className="button">
        <button className="button"> 提交</button>
      </View>
    </Form>
  );
}

index.scss如下：

.form-item {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  margin-top: 20px;
  .col-md-4 {
    width: 30%;
    text-align: right;
    font-size: 32px;
  }
  .col-md-6 {
    width: 50%;
    .form-value {
      width: 100%;
      border-style: solid;
      border-width: 1px;
      border-color: #333333;
      font-size: 32px;
    }
  }
}
.button {
  width: 15%;
  background-color: #4caf50;
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 24px;
  margin-left: 30%;
  margin-top: 20px;
}
Flutter框架+H5接入智能填充
Weex框架+H5接入智能填充
