# 开发预加载资源接口

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-cloud-interdev_

-----Finished-------");
    callback(res);
  } catch (error) {
    logger.error("--------Error-------");
    logger.error("error: " + error);
    callback(error);
  }
};


export { myHandler };

周期性预加载

import axios from 'axios';


let myHandler = async function (event, context, callback, logger) {
  logger.info("event:" + JSON.stringify(event));
  let env1 = context.env.env1; // 环境变量
  logger.info("env1: " + env1)
  try {
    let body = event.body ? JSON.parse(event.body) : event;
    let appId = body.appId;
    let token = body.token;
    let paramsStr = body.params; // 如果需要解析json结构paramsStr中的参数，需要使用 let params = JSON.parse(paramsStr);


    logger.info("appId: " + appId + ",token:" + token + ",params:" + paramsStr);


    // http请求示例，请按照实际业务修改
    let url = 'https://example.com/prefetchApi'; // 页面资源数据的请求url
    let headers = { 'k1': 'v1' }; // 请求header
    let res; // 返回数据
    await axios.post(url, {}, { headers }) // http post请求
      .then(response => {
        res = response.data;
      })
    logger.info("--------Finished-------");
    callback(res);
  } catch (error) {
    logger.error("--------Error-------");
    logger.error("error: " + error);
    callback(error);
  }
};


export { myHandler };

跳链安装预加载

import axios from 'axios';


let myHandler = async function (event, context, callback, logger) {
  logger.info("event:" + JSON.stringify(event));
  let env1 = context.env.env1; // 环境变量
  logger.info("env1: " + env1)
  try {
    let body = event.body ? JSON.parse(event.body) : event;
    let appId = body.appId;
    let link = body.link; // 跳链安装预加载link信息


    logger.info("appId: " + appId + ",link:" + link);


    // http请求示例，请按照实际业务修改
    let url = 'https://example.com/prefetchApi'; // 页面资源数据的请求url
    let headers = { 'k1': 'v1' }; // 请求header
    let res; // 返回数据
    await axios.post(url, {}, { headers }) // http post请求
      .then(response => {
        res = response.data;
      })
    logger.info("--------Finished-------");
    callback(res);
  } catch (error) {
    logger.error("--------Error-------");
    logger.error("error: " + error);
    callback(error);
  }
};


export { myHandler };
开发者服务器

申请开通开发者服务器权限之后，开发者使用自己的服务器自行开发和实现预加载资源接口，接口需遵循开发者服务器接口规范。

开发者服务器接口规范
预加载类型	API/PATH名称	说明	参数	请求方式	返回值
安装预加载	自定义	获取预加载数据接口	appId：应用ID，获取方法请参见查看应用信息。	GET	自定义JSON字符串
周期性预加载	自定义	获取预加载数据接口	

- appId：应用ID，获取方法请参见查看应用信息。

- token：可选，注册周期性预加载任务时开发者自行传入的用户级认证信息，长度不超过2048个字符。

- params：可选，注册周期性预加载任务时开发者自行传入的自定义参数，长度不超过1024个字符。

	GET	自定义JSON字符串
跳链安装预加载	自定义	获取预加载数据接口	

- appId：应用ID，获取方法请参见查看应用信息。

- link：可选，跳链安装预加载延迟链接。

	GET	自定义JSON字符串
示例

定义名称为prefetchData的接口，示例如下：

https://www.example.com/prefetchData?appId=1234&token=xxxx&params=yyyy
配置预加载
调用预加载
