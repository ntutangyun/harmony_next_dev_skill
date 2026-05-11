# 个人数据处理说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-personal-data_

（可选）华为账号信息	如果开发者在初始化Cloud Foundation Kit时携带了华为账号信息，Cloud Foundation Kit在访问云侧接口时会携带该账号信息用于资源的访问权限控制。	

端侧不保存信息，云侧信息将保存至如下时刻：

- 最终用户或开发者主动删除上传的数据

- 开发者主动删除整个项目


（可选）用户凭证信息	Cloud Foundation Kit的预加载能力是一种数据传输通道，开发者可以通过该通道传递用户凭证信息给自己的服务器，以对预加载资源进行访问权限控制。	直接透传给开发者服务器，由开发者自行处理，华为不保存该信息。
指导开发者如何帮助最终用户实现对数据的控制

如何清除最终用户的数据

最终用户或开发者主动删除上传的数据
清除云存储中的用户数据：可通过StorageBucket.deleteFile接口删除通过云存储上传的用户数据。
清除云数据库中的用户数据：可通过DatabaseZone.delete接口删除写入云数据库的用户数据。
开发者主动删除整个项目

如何导出最终用户的数据

不涉及

运行应用时报“XXX Read timed out”异常
附录
