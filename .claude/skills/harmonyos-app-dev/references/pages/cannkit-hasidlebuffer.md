# HasIdleBuffer

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-hasidlebuffer_

AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
bool ret = que.HasIdleBuffer(); // 没有AllocTensor的操作，返回值为true
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
ret = que.HasIdleBuffer(); // AllocTensor了一块内存，返回值为true
AscendC::LocalTensor<half> tensor2 = que.AllocTensor<half>();
AscendC::LocalTensor<half> tensor3 = que.AllocTensor<half>();
AscendC::LocalTensor<half> tensor4 = que.AllocTensor<half>();
ret = que.HasIdleBuffer(); // AllocTensor了四块内存，当前无空闲内存，返回值为false，继续AllocTensor会报错
GetTensorCountInQue
FreeAllEvent
