# GetBlockIdx

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getblockidx_

__aicore__ inline void Init(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
    {
        // 根据index对每个核进行地址偏移
        src0Global.SetGlobalBuffer((__gm__ float*)src0Gm + AscendC::GetBlockIdx() * SINGLE_CORE_OFFSET);
        src1Global.SetGlobalBuffer((__gm__ float*)src1Gm + AscendC::GetBlockIdx() * SINGLE_CORE_OFFSET);
        dstGlobal.SetGlobalBuffer((__gm__ float*)dstGm + AscendC::GetBlockIdx() * SINGLE_CORE_OFFSET);
        pipe.InitBuffer(inQueueSrc0, 1, 256 * sizeof(float));
        pipe.InitBuffer(inQueueSrc1, 1, 256 * sizeof(float));
        pipe.InitBuffer(selMask, 1, 256);
        pipe.InitBuffer(outQueueDst, 1, 256 * sizeof(float));
    }
    // ...
};
GetBlockNum
调测接口
