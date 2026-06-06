# 迁移模式设置

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/networkboost-reporthandovermode_

let mode: netHandover.HandoverMode = netHandover.HandoverMode.DISCRETION;
  netHandover.setHandoverMode(mode);
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
连接迁移通知
连接迁移（多网并发）
