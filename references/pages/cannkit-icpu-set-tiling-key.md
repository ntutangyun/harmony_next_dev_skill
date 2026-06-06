# ICPU_SET_TILING_KEY

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-icpu-set-tiling-key_

未使用该接口设置tilingKey的情况下，tilingKey将会为默认值0，在调测执行时，会有告警提示Tiling Key是0，并继续进行调测。如果核函数中有tilingKey分支，将会执行tilingKey为0的分支，其他tilingKey对应的分支不会执行。

tilingKey建议传入正整数，如果设置为负数或者0，将会告警并继续调测。如果传入0，将会执行tilingKey为0的分支；tilingKey传入负数，将导致未定义的行为。

该接口需要在ICPU_RUN_KF前调用。

调用示例
ICPU_SET_TILING_KEY(10086)
ICPU_RUN_KF(sort_kernel0, coreNum, (uint8_t*)x, (uint8_t*)y);
ICPU_RUN_KF
基础数据结构和接口
