# 使用RSA私钥进行编码解码(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-rsa-encoded-decoded-ndk_

--BEGIN RSA PRIVATE KEY-----\n"
        "Proc-Type: 4,ENCRYPTED\n"
        "DEK-Info: AES-128-CBC,815A066131BF05CF87CE610A59CC69AE\n\n"
        "7Jd0vmOmYGFZ2yRY8fqRl3+6rQlFtNcMILvcb5KWHDSrxA0ULmJE7CW0DSRikHoA\n"
        "t0KgafhYXeQXh0dRy9lvVRAFSLHCLJVjchx90V7ZSivBFEq7+iTozVp4AlbgYsJP\n"
        "vx/1sfZD2WAcyMJ7IDmJyft7xnpVSXsyWGTT4f3eaHJIh1dqjwrso7ucAW0FK6rp\n"
        "/TONyOoXNfXtRbVtxNyCWBxt4HCSclDZFvS9y8fz9ZwmCUV7jei/YdzyQI2wnE13\n"
        "W8cKlpzRFL6BWi8XPrUtAw5MWeHBAPUgPWMfcmiaeyi5BJFhQCrHLi+Gj4EEJvp7\n"
        "mP5cbnQAx6+paV5z9m71SKrI/WSc4ixsYYdVmlL/qwAK9YliFfoPl030YJWW6rFf\n"
        "T7J9BUlHGUJ0RB2lURNNLakM+UZRkeE9TByzCzgTxuQtyv5Lwsh2mAk3ia5x0kUO\n"
        "LHg3Eoabhdh+YZA5hHaxnpF7VjspB78E0F9Btq+A41rSJ6zDOdToHey4MJ2nxdey\n"
        "Z3bi81TZ6Fp4IuROrvZ2B/Xl3uNKR7n+AHRKnaAO87ywzyltvjwSh2y3xhJueiRs\n"
        "BiYkyL3/fnocD3pexTdN6h3JgQGgO5GV8zw/NrxA85mw8o9im0HreuFObmNj36T9\n"
        "k5N+R/QIXW83cIQOLaWK1ThYcluytf0tDRiMoKqULiaA6HvDMigExLxuhCtnoF8I\n"
        "iOLN1cPdEVQjzwDHLqXP2DbWW1z9iRepLZlEm1hLRLEmOrTGKezYupVv306SSa6J\n"
        "OA55lAeXMbyjFaYCr54HWrpt4NwNBX1efMUURc+1LcHpzFrBTTLbfjIyq6as49pH\n"
        "-----END RSA PRIVATE KEY-----\n";


    OH_CryptoAsymKeyGenerator *keyGen = nullptr;
    OH_Crypto_ErrCode ret = OH_CryptoAsymKeyGenerator_Create("RSA2048", &keyGen);
    if (ret != CRYPTO_SUCCESS) {
        return ret;
    }


    OH_CryptoKeyPair *dupKeyPair = nullptr;
    Crypto_DataBlob priKeyPkcs1EncodingData = {};
    priKeyPkcs1EncodingData.data = reinterpret_cast<uint8_t *>(const_cast<char *>(priKeyPkcs1EncodingStr.c_str()));
    priKeyPkcs1EncodingData.len = strlen(priKeyPkcs1EncodingStr.c_str());
    std::string password = "123456";
    ret = OH_CryptoAsymKeyGenerator_SetPassword(keyGen, reinterpret_cast<const unsigned char *>(password.c_str()),
        password.size());
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(keyGen);
        return ret;
    }
    ret = OH_CryptoAsymKeyGenerator_Convert(keyGen, CRYPTO_PEM, nullptr, &priKeyPkcs1EncodingData, &dupKeyPair);
    if (ret != CRYPTO_SUCCESS) {
        OH_CryptoAsymKeyGenerator_Destroy(keyGen);
        return ret;
    }
    OH_CryptoKeyPair_Destroy(dupKeyPair);
    OH_CryptoAsymKeyGenerator_Destroy(keyGen);
    return ret;
}
prikey_decoding.cpp
使用RSA私钥进行编码解码(ArkTS)
使用私钥对象获取公钥对象(ArkTS)
