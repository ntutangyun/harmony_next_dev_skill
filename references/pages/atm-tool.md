# atm工具

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/atm-tool_

Access Token Manager (程序访问控制管理工具，简称atm工具)，是用于查询应用进程的权限、使用类型等信息的工具，为开发者提供了根据tokenId、包名、进程名等信息进行访问控制管理的能力。

环境说明

在使用本工具前，开发者需要先获取hdc工具，执行hdc shell。

atm工具命令列表

命令	描述
help	帮助命令，显示atm支持的命令信息。
dump	查询命令，用于查询访问控制相关数据信息。

帮助命令

# 显示帮助信息
atm help

查询命令

atm dump [-h] [-d [-p <permission-name>]] [-t [-i <token-id>] [-b <bundle-name>] [-n <process-name>] [-p <permission-name>]]

下表所列命令中，-d、-t为必选参数，-i、-b、-n、-p为可选参数。对atm dump -t命令，-i、-b、-n、-p参数只能单独使用。

参数	参数说明
-h	帮助信息。
-d	必选参数，查询系统中所有的权限定义。
-d -p <permission-name>	可选参数，通过权限名，查询权限定义。
-t	必选参数，查询系统中所有进程的tokenId。
-t -i <token-id>	可选参数，通过进程的tokenId，查询该进程的基本信息以及对应的GrantStatus。
-t -b <bundle-name>	可选参数，通过应用进程的包名bundle-name，查询该应用的基本信息以及对应的GrantStatus。
-t -n <process-name>	可选参数，通过进程名process-name，查询该进程的基本信息以及对应的GrantStatus。
-t -p <permission-name>	可选参数，通过权限名，查询申请该权限的应用进程的tokenId。 说明：从版本26.0.0开始，支持该参数。

示例：

#查询系统中所有的权限定义
atm dump -d

#按权限名查询权限定义
atm dump -d -p *********
# 执行结果
# {
#     "permissionName": "ohos.permission.KERNEL_ATM_SELF_USE",
#     "grantMode": "SYSTEM_GRANT",
#     "availableLevel": "SYSTEM_CORE",
#     "availableType": "SYSTEM",
#     "distributedSceneEnable": true,
#     "isKernelEffect": true,
#     "hasValue": true,
# }

#显示atm dump的帮助信息
atm dump -h

#查询系统中所有进程的tokenId
atm dump -t

#按tokenId查询权限信息
atm dump -t -i *********
# 执行结果
# {
#   "tokenId": 672078897,
#   "processName": "samgr",
#   "apl": 2,
#   "permStateList": [
#     {
#       "permissionName": "ohos.permission.DISTRIBUTED_DATASYNC",
#       "grantStatus": 0,
#       "grantFlag": 4,
#     }
#   ]
# }

#按包名查询权限信息
atm dump -t -b ohos.telephony.resources
# 执行结果
# {
#   "tokenId": 537280686,
#   "tokenAttr": 1,
#   "ver": 1,
#   "userId": 100,
#   "bundleName": "ohos.telephony.resources",
#   "instIndex": 0,
#   "dlpType": 0,
#   "isRemote": false,
#   "isPermDialogForbidden": false,
#   "permStateList": [
#     {
#       "permissionName": "ohos.permission.DISTRIBUTED_DATASYNC",
#       "grantStatus": 0,
#       "grantFlag": 4,
#     }
#   ]
# }

#按权限名查询申请该权限的所有应用进程的tokenId和包名
atm dump -t -p ohos.permission.CAMERA
# 执行结果
# Permission: ohos.permission.CAMERA
# Total Tokens: 1

# 537538306: com.ohos.camera


#按进程名查询权限信息
atm dump -t -n *********

## Code blocks

### Code block 1

```
# 显示帮助信息
atm help
```

### Code block 2

```
atm dump [-h] [-d [-p <permission-name>]] [-t [-i <token-id>] [-b <bundle-name>] [-n <process-name>] [-p <permission-name>]]
```

### Code block 3

```
#查询系统中所有的权限定义
atm dump -d

#按权限名查询权限定义
atm dump -d -p *********
# 执行结果
# {
#     "permissionName": "ohos.permission.KERNEL_ATM_SELF_USE",
#     "grantMode": "SYSTEM_GRANT",
#     "availableLevel": "SYSTEM_CORE",
#     "availableType": "SYSTEM",
#     "distributedSceneEnable": true,
#     "isKernelEffect": true,
#     "hasValue": true,
# }

#显示atm dump的帮助信息
atm dump -h

#查询系统中所有进程的tokenId
atm dump -t

#按tokenId查询权限信息
atm dump -t -i *********
# 执行结果
# {
#   "tokenId": 672078897,
#   "processName": "samgr",
#   "apl": 2,
#   "permStateList": [
#     {
#       "permissionName": "ohos.permission.DISTRIBUTED_DATASYNC",
#       "grantStatus": 0,
#       "grantFlag": 4,
#     }
#   ]
# }

#按包名查询权限信息
atm dump -t -b ohos.telephony.resources
# 执行结果
# {
#   "tokenId": 537280686,
#   "tokenAttr": 1,
#   "ver": 1,
#   "userId": 100,
#   "bundleName": "ohos.telephony.resources",
#   "instIndex": 0,
#   "dlpType": 0,
#   "isRemote": false,
#   "isPermDialogForbidden": false,
#   "permStateList": [
#     {
#       "permissionName": "ohos.permission.DISTRIBUTED_DATASYNC",
#       "grantStatus": 0,
#       "grantFlag": 4,
#     }
#   ]
# }

#按权限名查询申请该权限的所有应用进程的tokenId和包名
atm dump -t -p ohos.permission.CAMERA
# 执行结果
# Permission: ohos.permission.CAMERA
# Total Tokens: 1

# 537538306: com.ohos.camera


#按进程名查询权限信息
atm dump -t -n *********
```
