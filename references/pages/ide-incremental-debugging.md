# 增量调试

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-incremental-debugging_

对于大型应用来说，每次修改代码后需要重新构建、推包、安装，整个流程耗时较长。针对该场景，在DevEco Studio和命令行场景中分别提供增量运行调试功能，支持开发者在真机上调试应用时，修改代码后，会识别出代码差异，构建增量包，增量运行调试时只推送增量包，减少大型应用调试推包时间。

说明

C++代码增量调试支持API Version 11及以上版本Stage模型的工程；ArkTS代码增量调试仅支持API Version 12及以上版本Stage模型工程的资源文件修改。

使用DevEco Studio增量调试

[h2]调试C++代码

在工具栏中，选择调试的设备，并单击Run或Debug 启动工程。

点击Apply Changes按钮后，DevEco Studio启动构建的增量构建任务，构建出增量包hqf。增量包构建完成后，将推送安装至设备。

说明

当前增量运行Apply Changes功能，不支持新建和删除代码文件，不支持修改装饰器相关的代码，不支持在代码中使用import新增引用文件。

[h2]调试rawfile/resfile资源

从DevEco Studio 5.1.0 Release版本开始支持增量调试rawfile资源。

在工具栏中，选择调试的设备，并单击Run或Debug 启动工程。

说明

当前对rawfile/resfile资源的增量调试，仅支持代码中直接调用的资源文件。

点击Apply Changes按钮后，DevEco Studio启动构建的增量构建任务，构建出增量包hqf。增量包构建完成后，将推送安装至设备。

使用命令行增量调试

[h2]通过hvigorw构建hqf包

说明

如果已执行步骤1，则步骤2和3无需再执行。

hvigorw --mode module -p module=entry@default,library@default -p product=default assembleHap assembleHsp --info --no-daemon

关于命令行的使用指导请参考hvigorw。

$ hdc shell mkdir data/local/tmp/99c24fdc44694c05be12491d0a48e139
$ hdc file send library-default-signed.hsp "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
$ hdc file send entry-default-signed.hap "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
$ hdc shell bm install -p "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
$ hdc shell rm -rf data/local/tmp/99c24fdc44694c05be12491d0a48e139
$ hdc shell aa start -a {abilityName} -b {bundleName}

abilityName：应用的ability名称。

bundleName：应用包名。

{
  "resources": {
    "resFile": [
      {
        "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\resfile\\test.txt",
        "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
      }
    ],
    "rawFile": [
      {
        "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\rawfile\\test.txt",
        "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
      }
    ]
  }
}

hvigorw --mode module -p module=entry@default,library@default -p product=default assembleDevHqf --info --no-daemon

$ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
$ hdc file send library-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
$ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
$ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o

[h2]通过SDK工具构建hqf包

hdc bm install {hap_path} // 安装包在电脑上，使用该命令，hap_path是安装包路径
hdc shell bm install -p {hap_path}  // 安装包在设备上，使用该命令

{
  "resources": {
    "resFile": [
      {
        "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\resfile\\test.txt",
        "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
      }
    ],
    "rawFile": [
      {
        "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\rawfile\\test.txt",
        "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
      }
    ]
  }
}

可以从工程的build-profile.json5文件中获取到对应的签名文件。

{
    "app" : {
        "bundleName" : "com.ohos.quickfix",
        "versionCode" : 1000000, // 应用版本号
        "versionName" : "1.0.0",
        "patchVersionCode" : 1000000, // 补丁版本号，在每次进行增量调试前，将版本号+1，确保此次增量调试补丁包版本号大于上次增量调试补丁包版本号
        "patchVersionName" : "1000000"  // 与补丁版本号保持一致
    },
    "module" : {
        "name" : "entry",
        "type" : "patch",
        "deviceTypes" : [
            "phone",
            "tablet"
        ],
        "originalModuleHash" : "" // 待修复HAP包的sha256值，置空即可
    }
}

java -jar app_packing_tool.jar --mode hqf --json-path D:\MyApplication\entry\patch.json --lib-path D:\MyApplication\entry\change_test --resources-path D:\MyApplication\entry\src\main\resources --out-path entry-default-unsigned.hqf --force true

关于该命令中需要修改的参数说明如下，其余参数不需要修改：

json-path：指定增量包信息patch.json路径，必选，参考步骤5。

lib-path：指定希望构建打包的so路径，参考步骤2，注意路径不能带上ABI编译环境。

resources-path：指定希望构建打包的resources资源目录，包含rawfile和resfile目录。

out-path：指定输出hqf包路径。

java -jar hap-sign-tool.jar sign-app -keyAlias "OpenHarmony Application Release" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "OpenHarmonyApplication.cer" -profileFile "ohos_provision_release.p7b" -inFile "entry-default-unsigned.hqf" -keystoreFile "OpenHarmony.p12" -outFile "entry-default-signed.hqf" -keyPwd "123456Abc" -keystorePwd "123456Abc"

关于该命令中需要修改的参数说明如下，其余参数不需要修改：

keyAlias：密钥别名。

appCertFile：申请的调试证书文件，格式为.cer。

profileFile：申请的调试Profile文件，格式为.p7b。

inFile：通过打包工具生成的未携带签名信息的hqf。

keystoreFile：密钥库文件，格式为.p12。

outFile：经过签名后生成的携带签名信息的hqf。

keyPwd：密钥密码。

keystorePwd：密钥库密码。

$ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
$ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
$ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o

常见问题

[h2]在其他的开发工具中修改打包so库文件，无法使用DevEco Studio的增量调试功能

问题现象

如果开发者在其他的开发工具中修改打包so库文件，在使用DevEco Studio 4.1 Canary2版本的增量调试功能时，出现无法使用增量调试功能的现象。

解决措施

导致这个问题的原因是在DevEco Studio 4.1 Canary2版本上，对于超过16KB的Native文件，在命中其中的断点后，LLDB调试器会默认持有文件句柄，导致调试过程中无法修改保存该文件。

开发者可通过以下两种方式处理：

settings set use-source-cache false

方式二：建议开发者升级至DevEco Studio 5.1.0 Beta1版本。

## Code blocks

### Code block 1

```
hvigorw --mode module -p module=entry@default,library@default -p product=default assembleHap assembleHsp --info --no-daemon
```

### Code block 2

```
$ hdc shell mkdir data/local/tmp/99c24fdc44694c05be12491d0a48e139
$ hdc file send library-default-signed.hsp "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
$ hdc file send entry-default-signed.hap "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
$ hdc shell bm install -p "data/local/tmp/99c24fdc44694c05be12491d0a48e139"
$ hdc shell rm -rf data/local/tmp/99c24fdc44694c05be12491d0a48e139
$ hdc shell aa start -a {abilityName} -b {bundleName}
```

### Code block 3

```
{
  "resources": {
    "resFile": [
      {
        "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\resfile\\test.txt",
        "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
      }
    ],
    "rawFile": [
      {
        "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\rawfile\\test.txt",
        "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
      }
    ]
  }
}
```

### Code block 4

```
hvigorw --mode module -p module=entry@default,library@default -p product=default assembleDevHqf --info --no-daemon
```

### Code block 5

```
$ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
$ hdc file send library-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
$ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
$ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o
```

### Code block 6

```
hdc bm install {hap_path} // 安装包在电脑上，使用该命令，hap_path是安装包路径
hdc shell bm install -p {hap_path}  // 安装包在设备上，使用该命令
```

### Code block 7

```
{
  "resources": {
    "resFile": [
      {
        "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\resfile\\test.txt",
        "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
      }
    ],
    "rawFile": [
      {
        "filePath": "D:\\MyApplication\\entry\\src\\main\\resources\\rawfile\\test.txt",
        "resourcePath": "D:\\MyApplication\\entry\\src\\main\\resources"
      }
    ]
  }
}
```

### Code block 8

```
{
    "app" : {
        "bundleName" : "com.ohos.quickfix",
        "versionCode" : 1000000, // 应用版本号
        "versionName" : "1.0.0",
        "patchVersionCode" : 1000000, // 补丁版本号，在每次进行增量调试前，将版本号+1，确保此次增量调试补丁包版本号大于上次增量调试补丁包版本号
        "patchVersionName" : "1000000"  // 与补丁版本号保持一致
    },
    "module" : {
        "name" : "entry",
        "type" : "patch",
        "deviceTypes" : [
            "phone",
            "tablet"
        ],
        "originalModuleHash" : "" // 待修复HAP包的sha256值，置空即可
    }
}
```

### Code block 9

```
java -jar app_packing_tool.jar --mode hqf --json-path D:\MyApplication\entry\patch.json --lib-path D:\MyApplication\entry\change_test --resources-path D:\MyApplication\entry\src\main\resources --out-path entry-default-unsigned.hqf --force true
```

### Code block 10

```
java -jar hap-sign-tool.jar sign-app -keyAlias "OpenHarmony Application Release" -signAlg "SHA256withECDSA" -mode "localSign" -appCertFile "OpenHarmonyApplication.cer" -profileFile "ohos_provision_release.p7b" -inFile "entry-default-unsigned.hqf" -keystoreFile "OpenHarmony.p12" -outFile "entry-default-signed.hqf" -keyPwd "123456Abc" -keystorePwd "123456Abc"
```

### Code block 11

```
$ hdc shell mkdir data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708
$ hdc file send entry-default-signed.hqf "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708"
$ hdc shell bm quickfix -a -f "data/local/tmp/3b7d97cdf4de41c4aecc465ff5069708" -d -o
```

### Code block 12

```
settings set use-source-cache false
```
