# 数据类型转换说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-arraybuffer-info_

在一些不支持接收ArrayBuffer数据类型的方法中，需要将其反序列化为int32或者float32类型，涉及转换的接口列表如下：

接口名	描述
ImageComponent	参数buffer为ArrayBuffer类型，可转换为int32。
ARPlane.getPolygonXZ	返回值为ArrayBuffer类型，可转换为float32。
ARSceneMesh.getVertices	返回值为ArrayBuffer类型，可转换为float32。
ARSceneMesh.getVertexNormals	返回值为ArrayBuffer类型，可转换为float32。
ARSceneMesh.getTriangleIndices	返回值为ArrayBuffer类型，可转换为int32。
ARSemanticDensePointData	参数id为ArrayBuffer类型，可转换为int32。
ARSemanticDensePointData	参数position为ArrayBuffer类型，可转换为float32。
ARSemanticDensePointData	参数color为ArrayBuffer类型，可转换为int32。

转换的示例如下：

// ArrayBuffer转float32
function arrayBufferFloat32ToNumber(buffer: ArrayBuffer): number[] {
  let view: Float32Array = new Float32Array(buffer);
  let numberArray: number[] = Array.from(view);
  return numberArray;
}


// ArrayBuffer转int32
function arrayBufferInt32ToNumber(buffer: ArrayBuffer): number[] {
  let view: Int32Array = new Int32Array(buffer);
  let numberArray: number[] = Array.from(view);
  return numberArray;
}
某些特殊场景下（如附近存在磁场干扰、手机发烫或扫描到重复纹理等），出现平面漂移或者位姿数据跳变现象
个人数据处理说明
