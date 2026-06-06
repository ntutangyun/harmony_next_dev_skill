# ICPU_RUN_KF

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-icpu-run-kf_

除了func、blkdim以外，其他的变量都必须是通过GmAlloc分配的共享内存的指针，传入的参数的数量和顺序都必须和kernel保持一致。

调用示例
ICPU_RUN_KF(sort_kernel0, coreNum, (uint8_t*)x, (uint8_t*)y);
GmFree
ICPU_SET_TILING_KEY
