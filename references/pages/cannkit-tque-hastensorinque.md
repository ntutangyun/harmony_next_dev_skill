# HasTensorInQue

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tque-hastensorinque_

// 根据HasTensorInQue判断当前Queue中是否有已入队的Tensor，当前Queue的深度为4，无内存EnQue动作，返回为false
AscendC::TPipe pipe;
AscendC::TQue<AscendC::TPosition::VECOUT, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
bool ret = que.HasTensorInQue();
VacantInQue
GetTensorCountInQue
