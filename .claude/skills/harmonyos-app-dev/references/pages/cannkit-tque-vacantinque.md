# VacantInQue

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tque-vacantinque_

AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
AscendC::LocalTensor<half> tensor2 = que.AllocTensor<half>();
AscendC::LocalTensor<half> tensor3 = que.AllocTensor<half>();
AscendC::LocalTensor<half> tensor4 = que.AllocTensor<half>();
AscendC::LocalTensor<half> tensor5 = que.AllocTensor<half>();
que.EnQue(tensor1);// 将tensor1加入VECOUT的Queue中
que.EnQue(tensor2);// 将tensor2加入VECOUT的Queue中
que.EnQue(tensor3);// 将tensor3加入VECOUT的Queue中
que.EnQue(tensor4);// 将tensor4加入VECOUT的Queue中
ret = que.VacantInQue(); // 返回为false, 继续入队操作（EnQue）将报错
DeQue
HasTensorInQue
