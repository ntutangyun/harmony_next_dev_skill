# GetShapeSize

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshapesize_

Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}},       // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}},  // format
              kOnDeviceHbm,                                // placement
              ge::DT_FLOAT16,                              // dt
              nullptr};
auto shape_size = tensor.GetShapeSize(); // 16*3*224*224
构造函数
GetData
