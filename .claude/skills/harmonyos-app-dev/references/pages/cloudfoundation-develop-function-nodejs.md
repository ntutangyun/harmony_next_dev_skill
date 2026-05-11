# Node.js

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-develop-function-nodejs_

-----Start-------");
  try {
    let startTime = new Date().getTime();
    let endTime = startTime;
    let interval = 0;
    startTime = process.uptime() * 1000;


    // print input parameters and environment variables
    logger.info("request: " + JSON.stringify(event.request));
    logger.info("env1: " + env1);


    endTime = process.uptime() * 1000;
    interval = endTime - startTime;
    logger.info("intervalTime: " + interval);
    logger.info("--------Finished-------");


    let res = new context.HTTPResponse(context.env, {
      "res-type": "context.env",
      "faas-content-type": "json"
    }, "application/json", "200");
    res.body = { "intervalTime": interval };
    callback(res);
  } catch (error) {
    logger.error("--------Error-------");
    logger.error("error: " + error);
    callback(error);
  }
};


module.exports.myHandler = myHandler;
准备函数部署包

上传的Node.js函数部署包须使用如下结构，处理程序所在代码文件，例如示例中的handler.js，必须在zip包根目录下，依赖项放到node_modules目录下。

my-function.zip
  |---- handler.js
  |---- node_modules
    |----async
    |----async-listener

可通过npm工具的相关命令，安装与管理依赖。例如npm install xxx命令（执行路径无限制）可将依赖xxx自动安装到根目录的node_modules文件夹下。

开发函数
创建函数
