# 获取检测平面的二维顶点数组时报错：“plane is nullptr!”，返回错误码：401

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-faq-1_

调用HMS_AREngine_ARPlane_GetPolygonSize获取检测到平面的二维顶点数组大小时报错：“plane is nullptr!”，返回错误码：401。

可能原因

初次打开应用还未识别到平面，调用HMS_AREngine_ARSession_GetAllTrackables获取的可跟踪对象列表为空，导致后续HMS_AREngine_ARTrackableList_AcquireItem获取对应索引的对象也为空，使用前未做有效性判断，使用时出现无效参数错误。

处理步骤

开发者从AR Engine获取平面之后需判断其有效性后使用，例如，进行非空判断。

AR Engine常见问题
摄像头被遮挡一段时间后再放开，输出的位姿有跳变
