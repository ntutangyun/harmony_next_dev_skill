# 随机生成非对称密钥对(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-generate-asym-key-pair-randomly-ndk_

调用OH_CryptoAsymKeyGenerator_Create，指定字符串参数'RSA1024|PRIMES_2'，创建RSA密钥类型为RSA1024、素数个数为2的非对称密钥生成器（OH_CryptoAsymKeyGenerator）。

调用OH_CryptoAsymKeyGenerator_Generate，随机生成非对称密钥对象（OH_CryptoKeyPair）。

调用OH_CryptoPubKey_Encode获取公钥密钥对象的二进制数据。

#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_asym_key.h"
#include "file.h"


OH_Crypto_ErrCode generateRSAKey()
{
    OH_CryptoAsymKeyGenerator *ctx = nullptr;
    OH_CryptoKeyPair *keyPair = nullptr;
    OH_Crypto_ErrCode ret;


    ret = OH_CryptoAsymKeyGenerator_Create("RSA1024|PRIMES_2", &ctx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        return ret;
    }
    
    ret = OH_CryptoAsymKeyGenerator_Generate(ctx, &keyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        OH_CryptoKeyPair_Destroy(keyPair);
        return ret;
    }


    OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(keyPair);
    Crypto_DataBlob retBlob = {.data = nullptr, .len = 0};
    ret = OH_CryptoPubKey_Encode(pubKey, CRYPTO_PEM, "PKCS1", &retBlob);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        OH_CryptoKeyPair_Destroy(keyPair);
        return ret;
    }


    OH_Crypto_FreeDataBlob(&retBlob);


    OH_CryptoAsymKeyGenerator_Destroy(ctx);
    OH_CryptoKeyPair_Destroy(keyPair);
    return ret;
}
rsa.cpp
随机生成SM2密钥对

对应的算法规格请查看非对称密钥生成和转换规格：SM2。

调用OH_CryptoAsymKeyGenerator_Create，指定字符串参数'SM2_256'，创建密钥算法为SM2、密钥长度为256位的非对称密钥生成器（OH_CryptoAsymKeyGenerator）。

调用OH_CryptoAsymKeyGenerator_Generate，随机生成非对称密钥对象（OH_CryptoKeyPair）。

调用OH_CryptoPubKey_Encode获取公钥密钥对象的二进制数据。

#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_asym_key.h"
#include "file.h"


OH_Crypto_ErrCode generateSM2Key()
{
    OH_CryptoAsymKeyGenerator *ctx = nullptr;
    OH_CryptoKeyPair *dupKeyPair = nullptr;
    OH_Crypto_ErrCode ret;


    ret = OH_CryptoAsymKeyGenerator_Create("SM2_256", &ctx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        return ret;
    }


    ret = OH_CryptoAsymKeyGenerator_Generate(ctx, &dupKeyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        OH_CryptoKeyPair_Destroy(dupKeyPair);
        return ret;
    }


    OH_CryptoPubKey *pubKey = OH_CryptoKeyPair_GetPubKey(dupKeyPair);
    Crypto_DataBlob retBlob = { .data = nullptr, .len = 0 };
    ret = OH_CryptoPubKey_Encode(pubKey, CRYPTO_DER, nullptr, &retBlob);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(ctx);
        OH_CryptoKeyPair_Destroy(dupKeyPair);
        return ret;
    }


    OH_Crypto_FreeDataBlob(&retBlob);
    OH_CryptoAsymKeyGenerator_Destroy(ctx);
    OH_CryptoKeyPair_Destroy(dupKeyPair);
    return ret;
}
sm2.cpp
随机生成非对称密钥对(ArkTS)
指定二进制数据转换非对称密钥对(ArkTS)
