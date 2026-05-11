# 更多样例

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkitvectorcalculation-binocularinstructions_

__aicore__ inline void Init(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
    {
        src0Global.SetGlobalBuffer((__gm__ int16_t*)src0Gm);
        src1Global.SetGlobalBuffer((__gm__ int16_t*)src1Gm);
        dstGlobal.SetGlobalBuffer((__gm__ int16_t*)dstGm);
        pipe.InitBuffer(inQueueSrc0, 1, 512 * sizeof(int16_t));
        pipe.InitBuffer(inQueueSrc1, 1, 512 * sizeof(int16_t));
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
        AscendC::LocalTensor<int16_t> src0Local = inQueueSrc0.AllocTensor<int16_t>();
        AscendC::LocalTensor<int16_t> src1Local = inQueueSrc1.AllocTensor<int16_t>();
        AscendC::DataCopy(src0Local, src0Global, 512);
        AscendC::DataCopy(src1Local, src1Global, 512);
        inQueueSrc0.EnQue(src0Local);
        inQueueSrc1.EnQue(src1Local);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<int16_t> src0Local = inQueueSrc0.DeQue<int16_t>();
        AscendC::LocalTensor<int16_t> src1Local = inQueueSrc1.DeQue<int16_t>();
        AscendC::LocalTensor<int16_t> dstLocal = outQueueDst.AllocTensor<int16_t>();
  
        AscendC::Add(dstLocal, src0Local, src1Local, 512);
 
        outQueueDst.EnQue<int16_t>(dstLocal);
        inQueueSrc0.FreeTensor(src0Local);
        inQueueSrc1.FreeTensor(src1Local);
    }
    __aicore__ inline void CopyOut()
    {
        AscendC::LocalTensor<int16_t> dstLocal = outQueueDst.DeQue<int16_t>();
        AscendC::DataCopy(dstGlobal, dstLocal, 512);
        outQueueDst.FreeTensor(dstLocal);
    }
private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueSrc0, inQueueSrc1;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueueDst;
    AscendC::GlobalTensor<int16_t> src0Global, src1Global, dstGlobal;
};
  
extern "C" __global__ __aicore__ void add_simple_kernel(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
{
    KernelAdd op;
    op.Init(src0Gm, src1Gm, dstGm);
    op.Process();
}
Or
标量双目指令
