# Init

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tpipe-init_

__aicore__ inline void Init(GM_ADDR src_gm, GM_ADDR dst_gm, uint32_t srcSize, TPipe *pipe)
    {
        src_global.SetGlobalBuffer(reinterpret_cast<__gm__ srcType *>(src_gm), srcSize);
        dst_global.SetGlobalBuffer(reinterpret_cast<__gm__ srcType *>(dst_gm), srcSize);
        pipe->InitBuffer(inQueueX, 1, srcSize * sizeof(srcType));
        pipe->InitBuffer(outQueue, 1, srcSize * sizeof(srcType));
        bufferSize = srcSize;
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
        AscendC::LocalTensor<srcType> srcLocal = inQueueX.AllocTensor<srcType>();
        AscendC::DataCopy(srcLocal, src_global, bufferSize);
        inQueueX.EnQue(srcLocal);
    }
    __aicore__ inline void Compute()
    {
        AscendC::LocalTensor<srcType> dstLocal = outQueue.AllocTensor<srcType>();
        AscendC::LocalTensor<srcType> srcLocal = inQueueX.DeQue<srcType>();
        int16_t scalar_value = 3;
        AscendC::Muls(dstLocal, srcLocal, (srcType)scalar_value, bufferSize);
        outQueue.EnQue<srcType>(dstLocal);
        inQueueX.FreeTensor(srcLocal);
    }
    __aicore__ inline void CopyOut(uint32_t offset)
    {
        AscendC::LocalTensor<srcType> dstLocal = outQueue.DeQue<srcType>();
        AscendC::DataCopy(dst_global, dstLocal, bufferSize);
        outQueue.FreeTensor(dstLocal);
    }
private:
    AscendC::GlobalTensor<srcType> src_global;
    AscendC::GlobalTensor<srcType> dst_global;
    AscendC::TQue<AscendC::QuePosition::VECIN, 1> inQueueX;
    AscendC::TQue<AscendC::QuePosition::VECOUT, 1> outQueue;
    uint32_t bufferSize = 0;
};
template <typename dataType> 
__aicore__ void kernel_Test_operator(GM_ADDR src_gm, GM_ADDR dst_gm, uint32_t srcSize)
{
    KernelAsin<dataType> op;
    AscendC::TPipe pipeIn;
    for (uint32_t index =0; index < 1; index++) {
        if (index != 0) {
            pipeIn.Init();
        }
        op.Process();
        pipeIn.Destroy();
        AscendC::TPipe pipeCast;
        op.Init(src_gm, dst_gm, srcSize, &pipeCast);
        op.Process();
        pipeCast.Destroy();
    }
}
InitBuffer
Destroy
