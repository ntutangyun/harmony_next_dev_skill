# 使用RSA非对称密钥（PKCS1模式）加解密(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-asym-encrypt-decrypt-pkcs1-ndk_

调用OH_CryptoAsymKeyGenerator_Create、OH_CryptoAsymKeyGenerator_Generate，生成RSA密钥类型为RSA1024、素数个数为2的非对称密钥对（keyPair）。keyPair对象中包括公钥PubKey、私钥PriKey。

如何生成RSA非对称密钥对，开发者可参考下文示例，并结合非对称密钥生成和转换规格：RSA和随机生成非对称密钥对理解。参考文档与当前示例可能存在入参差异，请在阅读时注意区分。

调用OH_CryptoAsymCipher_Create，指定字符串参数'RSA1024|PKCS1'，创建非对称密钥类型为RSA1024、填充模式为PKCS1的Cipher实例，用于完成加解密操作。

调用OH_CryptoAsymCipher_Init，设置模式为加密（CRYPTO_ENCRYPT_MODE），指定加密密钥（keyPair），初始化加密Cipher实例。

调用OH_CryptoAsymCipher_Final，传入明文，获取加密后的数据。

OH_CryptoAsymCipher_Final输出结果可能为NULL，在访问具体数据前，需要先判断结果是否为NULL，避免产生异常。
当数据量较大时，可以多次调用OH_CryptoAsymCipher_Final，即分段加解密。

解密

由于RSA算法的Cipher实例不支持重复init操作，需要调用OH_CryptoAsymCipher_Create，重新生成Cipher实例。

调用OH_CryptoAsymCipher_Init，设置模式为解密（CRYPTO_DECRYPT_MODE），指定解密密钥（keyPair）初始化解密Cipher实例。

调用OH_CryptoAsymCipher_Final，传入密文，获取解密后的数据。

#include "CryptoArchitectureKit/crypto_architecture_kit.h"
#include <cstring>


static OH_Crypto_ErrCode doRsaEncrypt(const Crypto_DataBlob *plainData, OH_CryptoKeyPair **keyPair,
    OH_CryptoAsymKeyGenerator **keyGen, Crypto_DataBlob *encryptedData)
{
    OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("RSA1024", keyGen);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }


    ret = OH_CryptoAsymKeyGenerator_Generate(*keyGen, keyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(*keyGen);
        return ret;
    }


    OH_CryptoAsymCipher *cipher = nullptr;
    ret = OH_CryptoAsymCipher_Create("RSA1024|PKCS1", &cipher);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKeyPair_Destroy(*keyPair);
        OH_CryptoAsymKeyGenerator_Destroy(*keyGen);
        return ret;
    }


    ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_ENCRYPT_MODE, *keyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymCipher_Destroy(cipher);
        OH_CryptoKeyPair_Destroy(*keyPair);
        OH_CryptoAsymKeyGenerator_Destroy(*keyGen);
        return ret;
    }


    ret = OH_CryptoAsymCipher_Final(cipher, plainData, encryptedData);
    OH_CryptoAsymCipher_Destroy(cipher);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKeyPair_Destroy(*keyPair);
        OH_CryptoAsymKeyGenerator_Destroy(*keyGen);
        return ret;
    }


    return ret;
}


static OH_Crypto_ErrCode doRsaDecrypt(const Crypto_DataBlob *encryptedData, OH_CryptoKeyPair *keyPair,
    const Crypto_DataBlob *expectedPlainData)
{
    OH_CryptoAsymCipher *cipher = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoAsymCipher_Create("RSA1024|PKCS1", &cipher);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }


    ret = OH_CryptoAsymCipher_Init(cipher, CRYPTO_DECRYPT_MODE, keyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymCipher_Destroy(cipher);
        return ret;
    }


    Crypto_DataBlob decrypted = { 0 };
    ret = OH_CryptoAsymCipher_Final(cipher, encryptedData, &decrypted);
    OH_CryptoAsymCipher_Destroy(cipher);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }


    if ((decrypted.len != expectedPlainData->len) ||
        (memcmp(decrypted.data, expectedPlainData->data, decrypted.len) != 0)) {
        OH_Crypto_FreeDataBlob(&decrypted);
        return CRYPTO_OPERTION_ERROR;
    }


    OH_Crypto_FreeDataBlob(&decrypted);
    return ret;
}


OH_Crypto_ErrCode doTestRsaEncDec()
{
    const char *testData = "Hello, RSA!";
    Crypto_DataBlob plainData = {
        .data = (uint8_t *)testData,
        .len = strlen(testData)
    };


    OH_CryptoKeyPair *keyPair = nullptr;
    OH_CryptoAsymKeyGenerator *keyGen = nullptr;
    Crypto_DataBlob encryptedData = { 0 };


    OH_Crypto_ErrCode ret = doRsaEncrypt(&plainData, &keyPair, &keyGen, &encryptedData);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }


    ret = doRsaDecrypt(&encryptedData, keyPair, &plainData);
    OH_Crypto_FreeDataBlob(&encryptedData);
    OH_CryptoKeyPair_Destroy(keyPair);
    OH_CryptoAsymKeyGenerator_Destroy(keyGen);
    return ret;
}
PKCS1_RSA.cpp
使用RSA非对称密钥（PKCS1模式）加解密(ArkTS)
使用RSA非对称密钥分段加解密(ArkTS)
