# 使用X963KDF进行密钥派生(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-derivation-using-x963kdf-ndk_

OH_Crypto_ErrCode ret = OH_CryptoKdfParams_Create("X963KDF", &params);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }


    // 设置原始密钥材料。
    const char *keyData = "012345678901234567890123456789";
    Crypto_DataBlob key = {
        .data = reinterpret_cast<uint8_t *>(const_cast<char *>(keyData)),
        .len = strlen(keyData)
    };
    ret = OH_CryptoKdfParams_SetParam(params, CRYPTO_KDF_KEY_DATABLOB, &key);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }


    // 设置应用程序特定信息。
    const char *infoData = "infostring";
    Crypto_DataBlob info = {
        .data = reinterpret_cast<uint8_t *>(const_cast<char *>(infoData)),
        .len = strlen(infoData)
    };
    ret = OH_CryptoKdfParams_SetParam(params, CRYPTO_KDF_INFO_DATABLOB, &info);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }


    // 创建密钥派生函数对象。
    OH_CryptoKdf *kdfCtx = nullptr;
    ret = OH_CryptoKdf_Create("X963KDF|SHA256", &kdfCtx);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }


    // 派生密钥。
    Crypto_DataBlob out = {0};
    uint32_t keyLength = 32; // 生成32字节的密钥。
    ret = OH_CryptoKdf_Derive(kdfCtx, params, keyLength, &out);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoKdf_Destroy(kdfCtx);
        OH_CryptoKdfParams_Destroy(params);
        return ret;
    }


    printf("Derived key length: %u\n", out.len);


    // 清理资源。
    OH_Crypto_FreeDataBlob(&out);
    OH_CryptoKdf_Destroy(kdfCtx);
    OH_CryptoKdfParams_Destroy(params);
    return CRYPTO_SUCCESS;
}
x963kdf_test.cpp
使用X963KDF进行密钥派生(ArkTS)
跨平台数据兼容实践指导
