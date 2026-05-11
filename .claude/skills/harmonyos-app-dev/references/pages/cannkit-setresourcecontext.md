# SetResourceContext

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setresourcecontext_

graphStatus SetResourceContext(const ge::AscendString &key, ResourceContext *resource_context)
参数说明
参数名	输入/输出	描述
key	输入	资源唯一标识。
resource_context	输入	资源上下文对象指针，可参见GetResourceContext接口的返回值。
返回值

graphStatus：GRAPH_SUCCESS，代表成功；GRAPH_FAILED，代表失败。

约束说明

若使用Create接口创建InferenceContext时未传入resource context管理器指针，则该接口返回失败。

GetResourceContext
RegisterReliedOnResourceKey
