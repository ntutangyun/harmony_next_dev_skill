# ReleaseEventID

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-releaseeventid_

AllocEventID、ReleaseEventID需成对出现，ReleaseEventID传入的TEventID需由对应的AllocEventID申请而来。

返回值

无

调用示例
AscendC::TEventID eventID = GetTPipePtr()->AllocEventID<AscendC::HardEvent::V_S>(); // 需要插入scalar与vector之间的同步，申请对应的HardEvent的ID
AscendC::SetFlag<AscendC::HardEvent::V_S>(eventID);
// ...
AscendC::WaitFlag<AscendC::HardEvent::V_S>(eventID);
GetTPipePtr()->ReleaseEventID<AscendC::HardEvent::V_S>(eventID); // 释放scalar等vector的同步HardEvent的ID
// ...
AllocEventID
FetchEventID
