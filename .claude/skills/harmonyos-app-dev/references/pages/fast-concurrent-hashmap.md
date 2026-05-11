# 使用ConcurrentHashmap在多线程下完成键值信息的查找维护

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-concurrent-hashmap_

FAST Kit提供的Concurrent HashMap（并发哈希表）专为高并发场景下的键值对数据管理而设计。它通过细粒度的锁策略实现多线程环境下的安全存储、快速访问与高效更新，适用于对并发吞吐量和数据一致性要求较高的增删改查操作，典型场景包括单点插入、删除、查询及并发修改等。

接口说明

具体API说明详见接口文档。

名称	描述
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Create (FAST_ConcurrentHashmap* handle, HMS_FAST_ConcurrentHashmap_HashFunc hasher, HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler, float maxLoadFac, size_t numShards)	使用给定配置创建并发哈希表。
void HMS_FAST_ConcurrentHashmap_Destroy (FAST_ConcurrentHashmap* handle)	销毁指定并发哈希表。
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Insert (FAST_ConcurrentHashmap* handle, const FAST_ConcurrentHashmapKeyPtr key, const FAST_ConcurrentHashmapValuePtr value, FAST_ConcurrentHashmapValuePtr* originValue)	将给定的键值对插入并发哈希表中，如果键已经存在，则使用value覆写原有的值，并将对应值的地址保存在originValue中。
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Find (FAST_ConcurrentHashmap* handle, const FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr* value)	在给定并发哈希表中查找输入的键，并将对应的值保存在value中。
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_Erase (FAST_ConcurrentHashmap* handle, const FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapKeyPtr* originKey, FAST_ConcurrentHashmapValuePtr* originValue)	在给定哈希表中删除输入的键，并将键/值对应的地址保存在originKey和originValue中。
FAST_ErrorCode HMS_FAST_ConcurrentHashmap_TryInsert (FAST_ConcurrentHashmap* handle, const FAST_ConcurrentHashmapKeyPtr key, const FAST_ConcurrentHashmapValuePtr value)	将给定的键值对插入并发哈希表中，如果键已经存在、则不做操作。
size_t HMS_FAST_ConcurrentHashmap_Size (FAST_ConcurrentHashmap* handle)	返回给定哈希表当前的元素个数。
void HMS_FAST_ConcurrentHashmap_Clear (FAST_ConcurrentHashmap* handle)	清空给定哈希表中维护的所有元素。
size_t HMS_FAST_ConcurrentHashmap_EraseIf (FAST_ConcurrentHashmap* handle, HMS_FAST_ConcurrentHashmap_HookFunc condFunc, void* condCtx, HMS_FAST_ConcurrentHashmap_HookFunc freeFunc, void* freeCtx)	删除哈希表中符合开发者定义条件的所有元素，并使用开发者定义的方式释放其内存。
void HMS_FAST_ConcurrentHashmap_Traverse (FAST_ConcurrentHashmap* handle, HMS_FAST_ConcurrentHashmap_HookFunc condFunc, void* condCtx, HMS_FAST_ConcurrentHashmap_HookFunc workFunc, void* workCtx)	遍历哈希表，将所有符合开发者输入条件的键值对按开发者给定的方式修改。
开发步骤

在CMake脚本中链接相关动态库。

target_link_libraries(entry PUBLIC libfast_ads.so)

定义哈希值如何计算，键如何比较。

#include "FASTKit/fast_ads_concurrent_hashmap.h"


uint64_t custom_hash_int(const FAST_ConcurrentHashamapKeyPtr key) {
    static std::hash<int> hasher;
    int* intKey = (int*)key;
    return hasher(*intKey);
}


int32_t custom_equal_int(const FAST_ConcurrentHashmapKeyPtr key1, const FAST_ConcurrentHashmapKeyPtr key2) {
    int* intKey1 = (int*)key1;
    int* intKey2 = (int*)key2;
    return (*intKey1) == (*intKey2);
}

使用合适的配置创建并发哈希表，负载因子（loadfac）和分段数（numShards）的典型值一般为0.8和64。负载因子主要作用于分段内部，更大的负载因子通常意味着更小的内存消耗和更大的操作开销；分段数主要作用域并发哈希表全局，更大的分段数通常意味着更好的并发性能和更大的内存消耗。

FAST_ConcurrentHashmapHandle handle;
HMS_FAST_ConcurrentHashmap_HashFunc hasher = &custom_hash_int;
HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler = &custom_equal_int;
float loadfac = 0.8;
size_t numShards = 64;
int ret = HMS_FAST_ConcurrentHashmap_Create(&handle, hasher, equaler, loadfac, numShards);
EXPECT_EQ(ret, FAST_ErrorCode::FAST_ERROR_CODE_SUCCESS);

向并发哈希表中插入键值对。

// 初始化空的哈希表
int* key0 = new int{0};
int* val0 = new int{0};
ret = HMS_FAST_ConcurrentHashmap_Insert(
    handle,
    (FAST_ConcurrentHashmapKeyPtr)key0,
    (FAST_ConcurrentHashmapValuePtr)val0,
    nullptr
); // {0: 0}


// 或者
int key1 = 1;
int val1 = 1;
ret = HMS_FAST_ConcurrentHashmap_Insert(
    handle,
    (FAST_ConcurrentHashmapKeyPtr)&key1,
    (FAST_ConcurrentHashmapValuePtr)&val1,
    nullptr
); // {0: 0, 1: 1}


// 使用insert覆写已有的key，如果使用tryInsert则不会覆写
int key2 = 1;
int val2 = 2;
int* originVal;
ret = HMS_FAST_ConcurrentHashmap_Insert(
    handle,
    (FAST_ConcurrentHashmapKeyPtr)&key2,
    (FAST_ConcurrentHashmapValuePtr)&val2,
    (FAST_ConcurrentHashmapValuePtr*)&originVal
); // {0： 0， 1: 2}, 且originVal == &val1

开发者使用键查找对应的值，并将结果保存在输入指针中。开发者需注意在使用此接口时应校验返回值ret，如果ret值不等于FAST_ERROR_CODE_SUCCESS，则res获取到的值是无效的。

// 预先插入元素 {0： 0， 1： 2}
int targetKey = 1;
int* res;
ret = HMS_FAST_ConcurrentHashmap_Find(
    handle,
    (FAST_ConcurrentHashmapKeyPtr)&targetKey,
    (FAST_ConcurrentHashmapValuePtr*)&res
);
EXPECT_EQ(ret == FAST_ERROR_CODE_SUCCESS);
EXPECT_EQ((*res) == 2);

开发者使用键删除并发哈希表中对应的键值对，并获取关联内存的地址。

// 预先插入元素 {0： 0， 1： 2}
// 使用originKey/Val获得预先插入的元素地址，便于内存管理
int* originKey;
int* originVal;
int deleteKey = 0;
ret = HMS_FAST_ConcurrentHashmap_Erase(
    handle,
    (FAST_ConcurrentHashmapKeyPtr)&deleteKey,
    (FAST_ConcurrentHashmapKeyPtr*)&originKey,
    (FAST_ConcurrentHashmapValuePtr*)&originVal
);
delete originKey;
delete originVal;


// 如果不需要获取地址，也可直接使用nullptr
deleteKey = 1;
ret = HMS_FAST_ConcurrentHashmap_Erase(
    handle,
    (FAST_ConcurrentHashmapKeyPtr)&deleteKey,
    nullptr, nullptr
);

开发者查询并发哈希表当前元素个数。

// 预先插入元素 {0： 0， 1： 2}
// 需注意在重度的并发场景下，该方法获取到的尺寸与实际尺寸可能存在细微差异
size_t curSize = HMS_FAST_ConcurrentHashmap_Size(handle);
EXPECT_EQ(curSize == 2);

开发者清空并发哈希表中所有元素。

// 预先插入元素 {0： 0， 1： 2}
HMS_FAST_ConcurrentHashmap_Clear(handle);
curSize = HMS_FAST_ConcurrentHashmap_Size(handle);
EXPECT_EQ(curSize == 0);

开发者遍历给定并发哈希表，并删除或修改符合输入条件的所有键值对。

// 删除key为偶数的键值对
int32_t coustom_erase_cond(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
    int* intKey = (int*)key;
    if ((*intKey) % 2 == 0) {
        return 1;
    }
    return 0;
}


// 释放键和值指针持有的内存
int32_t custom_free(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
    int* intKey = (int*)key;
    int* intVal = (int*)val;
    delete intKey;
    delete intVal;
    return 0;
}


// 对哈希表中所有元素执行修改，也可传入nullptr达到相同效果
int32_t custom_modify_cond(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
    return 1;
}


int32_t custom_work(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
    int* intVal = (int*)val;
    int* intCtx = (int*)context;
    *intVal += (*intCtx);
    return 1;
}


// 预先插入元素 {1： 1， 3： 3， 5： 5}
for (int i = 0; i < 6; i += 2) {
    int* key = new int{i};
    int* val = new int{i};
    ret = HMS_FAST_ConcurrentHashmap_Insert(
        handle,
        (FAST_ConcurrentHashmapKeyPtr)key,
        (FAST_ConcurrentHashmapValuePtr)val,
        nullptr
    );
} // {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


// EraseIf接口返回被删除的元素的个数
ret = HMS_FAST_ConcurrentHashmap_EraseIf(
    handle,
    (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_erase_cond,
    nullptr,
    (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_free,
    nullptr
); // {1： 1， 3： 3， 5： 5}
EXPECT_EQ(ret == 3);


int context = 10;
HMS_FAST_ConcurrentHashmap_Traverse(
    handle,
    (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_modify_cond,
    nullptr,
    (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_work,
    (void*)&context
); // {1: 11, 3: 13, 5: 15}
使用RectPartition求解矩形划分
使用DSP进行向量计算
