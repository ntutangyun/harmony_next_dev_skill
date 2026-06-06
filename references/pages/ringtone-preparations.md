# 设置铃声

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ringtone-preparations_

let ringtoneTypeList: Array<ringtone.RingtoneType> = ringtone.getSupportedRingtoneTypes();
hilog.info(DOMAIN, APP_TAG,'getSupportedRingtoneTypes : ' + JSON.stringify(ringtoneTypeList));

调用ringtone.getSupportedDataTypes接口，查询支持的数据类型。当前支持格式：MP3，OGG，FLAC，AAC，MP2，M4A。

// 其中 ringtone.RingtoneType.NOTIFICATION 为通知铃声
let dataTypeList: Array<uniformTypeDescriptor.UniformDataType> = ringtone.getSupportedDataTypes(ringtone.RingtoneType.NOTIFICATION);
hilog.info(DOMAIN, APP_TAG,'getSupportedDataTypes: ' + JSON.stringify(dataTypeList));

调用ringtone.startRingtoneSetting接口拉起设置弹窗，用户设置铃声后返回设置的铃声类型。

通过promise异步方式：

// 详细代码参考API参考
let prefixUri: string = '';
let audioPath: string = prefixUri + '/' + this.buttonText;
let fileName: string = audioPath.substring(audioPath.lastIndexOf('/') + 1, audioPath.lastIndexOf('.'));
await ringtone.startRingtoneSetting(this.context, audioPath, fileName).then(res => {
  hilog.info(DOMAIN, APP_TAG,'setFlag :' + res);
});

通过callback异步方式：

// 详细代码参考API参考
let prefixUri: string = '';
let audioPath: string = prefixUri + '/' + this.buttonText;
let fileName: string = audioPath.substring(audioPath.lastIndexOf('/') + 1, audioPath.lastIndexOf('.'));
ringtone.startRingtoneSetting(this.context, audioPath, fileName, (err, data) => {
  hilog.info(DOMAIN, APP_TAG,'setFlag :' + data);
});

调用ringtone.getSupportedMaxDuration接口，获取当前铃声支持的最大时长。

// 其中 ringtone.RingtoneType.MESSAGE 为短信铃声
let maxDuration: number =
  ringtone.getSupportedMaxDuration(ringtone.RingtoneType.MESSAGE, uniformTypeDescriptor.UniformDataType.MP3)
hilog.info(DOMAIN, APP_TAG,'getSupportedMaxDuration: ' + maxDuration);
Ringtone Kit简介
Scan Kit（统一扫码服务）
