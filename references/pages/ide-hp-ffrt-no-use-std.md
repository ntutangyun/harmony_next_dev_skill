# @performance/hp

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-ffrt-no-use-std_

// ffrt::submit中使用了pthread_rwlock_wrlock或pthread_rwlock_rdlock
    void PositiveCase4(int temp) {
    int a = 0;
    ffrt_rwlock_t mtx;
    ffrt::submit(
        [&]() {
        int ret = ffrt_rwlock_wrlock(&mtx);
        if (ret != ffrt_success) {
            printf("error\n");
        }
        a++;
        ret = ffrt_rwlock_unlock(&mtx);
        if (ret != ffrt_success) {
            printf("error\n");
        }
    }, {}, {});
    ffrt::submit(
        [&]() {
        int ret = ffrt_rwlock_rdlock(&mtx);
        if (ret != ffrt_success) {
            printf("error\n");
        }
        printf("sum is %d\n", a);
        ret = ffrt_rwlock_unlock(&mtx);
        if (ret != ffrt_success) {
            printf("error\n");
        }
    }, {}, {});
}

反例
#include <iostream>
#include <algorithm>
#include <mutex>
#include <condition_variable>
#include <unistd.h>
// ffrt头文件 
#include "ffrt/ffrt.h" 
using namespace std;
int N = 100;
int M = 100;
// ffrt::submit中使用了std::mutex
    void NegativeCase1(int temp) {
    std::mutex lock;
    int acc = 0;
    for (int i = 0; i < N; ++i) {
        ffrt::submit(
            [&]() {
                for (int j = 0; j < M; ++j) {
                    lock.lock();
                    acc++;
                    lock.unlock();
                }
            },
            {}, {});
    }
}
// ffrt::submit中使用了std::condition_variable
    void NegativeCase2(int temp) {
    std::condition_variable cond;
    int a = 0;
    std::mutex lock_;
    ffrt::submit(
        [&]() {
            std::unique_lock<std::mutex> lck(lock_);
            cond.wait(lck, [&] { return a == 1; });
        },
        {}, {});
    ffrt::submit(
        [&]() {
            std::unique_lock<std::mutex> lck(lock_);
            a = 1;
            cond.notify_one();
        },
        {}, {});
    ffrt::wait();
}
// ffrt::submit中使用了std::usleep
    void NegativeCase3(int temp) {
    ffrt::submit(
        [&]() {
        usleep(100);
        printf("test");
        ffrt_yield();
    }, {}, {});
}
// ffrt::submit中使用了pthread_rwlock_wrlock或pthread_rwlock_rdlock
    void NegativeCase4(int temp) {
    int a = 0;
    pthread_rwlock_t mtx;
    ffrt::submit(
        [&]() {
        int ret = pthread_rwlock_wrlock(&mtx);
        if (ret != 0) {
            printf("error\n");
        }
        a++;
        ret = pthread_rwlock_unlock(&mtx);
        if (ret != 0) {
            printf("error\n");
        }
    }, {}, {});
    ffrt::submit(
        [&]() {
        int ret = pthread_rwlock_rdlock(&mtx);
        if (ret != 0) {
            printf("error\n");
        }
        printf("sum is %d\n", a);
        ret = pthread_rwlock_unlock(&mtx);
        if (ret != 0) {
            printf("error\n");
        }
    }, {}, {});
}
规则集
plugin:@performance/recommended
plugin:@performance/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@performance/high-frequency-log-check
@performance/hp-performance-no-closures
