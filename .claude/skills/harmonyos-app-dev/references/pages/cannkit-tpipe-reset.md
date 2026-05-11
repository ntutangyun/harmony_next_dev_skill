# Reset

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tpipe-reset_

AscendC::TQue<AscendC::TPosition::VECOUT, 1> que; // 输出数据Queue队列管理对象，QuePosition为VECOUT
uint8_t num = 1;
uint32_t len = 192 * 1024;
for (int i = 0; i < 2; i++) {
    pipe.InitBuffer(que, num, len);
    // ... // process
    pipe.Reset();
}
Destroy
AllocEventID
