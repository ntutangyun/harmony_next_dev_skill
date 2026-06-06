# 使用说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-matmul-usage-description_

// 纯cube模式（只有矩阵计算）场景下，需要设置该代码宏，并且必须在#include "lib/matmul_intf.h"之前设置
// #define ASCENDC_CUBE_ONLY
#include "lib/matmul_intf.h"
 
typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> aType;
typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, half> bType;
typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> cType;
typedef matmul::MatmulType<AscendC::TPosition::GM, CubeFormat::ND, float> biasType;
matmul::Matmul<aType, bType, cType, biasType> mm;

创建对象时需要传入A、B、C、Bias的参数类型信息， 类型信息通过MatmulType来定义，包括：内存逻辑位置、数据格式、数据类型。

template <AscendC::TPosition POSITION, CubeFormat FORMAT, typename TYPE, bool ISTRANS = false, LayoutMode LAYOUT = LayoutMode::NONE, bool IBSHARE = false> struct MatmulType {
    constexpr static AscendC::TPosition pos = POSITION;
    constexpr static CubeFormat format = FORMAT;
    using T = TYPE;
    constexpr static bool isTrans = ISTRANS;
    constexpr static LayoutMode layout = LAYOUT;
    constexpr static bool ibShare = IBSHARE;
};

表1 MatmulType参数说明

参数	说明
POSITION	

内存逻辑位置

Kirin9020系列处理器：

- A矩阵可设置为TPosition::GM，TPosition::TSCM

- B矩阵可设置为TPosition::GM，TPosition::TSCM

- C矩阵可设置为TPosition::GM


CubeFormat	

Kirin9020系列处理器：

- A矩阵在GM时，支持CubeFormat::ND。

- A矩阵在TSCM时，支持CubeFormat::NZ/CubeFormat::VECTOR。

- B矩阵在GM时，支持CubeFormat::ND/CubeFormat::NZ。

- B矩阵在TSCM时支持CubeFormat::NZ。

- C矩阵在GM时，支持CubeFormat::ND。


TYPE	

Kirin9020系列处理器：

- A矩阵可设置为half。

- B矩阵可设置为half。

- C矩阵可设置为half。


ISTRANS	

是否开启使能矩阵转置的功能。当前不支持转置，只支持设为false。

false为不开启使能矩阵转置的功能，通过SetTensorA和SetTensorB不能设置A、B矩阵是否转置。Matmul会认为A矩阵形状为[M, K]，B矩阵形状为[K, N]。

默认为false不使能转置。


LAYOUT	

表征数据的排布。

NONE：默认值，表示不使用BatchMatmul，其他选项表示使用BatchMatmul。

初始化操作。

REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm, &tiling);

设置左矩阵A、右矩阵B、Bias。

mm.SetTensorA(gm_a);    // 设置左矩阵A
mm.SetTensorB(gm_b);    // 设置右矩阵B
mm.SetBias(gm_bias);    // 设置Bias
 
mm.SetLocalWorkspace(ubBuf);

完成矩阵乘操作。

调用Iterate完成单次迭代计算，叠加while循环完成单核全量数据的计算。Iterate方式，可以自行控制迭代次数，完成所需数据量的计算，方式比较灵活。
while (mm.Iterate()) {
     mm.GetTensorC(gm_c);
 }
调用IterateAll完成单核上所有数据的计算。IterateAll方式，无需循环迭代，使用比较简单。
mm.IterateAll(gm_c);

结束矩阵乘操作。

mm.End();
Matmul
Matmul模板参数
