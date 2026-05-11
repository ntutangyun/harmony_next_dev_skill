# 模型转换前准备

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-preparing-for-model-conversion_

CANN Kit当前仅支持Caffe、TensorFlow、ONNX和MindSpore模型转换为离线模型，其他格式的模型需要开发者自行转换为CANN Kit支持的模型格式。

准备训练好的Caffe、TensorFlow、ONNX等模型。例如：Caffe SqueezeNet V1.0模型。

下载Tools，解压使用Tools下的OMG工具，将TensorFlow或Caffe模型转换为IR模型，使用方式请参见模型转换示例。

说明

若TensorFlow或Caffe模型过大，可以在OMG转换之前使用Tools下载的轻量化工具，使用方式请参见模型轻量化。

离线模型转换
模型转换示例
