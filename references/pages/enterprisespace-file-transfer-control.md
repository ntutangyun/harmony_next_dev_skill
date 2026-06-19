# 文件外发管控

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-file-transfer-control_

从6.0.0(20)开始，支持设置和获取审批信息、配置空间互传单双通策略的能力。

场景介绍

支持在文件传输场景中，通过设置空间的单通或双通策略，灵活配置应用文件在空间间的外发权限，实现安全可控的跨空间文件共享。当文件外发需纳入审批流程管控时，系统支持配置相关审批信息。同时，通过调用审批状态同步接口，实时获取审批结果，确保外发流程的安全与合规。

单通模式下，仅允许个人空间向企业空间发送文件，禁止反向传输。

双通模式则允许个人空间与企业空间双向互发文件。

接口说明

详细接口说明可参考接口文档。

接口名	描述
policyPush(policyContext: string): void	配置空间互传单双通策略。
setAuditInfo(transactionNum: string, info: AuditInfo): number	设置审批信息并返回结果。
getAuditInfo(transactionNum: string): AuditInfo	获取审批信息。

开发步骤

1.导入Enterprise Space Kit模块。

import { fileTransfer } from '@kit.EnterpriseSpaceKit';

2.配置空间互传单双通策略。

@Entry()
@Component
struct Index {
  // 配置空间互传单双通策略
  policyPush() {
    let policyContext =
      '{' +
        '  "config": {' +
        '    "inEnable": "1",' +
        '    "incoming_check": {' +
        '      "data_list": [' +
        '        {' +
        '          "allow": "VirusCheck.result == 0",' +
        '          "approval": "",' +
        '          "check_point": "VirusCheck",' +
        '          "check_point_name": "VirusCheck_in",' +
        '          "is_enable": "true",' +
        '          "forbidden": "VirusCheck.result == 1",' +
        '          "order": "0"' +
        '        }' +
        '      ]' +
        '    },' +
        '    "outEnable": "1",' +
        '    "outgoing_check": {' +
        '      "data_list": [' +
        '        {' +
        '          "allow": "SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7",' +
        '          "approval": "SecurityCheck.Result == 10",' +
        '          "check_point": "SecurityCheck",' +
        '          "check_point_name": "SecurityCheck_out",' +
        '          "is_enable": "true",' +
        '          "forbidden": "SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11",' +
        '          "order": "0"' +
        '        }' +
        '      ]' +
        '    },' +
        '    "checkpoint_config": {' +
        '      "data_list": [' +
        '        {' +
        '          "check_point_name": "SecurityCheck",' +
        '          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",' +
        '          "ability_name": "TestScanAbility",' +
        '          "func_code": "2",' +
        '          "type": "2"' +
        '        },' +
        '        {' +
        '          "check_point_name": "VirusCheck",' +
        '          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",' +
        '          "ability_name": "TestScanAbility",' +
        '          "func_code": "3",' +
        '          "type": "1"' +
        '        }' +
        '      ]' +
        '    },' +
        '    "approvalpoint_config": {' +
        '      "data_list": [' +
        '        {' +
        '          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",' +
        '          "ability_name": "TestApprovalAbility"' +
        '        }' +
        '      ]' +
        '    }' +
        '  }' +
        '}';
    try {
      fileTransfer.policyPush(policyContext);
      console.info(`Succeeded in pushing policy`);
    } catch (err) {
      console.error(`Failed to push policy. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('配置空间互传单双通策略')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.policyPush();
          })
      }
    }
  }
}

3.设置文件外发流程控制的审批信息以及实时获取审批结果，开发者可通过审批结果判断是否允许文件外发至个人空间。

@Entry
@Component
struct Index {
  // 设置审批信息
  setAuditInfo() {
    const transactionNum: string = '1234567890123456789'; // 数据库自动生成的传输编号，需要在数据库中实际存在。
    const info: fileTransfer.AuditInfo = {
      auditId: '123456789', // 企业应用对审批条目的自定义唯一标识
      userId: '100', // 用户ID
      userName: 'test', // 用户名称
      time: Date.now(), // 审批时间戳
      comments: 'Waiting approval', // 审批评论
      status: '1' // 文件审批状态
    };
    try {
      const ret: number = fileTransfer.setAuditInfo(transactionNum, info);
      console.info(`Succeeded in setting audit info, number:`, ret);
    } catch (err) {
      console.error(`Failed to set audit info. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 获取审批信息
  getAuditInfo() {
    const transactionNum: string = '1234567890123456789'; // 数据库自动生成的传输编号，需要在数据库中实际存在。
    try {
      const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
      console.info(`Succeeded in getting audit info:` + JSON.stringify(auditInfo));
    } catch (err) {
      console.error(`Failed to get audit info. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('设置审批信息')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setAuditInfo();
          })
      }

      Row() {
        Button('获取审批信息')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getAuditInfo();
          })
      }
    }
  }
}

## Code blocks

### Code block 1

```
import { fileTransfer } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
@Entry()
@Component
struct Index {
  // 配置空间互传单双通策略
  policyPush() {
    let policyContext =
      '{' +
        '  "config": {' +
        '    "inEnable": "1",' +
        '    "incoming_check": {' +
        '      "data_list": [' +
        '        {' +
        '          "allow": "VirusCheck.result == 0",' +
        '          "approval": "",' +
        '          "check_point": "VirusCheck",' +
        '          "check_point_name": "VirusCheck_in",' +
        '          "is_enable": "true",' +
        '          "forbidden": "VirusCheck.result == 1",' +
        '          "order": "0"' +
        '        }' +
        '      ]' +
        '    },' +
        '    "outEnable": "1",' +
        '    "outgoing_check": {' +
        '      "data_list": [' +
        '        {' +
        '          "allow": "SecurityCheck.Result == 3 or SecurityCheck.Result == 4 or SecurityCheck.Result == 6 or SecurityCheck.Result == 7",' +
        '          "approval": "SecurityCheck.Result == 10",' +
        '          "check_point": "SecurityCheck",' +
        '          "check_point_name": "SecurityCheck_out",' +
        '          "is_enable": "true",' +
        '          "forbidden": "SecurityCheck.Result == 0 or SecurityCheck.Result == 1 or SecurityCheck.Result == 12 or SecurityCheck.Result == 2 or SecurityCheck.Result == 5 or SecurityCheck.Result == 8 or SecurityCheck.Result == 9 or SecurityCheck.Result == 11",' +
        '          "order": "0"' +
        '        }' +
        '      ]' +
        '    },' +
        '    "checkpoint_config": {' +
        '      "data_list": [' +
        '        {' +
        '          "check_point_name": "SecurityCheck",' +
        '          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",' +
        '          "ability_name": "TestScanAbility",' +
        '          "func_code": "2",' +
        '          "type": "2"' +
        '        },' +
        '        {' +
        '          "check_point_name": "VirusCheck",' +
        '          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",' +
        '          "ability_name": "TestScanAbility",' +
        '          "func_code": "3",' +
        '          "type": "1"' +
        '        }' +
        '      ]' +
        '    },' +
        '    "approvalpoint_config": {' +
        '      "data_list": [' +
        '        {' +
        '          "bundle_name": "com.example.enterprisespacekit_samplecode_clientdemo_arkts",' +
        '          "ability_name": "TestApprovalAbility"' +
        '        }' +
        '      ]' +
        '    }' +
        '  }' +
        '}';
    try {
      fileTransfer.policyPush(policyContext);
      console.info(`Succeeded in pushing policy`);
    } catch (err) {
      console.error(`Failed to push policy. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('配置空间互传单双通策略')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.policyPush();
          })
      }
    }
  }
}
```

### Code block 3

```
@Entry
@Component
struct Index {
  // 设置审批信息
  setAuditInfo() {
    const transactionNum: string = '1234567890123456789'; // 数据库自动生成的传输编号，需要在数据库中实际存在。
    const info: fileTransfer.AuditInfo = {
      auditId: '123456789', // 企业应用对审批条目的自定义唯一标识
      userId: '100', // 用户ID
      userName: 'test', // 用户名称
      time: Date.now(), // 审批时间戳
      comments: 'Waiting approval', // 审批评论
      status: '1' // 文件审批状态
    };
    try {
      const ret: number = fileTransfer.setAuditInfo(transactionNum, info);
      console.info(`Succeeded in setting audit info, number:`, ret);
    } catch (err) {
      console.error(`Failed to set audit info. Code: ${err.code}, message: ${err.message}`);
    }
  }

  // 获取审批信息
  getAuditInfo() {
    const transactionNum: string = '1234567890123456789'; // 数据库自动生成的传输编号，需要在数据库中实际存在。
    try {
      const auditInfo: fileTransfer.AuditInfo = fileTransfer.getAuditInfo(transactionNum);
      console.info(`Succeeded in getting audit info:` + JSON.stringify(auditInfo));
    } catch (err) {
      console.error(`Failed to get audit info. Code: ${err.code}, message: ${err.message}`);
    }
  }

  build() {
    Column() {
      Row() {
        Button('设置审批信息')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.setAuditInfo();
          })
      }

      Row() {
        Button('获取审批信息')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getAuditInfo();
          })
      }
    }
  }
}
```
