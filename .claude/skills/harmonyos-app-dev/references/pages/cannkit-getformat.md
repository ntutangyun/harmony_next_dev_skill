# GetFormat

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getformat_

Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}},       // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}},  // format
              kFollowing,                                  // placement
              ge::DT_FLOAT16,                              // dt
              nullptr};
auto fmt = tensor.GetFormat();
SetOriginFormat
MutableFormat
