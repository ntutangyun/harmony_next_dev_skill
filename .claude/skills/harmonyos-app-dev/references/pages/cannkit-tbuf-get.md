# Get

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tbuf-get_

AscendC::TBuf<AscendC::TPosition::VECCALC> calcBuf; // 模板参数为TPosition中的VECCALC类型
uint32_t byteLen = 1024;
pipe.InitBuffer(calcBuf, byteLen);
// 从calcBuf获取Tensor,Tensor为pipe分配的所有内存大小，为1024Bytes
AscendC::LocalTensor<int32_t> tempTensor1 = calcBuf.Get<int32_t>();
// 从calcBuf获取Tensor,Tensor为128个int32_t类型元素的内存大小，为512Bytes
AscendC::LocalTensor<int32_t> tempTensor1 = calcBuf.Get<int32_t>(128);
/* 在相对复杂计算场景，可以使用TBuf作为临时变量，存储中间计算结果，避免复杂的出队，入队过程。
 * 下面代码来源于某种距离计算的API中,C矩阵需要除以A矩阵和B矩阵的点乘结果。在该算法中所有矩阵均提前转换成向量。
 */
auto normADotB = calcBuf.Get<int32_t>(); // 存储A矩阵和B矩阵点乘后的结果
auto normB = qidVecIn.AllocTensor<DTypeOut>();
// ...
normB= qidVecIn.DeQue<DTypeOut>(); // 获取B矩阵
for(int i = 0; i < tiling.baseM; i++) {
   AscendC::Muls(normADotB[i * tiling.baseN], normB, normA.GetValue(i), tiling.baseN); // A矩阵和B矩阵均转换为向量后做数乘，normADotB作为临时变量存储结果。
}
qidVecIn.FreeTensor(normB);
// ...
for(int i = 0; i < tiling.baseM; i++) {
   AscendC::Mul(baseCVecFloat[i * tiling.baseN], baseCVecFloat[i * tiling.baseN], normADotB[i * tiling.baseN], tiling.baseN); // 通过计算获取C矩阵，并除以normADotB
}
构造函数
GetWithOffset
