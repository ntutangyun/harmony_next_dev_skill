# 开发函数

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-funccoding_

-----Start-------");
    try {
        let startTime = new Date().getTime();
        let endTime = startTime;
        let interval = 0;
        startTime = process.uptime() * 1000;


        // print input parameters and environment variables
        let request = event.body ? JSON.parse(event.body): event;
        logger.info("request: " + JSON.stringify(request));
        logger.info("env1: " + env1);


        endTime = process.uptime() * 1000;
        interval = endTime - startTime;
        logger.info("intervalTime: " + interval);
        logger.info("--------Finished-------");


        let res = new context.HTTPResponse(context.env, {
            "res-type": "context.env",
            "faas-content-type": "json",
        }, "application/json", "200");
        res.body = {"intervalTime": interval};
        callback(res);
    } catch (error) {
        logger.error("--------Error-------");
        logger.error("error: " + error);
        callback(error);
    }
};


module.exports.myHandler = myHandler;
注意

云函数之间是相互独立的，部署至云侧时，只会部署所选云函数目录下的文件，不可在一个云函数中通过import '../anotherDirectory/xxx'的方式引入依赖。如果有多个云函数公共的配置，建议存储在云数据库中，通过云数据库Server API类查询出公共配置；也可以将多个云函数整合成一个云对象，将公共配置变成云对象的私有配置。

（可选）如函数存在依赖关系，可在“package.json”文件的“dependencies”下添加需要的依赖，然后点击右上角“Sync Now”。
下文以添加“@hw-agconnect/cloud-server”依赖为例进行说明，请添加实际业务所需的依赖。
说明

右击“package.json”文件，选择“Run 'npm install'”菜单，也可以实现依赖包安装。

所有安装的依赖包都会存储在当前函数的“node_modules”目录下。

创建并配置函数
调试函数
