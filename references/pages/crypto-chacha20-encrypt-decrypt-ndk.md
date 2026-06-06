# 使用ChaCha20对称密钥加解密(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-chacha20-encrypt-decrypt-ndk_

调用OH_CryptoSymKeyGenerator_Create、OH_CryptoSymKeyGenerator_Generate，生成密钥算法为ChaCha20的对称密钥（OH_CryptoSymKey）。

如何生成ChaCha20对称密钥，开发者可参考下文示例，并结合对称密钥生成和转换规格：ChaCha20和随机生成对称密钥理解。参考文档与示例可能存在入参差异，请注意区分。

加密

调用OH_CryptoSymCipher_Create，指定字符串参数'ChaCha20'，创建对称密钥类型为ChaCha20的Cipher实例，用于完成加密操作。

调用OH_CryptoSymCipherParams_Create创建参数对象，调用OH_CryptoSymCipherParams_SetParam设置对应的加密参数。

调用OH_CryptoSymCipher_Init，设置模式为加密（CRYPTO_ENCRYPT_MODE），指定加密密钥（OH_CryptoSymKey）和对应的加密参数（OH_CryptoSymCipherParams），初始化加密Cipher实例。

调用OH_CryptoSymCipher_Update，更新数据（明文）。

调用OH_CryptoSymCipher_Final，获取加密后的数据。

说明

由于已使用update传入数据，此处data传入null。

doFinal输出结果可能为null，在访问具体数据前，需要先判断结果是否为null，避免产生异常。

调用OH_CryptoSymKeyGenerator_Destroy、OH_CryptoSymCipher_Destroy、OH_CryptoSymCipherParams_Destroy销毁各对象。

解密

调用OH_CryptoSymCipher_Create，指定字符串参数'ChaCha20'，创建对称密钥类型为ChaCha20的Cipher实例，用于完成解密操作。

调用OH_CryptoSymCipher_Init，设置模式为解密（CRYPTO_DECRYPT_MODE），指定解密密钥（OH_CryptoSymKey）和对应的解密参数（OH_CryptoSymCipherParams），初始化解密Cipher实例。

调用OH_CryptoSymCipher_Update，更新数据（密文）。

调用OH_CryptoSymCipher_Final，获取解密后的数据。

#include "CryptoArchitectureKit/crypto_common.h"
#include "CryptoArchitectureKit/crypto_sym_cipher.h"
#include <cstring>
#include "file.h"


// 参数赋值函数
static OH_Crypto_ErrCode doChaCha20SetParams(Crypto_DataBlob *ivBlob, OH_CryptoSymCipherParams **params)
{
    OH_Crypto_ErrCode ret = OH_CryptoSymCipherParams_Create(params);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }
    ret = OH_CryptoSymCipherParams_SetParam(*params, CRYPTO_IV_DATABLOB, ivBlob);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoSymCipherParams_Destroy(*params);
        *params = nullptr;
        return ret;
    }
    return ret;
}


// 加密函数
static OH_Crypto_ErrCode doChaCha20Encrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
    Crypto_DataBlob *msgBlob, Crypto_DataBlob *encData)
{
    OH_CryptoSymCipher *encCtx = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("ChaCha20", &encCtx);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymCipher_Init(encCtx, CRYPTO_ENCRYPT_MODE, keyCtx, params);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymCipher_Final(encCtx, msgBlob, encData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }


end:
    OH_CryptoSymCipher_Destroy(encCtx);
    return ret;
}


// 解密函数
static OH_Crypto_ErrCode doChaCha20Decrypt(OH_CryptoSymKey *keyCtx, OH_CryptoSymCipherParams *params,
    Crypto_DataBlob *encData, Crypto_DataBlob *decData)
{
    OH_CryptoSymCipher *decCtx = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoSymCipher_Create("ChaCha20", &decCtx);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymCipher_Init(decCtx, CRYPTO_DECRYPT_MODE, keyCtx, params); // 解密使用的params与加密时相同。
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymCipher_Final(decCtx, encData, decData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }


end:
    OH_CryptoSymCipher_Destroy(decCtx);
    return ret;
}


OH_Crypto_ErrCode doTestChaCha20()
{
    OH_CryptoSymKeyGenerator *genCtx = nullptr;
    OH_CryptoSymKey *keyCtx = nullptr;
    OH_CryptoSymCipherParams *params = nullptr;
    Crypto_DataBlob encData = {.data = nullptr, .len = 0};
    Crypto_DataBlob decData = {.data = nullptr, .len = 0};
    char *plainText = const_cast<char *>("this is test!");
    Crypto_DataBlob msgBlob = {.data = (uint8_t *)(plainText), .len = strlen(plainText)};
    uint8_t iv[16] = {1, 2, 4, 12, 3, 4, 2, 3, 3, 2, 0, 4, 3, 1, 0, 10}; // 示例代码iv值，开发者可使用安全随机数生成。
    Crypto_DataBlob ivBlob = {.data = iv, .len = sizeof(iv)};
    // 生成对称密钥。
    OH_Crypto_ErrCode ret = OH_CryptoSymKeyGenerator_Create("ChaCha20", &genCtx);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }
    ret = OH_CryptoSymKeyGenerator_Generate(genCtx, &keyCtx);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }


    // 参数赋值。
    ret = doChaCha20SetParams(&ivBlob, &params);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }


    // 加密。
    ret = doChaCha20Encrypt(keyCtx, params, &msgBlob, &encData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }


    // 解密。
    ret = doChaCha20Decrypt(keyCtx, params, &encData, &decData);
    if (ret != CRYPTO_SUCCESS) {
        goto end;
    }


end:
    OH_CryptoSymCipherParams_Destroy(params);
    OH_CryptoSymKeyGenerator_Destroy(genCtx);
    OH_CryptoSymKey_Destroy(keyCtx);
    OH_Crypto_FreeDataBlob(&encData);
    OH_Crypto_FreeDataBlob(&decData);
    return ret;
}
chacha20_encryption_decryption.cpp
使用ChaCha20对称密钥加解密(ArkTS)
使用ChaCha20对称密钥（Poly1305模式）加解密(ArkTS)
