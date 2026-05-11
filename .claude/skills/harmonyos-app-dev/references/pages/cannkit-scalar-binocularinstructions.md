# 更多样例

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalar-binocularinstructions_

__aicore__ inline void Init(__gm__ uint8_t* src, __gm__ uint8_t* dstGm)
    {
        srcGlobal.SetGlobalBuffer((__gm__ int16_t*)src);
        dstGlobal.SetGlobalBuffer((__gm__ int16_t*)dstGm);
        pipe.InitBuffer(inQueueSrc, 1, 512 * sizeof(int16_t));
        pipe.InitBuffer(outQueueDst, 1, 512 * sizeof(int16_t));
    }
    __aicore__ inline void Process()
    {
        CopyIn();
        Compute();
        CopyOut();
    }
private:
    __aicore__ inline void CopyIn()
    {
        AscendC::LocalTensor<int16_t> srcLocal = inQueueSrc.AllocTensor<int16_t>();
        AscendC::DataCopy(srcLocal, srcGlobal, 512);
        inQueueSrc.EnQue(srcLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<int16_t> srcLocal = inQueueSrc.DeQue<int16_t>();
        AscendC::LocalTensor<int16_t> dstLocal = outQueueDst.AllocTensor<int16_t>();
        int16_t scalar = 2;
        AscendC::Adds(dstLocal, srcLocal, scalar, 512);
         
        outQueueDst.EnQue<int16_t>(dstLocal);
        inQueueSrc.FreeTensor(srcLocal);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<int16_t> dstLocal = outQueueDst.DeQue<int16_t>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        outQueueDst.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    AscendC::GlobalTensor<int16_t> srcGlobal, dstGlobal;
};
extern "C" __global__ __aicore__ void binary_scalar_simple_kernel(__gm__ uint8_t* src, __gm__ uint8_t* dstGm)
{
    KernelBinaryScalar op;
    op.Init(src, dstGm);
    op.Process();
}
LeakyRelu
标量三目指令
