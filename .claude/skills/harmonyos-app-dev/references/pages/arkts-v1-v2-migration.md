# V1

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration_

@ObjectLink/@Observed/@Track -> @ObservedV2/@Trace。


@ObjectLink	@ObservedV2、@Trace	直接兼容，@ObjectLink需要被@Observed装饰的class的实例初始化，主要应用于观察嵌套类场景。在状态管理V2中可以使用@ObservedV2@Trace。详情见迁移场景---@ObjectLink/@Observed/@Track -> @ObservedV2/@Trace。
@Track	@Trace	

V1装饰器@Track为精确观察，不使用则无法做到类属性的精准观察。

V2@Trace装饰的属性可以被精确跟踪观察。详情见迁移场景---@ObjectLink/@Observed/@Track -> @ObservedV2/@Trace。


@Provide、@Consume	@Provider、@Consumer	兼容。详情见@Provide/@Consume迁移场景。
@Watch	@Monitor	

@Watch用于监听V1状态变量的变化，具有监听状态变量本身和其第一层属性变化的能力。状态变量可观察到的变化会触发其@Watch监听事件，详情见迁移场景--@Watch -> @Monitor。

@Monitor用于监听V2状态变量的变化，搭配@Observed和@Trace一起使用，可有深层监听的能力。状态变量在一次事件中多次变化时，仅会以最终的结果判断是否触发@Monitor监听事件。


无计算属性能力	@Computed	状态管理V1无计算属性相关能力，状态管理V2可使用@Computed避免重复计算。详情见迁移场景--重复计算->@Computed计算属性。
LocalStorage	@ObservedV2、@Trace	兼容。详情见迁移场景--LocalStorage->@ObservedV2/@Trace。
AppStorage	AppStorageV2	兼容。详情见迁移场景--AppStorage->AppStorageV2。
Environment	调用Ability接口获取系统环境变量	Environment获取环境变量能力和AppStorage耦合。在V2中可直接调用Ability接口获取系统环境变量。详情见迁移场景--Environment->调用Ability接口直接获取系统环境变量。
PersistentStorage	PersistenceV2	PersistentStorage持久化能力和AppStorage耦合，PersistenceV2持久化能力可独立使用。详情见迁移场景--PersistentStorage->PersistenceV2。
状态管理V1向V2逐步迁移策略

对于已经使用V1开发的大型应用，通常难以一次性从V1迁移到V2，而是需要分批次、分组件地逐步迁移；首先考虑将V1组件迁移为V2组件，这部分可以参考状态管理V1向V2迁移场景进行适配。

迁移过程中由于V1与V2存在共存的情况，这就必然会带来V1和V2的混用。针对混用的场景，可以参考状态管理V1和V2混用场景进行适配，并最终完成V1->V2的全量适配。

状态管理V1-V2迁移指导
状态管理V1向V2迁移场景
