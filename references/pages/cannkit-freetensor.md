# FreeTensor

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-freetensor_

AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 2> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.FreeTensor<half>(tensor1);
AllocTensor
EnQue
