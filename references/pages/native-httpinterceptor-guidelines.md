# 使用HTTP全局拦截器 (C/C++)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-httpinterceptor-guidelines_

------------------header begin---------------------");
    while (headers != nullptr) {
        if (headers->data != nullptr) {
            OH_LOG_INFO(LOG_APP, "%{public}s", headers->data);
        }
        headers = headers->next;
    }
    OH_LOG_INFO(LOG_APP, "---------------------header end---------------------");
}


// 打印响应信息
void PrintResponseInfo(OH_Http_Interceptor_Response *response)
{
    OH_LOG_INFO(LOG_APP, "-----PrintResponseInfo Begin-----");
    if (response != nullptr) {
        OH_LOG_INFO(LOG_APP, "responseCode = %{public}d", response->responseCode);
        if (response->body.buffer != nullptr) {
            OH_LOG_INFO(LOG_APP, "body = %{public}s", response->body.buffer);
        }
        if (response->headers != nullptr) {
            LogHeader(response->headers);
        }


        OH_LOG_INFO(LOG_APP, "dns: %{public}lf", response->performanceTiming.dnsTiming);
        OH_LOG_INFO(LOG_APP, "tcp: %{public}lf", response->performanceTiming.tcpTiming);
        OH_LOG_INFO(LOG_APP, "tls: %{public}lf", response->performanceTiming.tlsTiming);
        OH_LOG_INFO(LOG_APP, "snd: %{public}lf", response->performanceTiming.firstSendTiming);
        OH_LOG_INFO(LOG_APP, "rcv: %{public}lf", response->performanceTiming.firstReceiveTiming);
        OH_LOG_INFO(LOG_APP, "tot: %{public}lf", response->performanceTiming.totalFinishTiming);
        OH_LOG_INFO(LOG_APP, "rdr: %{public}lf", response->performanceTiming.redirectTiming);
        OH_LOG_INFO(LOG_APP, "-----PrintResponseInfo End-----");
    }
}


// 响应拦截器处理函数
OH_Interceptor_Result ResponseInterceptorHandler(
    OH_Http_Interceptor_Request *request,
    OH_Http_Interceptor_Response *response,
    int32_t *isModified)
{
    (void)request;
    (void)isModified;
    
    if (response != nullptr) {
        OH_LOG_INFO(LOG_APP, "---Response Interceptor Handler---");
        PrintResponseInfo(response);
    }
    return OH_CONTINUE;
}


// 添加只读响应拦截器
static napi_value AddResponseInterceptor(napi_env env, napi_callback_info info)
{
    napi_value result;
    
    // 设置拦截器处理函数
    g_responseInterceptor.handler = ResponseInterceptorHandler;
    
    // 添加拦截器
    int ret = OH_Http_AddReadOnlyInterceptor(&g_responseInterceptor);
    
    OH_LOG_INFO(LOG_APP, "AddResponseInterceptor ret: %{public}d", ret);
    napi_create_int32(env, ret, &result);
    return result;
}


// 移除拦截器
static napi_value RemoveInterceptor(napi_env env, napi_callback_info info)
{
    napi_value result;
    
    // 移除拦截器
    int ret = OH_Http_RemoveInterceptor(&g_responseInterceptor);
    
    OH_LOG_INFO(LOG_APP, "RemoveInterceptor ret: %{public}d", ret);
    napi_create_int32(env, ret, &result);
    return result;
}


// 启用指定组的所有拦截器
static napi_value StartInterceptors(napi_env env, napi_callback_info info)
{
    napi_value result;
    
    // 启用组ID为1的所有拦截器
    int ret = OH_Http_StartAllInterceptors(1);
    
    OH_LOG_INFO(LOG_APP, "StartInterceptors ret: %{public}d", ret);
    napi_create_int32(env, ret, &result);
    return result;
}


// 停用指定组的所有拦截器
static napi_value StopInterceptors(napi_env env, napi_callback_info info)
{
    napi_value result;
    
    // 停用组ID为1的所有拦截器
    int ret = OH_Http_StopAllInterceptors(1);
    
    OH_LOG_INFO(LOG_APP, "StopInterceptors ret: %{public}d", ret);
    napi_create_int32(env, ret, &result);
    return result;
}


// 删除指定组的所有拦截器
static napi_value RemoveAllInterceptors(napi_env env, napi_callback_info info)
{
    napi_value result;
    
    // 删除组ID为1的所有拦截器
    int ret = OH_Http_RemoveAllInterceptors(1);
    
    OH_LOG_INFO(LOG_APP, "RemoveAllInterceptors ret: %{public}d", ret);
    napi_create_int32(env, ret, &result);
    return result;
}
napi_init.cpp

上述代码实现了一个HTTP全局只读响应拦截器，用于监控HTTP响应。在响应拦截器处理函数中，会打印响应的状态码、响应体、响应头以及性能指标等信息。

初始化并导出通过N-API封装的napi_value类型对象，通过外部函数接口将函数提供给JavaScript调用。

EXTERN_C_START
static napi_value Init(napi_env env, napi_value exports)
{
    napi_property_descriptor desc[] = {
        {"AddResponseInterceptor", nullptr, AddResponseInterceptor, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"RemoveInterceptor", nullptr, RemoveInterceptor, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"StartInterceptors", nullptr, StartInterceptors, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"StopInterceptors", nullptr, StopInterceptors, nullptr, nullptr, nullptr, napi_default, nullptr},
        {"RemoveAllInterceptors", nullptr, RemoveAllInterceptors, nullptr, nullptr, nullptr, napi_default, nullptr},
    };
    napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
    return exports;
}
EXTERN_C_END
napi_init.cpp

将上一步中初始化成功的对象通过RegisterEntryModule函数，使用napi_module_register函数将模块注册到Node.js中。

static napi_module demoModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init,
    .nm_modname = "entry",
    .nm_priv = ((void *)0),
    .reserved = {0},
};


extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
{
    napi_module_register(&demoModule);
}
napi_init.cpp

在工程的Index.d.ts文件中定义函数的类型。

export const AddResponseInterceptor: () => number;
export const RemoveInterceptor: () => number;
export const StartInterceptors: () => number;
export const StopInterceptors: () => number;
export const RemoveAllInterceptors: () => number;
Index.d.ts

在Index.ets文件中对上述封装好的接口进行调用。

import { hilog } from '@kit.PerformanceAnalysisKit';
import httpInterceptor from 'libentry.so';
import { http } from '@kit.NetworkKit';


const LOG_TAG: string = 'HttpInterceptorDemo';
const HTTP_URL_BAIDU: string = "http://www.baidu.com";


@Entry
@Component
struct Index {
  @State message: string = 'HTTP Interceptor Demo';


  build() {
    Navigation() {
      Column() {
        Text(this.message)
          .fontSize(20)
          .margin({ bottom: 20 })


        Column({
          space: 12
        }) {
          Button('Add Response Interceptor')
            .id('AddInterceptor')
            .onClick(() => {
              let ret = httpInterceptor.AddResponseInterceptor();
              hilog.info(0x0000, LOG_TAG, `AddResponseInterceptor ret: ${ret}`);
            })


          Button('Start Interceptors')
            .id('StartInterceptors')
            .onClick(() => {
              let ret = httpInterceptor.StartInterceptors();
              hilog.info(0x0000, LOG_TAG, `StartInterceptors ret: ${ret}`);
            })


          Button('Send HTTP Request')
            .id('networkRequest')
            .onClick(() => {
              let httpRequest: http.HttpRequest = http.createHttp();
              let options: http.HttpRequestOptions = {
                method: http.RequestMethod.POST,
              };
              httpRequest.request(HTTP_URL_BAIDU, options, (err: BusinessError, res: http.HttpResponse) => {
                if (err) {
                  hilog.info(0x0000, LOG_TAG, `request fail, error code: ${err.code}, msg: ${err.message}`);
                  httpRequest.destroy();
                } else {
                  hilog.info(0x0000, LOG_TAG, `res:${JSON.stringify(res)}`);
                  httpRequest.destroy();
                }
              });
            })


          Button('Stop Interceptors')
            .id('StopInterceptors')
            .onClick(() => {
              let ret = httpInterceptor.StopInterceptors();
              hilog.info(0x0000, LOG_TAG, `StopInterceptors ret: ${ret}`);
            })


          Button('Remove Interceptor')
            .id('RemoveInterceptor')
            .onClick(() => {
              let ret = httpInterceptor.RemoveInterceptor();
              hilog.info(0x0000, LOG_TAG, `RemoveInterceptor ret: ${ret}`);
            })


          Button('Remove All Interceptors')
            .id('RemoveAllInterceptors')
            .onClick(() => {
              let ret = httpInterceptor.RemoveAllInterceptors();
              hilog.info(0x0000, LOG_TAG, `RemoveAllInterceptors ret: ${ret}`);
            })
        }
      }
      .padding(20)
    }
  }
}
Index.ets

配置CMakeLists.txt，本模块需要用到的共享库是libhttp_interceptor.so，在工程自动生成的CMakeLists.txt中的target_link_libraries中添加此共享库。

注意：如图所示，在add_library中的entry是工程自动生成的module name，若要做修改，需和步骤 3 中.nm_modname保持一致。

调用HTTP全局拦截器C API接口要求应用拥有ohos.permission.INTERNET权限，在module.json5中的requestPermissions项添加该权限。

完成上述步骤后，工程搭建已全部完成，后续可连接设备运行工程并查看日志。

测试步骤

连接设备，使用DevEco Studio打开搭建好的工程。

运行工程，设备上会弹出以下图片所示界面。

点击Add Response Interceptor按钮，添加一个HTTP全局只读响应拦截器。

点击Start Interceptors按钮，启用组ID为1的所有拦截器。

点击Send HTTP Request按钮，拦截器会捕获响应并打印相关信息到日志。

点击Stop Interceptors按钮，停用组ID为1的所有拦截器。

点击Remove Interceptor按钮，移除之前添加的拦截器。

点击Remove All Interceptors按钮，删除组ID为1的所有拦截器。

使用DNS解析域名
连接网络
