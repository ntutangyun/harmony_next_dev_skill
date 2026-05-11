# 准备证书

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-certificates-config_

--BEGIN PUBLIC KEY-----
MIIBIjANBgkq*********************************vW7gQTM8BHFTezQjdRI
A7xka2TaVHt***********************************rOA3P5rew9cO96q/7Z
kQ6lRd3oVsf************************************rGYCrA2RVgr79mRx+
s22qfA5FdTC*************************************i6I2cRVb1grBQphR
yFBxCGC/NeV*************************************K1QM1SC4GCORHocS
MQvApBQwQF9*************************************eEQvwpVfFxg4dGBz
DQIDAQAB
-----END PUBLIC KEY-----
华为支付证书

华为支付证书是指由华为支付提供的，包含华为支付平台标识、公钥信息的证书。该证书算法为SM2。

商户请通过华为支付商户平台下载华为支付证书。

华为支付证书中的公钥用于商户对回调通知中的信息进行验签。

下载华为支付证书

登录华为支付商户平台后，通过“商户中心 > 证书管理 > 华为支付证书”页签进行华为支付证书下载，该证书用于校验华为支付给商户业务系统发送的信息，如支付结果信息等。

商户号绑定AppID
端侧应用配置
