# netcopilot工具

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-netcopilot_

---------+------------------------------+
  | ScenarioID | ScenarioName                 |
  +------------+------------------------------+
  1            | 进出电梯
  2            | 离家断开WLAN
  3            | 到家连上WLAN
  4            | 人员拥挤的饭堂
  5            | 信号弱的地库
  6            | 乘坐地铁
  7            | 乘坐高铁（多SIM切换）
  8            | 高速公路自驾
  +------------+------------------------------+
启动场景模拟
> hdc shell netcopilot -s 4
Success to simulate scenario 4
停止场景模拟
> hdc shell netcopilot -c 4
Clear active net scenario success
新增自定义场景
> hdc shell netcopilot -a "{\"scenarioName\":\"自定义场景1\",\"uplinkBandwidth\":100000,\"downlinkBandwidth\":500000,\"uplinkLatency\":200,\"downlinkLatency\":200,\"uplinkDropRate\":0.05,\"downlinkDropRate\":0.01}"
注意

自定义场景子参数需要转成json字符串。

查看自定义场景详情
> hdc shell netcopilot -P 1000
Scenario Name: 自定义场景1
Uplink Bandwidth: 100000Kbps
Downlink Bandwidth: 500000Kbps
Uplink Latency: 200ms
Downlink Latency: 200ms
Uplink Drop Rate: 0.05%
Downlink Drop Rate: 0.01%
删除自定义场景
> hdc shell netcopilot -d 1000
Delete custom scenario success
rawheap-translator工具
二进制签名工具
