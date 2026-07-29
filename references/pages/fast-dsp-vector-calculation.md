# 使用DSP进行向量计算

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-vector-calculation_

数字信号处理（DSP）中的向量计算功能，提供涵盖向量基本算术运算、初始化与统计归约、复数运算以及信号处理与线性代数等领域的接口。当开发者需要对传感器数据、音频信号或其他数值序列进行算术运算、统计计算、复数分析、卷积、矩阵乘法或窗函数生成等操作时，可以使用向量计算接口。

向量计算支持单精度（float）和双精度（double）两种数据类型，并针对ARM NEON指令集进行了优化，在步长为1的连续存储场景下可获得显著性能提升。需要注意的是，为了提升性能，部分接口对浮点数的计算顺序进行了调整，可能影响结果精度。

接口说明

具体API说明详见接口文档。

[h2]向量基本算术运算

涵盖所有逐元素的基础数值运算，包括标量与向量的组合运算、向量之间的四则运算、绝对值、平方、阈值以及幂运算等。

标量与向量的运算

名称	描述
void HMS_FAST_DSP_Vsmul (const float* input, size_t strideInput, const float scalar, float* output, size_t strideOutput, size_t length)	将向量的每个元素乘以标量（单精度）。
void HMS_FAST_DSP_VsmulD (const double* input, size_t strideInput, const double scalar, double* output, size_t strideOutput, size_t length)	将向量的每个元素乘以标量（双精度）。
void HMS_FAST_DSP_Vsdiv (const float* input, size_t strideInput, const float scalar, float* output, size_t strideOutput, size_t length)	将向量的每个元素除以标量（单精度）。
void HMS_FAST_DSP_VsdivD (const double* input, size_t strideInput, const double scalar, double* output, size_t strideOutput, size_t length)	将向量的每个元素除以标量（双精度）。
void HMS_FAST_DSP_Svdiv (const float scalar, const float* input, size_t strideInput, float* output, size_t strideOutput, size_t length)	将标量除以向量的每个元素（单精度）。
void HMS_FAST_DSP_SvdivD (const double scalar, const double* input, size_t strideInput, double* output, size_t strideOutput, size_t length)	将标量除以向量的每个元素（双精度）。
void HMS_FAST_DSP_Vsadd (const float* input, size_t strideInput, const float scalar, float* output, size_t strideOutput, size_t length)	将标量加到向量的每个元素（单精度）。
void HMS_FAST_DSP_VsaddD (const double* input, size_t strideInput, const double scalar, double* output, size_t strideOutput, size_t length)	将标量加到向量的每个元素（双精度）。

向量之间的运算

名称	描述
void HMS_FAST_DSP_Vadd (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length)	执行向量逐元素加法（单精度）。
void HMS_FAST_DSP_VaddD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length)	执行向量逐元素加法（双精度）。
void HMS_FAST_DSP_Vsub (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length)	执行向量逐元素减法（单精度）。
void HMS_FAST_DSP_VsubD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length)	执行向量逐元素减法（双精度）。
void HMS_FAST_DSP_Vmul (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length)	执行向量逐元素乘法（单精度）。
void HMS_FAST_DSP_VmulD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length)	执行向量逐元素乘法（双精度）。
void HMS_FAST_DSP_Vdiv (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length)	执行向量逐元素除法（单精度）。
void HMS_FAST_DSP_VdivD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length)	执行向量逐元素除法（双精度）。
void HMS_FAST_DSP_Vsbsm (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float scalar, float* outputC, size_t strideC, size_t length)	执行向量减法并缩放（单精度）。
void HMS_FAST_DSP_VsbsmD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double scalar, double* outputC, size_t strideC, size_t length)	执行向量减法并缩放（双精度）。
void HMS_FAST_DSP_Vdist (const float* inputA, size_t strideA, const float* inputB, size_t strideB, float* outputC, size_t strideC, size_t length)	计算两个向量对应元素的欧几里得范数：C[i]等于A[i]与B[i]的平方和的算术开方根（单精度）。
void HMS_FAST_DSP_VdistD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, double* outputC, size_t strideC, size_t length)	计算两个向量对应元素的欧几里得范数：C[i]等于A[i]与B[i]的平方和的算术开方根（双精度）。

向量变换

名称	描述
void HMS_FAST_DSP_Vsq (const float* input, size_t strideInput, float* output, size_t strideOutput, size_t length)	计算向量每个元素的平方（单精度）。
void HMS_FAST_DSP_VsqD (const double* input, size_t strideInput, double* output, size_t strideOutput, size_t length)	计算向量每个元素的平方（双精度）。
void HMS_FAST_DSP_Vabs (const float* input, size_t strideInput, float* output, size_t strideOutput, size_t length)	计算向量每个元素的绝对值（单精度）。
void HMS_FAST_DSP_VabsD (const double* input, size_t strideInput, double* output, size_t strideOutput, size_t length)	计算向量每个元素的绝对值（双精度）。
void HMS_FAST_DSP_Vthr (const float* input, size_t strideInput, const float threshold, float* output, size_t strideOutput, size_t length)	对向量应用阈值：若input[i] < threshold则取threshold，否则取原值（单精度）。
void HMS_FAST_DSP_VthrD (const double* input, size_t strideInput, const double threshold, double* output, size_t strideOutput, size_t length)	对向量应用阈值：若input[i] < threshold则取threshold，否则取原值（双精度）。

幂运算

名称	描述
void HMS_FAST_DSP_Vvpow (const float* inputA, const float* inputB, float* outputC, size_t length)	执行向量逐元素幂运算：C[i]等于A[i]的B[i]次方（单精度）。
void HMS_FAST_DSP_VvpowD (const double* inputA, const double* inputB, double* outputC, size_t length)	执行向量逐元素幂运算：C[i]等于A[i]的B[i]次方（双精度）。

[h2]初始化、归约与统计

包含将向量数据归纳为标量的操作、数据生成与填充、类型转换以及元素顺序调整。

初始化/填充

名称	描述
void HMS_FAST_DSP_Vfill (float* vector, size_t stride, size_t length, const float scalar)	使用指定标量值填充向量（单精度）。
void HMS_FAST_DSP_VfillD (double* vector, size_t stride, size_t length, const double scalar)	使用指定标量值填充向量（双精度）。
void HMS_FAST_DSP_Vclr (float* vector, size_t stride, size_t length)	将向量所有元素清零（单精度）。
void HMS_FAST_DSP_VclrD (double* vector, size_t stride, size_t length)	将向量所有元素清零（双精度）。

类型转换

名称	描述
void HMS_FAST_DSP_Vspdp (const float* input, size_t strideInput, double* output, size_t strideOutput, size_t length)	将单精度向量转换为双精度向量。
void HMS_FAST_DSP_Vdpsp (const double* input, size_t strideInput, float* output, size_t strideOutput, size_t length)	将双精度向量转换为单精度向量。

归约运算

名称	描述
float HMS_FAST_DSP_Maxmgv (const float* input, size_t stride, size_t length)	计算步长实数向量中的最大幅值（单精度）。
double HMS_FAST_DSP_MaxmgvD (const double* input, size_t stride, size_t length)	计算步长实数向量中的最大幅值（双精度）。
void HMS_FAST_DSP_Maxvi (const float* input, size_t stride, size_t length, float* value, size_t* index)	查找步长实数向量中的最大值及其索引（单精度）。
void HMS_FAST_DSP_MaxviD (const double* input, size_t stride, size_t length, double* value, size_t* index)	查找步长实数向量中的最大值及其索引（双精度）。
void HMS_FAST_DSP_Minvi (const float* input, size_t stride, size_t length, float* value, size_t* index)	查找步长实数向量中的最小值及其索引（单精度）。
void HMS_FAST_DSP_MinviD (const double* input, size_t stride, size_t length, double* value, size_t* index)	查找步长实数向量中的最小值及其索引（双精度）。
float HMS_FAST_DSP_Sve (const float* input, size_t stride, size_t length)	计算步长实数向量的和（单精度）。
double HMS_FAST_DSP_SveD (const double* input, size_t stride, size_t length)	计算步长实数向量的和（双精度）。
float HMS_FAST_DSP_Svemg (const float* input, size_t stride, size_t length)	计算步长向量的绝对值之和（L1范数）（单精度）。
double HMS_FAST_DSP_SvemgD (const double* input, size_t stride, size_t length)	计算步长向量的绝对值之和（L1范数）（双精度）。
float HMS_FAST_DSP_Meamgv (const float* input, size_t stride, size_t length)	计算步长实数向量绝对值的均值（单精度）。
double HMS_FAST_DSP_MeamgvD (const double* input, size_t stride, size_t length)	计算步长实数向量绝对值的均值（双精度）。
float HMS_FAST_DSP_Svesq (const float* input, size_t stride, size_t length)	计算向量元素的平方和（单精度）。
double HMS_FAST_DSP_SvesqD (const double* input, size_t stride, size_t length)	计算向量元素的平方和（双精度）。
float HMS_FAST_DSP_Dotpr (const float* inputA, size_t strideA, const float* inputB, size_t strideB, size_t length)	计算两个步长实数向量的点积（单精度）。
double HMS_FAST_DSP_DotprD (const double* inputA, size_t strideA, const double* inputB, size_t strideB, size_t length)	计算两个步长实数向量的点积（双精度）。

向量元素操作

名称	描述
void HMS_FAST_DSP_Vrvrs (float* vector, size_t stride, size_t length)	原地反转向量中元素的顺序（单精度）。
void HMS_FAST_DSP_VrvrsD (double* vector, size_t stride, size_t length)	原地反转向量中元素的顺序（双精度）。
void HMS_FAST_DSP_Vsort (float* vector, size_t length, int order)	对向量进行原地排序（单精度）。
void HMS_FAST_DSP_VsortD (double* vector, size_t length, int order)	对向量进行原地排序（双精度）。

[h2]复数运算

包含复数向量的幅度、相位计算以及复数格式转换。

复数基础运算

名称	描述
void HMS_FAST_DSP_Zvabs (const FAST_SplitComplex* input, size_t strideInput, float* output, size_t strideOutput, size_t length)	计算复数向量的幅值（单精度）。
void HMS_FAST_DSP_ZvabsD (const FAST_SplitComplexD* input, size_t strideInput, double* output, size_t strideOutput, size_t length)	计算复数向量的幅值（双精度）。
void HMS_FAST_DSP_Zvmags (const FAST_SplitComplex* input, size_t strideInput, float* output, size_t strideOutput, size_t length)	计算复数向量的幅值平方（单精度）。
void HMS_FAST_DSP_ZvmagsD (const FAST_SplitComplexD* input, size_t strideInput, double* output, size_t strideOutput, size_t length)	计算复数向量的幅值平方（双精度）。
void HMS_FAST_DSP_Zvphas (const FAST_SplitComplex* input, size_t strideInput, float* output, size_t strideOutput, size_t length)	计算复数向量的相位角（弧度制）（单精度）。
void HMS_FAST_DSP_ZvphasD (const FAST_SplitComplexD* input, size_t strideInput, double* output, size_t strideOutput, size_t length)	计算复数向量的相位角（弧度制）（双精度）。

复数格式转换

名称	描述
void HMS_FAST_DSP_Ctoz (const float* input, size_t strideInput, FAST_SplitComplex* output, size_t strideOutput, size_t length)	将交错复数数组转换为分离格式（单精度）。
void HMS_FAST_DSP_CtozD (const double* input, size_t strideInput, FAST_SplitComplexD* output, size_t strideOutput, size_t length)	将交错复数数组转换为分离格式（双精度）。
void HMS_FAST_DSP_Ztoc (const FAST_SplitComplex* input, size_t strideInput, float* output, size_t strideOutput, size_t length)	将分离复数数组转换为交错格式（单精度）。
void HMS_FAST_DSP_ZtocD (const FAST_SplitComplexD* input, size_t strideInput, double* output, size_t strideOutput, size_t length)	将分离复数数组转换为交错格式（双精度）。

[h2]信号处理与线性代数

包含卷积、窗口生成和矩阵运算。

卷积

名称	描述
void HMS_FAST_DSP_Conv (const float* input, size_t strideInput, const float* filter, size_t strideFilter, float* output, size_t strideOutput, size_t outputLength, size_t filterLength)	执行两个向量的卷积运算（单精度）。
void HMS_FAST_DSP_ConvD (const double* input, size_t strideInput, const double* filter, size_t strideFilter, double* output, size_t strideOutput, size_t outputLength, size_t filterLength)	执行两个向量的卷积运算（双精度）。

窗口生成

名称	描述
void HMS_FAST_DSP_HannWindow (float* output, size_t length, HMS_FAST_HannWindowType type)	生成汉宁窗序列（单精度）。
void HMS_FAST_DSP_HannWindowD (double* output, size_t length, HMS_FAST_HannWindowType type)	生成汉宁窗序列（双精度）。

矩阵运算

名称	描述
void HMS_FAST_DSP_Mmul (const float* matrixA, size_t strideA, const float* matrixB, size_t strideB, float* matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP)	执行矩阵乘法（单精度）。
void HMS_FAST_DSP_MmulD (const double* matrixA, size_t strideA, const double* matrixB, size_t strideB, double* matrixC, size_t strideC, size_t rowsM, size_t colsN, size_t colsP)	执行矩阵乘法（双精度）。

开发步骤

在CMake脚本中链接相关动态库。

find_library(
    lib_fast_dsp
    NAMES fast_dsp
)
target_link_libraries(entry PRIVATE ${lib_fast_dsp})

引入头文件。

#include "FASTKit/fast_dsp_common.h"

根据数据类型选择对应的函数（单精度无后缀，双精度带D后缀）。

调用向量计算函数，注意设置正确的stride参数（连续存储时stride为1）。

检查返回结果。

代码示例

[h2]最大值查找示例

#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode max_value_demo() {
    // 定义输入向量
    float input[] = {1.0f, -2.0f, 3.0f, -4.0f, 5.0f};
    size_t length = sizeof(input) / sizeof(float);
    size_t stride = 1;

    // 计算最大幅值（绝对值最大值）
    float max_magnitude = HMS_FAST_DSP_Maxmgv(input, stride, length);
    printf("Max magnitude: %f\n", max_magnitude);  // 输出5.0

    // 查找最大值及其索引
    float max_value = 0.0f;
    size_t max_index = 0;
    HMS_FAST_DSP_Maxvi(input, stride, length, &max_value, &max_index);
    printf("Max value: %f at index %zu\n", max_value, max_index);  // 输出5.0 at index 4

    return FAST_ERROR_CODE_SUCCESS;
}

[h2]统计计算示例

#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode statistics_demo() {
    // 定义输入向量
    float input[] = {1.0f, -2.0f, 3.0f, -4.0f, 5.0f};
    size_t length = sizeof(input) / sizeof(float);
    size_t stride = 1;

    // 计算向量总和
    float sum = HMS_FAST_DSP_Sve(input, stride, length);
    printf("Sum: %f\n", sum);  // 输出3.0

    // 计算绝对值之和（L1范数）
    float sum_abs = HMS_FAST_DSP_Svemg(input, stride, length);
    printf("Sum of absolute values: %f\n", sum_abs);  // 输出15.0

    // 计算绝对值均值
    float mean_abs = HMS_FAST_DSP_Meamgv(input, stride, length);
    printf("Mean of absolute values: %f\n", mean_abs);  // 输出3.0

    return FAST_ERROR_CODE_SUCCESS;
}

[h2]向量运算示例

#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode vector_operations_demo() {
    // 定义两个输入向量
    float inputA[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};
    float inputB[] = {0.5f, 1.0f, 1.5f, 2.0f, 2.5f};
    size_t length = 5;
    size_t stride = 1;

    // 计算点积
    float dot_product = HMS_FAST_DSP_Dotpr(inputA, stride, inputB, stride, length);
    printf("Dot product: %f\n", dot_product);  // 输出27.5

    // 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * 2.0
    float outputC[5];
    float scalar = 2.0f;
    HMS_FAST_DSP_Vsbsm(inputA, stride, inputB, stride, scalar, outputC, stride, length);

    printf("Vector subtraction result:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  outputC[%zu] = %f\n", i, outputC[i]);
    }
    // 输出: 1.0, 2.0, 3.0, 4.0, 5.0

    return FAST_ERROR_CODE_SUCCESS;
}

[h2]复数格式转换示例

#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode complex_conversion_demo() {
    // 定义交错格式复数输入 (real, imag, real, imag...)
    float interleaved[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f};
    size_t length = 3;  // 3个复数
    size_t stride_input = 1;

    // 准备分离格式输出
    float real_array[3];
    float imag_array[3];
    FAST_SplitComplex split_output = {
        .real = real_array,
        .imag = imag_array
    };
    size_t stride_output = 1;

    // 转换为分离格式
    HMS_FAST_DSP_Ctoz(interleaved, stride_input, &split_output, stride_output, length);

    printf("Split format:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  Complex[%zu] = %f + %fi\n", i, real_array[i], imag_array[i]);
    }
    /* xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        Split format:
        Complex[0] = 1.000000 + 2.000000i
        Complex[1] = 3.000000 + 4.000000i
        Complex[2] = 5.000000 + 6.000000i
     */

    // 转换回交错格式
    float interleaved_output[6];
    HMS_FAST_DSP_Ztoc(&split_output, stride_output, interleaved_output, stride_input, length);

    printf("Interleaved format:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  Complex[%zu] = %f + %fi\n", i, interleaved_output[i * 2], interleaved_output[i * 2 + 1]);
    }

    return FAST_ERROR_CODE_SUCCESS;
}

[h2]非连续存储示例

#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode strided_access_demo() {
    // 定义交错存储的复数数据 (real, imag, real, imag...)
    float interleaved[] = {1.0f, 10.0f, 2.0f, 20.0f, 3.0f, 30.0f, 4.0f, 40.0f, 5.0f, 50.0f};
    size_t length = 5;  // 5个实数值
    size_t stride = 2;  // 步长为2，跳过虚部

    // 计算实部向量的最大幅值
    float max_magnitude = HMS_FAST_DSP_Maxmgv(interleaved, stride, length);
    printf("Max magnitude of real parts: %f\n", max_magnitude);  // 输出5.0

    return FAST_ERROR_CODE_SUCCESS;
}

## Code blocks

### Code block 1

```
find_library(
    lib_fast_dsp
    NAMES fast_dsp
)
target_link_libraries(entry PRIVATE ${lib_fast_dsp})
```

### Code block 2

```
#include "FASTKit/fast_dsp_common.h"
```

### Code block 3

```
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode max_value_demo() {
    // 定义输入向量
    float input[] = {1.0f, -2.0f, 3.0f, -4.0f, 5.0f};
    size_t length = sizeof(input) / sizeof(float);
    size_t stride = 1;

    // 计算最大幅值（绝对值最大值）
    float max_magnitude = HMS_FAST_DSP_Maxmgv(input, stride, length);
    printf("Max magnitude: %f\n", max_magnitude);  // 输出5.0

    // 查找最大值及其索引
    float max_value = 0.0f;
    size_t max_index = 0;
    HMS_FAST_DSP_Maxvi(input, stride, length, &max_value, &max_index);
    printf("Max value: %f at index %zu\n", max_value, max_index);  // 输出5.0 at index 4

    return FAST_ERROR_CODE_SUCCESS;
}
```

### Code block 4

```
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode statistics_demo() {
    // 定义输入向量
    float input[] = {1.0f, -2.0f, 3.0f, -4.0f, 5.0f};
    size_t length = sizeof(input) / sizeof(float);
    size_t stride = 1;

    // 计算向量总和
    float sum = HMS_FAST_DSP_Sve(input, stride, length);
    printf("Sum: %f\n", sum);  // 输出3.0

    // 计算绝对值之和（L1范数）
    float sum_abs = HMS_FAST_DSP_Svemg(input, stride, length);
    printf("Sum of absolute values: %f\n", sum_abs);  // 输出15.0

    // 计算绝对值均值
    float mean_abs = HMS_FAST_DSP_Meamgv(input, stride, length);
    printf("Mean of absolute values: %f\n", mean_abs);  // 输出3.0

    return FAST_ERROR_CODE_SUCCESS;
}
```

### Code block 5

```
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode vector_operations_demo() {
    // 定义两个输入向量
    float inputA[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};
    float inputB[] = {0.5f, 1.0f, 1.5f, 2.0f, 2.5f};
    size_t length = 5;
    size_t stride = 1;

    // 计算点积
    float dot_product = HMS_FAST_DSP_Dotpr(inputA, stride, inputB, stride, length);
    printf("Dot product: %f\n", dot_product);  // 输出27.5

    // 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * 2.0
    float outputC[5];
    float scalar = 2.0f;
    HMS_FAST_DSP_Vsbsm(inputA, stride, inputB, stride, scalar, outputC, stride, length);

    printf("Vector subtraction result:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  outputC[%zu] = %f\n", i, outputC[i]);
    }
    // 输出: 1.0, 2.0, 3.0, 4.0, 5.0

    return FAST_ERROR_CODE_SUCCESS;
}
```

### Code block 6

```
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode complex_conversion_demo() {
    // 定义交错格式复数输入 (real, imag, real, imag...)
    float interleaved[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f};
    size_t length = 3;  // 3个复数
    size_t stride_input = 1;

    // 准备分离格式输出
    float real_array[3];
    float imag_array[3];
    FAST_SplitComplex split_output = {
        .real = real_array,
        .imag = imag_array
    };
    size_t stride_output = 1;

    // 转换为分离格式
    HMS_FAST_DSP_Ctoz(interleaved, stride_input, &split_output, stride_output, length);

    printf("Split format:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  Complex[%zu] = %f + %fi\n", i, real_array[i], imag_array[i]);
    }
    /* xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        Split format:
        Complex[0] = 1.000000 + 2.000000i
        Complex[1] = 3.000000 + 4.000000i
        Complex[2] = 5.000000 + 6.000000i
     */

    // 转换回交错格式
    float interleaved_output[6];
    HMS_FAST_DSP_Ztoc(&split_output, stride_output, interleaved_output, stride_input, length);

    printf("Interleaved format:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  Complex[%zu] = %f + %fi\n", i, interleaved_output[i * 2], interleaved_output[i * 2 + 1]);
    }

    return FAST_ERROR_CODE_SUCCESS;
}
```

### Code block 7

```
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode strided_access_demo() {
    // 定义交错存储的复数数据 (real, imag, real, imag...)
    float interleaved[] = {1.0f, 10.0f, 2.0f, 20.0f, 3.0f, 30.0f, 4.0f, 40.0f, 5.0f, 50.0f};
    size_t length = 5;  // 5个实数值
    size_t stride = 2;  // 步长为2，跳过虚部

    // 计算实部向量的最大幅值
    float max_magnitude = HMS_FAST_DSP_Maxmgv(interleaved, stride, length);
    printf("Max magnitude of real parts: %f\n", max_magnitude);  // 输出5.0

    return FAST_ERROR_CODE_SUCCESS;
}
```
