# 共享联系人信息到分享推荐区

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-intents-share_

let context: Context = uiContext.getHostContext() as Context;
insightIntent.shareIntent(context, [intent]).then(() => {
  console.info('shareIntent ok');
}).catch((err: BusinessError) => {
  console.error(`shareIntent failed. Code: ${err.code}. message: ${err.message}`);
});
判断应用是否被系统分享拉起
目标应用设计规范
