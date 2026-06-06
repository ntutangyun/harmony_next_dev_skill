# 能力说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-customized-multi-targets-and-products-guides_

-main
|------ets
|--------code
|----------test.ets
|----target
|------util
|--------util.ets
packageName为entry。
sourceRoot为src/main、src/target。
sourcePath为ets/code、util。
sourceFileName为test.ets、util.ets。

规格限制

1. import xxx from '<packageName>/sourcePath/sourceFileName' ：通过packageName的方式，省略sourceRoot，可以实现不同target下的差异化构建。

2. 支持hap、hsp、har（请注意：开启文件/文件夹名称混淆的har模块需要使用-keep-file-name指定sourceRoot，sourcePath，sourceFileName对应的文件/文件夹名称不被混淆）。

3. 不支持跨模块引用。

4. 不支持动态import。

编译时模块target的选择优先级说明

在模块编译的过程中，该模块使用的sourceRoots由当前模块编译时的target来决定。当前模块编译时选择target的优先级则为：命令行显式指定 > 直接引用方target > default。

如以下示例：

hap -> hsp -> har（->表示依赖）

其中hap和hsp存在三个target：default、custom、static，而har存在两个target：default、static。

执行编译命令：hvigorw -p module=hap@custom assembleHap，hap指定target为custom进行编译，那么三个模块编译时的target分别为：

hap: custom，命令行显式指定；

hsp: custom，命令行没有显式指定，则基于直接引用方查找，hsp的直接引用方为hap，hap的target为custom，hsp存在该target，则hsp的target为custom；

har: default，命令行没有显式指定，则基于直接引用方查找，har的直接引用方为hsp，hsp的target为custom，har不存在该target，则har的target为default；

执行编译命令：hvigorw -p module=hap@custom,hsp@static assembleHap assembleHsp，hap指定target为custom，hsp则指定target为static进行编译，那么三个模块编译时的target分别为：

hap: custom，命令行显式指定；

hsp: static，命令行显式指定；

har: static，命令行没有显式指定，则基于直接引用方查找，har的直接引用方为hsp，hsp的target为static，har存在该target，则har的target为static。

在当前依赖关系的基础上，添加依赖：hap -> har。执行编译命令：hvigorw -p module=hap@custom,hsp@static assembleHap assembleHsp。由于har没有显式指定target，且存在两个target不同的直接引用方（hap和hsp，对应的target分别为custom和static），所以编译过程中har的target只能二选一。基于这种场景，建议开发者显式指定模块的target进行编译：hvigorw -p module=hap@custom,hsp@static,har@static assembleHap assembleHsp assembleHar。

示例

1. 在entry模块的build-profile.json5中添加sourceRoots：

{
  "apiType": "stageMode",
  "buildOption": {},
  "targets": [ 
    { 
      "name": "default", 
      "source": { 
        "sourceRoots": ["./src/default"] // 配置target为default的差异化代码空间
      } 
    }, 
    { 
      "name": "custom", 
      "source": { 
        "sourceRoots": ["./src/custom"] // 配置target为custom的差异化代码空间
      } 
    } 
  ]
}

2. 在src目录下新增default/Test.ets和custom/Test.ets，新增后的模块目录结构：

entry
  |--src
    |--main
      |--ets
        |--pages
          |--Index.ets
    |--default
      |--Test.ets  // 新增
    |--custom
      |--Test.ets  // 新增  

3. 在default/Test.ets中写入代码：

export const getName = () => "default"

4. 在custom/Test.ets中写入代码：

export const getName = () => "custom"

5. 修改src/main/ets/pages/Index.ets的代码：

import { getName } from 'entry/Test'; // 其中entry为模块级的oh-package.json5中的name字段的值
@Entry
@Component
struct Index { 
  @State message: string = getName(); 
  build() { 
    RelativeContainer() { 
      Text(this.message) 
    } 
    .height('100%') 
    .width('100%') 
  }
}

6. 在工程级的build-profile.json5中配置targets：

{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.1.1(24)",
        "runtimeOS": "HarmonyOS",
      }
    ],
    "buildModeSet": [
      {
        "name": "debug",
      },
      {
        "name": "release"
      }
    ]
  },
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        {
          "name": "default",
          "applyToProducts": [
            "default"
          ]
        },
        {
          "name": "custom",
          "applyToProducts": [
            "default"
          ]
        }
      ]
    }
  ]
}

7. Sync完成后，选择entry的target为default，点击Run，界面展示default；选择entry的target为custom，点击Run，则界面展示custom。

定义产物的资源

每个target使用的资源文件可能存在差异，在开发过程中，开发者可以将每个target所使用的资源存放在不同的资源目录下。其中，ArkTS工程支持对main目录下的资源文件目录（resource）进行定制；JS工程支持对main目录下的资源文件目录（resource）及 Ability下的资源文件目录（res）进行定制。如下为ArkTS工程的资源文件目录定制示例：

{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default", 
      "source": { 
        "pages": [ 
          "pages/Index" 
        ] 
      }, 
      "resource": {  // 定义默认版target使用的资源文件目录 
        "directories": [ 
          "./src/main/resources_default" 
        ] 
      } 
    }, 
    { 
      "name": "free", 
      "config": { 
        "deviceType": [ 
          "phone" 
        ] 
      }, 
      "source": {   
        "pages": [ 
          "pages/Index", 
          "pages/Page1" 
        ] 
      }, 
      "resource": {  // 定义免费版target使用的资源文件目录 
        "directories": [ 
          "./src/main/resources_free",
          "./src/main/resources_default"
        ] 
      } 
    }, 
    { 
      "name": "pay", 
      "config": { 
        "deviceType": [ 
          "phone" 
        ] 
      }, 
      "source": {   
        "pages": [ 
          "pages/Index", 
          "pages/Page2" 
        ] 
      }, 
      "resource": {  // 定义付费版target使用的资源文件目录
        "directories": [ 
          "./src/main/resources_pay",
          "./src/main/resources_default"
        ] 
      } 
    } 
  ] 
}

编译构建时，资源文件存在以下优先级顺序：

AppScope目录下的资源文件会合入到模块下相同路径的资源目录中。如果两个目录下存在重名文件，编译打包后AppScope目录下的资源文件会覆盖模块下的资源。
如果target引用的多个资源文件目录下，存在重名文件，则在构建打包过程中，将按照配置的资源文件目录顺序进行选择。例如，上述付费版target引用的资源中，resources_pay和resources_default中存在重名文件，则resources_pay中的资源会被打包到HAP中。
定义产物的icon、label、launchType

针对每一个的target的ability，均可以定制不同的icon、label和launchType。如果不定义，则该target采用module.json5中module.abilities配置的icon、label，launchType默认为"singleton"。示例如下所示：

{ 
   "apiType": 'stageMode', 
   "buildOption": { 
   }, 
   "targets": [ 
     { 
       "name": "default", 
       "source": {
        "abilities": [
          {
            "name": "EntryAbility",
            "icon":"$media:layered_image",
            "label":"$string:EntryAbility_label",
            "launchType": "singleton"
          }
        ]
      }
     }, 
     { 
       "name": "free", 
       "source": {
        "abilities": [
          {
            "name": "EntryAbility",
            "icon":"$media:layered_image",
            "label":"$string:EntryAbility_label",
            "launchType": "multiton"
          }
        ]
      }
     }
   ] 
 }
定义C++工程依赖的.so文件

在 C++ 工程中，可以对每个target依赖的.so文件进行定制。例如某模块依赖了function1.so、function2.so和function3.so三个文件，其中target为default的产物依赖了function1.so和function2.so；其中target为vip的产物依赖了function1.so和 function3.so，则示例代码如下所示：

{
  "apiType": 'stageMode',
  "buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": [],
      "abiFilters": [
        "arm64-v8a",
        "x86_64"
      ],
      "cppFlags": "",
    }
  },
  "targets": [  //定义不同的target 
    {
      "name": "default",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              //按照.so文件的优先级顺序，打包最高优先级的function1.so文件 
              "pickFirsts": [
                "**/function1.so"
              ],
              //排除不打包的function3.so文件 
              "excludes": [
                "**/function3.so"
              ],
              //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件 
              "enableOverride": true
            }
          }
        }
      }
    },
    {
      "name": "vip",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              //按照.so文件的优先级顺序，打包最高优先级的function1.so文件 
              "pickFirsts": [
                "**/function1.so"
              ],
              //排除不打包的function2.so文件 
              "excludes": [
                "**/function2.so"
              ],
              //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件 
              "enableOverride": true
            }
          }
        }
      }
    }
  ]
}
定制HAR多目标构建产物

每一个HAR模块均支持定制不同的target，通过在模块中的build-profile.json5文件中实现差异化定制，当前支持设备类型（deviceType）、资源（resource）、buildOption配置项（如C++依赖的.so、混淆配置、abi类型、cppFlags等）、源码集（source）的定制。

DevEco Studio 6.0.2 Beta1版本之前，在DevEco Studio中构建HAR模块时，仅支持default target，若需指定其他target，需通过命令行来指定和构建。

例如构建自定义target为free的HAR，可参考执行以下命令：

hvigorw --mode module -p product=default -p module=library@free -p buildMode=debug assembleHar

从DevEco Studio 6.0.2 Beta1版本开始，支持在DevEco Studio中选择HAR模块的target，选择的target仅在单独构建HAR包时生效。如果是构建HAP/HSP，会动态计算依赖HAR的target，具体请参考多产物构建target。

定义产物的deviceType

每一个target均可以指定支持的设备类型deviceType，也可以不定义。如果不定义，则该target默认支持module.json5/config.json中定义的设备类型。

同时，在定义每个target的deviceType时，支持的设备类型必须在module.json5或config.json中已经定义。例如，在上述定义的2个target中，分别定义default默认支持所有设备类型，free版本只支持2in1设备。

{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default"  //未定义deviceType，默认支持config.json或module.json5中定义的设备类型 
    }, 
    { 
      "name": "free",
      "config": { 
        "deviceType": [  //定义free支持的设备类型为2in1
          "2in1" 
        ] 
      } 
    }
  ] 
}

定义C++工程依赖的.so文件

在 C++ 工程中，可以对每个target依赖的.so文件进行定制。例如某模块依赖了function1.so、function2.so和function3.so三个文件，其中target为default的产物依赖了function1.so和function2.so；其中target为vip的产物依赖了function1.so和 function3.so，则示例代码如下所示：

{
  "apiType": 'stageMode',
  "buildOption": {
    "externalNativeOptions": {
      "path": "./src/main/cpp/CMakeLists.txt",
      "arguments": [],
      "abiFilters": [
        "arm64-v8a",
        "x86_64"
      ],
      "cppFlags": "",
    }
  },
  "targets": [  //定义不同的target 
    {
      "name": "default",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              //按照.so文件的优先级顺序，打包最高优先级的function1.so文件 
              "pickFirsts": [
                "**/function1.so"
              ],
              //排除不打包的function3.so文件 
              "excludes": [
                "**/function3.so"
              ],
              //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件 
              "enableOverride": true
            }
          }
        }
      }
    },
    {
      "name": "vip",
      "config": {
        "buildOption": {
          "nativeLib": {
            "filter": {
              //按照.so文件的优先级顺序，打包最高优先级的function1.so文件 
              "pickFirsts": [
                "**/function1.so"
              ],
              //排除不打包的function2.so文件 
              "excludes": [
                "**/function2.so"
              ],
              //允许当.so中资源重名冲突时，使用高优先级的.so文件覆盖低优先级的.so文件 
              "enableOverride": true
            }
          }
        }
      }
    }
  ]
}
定义产物的资源

每个target使用的资源文件可能存在差异，在开发过程中，开发者可以将每个target所使用的资源存放在不同的资源目录下。其中，ArkTS工程支持对main目录下的资源文件目录（resource）进行定制；JS工程支持对main目录下的资源文件目录（resource）及 Ability下的资源文件目录（res）进行定制。如下为ArkTS工程的资源文件目录定制示例：

{ 
  "apiType": 'stageMode', 
  "buildOption": { 
  }, 
  "targets": [ 
    { 
      "name": "default",
      "resource": {  //定义默认版target使用的资源文件目录 
        "directories": [ 
          "./src/main/resources_default" 
        ] 
      } 
    }, 
    { 
      "name": "free", 
      "config": { 
        "deviceType": [ 
          "2in1" 
        ] 
      }, 
      "resource": {  //定义免费版target使用的资源文件目录 
        "directories": [ 
          "./src/main/resources_free",
          "./src/main/resources_default"
        ] 
      } 
    },
  ] 
}
定义产物的source源码集-sourceRoots

请参考定义产物的source源码集-sourceRoots。

配置APP多目标构建产物

APP用于应用/元服务上架发布，针对不同的应用场景，可以定制不同的product，每个product中支持对bundleName、bundleType、签名信息、icon和label以及包含的target进行定制。

定义目标产物product

每一个product对应一个定制的APP包，因此，在定制APP多目标构建产物前，应提前规划好需要定制的product名称。例如，定义productA和productB。工程级build-profile.json5文件示例如下：

在定制product时，必须存在"default"的product，否则编译时会出现错误。

说明

在编译构建流程中，default product或者default target都承载着兜底机制，其中，default target可以缺省。当某个模块的default target缺省时，Hvigor会默认加上default target并挂载到default product中，因此，构建default product时，默认会构建出default target。如果不想构建出default target，建议参考定义product中包含的target，自定义product以及包含的target。

"app": { 
  "signingConfigs": [], 
  "products": [ 
    { 
      "name": "default", 
      "signingConfig": "default", 
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
    }, 
    { 
      "name": "productA", 
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
    }, 
    { 
      "name": "productB", 
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
    } 
  ], 
  "buildModeSet": [ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  ] 
}

定义产物的APP包名和供应商名称

每一个product均可以指定产物命名和供应商名称。

{ 
  "app": { 
    "signingConfigs": [], 
    "products": [ 
      { 
        "name": "default", 
        "signingConfig": "default", 
        "compatibleSdkVersion": "6.1.1(24)", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputName-1.0.0"  //产物名称为customizedProductOutputName-1.0.0
        }, 
        "vendor": "customizedProductVendorName"   //供应商名称为customizedProductVendorName
      }, 
      { 
        "name": "productA", 
        "compatibleSdkVersion": "6.1.1(24)", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputNameA-1.0.0"  //产物名称为customizedProductOutputNameA-1.0.0
        }, 
        "vendor": "customizedProductVendorNameA"   //供应商名称为customizedProductVendorNameA
      }, 
      { 
        "name": "productB", 
        "compatibleSdkVersion": "6.1.1(24)", 
        "runtimeOS": "HarmonyOS", 
        "output": { 
          "artifactName": "customizedProductOutputNameB-1.0.0" //产物名称为customizedProductOutputNameB-1.0.0
        }, 
        "vendor": "customizedProductVendorNameB"   //供应商名称为customizedProductVendorNameB
      } 
    ], 
    "buildModeSet": [ 
      { 
        "name": "debug", 
      }, 
      { 
        "name": "release" 
      } 
    ] 
  }, 
}

如果已配置签名，product产物对应的APP包名为开发者定制的名称；如果未配置签名，product产物对应的APP包名为开发者定制的名称+unsigned。

定义product的bundleName

针对每个定义的product，均可以定制不同的bundleName，如果product未定义bundleName，则采用工程默认的bundleName。示例如下所示：

"app": { 
  "signingConfigs": [], 
  "products": [ 
    { 
      "name": "default", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com"  //定义default的bundleName信息 
    }, 
    { 
      "name": "productA", 
      "signingConfig": "default", 
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com"  //定义productA的bundleName信息
    }, 
    { 
      "name": "productB", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com"  //定义productB的bundleName信息 
    } 
  ], 
  "buildModeSet": [ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  ] 
}

定义product的bundleType

针对每个定义的product，均可以定制不同的bundleType。开发者可以通过定义每个product的bundleType，分别定义产物类型：

bundleType值为app，表示产物为应用；
bundleType值为atomicService，表示产物为元服务。

如果product未定义bundleType，则采用工程的bundleType（即创建工程时选择的Application/Atomic Service）。示例如下所示：

"app": { 
  "signingConfigs": [], 
  "products": [ 
    { 
      "name": "default", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com",   
      "bundleType": "app" //定义default的bundleType信息 
    },
    { 
      "name": "productA", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com",    
      "bundleType": "atomicService"  //定义productA的bundleType信息 
    },
    { 
      "name": "productB", 
      "signingConfig": "default",
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com",    
      "bundleType": "atomicService"  //定义productB的bundleType信息 
    } 
  ], 
  "buildModeSet": [ 
    { 
      "name": "debug", 
    },
    { 
      "name": "release"
    } 
  ] 
}

定义product的签名配置信息

针对每个定义的product，均可以定制不同的signingConfig签名文件，如果product未定义signingConfig，则构建生成未签名的APP包。

通常情况下，您首先需要在签名配置界面或工程的build-profile.json5文件中配置签名信息。例如在File > Project Structure > Project > Signing Configs界面，分别配置default、productA和productB的签名信息，如下图所示：

签名信息配置完成后，再添加各个product对应的签名文件，示例如下所示：

您也可以提前在product中定义签名文件信息，然后在签名界面对每个product进行签名，确保配置的product签名文件与签名界面配置的签名文件保持一致即可。

"app": { 
  "signingConfigs": [], //此处通过界面配置签名后会自动生成相应的签名配置，本文略 
  "products": [ 
    { 
      "name": "default", 
      "signingConfig": "default", //定义default的签名文件信息
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example00.com"  
    }, 
    { 
      "name": "productA", 
      "signingConfig": "productA", //定义productA的签名文件信息
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example01.com"  
    }, 
    { 
      "name": "productB", 
      "signingConfig": "productB", //定义productB的签名文件信息
      "compatibleSdkVersion": "6.1.1(24)", 
      "runtimeOS": "HarmonyOS", 
      "bundleName": "com.example02.com" 
    } 
  ], 
  "buildModeSet": [ 
    { 
      "name": "debug", 
    }, 
    { 
      "name": "release" 
    } 
  ] 
}

定义product的icon和label

针对每个定义的product，均可以定制不同的icon和label，如果product未定义icon和label，则采用工程默认的icon和label。示例如下所示：

说明

products中的icon和label字段在编译时会替换app.json5中对应的字段，app.json5和module.json5均可以配置这两个字段，如果都配置，优先级顺序请参考配置优先级。

{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.1.1(24)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:default_icon", //定义default的icon
        "label":"$string:default_name", //定义default的label
      },
      {
        "name": "productA",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.1.1(24)",
        "icon":"$media:productA_icon", //定义productA的icon
        "label":"$string:productA_name", //定义productA的label
      },
      {
        "name": "productB",
        "signingConfig": "default",
        "compatibleSdkVersion": "6.1.1(24)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:productB_icon", //定义productB的icon
        "label":"$string:productB_name",  //定义productB的label
      }
    ],
    "buildModeSet": [
      {
        "name": "debug",
      },
      {
        "name": "release"
      }
    ]
  },
  ...
}
定义product中包含的target

开发者可以选择需要将定义的target分别打包到哪一个product中，每个product可以指定一个或多个target。

同时每个target也可以打包到不同的product中，但是同一个module的不同target不能打包到同一个product中（除非该module的不同target配置了不同的deviceType或distributionFilter/distroFilter）。

例如，前面定义了default、free和pay三个target，现需要将default target打包到default product中；将free target打包到productA中；将pay target打包到productB中，对应的示例代码如下所示：

{ 
  "app": { 
    "signingConfigs": [], //此处通过界面配置签名后会自动生成相应的签名配置，本文略 
    "products": [ 
      { 
        "name": "default", 
        "signingConfig": "default",
        "compatibleSdkVersion": "6.1.1(24)", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example00.com"  
      }, 
      { 
        "name": "productA", 
        "signingConfig": "productA",
        "compatibleSdkVersion": "6.1.1(24)", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example01.com"  
      }, 
      { 
        "name": "productB", 
        "signingConfig": "productB",  
        "compatibleSdkVersion": "6.1.1(24)", 
        "runtimeOS": "HarmonyOS", 
        "bundleName": "com.example02.com" 
      } 
    ], 
  "modules": [ 
    { 
      "name": "entry", 
      "srcPath": "./entry", 
      "targets": [ 
        { 
          "name": "default",  //将default target打包到default APP中 
          "applyToProducts": [ 
            "default" 
          ] 
        }, 
        { 
          "name": "free",  //将free target打包到productA APP中 
          "applyToProducts": [ 
            "productA" 
          ] 
        }, 
        { 
          "name": "pay",  //将pay target打包到productB APP中 
          "applyToProducts": [ 
            "productB" 
          ] 
        } 
      ] 
    } 
  ] 
}
构建定义的目标产物

每个target对应一个HAP，每个product对应一个APP包，在编译构建时，如果存在多product或多target时，您可以指定编译具体的包。

单击右上角的图标，指定需要打包的Product及Target，然后单击Apply保存。例如选择"ProductA"中，entry模块对应的"free" Target。

Product：选择需要构建的APP包。
Build Mode：选择编译模式。
Product Info：该APP包的BundleName和SigningConfig信息。
Target Select：选择各个模块的Target，该Target需要包含在定义的Product中才能选择，如果未包含则显示"No Target to apply"。

然后执行编译构建APP/HAP的任务：

单击菜单栏的Build > Build Hap(s)/APP(s) > Build APP(s) ，构建指定的Product对应的APP。例如，按照上述配置文件和上图中的配置，此时DevEco Studio将构建生成ProductA的APP包。default和ProductB的APP均不会生成。
单击菜单栏的Build > Build Hap(s)/APP(s) > Build Hap(s)，构建指定Product下的所有Target对应的HAP。

如果您想将某个模块下的指定target打包生成HAP，可以在工程目录中，单击模块名，然后再单击Build > Make Module ‘模块名 ’，此时DevEco Studio将构建生成模块下指定target对应的包。例如，按照上述配置，此时DevEco Studio将构建生成entry模块下free的HAP。

调试和运行指定的Target

使用DevEco Studio调试或运行应用/元服务时，每个模块只能选择其中的一个target运行，可以通过单击右上角的图标，指定需要调试或运行的Product下对应的Module Target，然后单击Apply保存。

说明

在选择需要调试或运行的target时，需要注意选择该target所属的Product，否则将找不到可调试和运行的target。

多产物构建target
align target

编译构建时，优先级最高的target。工程配置align target后，如果模块中存在align target，那么将自动选择align target进行构建。align target作用范围是整个工程，只能配置一个，支持命令行和配置文件两种方式。

命令行方式示例如下：
hvigorw -c properties.ohos.align.target=target1 assembleHap
在hvigor-config.json5配置文件中添加ohos.align.target，示例如下：
"properties": {
  'ohos.align.target': 'target1'
},
fallback target

当模块不存在指定的target时会选用default进行构建，但如果不想用default进行构建，那么可以配置fallback target，当找不到指定target时，如果模块中存在fallback target，则使用fallback target进行构建。fallback target作用范围是整个工程，可配置多个，配置多个时按数组顺序先命中的生效。

命令行方式示例如下：
hvigorw -c properties.ohos.fallback.target=target1,target2 assembleHap
在hvigor-config.json5配置文件中添加ohos.fallback.target，示例如下：
"properties": {
  'ohos.fallback.target': ['target1', 'target2']
}
说明
align target和fallback target配置方式命令行优先级高于配置文件。
使用配置文件配置align target和fallback target，仅支持DevEco Studio界面Build菜单栏功能，不支持Run菜单栏功能，可通过hdc命令行工具进行推包运行、调试。

多个target的优先级顺序为：align target > 命令行指定模块target > 父级模块target > fallback target > default。

举例说明：

工程依赖entry->lib1->lib2，需要构建多个产品A、B、C，工程中target配置如下：

entry: A、B、default

lib1: B、C、default

lib2: A、C、default

指定align target为A，fallback target为C。那么构建hap时的编译命令为：

hvigorw --mode module -p module=entry -c properties.ohos.align.target=A -c properties.ohos.fallback.target=C assembleHap

编译的target选择就是：entry@A, lib1@C, lib2@A。

说明

以上所有说明仅针对非ohosTest模式。在ohosTest模式下，依赖的target固定为default，其他target均不生效。

配置多目标产物
实践说明
