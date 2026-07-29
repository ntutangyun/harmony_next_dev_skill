# Wallet Kit接口调用注意事项？

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wallet-faq-3_

请确保创建WalletPassClient时传入的context类型是否为UIAbilityContext，且为有效状态。Wallet Kit会使用调用方的context进行通信，如果context失效，则调用会失败。

请确保调用Wallet Kit接口时应用处于前台，后台调用会被系统管控拦截，可能导致调用失败。
