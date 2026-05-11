# 加密导出导入密钥(C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-wrap-key-ndk_

static napi_value GenerateKey(napi_env env, napi_callback_info info)
{
    /* 1.确定密钥别名 */
    const char *alias = "test_generate";
    struct OH_Huks_Blob aliasBlob = { .size = (uint32_t)strlen(alias), .data = (uint8_t *)alias };
    struct OH_Huks_ParamSet *testGenerateKeyParamSet = nullptr;
    struct OH_Huks_ParamSet *wrapKeyParamSet = nullptr;
    struct OH_Huks_Result ohResult;
    do {
        /* 2.初始化密钥属性集 */
        ohResult = InitParamSet(&testGenerateKeyParamSet, g_testGenerateKeyParam,
            sizeof(g_testGenerateKeyParam) / sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        
        /* 3.生成密钥 */
        ohResult = OH_Huks_GenerateKeyItem(&aliasBlob, testGenerateKeyParamSet, nullptr);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        
        /* 4.初始化加密导出导入密钥属性集 */
        ohResult = InitParamSet(&wrapKeyParamSet, g_wrapKeyParam,
            sizeof(g_wrapKeyParam) / sizeof(OH_Huks_Param));
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        
        /* 5.加密导出密钥 */
        uint8_t WrappedData[2048] = {0};
        struct OH_Huks_Blob wrappedKey = {2048, WrappedData};
        ohResult = OH_Huks_WrapKey(&aliasBlob, wrapKeyParamSet, &wrappedKey);
        if (ohResult.errorCode != OH_HUKS_SUCCESS) {
            break;
        }
        
        /* 6.加密导入密钥 */
        ohResult = OH_Huks_UnwrapKey(&aliasBlob, wrapKeyParamSet, &wrappedKey);
    } while (0);
    OH_Huks_FreeParamSet(&testGenerateKeyParamSet);
    OH_Huks_FreeParamSet(&wrapKeyParamSet);
    napi_value ret;
    napi_create_int32(env, ohResult.errorCode, &ret);
    return ret;
}
加密导出导入密钥(ArkTS)
群组密钥
