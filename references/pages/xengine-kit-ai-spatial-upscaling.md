# 空域AI超分

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xengine-kit-ai-spatial-upscaling_

从26.0.0版本开始，新增支持Vulkan协议。

XEngine Kit提供空域AI超分能力，基于单帧图像使用AI推理生成滤波参数进行超采样，通过GPU、NPU协同工作，实现比空域GPU超分更好的画质，建议超分倍率在1.5倍以下时使用。

约束与限制

支持的设备类型：Phone，从5.1.0(18)版本开始新增支持Tablet、PC/2in1设备，从5.1.1(19)版本开始新增支持TV设备。

可通过以下方式查询相关扩展特性是否支持：

对于OpenGL ES，使用HMS_XEG_GetString扩展特性查询接口进行查询。

对于Vulkan，使用HMS_XEG_EnumerateDeviceExtensionProperties扩展特性查询接口进行查询。

如查询结果包含XEG_NEURAL_UPSCALE_EXTENSION_NAME，则表示支持该特性，若查询结果未包含，则表示不支持该特性。

接口说明

以下为空域AI超分特性需要使用的接口，详细说明请参考接口文档。

OpenGL ES接口：

接口名	描述
const GLubyte * HMS_XEG_GetString(GLenum name)	XEngine OpenGL ES扩展特性查询接口。
GL_APICALL void GL_APIENTRY HMS_XEG_NeuralUpscaleParameter(GLenum pname, GLvoid *param)	设置空域AI超分输入参数。
GL_APICALL void GL_APIENTRY HMS_XEG_RenderNeuralUpscale(GLuint inputTexture)	执行空域AI超分渲染命令。

Vulkan接口：

接口名	描述
VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_EnumerateDeviceExtensionProperties(VkPhysicalDevice physicalDevice, uint32_t *pPropertyCount, XEG_ExtensionProperties *pProperties)	XEngine Vulkan扩展特性查询接口。
VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CreateNeuralUpscale(VkDevice device, const XEG_NeuralUpscaleCreateInfo *pCreateInfo, XEG_NeuralUpscale *pNeuralUpscale)	创建XEG_NeuralUpscale对象。
VKAPI_ATTR VkResult VKAPI_CALL HMS_XEG_CmdRenderNeuralUpscale(VkCommandBuffer commandBuffer, XEG_NeuralUpscale neuralUpscale, const XEG_NeuralUpscaleDescription *pDescription)	执行空域AI超分渲染命令。
VKAPI_ATTR void VKAPI_CALL HMS_XEG_DestroyNeuralUpscale(XEG_NeuralUpscale neuralUpscale)	销毁XEG_NeuralUpscale对象。

业务流程

下面是基于OpenGL ES图形API平台集成空域AI超分的主要业务流程

用户在进入游戏初始化场景时调用HMS_XEG_GetString接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含空域AI超分时代表可以使用此特性。

初始化场景，空域AI超分的输入纹理需要使用OH_NativeBuffer来创建。

调用HMS_XEG_NeuralUpscaleParameter接口配置超分参数，包含超分输入纹理对应的OH_NativeBuffer句柄。

游戏运行时，每帧先渲染待超分的纹理。

调用HMS_XEG_RenderNeuralUpscale接口执行超分，超分结果会写出到当前绑定的帧缓冲。

渲染后续流程，如UI。

当前帧已全部渲染完成，进行送显。

当游戏退出时，释放游戏创建的资源，XEngine内部资源会自行释放。

下面是基于Vulkan图形API平台集成空域AI超分的主要业务流程

用户在进入游戏初始化场景时调用HMS_XEG_EnumerateDeviceExtensionProperties接口查询XEngine支持的特性，当查询接口返回支持的特性列表中包含空域AI超分时代表可以使用此特性。

调用HMS_XEG_CreateNeuralUpscale接口创建超分实例。

当游戏运行时，游戏渲染待超分的当前帧纹理。

当待超分纹理渲染完成时，调用HMS_XEG_CmdRenderNeuralUpscale接口对待超分的纹理超分。

当超分渲染完成时，游戏渲染剩下的纹理，如UI等。

当前帧已全部渲染完成，进行送显。

当游戏退出时，调用HMS_XEG_DestroyNeuralUpscale接口销毁超分实例。

开发步骤

本章以OpenGL ES和Vulkan图像API集成为例，说明XEngine集成操作过程。

[h2]配置项目

编译HAP时，Native层so编译需要依赖NDK中的libxengine.so。

头文件引用

按需引用XEngine的头文件，如使用OpenGL ES空域AI超分。

#include <cstring>
#include <cstdlib>
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <GLES2/gl2.h>
#include <GLES2/gl2ext.h>
#include <xengine/xeg_gles_extension.h>
#include <xengine/xeg_gles_neural_upscale.h>
#include <native_buffer/native_buffer.h>
#include <native_window/external_window.h>

按需引用XEngine的头文件，如使用Vulkan空域AI超分。

#include <string>
#include <vector>
#include <algorithm>
#include <xengine/xeg_vulkan_extension.h>
#include <xengine/xeg_vulkan_neural_upscale.h>

编写CMakeLists.txt

按需引用XEngine的CMakeLists，如使用OpenGL ES空域AI超分功能，CMakeLists.txt部分示例代码如下，完整示例代码请参见Demo（GPU加速引擎-GLES）。

find_library(
    # 设置路径变量的名称。
    native-buffer-lib
    # 指定希望CMake定位的NDK库的名称。
    native_buffer
)
find_library(
    # 设置路径变量的名称。
    native-window-lib
    # 指定希望CMake定位的NDK库的名称。
    native_window
)
find_library(
    # 设置路径变量的名称。
    xengine-lib
    # 指定希望CMake定位的NDK库的名称。
    xengine
)
find_library(
    # 设置路径变量的名称。
    EGL-lib
    # 指定希望CMake定位的NDK库的名称。
    EGL
)
find_library(
    # 设置路径变量的名称。
    GLES-lib
    # 指定希望CMake定位的NDK库的名称。
    GLESv3
)

target_link_libraries(nativerender PUBLIC
${EGL-lib} ${GLES-lib} ${xengine-lib} ${native-window-lib} ${native-buffer-lib})

按需引用XEngine的CMakeLists，如使用Vulkan空域AI超分功能，CMakeLists.txt部分示例代码如下，完整示例代码请参见Demo（GPU加速引擎-Vulkan）。

 find_library(
    # 设置路径变量的名称。
    hilog-lib
    # 指定希望CMake定位的NDK库的名称。
    hilog_ndk.z
 )
 find_library(
    # 设置路径变量的名称。
    libace-lib
    # 指定希望CMake定位的NDK库的名称。
    ace_ndk.z
 )
 find_library(
    # 设置路径变量的名称。
    libnapi-lib
    # 指定希望CMake定位的NDK库的名称。
    ace_napi.z
 )
 find_library(
    # 设置路径变量的名称。
    libuv-lib
    # 指定希望CMake定位的NDK库的名称。
    uv
 )
 find_library(
    # 设置路径变量的名称。
    xengine-lib
    # 指定希望CMake定位的NDK库的名称。
    xengine
 )
 add_library(libassimp SHARED IMPORTED)
 set_target_properties(
       libassimp
       PROPERTIES
       IMPORTED_LOCATION
       ${CMAKE_CURRENT_SOURCE_DIR}/libs/arm64-v8a/libassimp.so
 )
 target_link_libraries(nativerender PUBLIC
    ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} libnative_window.so libc++.a libktx librawfile.z.so libassimp ${xengine-lib})

[h2]集成XEngine空域AI超分（OpenGL ES）

Native层实现使用OpenGL ES和XEngine图形API搭建图像渲染管线并集成空域AI超分，渲染结果通过XComponent组件显示到屏幕。

本节阐述OpenGL ES图形API的空域AI超分的使用，详细代码请参见Demo（GPU加速引擎-GLES）。

在调用XEngine Kit能力前，需要先通过Syscap查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

调用HMS_XEG_GetString接口，获取XEngine支持的扩展信息，只有在支持XEG_NEURAL_UPSCALE_EXTENSION_NAME扩展时才可以使用空域AI超分的相关接口。

// 查询XEngine支持的GLES扩展信息
const char* extensions = (const char*)HMS_XEG_GetString(XEG_EXTENSIONS);
// 检查是否支持空域AI超分
if (!strstr(extensions, XEG_NEURAL_UPSCALE_EXTENSION_NAME)) {
    exit(1); // 异常退出
}

创建输入纹理，并关联一个OH_NativeBuffer。

// 渲染宽高和送显宽高均为用户自定义参数，这里以将800*600的分辨率进行1.5倍超分到1200*900的分辨率为例
uint32_t renderWidth = 800;
uint32_t renderHeight = 600;
uint32_t displayWidth = 1200;
uint32_t displayHeight = 900;
// 获取函数指针
PFNEGLCREATEIMAGEKHRPROC fp_eglCreateImageKHR = reinterpret_cast<PFNEGLCREATEIMAGEKHRPROC>(eglGetProcAddress("eglCreateImageKHR"));
PFNEGLDESTROYIMAGEKHRPROC fp_eglDestroyImageKHR = reinterpret_cast<PFNEGLDESTROYIMAGEKHRPROC>(eglGetProcAddress("eglDestroyImageKHR"));
PFNGLEGLIMAGETARGETTEXTURE2DOESPROC fp_glEGLImageTargetTexture2DOES = reinterpret_cast<PFNGLEGLIMAGETARGETTEXTURE2DOESPROC>(eglGetProcAddress("glEGLImageTargetTexture2DOES"));
// 创建OH_NativeBuffer
OH_NativeBuffer_Config config = {};
config.width = renderWidth;
config.height = renderHeight;
config.usage = NATIVEBUFFER_USAGE_CPU_READ | NATIVEBUFFER_USAGE_CPU_READ_OFTEN | NATIVEBUFFER_USAGE_HW_TEXTURE | NATIVEBUFFER_USAGE_HW_RENDER| NATIVEBUFFER_USAGE_ALIGNMENT_512;
config.format = NATIVEBUFFER_PIXEL_FMT_RGBA_8888;
OH_NativeBuffer* bufferHandle = OH_NativeBuffer_Alloc(&config);
if (bufferHandle == nullptr) {
    // 创建失败，用户可自定义错误处理
}
OHNativeWindowBuffer *nativeWindowBuffer = OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer(bufferHandle);
EGLImageKHR eglImage = fp_eglCreateImageKHR(eglGetCurrentDisplay(), EGL_NO_CONTEXT, EGL_NATIVE_BUFFER_OHOS, static_cast<EGLClientBuffer>(nativeWindowBuffer), nullptr);
// 创建超分输入纹理
GLuint textureID;
glGenTextures(1, &textureID);
glBindTexture(GL_TEXTURE_2D, textureID);
// 设置纹理环绕和过滤参数
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
// 关联超分输入纹理和eglImage
fp_glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, eglImage);

在超分输入纹理上进行渲染。

GLuint fboID = 0;
glGenFramebuffers(1, &fboID);
glBindFramebuffer(GL_FRAMEBUFFER, fboID);
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, textureID, 0);
if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE) {
    // 创建framebuffer失败，用户可自定义错误处理
}
glViewport(0, 0, renderWidth, renderHeight);

调用HMS_XEG_NeuralUpscaleParameter接口，设置空域AI超分的输入参数。

// sharpness为用户自定义超分锐化参数，此处以参数为0.3f为例
float sharpness = 0.3f;
HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_SHARPNESS, &sharpness);
// inputScissor为超分输入纹理的裁剪窗口参数
GLuint inputScissor[4] = {0, 0, renderWidth, renderHeight};
HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_SCISSOR, inputScissor);
// 设置超分输入纹理对应的OH_NativeBuffer句柄
HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_INPUT_HANDLE, bufferHandle);

调用HMS_XEG_RenderNeuralUpscale接口执行空域AI超分。

// 绑定绘制超分结果的帧缓冲，此处使用默认帧缓冲，也可使用用户自定义帧缓冲
glBindFramebuffer(GL_FRAMEBUFFER, 0);
glViewport(0, 0, displayWidth, displayHeight);
// 执行空域AI超分
HMS_XEG_RenderNeuralUpscale(textureID);

不需要进行超分渲染时，销毁相关资源。

glDeleteFramebuffers(1, &fboID);
glDeleteTextures(1, &textureID);
if (eglImage != nullptr) {
   fp_eglDestroyImageKHR(eglGetCurrentDisplay(), eglImage);
}
if (nativeWindowBuffer != nullptr) {
   OH_NativeWindow_DestroyNativeWindowBuffer(nativeWindowBuffer);
}
if (bufferHandle != nullptr) {
   OH_NativeBuffer_Unreference(bufferHandle);
}

[h2]集成XEngine空域AI超分（Vulkan）

使用Vulkan图形API搭建图像渲染管线并集成空域AI超分在Native层实现，渲染结果通过XComponent组件显示到屏幕。

本节阐述Vulkan图形API的空域AI超分使用，详细代码请参见Demo（GPU加速引擎-Vulkan）。

在调用XEngine Kit能力前，需要先通过Syscap查询您的目标设备是否支持SystemCapability.Graphic.XEngine系统能力。

调用HMS_XEG_EnumerateDeviceExtensionProperties接口，获取XEngine支持的扩展信息，只有在支持XEG_NEURAL_UPSCALE_EXTENSION_NAME扩展时才可以使用空域AI超分的相关接口。

// physicalDevice为Vulkan物理设备，用户需进行初始化
VkPhysicalDevice physicalDevice;
// 查询XEngine支持的Vulkan扩展列表
std::vector<std::string> supportedExtensions;
uint32_t pPropertyCount;
HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, nullptr);
if (pPropertyCount > 0) {
    std::vector<XEG_ExtensionProperties> pProperties(pPropertyCount);
    if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, &pProperties.front()) == VK_SUCCESS) {
        for (auto ext : pProperties) {
             supportedExtensions.push_back(ext.extensionName);
         }
    }
}
// 查询是否支持空域AI超分
if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_NEURAL_UPSCALE_EXTENSION_NAME) == supportedExtensions.end()) {
    exit(1); // 异常退出
}

声明实例句柄。

XEG_NeuralUpscale xegNeuralUpscale;

调用HMS_XEG_CreateNeuralUpscale接口，创建超分实例。

// 渲染宽高和超分后宽高均为用户自定义参数，此处以将800*600分辨率超分至1200*900分辨率为例
uint32_t m_renderWidth = 800;
uint32_t m_renderHeight = 600;
uint32_t m_upscaleWidth = 1200;
uint32_t m_upscaleHeight = 900;
// Vulkan逻辑设备，用户需进行初始化
VkDevice device = VK_NULL_HANDLE;
// VkRect2D为Vulkan指定的二维区域结构
// srcRect2D为超分输入纹理区域，用户可自定义
VkRect2D srcRect2D;
// srcRect2D.offset.x和srcRect2D.offset.y为原点偏移量
srcRect2D.offset.x = 0;
srcRect2D.offset.y = 0;
// srcRect2D.extent.width与srcRect2D.extent.height为输入纹理采样区域宽高
srcRect2D.extent.width = m_renderWidth;
srcRect2D.extent.height = m_renderHeight;
// dstRect2D为超分输出纹理区域，用户可自定义
VkRect2D dstRect2D;
// dstRect2D.offset.x和dstRect2D.offset.y为原点偏移量
dstRect2D.offset.x = 0;
dstRect2D.offset.y = 0;
// dstRect2D.extent.width与dstRect2D.extent.height为超分纹理写入区域宽高
dstRect2D.extent.width = m_upscaleWidth;
dstRect2D.extent.height = m_upscaleHeight;
XEG_NeuralUpscaleCreateInfo createInfo;
createInfo.sType = XEG_STRUCTURE_TYPE_NEURAL_UPSCALE_CREATE_INFO;
createInfo.pNext = nullptr;
createInfo.inputRegion = srcRect2D;
createInfo.outputRegion = dstRect2D;
createInfo.inputSize = srcRect2D.extent;
createInfo.outputSize = dstRect2D.extent;
createInfo.outputFormat = VK_FORMAT_R8G8B8A8_UNORM;
VkResult result = HMS_XEG_CreateNeuralUpscale(device, &createInfo, &xegNeuralUpscale);
if (result != VK_SUCCESS) {
    // 异常退出
}

调用HMS_XEG_CmdRenderNeuralUpscale接口下发超分，每帧都需要调用。

// inputImageView为用户创建的超分输入图像的VkImageView
VkImageView inputImageView = VK_NULL_HANDLE;
// outputImageView为用户创建的超分输出图像的VkImageView
VkImageView outputImageView = VK_NULL_HANDLE;
// cmdBuff为命令缓冲区，用户需进行初始化
VkCommandBuffer cmdBuff = VK_NULL_HANDLE;
XEG_NeuralUpscaleDescription description;
description.sType = XEG_STRUCTURE_TYPE_NEURAL_UPSCALE_DESCRIPTION;
description.pNext = nullptr;
description.inputImage = inputImageView;
description.outputImage = outputImageView;
// sharpness为用户自定义超分锐化参数，此处以参数为0.5f为例
description.sharpness = 0.5f;
VkResult res = HMS_XEG_CmdRenderNeuralUpscale(cmdBuff, xegNeuralUpscale, &description);
if (res != VK_SUCCESS) {
    // 异常退出
}

调用HMS_XEG_DestroyNeuralUpscale接口销毁实例。

HMS_XEG_DestroyNeuralUpscale(xegNeuralUpscale);

## Code blocks

### Code block 1

```
#include <cstring>
#include <cstdlib>
#include <EGL/egl.h>
#include <EGL/eglext.h>
#include <GLES2/gl2.h>
#include <GLES2/gl2ext.h>
#include <xengine/xeg_gles_extension.h>
#include <xengine/xeg_gles_neural_upscale.h>
#include <native_buffer/native_buffer.h>
#include <native_window/external_window.h>
```

### Code block 2

```
#include <string>
#include <vector>
#include <algorithm>
#include <xengine/xeg_vulkan_extension.h>
#include <xengine/xeg_vulkan_neural_upscale.h>
```

### Code block 3

```
find_library(
    # 设置路径变量的名称。
    native-buffer-lib
    # 指定希望CMake定位的NDK库的名称。
    native_buffer
)
find_library(
    # 设置路径变量的名称。
    native-window-lib
    # 指定希望CMake定位的NDK库的名称。
    native_window
)
find_library(
    # 设置路径变量的名称。
    xengine-lib
    # 指定希望CMake定位的NDK库的名称。
    xengine
)
find_library(
    # 设置路径变量的名称。
    EGL-lib
    # 指定希望CMake定位的NDK库的名称。
    EGL
)
find_library(
    # 设置路径变量的名称。
    GLES-lib
    # 指定希望CMake定位的NDK库的名称。
    GLESv3
)

target_link_libraries(nativerender PUBLIC
${EGL-lib} ${GLES-lib} ${xengine-lib} ${native-window-lib} ${native-buffer-lib})
```

### Code block 4

```
 find_library(
    # 设置路径变量的名称。
    hilog-lib
    # 指定希望CMake定位的NDK库的名称。
    hilog_ndk.z
 )
 find_library(
    # 设置路径变量的名称。
    libace-lib
    # 指定希望CMake定位的NDK库的名称。
    ace_ndk.z
 )
 find_library(
    # 设置路径变量的名称。
    libnapi-lib
    # 指定希望CMake定位的NDK库的名称。
    ace_napi.z
 )
 find_library(
    # 设置路径变量的名称。
    libuv-lib
    # 指定希望CMake定位的NDK库的名称。
    uv
 )
 find_library(
    # 设置路径变量的名称。
    xengine-lib
    # 指定希望CMake定位的NDK库的名称。
    xengine
 )
 add_library(libassimp SHARED IMPORTED)
 set_target_properties(
       libassimp
       PROPERTIES
       IMPORTED_LOCATION
       ${CMAKE_CURRENT_SOURCE_DIR}/libs/arm64-v8a/libassimp.so
 )
 target_link_libraries(nativerender PUBLIC
    ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} libnative_window.so libc++.a libktx librawfile.z.so libassimp ${xengine-lib})
```

### Code block 5

```
// 查询XEngine支持的GLES扩展信息
const char* extensions = (const char*)HMS_XEG_GetString(XEG_EXTENSIONS);
// 检查是否支持空域AI超分
if (!strstr(extensions, XEG_NEURAL_UPSCALE_EXTENSION_NAME)) {
    exit(1); // 异常退出
}
```

### Code block 6

```
// 渲染宽高和送显宽高均为用户自定义参数，这里以将800*600的分辨率进行1.5倍超分到1200*900的分辨率为例
uint32_t renderWidth = 800;
uint32_t renderHeight = 600;
uint32_t displayWidth = 1200;
uint32_t displayHeight = 900;
// 获取函数指针
PFNEGLCREATEIMAGEKHRPROC fp_eglCreateImageKHR = reinterpret_cast<PFNEGLCREATEIMAGEKHRPROC>(eglGetProcAddress("eglCreateImageKHR"));
PFNEGLDESTROYIMAGEKHRPROC fp_eglDestroyImageKHR = reinterpret_cast<PFNEGLDESTROYIMAGEKHRPROC>(eglGetProcAddress("eglDestroyImageKHR"));
PFNGLEGLIMAGETARGETTEXTURE2DOESPROC fp_glEGLImageTargetTexture2DOES = reinterpret_cast<PFNGLEGLIMAGETARGETTEXTURE2DOESPROC>(eglGetProcAddress("glEGLImageTargetTexture2DOES"));
// 创建OH_NativeBuffer
OH_NativeBuffer_Config config = {};
config.width = renderWidth;
config.height = renderHeight;
config.usage = NATIVEBUFFER_USAGE_CPU_READ | NATIVEBUFFER_USAGE_CPU_READ_OFTEN | NATIVEBUFFER_USAGE_HW_TEXTURE | NATIVEBUFFER_USAGE_HW_RENDER| NATIVEBUFFER_USAGE_ALIGNMENT_512;
config.format = NATIVEBUFFER_PIXEL_FMT_RGBA_8888;
OH_NativeBuffer* bufferHandle = OH_NativeBuffer_Alloc(&config);
if (bufferHandle == nullptr) {
    // 创建失败，用户可自定义错误处理
}
OHNativeWindowBuffer *nativeWindowBuffer = OH_NativeWindow_CreateNativeWindowBufferFromNativeBuffer(bufferHandle);
EGLImageKHR eglImage = fp_eglCreateImageKHR(eglGetCurrentDisplay(), EGL_NO_CONTEXT, EGL_NATIVE_BUFFER_OHOS, static_cast<EGLClientBuffer>(nativeWindowBuffer), nullptr);
// 创建超分输入纹理
GLuint textureID;
glGenTextures(1, &textureID);
glBindTexture(GL_TEXTURE_2D, textureID);
// 设置纹理环绕和过滤参数
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
// 关联超分输入纹理和eglImage
fp_glEGLImageTargetTexture2DOES(GL_TEXTURE_2D, eglImage);
```

### Code block 7

```
GLuint fboID = 0;
glGenFramebuffers(1, &fboID);
glBindFramebuffer(GL_FRAMEBUFFER, fboID);
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, textureID, 0);
if (glCheckFramebufferStatus(GL_FRAMEBUFFER) != GL_FRAMEBUFFER_COMPLETE) {
    // 创建framebuffer失败，用户可自定义错误处理
}
glViewport(0, 0, renderWidth, renderHeight);
```

### Code block 8

```
// sharpness为用户自定义超分锐化参数，此处以参数为0.3f为例
float sharpness = 0.3f;
HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_SHARPNESS, &sharpness);
// inputScissor为超分输入纹理的裁剪窗口参数
GLuint inputScissor[4] = {0, 0, renderWidth, renderHeight};
HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_SCISSOR, inputScissor);
// 设置超分输入纹理对应的OH_NativeBuffer句柄
HMS_XEG_NeuralUpscaleParameter(XEG_NEURAL_UPSCALE_INPUT_HANDLE, bufferHandle);
```

### Code block 9

```
// 绑定绘制超分结果的帧缓冲，此处使用默认帧缓冲，也可使用用户自定义帧缓冲
glBindFramebuffer(GL_FRAMEBUFFER, 0);
glViewport(0, 0, displayWidth, displayHeight);
// 执行空域AI超分
HMS_XEG_RenderNeuralUpscale(textureID);
```

### Code block 10

```
glDeleteFramebuffers(1, &fboID);
glDeleteTextures(1, &textureID);
if (eglImage != nullptr) {
   fp_eglDestroyImageKHR(eglGetCurrentDisplay(), eglImage);
}
if (nativeWindowBuffer != nullptr) {
   OH_NativeWindow_DestroyNativeWindowBuffer(nativeWindowBuffer);
}
if (bufferHandle != nullptr) {
   OH_NativeBuffer_Unreference(bufferHandle);
}
```

### Code block 11

```
// physicalDevice为Vulkan物理设备，用户需进行初始化
VkPhysicalDevice physicalDevice;
// 查询XEngine支持的Vulkan扩展列表
std::vector<std::string> supportedExtensions;
uint32_t pPropertyCount;
HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, nullptr);
if (pPropertyCount > 0) {
    std::vector<XEG_ExtensionProperties> pProperties(pPropertyCount);
    if (HMS_XEG_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, &pProperties.front()) == VK_SUCCESS) {
        for (auto ext : pProperties) {
             supportedExtensions.push_back(ext.extensionName);
         }
    }
}
// 查询是否支持空域AI超分
if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG_NEURAL_UPSCALE_EXTENSION_NAME) == supportedExtensions.end()) {
    exit(1); // 异常退出
}
```

### Code block 12

```
XEG_NeuralUpscale xegNeuralUpscale;
```

### Code block 13

```
// 渲染宽高和超分后宽高均为用户自定义参数，此处以将800*600分辨率超分至1200*900分辨率为例
uint32_t m_renderWidth = 800;
uint32_t m_renderHeight = 600;
uint32_t m_upscaleWidth = 1200;
uint32_t m_upscaleHeight = 900;
// Vulkan逻辑设备，用户需进行初始化
VkDevice device = VK_NULL_HANDLE;
// VkRect2D为Vulkan指定的二维区域结构
// srcRect2D为超分输入纹理区域，用户可自定义
VkRect2D srcRect2D;
// srcRect2D.offset.x和srcRect2D.offset.y为原点偏移量
srcRect2D.offset.x = 0;
srcRect2D.offset.y = 0;
// srcRect2D.extent.width与srcRect2D.extent.height为输入纹理采样区域宽高
srcRect2D.extent.width = m_renderWidth;
srcRect2D.extent.height = m_renderHeight;
// dstRect2D为超分输出纹理区域，用户可自定义
VkRect2D dstRect2D;
// dstRect2D.offset.x和dstRect2D.offset.y为原点偏移量
dstRect2D.offset.x = 0;
dstRect2D.offset.y = 0;
// dstRect2D.extent.width与dstRect2D.extent.height为超分纹理写入区域宽高
dstRect2D.extent.width = m_upscaleWidth;
dstRect2D.extent.height = m_upscaleHeight;
XEG_NeuralUpscaleCreateInfo createInfo;
createInfo.sType = XEG_STRUCTURE_TYPE_NEURAL_UPSCALE_CREATE_INFO;
createInfo.pNext = nullptr;
createInfo.inputRegion = srcRect2D;
createInfo.outputRegion = dstRect2D;
createInfo.inputSize = srcRect2D.extent;
createInfo.outputSize = dstRect2D.extent;
createInfo.outputFormat = VK_FORMAT_R8G8B8A8_UNORM;
VkResult result = HMS_XEG_CreateNeuralUpscale(device, &createInfo, &xegNeuralUpscale);
if (result != VK_SUCCESS) {
    // 异常退出
}
```

### Code block 14

```
// inputImageView为用户创建的超分输入图像的VkImageView
VkImageView inputImageView = VK_NULL_HANDLE;
// outputImageView为用户创建的超分输出图像的VkImageView
VkImageView outputImageView = VK_NULL_HANDLE;
// cmdBuff为命令缓冲区，用户需进行初始化
VkCommandBuffer cmdBuff = VK_NULL_HANDLE;
XEG_NeuralUpscaleDescription description;
description.sType = XEG_STRUCTURE_TYPE_NEURAL_UPSCALE_DESCRIPTION;
description.pNext = nullptr;
description.inputImage = inputImageView;
description.outputImage = outputImageView;
// sharpness为用户自定义超分锐化参数，此处以参数为0.5f为例
description.sharpness = 0.5f;
VkResult res = HMS_XEG_CmdRenderNeuralUpscale(cmdBuff, xegNeuralUpscale, &description);
if (res != VK_SUCCESS) {
    // 异常退出
}
```

### Code block 15

```
HMS_XEG_DestroyNeuralUpscale(xegNeuralUpscale);
```
