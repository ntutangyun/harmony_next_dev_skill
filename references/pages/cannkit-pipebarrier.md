# PipeBarrier(ISASI)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-pipebarrier_

如下示例，Mul指令的输入dst0Local是Add指令的输出，两个矢量运算指令产生依赖，需要插入PipeBarrier保证两条指令的执行顺序。

注：仅作为示例参考，开启自动同步的情况下，编译器自动插入PIPE_V同步，无需开发者手动插入。

图1 Mul指令和Add指令是串行关系，必须等待Add指令执行完成后，才能执行Mul指令。

AscendC::LocalTensor<half> src0Local;
AscendC::LocalTensor<half> src1Local;
AscendC::LocalTensor<half> src2Local;
AscendC::LocalTensor<half> dst0Local;
AscendC::LocalTensor<half> dst1Local;


AscendC::Add(dst0Local, src0Local, src1Local, 512);
AscendC::PipeBarrier<PIPE_V>();
AscendC::Mul(dst1Local, dst0Local, src2Local, 512);
核内同步
TPosition
