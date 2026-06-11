# 如何获取指定城市的天气数据

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/weather-service-faq-1_

先调用getAddressesFromLocationName方法获取指定城市的经纬度信息，然后根据返回的经纬度数据调用getWeather方法获取天气数据。
