# 企业账号认证

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprisespace-workspace-authentication_

从6.1.0(23)开始，支持企业认证和获取企业应用令牌的能力。

场景介绍

Enterprise Space Kit为企业应用提供企业账号认证的能力。在企业空间初始化阶段，实现企业用户的账号认证。同时支持获取企业应用令牌的能力。

接口说明

详细接口说明可参考接口文档。

接口名	描述
authenticate(enterpriseAuthInfo: WorkspaceDomainInfo, credential: Uint8Array): Promise<AuthResult>	企业账号认证并返回结果。
getAccessToken(businessParams: Record<string, string>): Promise<Uint8Array>	获取企业应用令牌并返回结果。

开发步骤

1.导入Enterprise Space Kit模块和相关依赖模块。

import { osAccount } from '@kit.BasicServicesKit';
import { spaceManager } from '@kit.EnterpriseSpaceKit';

2.企业账号认证和获取企业应用令牌并返回结果。

enum AuthModeType {
  SASL = 'SASL',
}

enum CertifiedProtocolType {
  GSSAPI = 'GSSAPI/Kerberos',
  OAUTH2 = 'OAuth 2.0',
}

enum LdapEncryptMode {
  LDAP = 'LDAP',
  LDAPS = 'LDAPS',
  LDAP_STARTTLS = 'LDAP STARTTLS',
}

enum ServerType {
  NONE = '',
  LDAP = 'LDAP',
  AD = 'AD',
  IDaaS = 'IDaaS',
}

type ADConfig = Record<string, string>;
type LDAPConfig = Record<string, string>;
type OAuthConfig = Record<string, string>;
type IDaaSConfig = Record<string, string | OAuthConfig>;
type ServerConfigParams = Record<string, string | ADConfig | LDAPConfig | IDaaSConfig>;
type ServerConfig = Record<string, string | ServerConfigParams>;

@Entry
@Component
struct Index {
  /**
   * 获取IDaaS协议服务器配置
   * @returns
   */
  public getIDaaSServerConfig(): ServerConfig {
    const idaasConfigData: IDaaSConfig = {
      'authProtocol': 'OAuth 2.0',
      'oauthConfig': {
        'userAuthenRequestUri': 'iDaaSUserAuthUrl',
        'authorizationRequestUri': 'iDaaSAuthUrl',
        'tokenRequestUri': 'iDaaSTokenUrl',
        'userInfoRequestUri': 'iDaaSUserUrl',
        'clientId': 'iDaaSClientID',
        'clientSecret': 'iDaaSClientSecret',
        'scope': 'iDaaSScope',
        'accountIdAttributeName': 'iDaaSAccountID',
        'accountNameAttributeName': 'iDaaSAccountName',
      },
    };
    const parameters: ServerConfigParams = {
      'serverType': 'IDaas',
      'idaasConfig': idaasConfigData,
    };
    const serverConfig: ServerConfig = {
      'parameters': parameters,
    };
    return serverConfig;
  }

  /**
   * 获取LDAP协议服务器配置
   * @returns
   */
  private getLDAPServerConfig(): ServerConfig {
    const ldapConfig: LDAPConfig = {
      'authServerAddress': 'domainName',
      'authenMode': AuthModeType.SASL,
      'authenProtocol': CertifiedProtocolType.GSSAPI,
      'kdcAddress': 'kdcAddress',
      'accountIdAttributeName': 'accountId',
      'accountNameAttributeName': 'accountName',
      'encryptMode': LdapEncryptMode.LDAP,
      'ldapPort': 'portNum',
      'baseDN': 'baseDN',
    };
    if (ldapConfig['encryptMode'] !== LdapEncryptMode.LDAP) {
      ldapConfig['kdcAddress'] = '';
    }
    const parameters: ServerConfigParams = {
      'ldapConfig': ldapConfig,
    };
    const serverConfig: ServerConfig = {
      'authServerName': ldapConfig['authServerAddress'],
      'parameters': parameters,
    };
    return serverConfig;
  }

  /**
   * 获取AD协议服务器配置
   * @returns
   */
  private getADServerConfig(): ServerConfig {
    const adConfig: ADConfig = {
      'adDomain': 'domainName',
      'authenMode': AuthModeType.SASL,
    };
    const parameters: ServerConfigParams = {
      'adConfig': adConfig,
    };
    const serverConfig: ServerConfig = {
      'authServerName': 'domainName',
      'parameters': parameters,
    };
    return serverConfig;
  }

  private getServiceConfig(serverType: string): ServerConfig {
    let serverConfig: ServerConfig;
    if (serverType === ServerType.IDaaS) {
      serverConfig = this.getIDaaSServerConfig();
    } else if (serverType === ServerType.LDAP) {
      serverConfig = this.getLDAPServerConfig();
    } else {
      serverConfig = this.getADServerConfig();
    }

    return serverConfig;
  }

  // 企业账号认证
  async authenticate() {
    // 绑定域服务器
    let serverType = ServerType.AD;
    let serverConfig: ServerConfig = this.getServiceConfig(serverType);
    await osAccount.DomainServerConfigManager.addServerConfig(serverConfig);
    // 获取域服务器ID
    let servers: osAccount.DomainServerConfig[] = await osAccount.DomainServerConfigManager.getAllServerConfigs();
    let serverConfigId: string = 'serverConfigId';
    servers.forEach((server) => {
      // 过滤非目标服务器
      serverConfigId = server.id;
    });
    const enterpriseAuthInfo: spaceManager.WorkspaceDomainInfo = {
      domain: 'testDomain', // 域名
      workspaceName: 'testAccountName', // 工作空间域账号名称
      serverConfigId: serverConfigId // 工作空间所属域的服务器配置标识符，绑定域服务器后本地生成
    };
    const credential = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0]); // 员工密码的ASCII码
    try {
      const authResult: spaceManager.AuthResult = await spaceManager.authenticate(enterpriseAuthInfo, credential);
      console.info(`Succeeded in authenticating. Auth result is: ` + JSON.stringify(authResult));
    } catch (err) {
      console.error(`Failed to authenticate. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 获取企业应用令牌
  async getAccessToken() {
    const params: Record<string, string> = {
      'clientId': 'test1' // 业务参数，由业务方根据请求协议自定义，企业应用在域服务器的唯一标识
    };

    try {
      const result: Uint8Array = await spaceManager.getAccessToken(params); // 从域服务器获取的一次性授权码，可使用授权码与域服务器直接交互。
      console.info(`Succeeded in getting access token. Result is: ` + JSON.stringify(result));
    } catch (err) {
      console.error(`Failed to get access token. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('企业账号认证')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.authenticate();
          })
      }

      Row() {
        Button('获取企业应用访问令牌')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getAccessToken();
          })
      }
    }
  }
}

## Code blocks

### Code block 1

```
import { osAccount } from '@kit.BasicServicesKit';
import { spaceManager } from '@kit.EnterpriseSpaceKit';
```

### Code block 2

```
enum AuthModeType {
  SASL = 'SASL',
}

enum CertifiedProtocolType {
  GSSAPI = 'GSSAPI/Kerberos',
  OAUTH2 = 'OAuth 2.0',
}

enum LdapEncryptMode {
  LDAP = 'LDAP',
  LDAPS = 'LDAPS',
  LDAP_STARTTLS = 'LDAP STARTTLS',
}

enum ServerType {
  NONE = '',
  LDAP = 'LDAP',
  AD = 'AD',
  IDaaS = 'IDaaS',
}

type ADConfig = Record<string, string>;
type LDAPConfig = Record<string, string>;
type OAuthConfig = Record<string, string>;
type IDaaSConfig = Record<string, string | OAuthConfig>;
type ServerConfigParams = Record<string, string | ADConfig | LDAPConfig | IDaaSConfig>;
type ServerConfig = Record<string, string | ServerConfigParams>;

@Entry
@Component
struct Index {
  /**
   * 获取IDaaS协议服务器配置
   * @returns
   */
  public getIDaaSServerConfig(): ServerConfig {
    const idaasConfigData: IDaaSConfig = {
      'authProtocol': 'OAuth 2.0',
      'oauthConfig': {
        'userAuthenRequestUri': 'iDaaSUserAuthUrl',
        'authorizationRequestUri': 'iDaaSAuthUrl',
        'tokenRequestUri': 'iDaaSTokenUrl',
        'userInfoRequestUri': 'iDaaSUserUrl',
        'clientId': 'iDaaSClientID',
        'clientSecret': 'iDaaSClientSecret',
        'scope': 'iDaaSScope',
        'accountIdAttributeName': 'iDaaSAccountID',
        'accountNameAttributeName': 'iDaaSAccountName',
      },
    };
    const parameters: ServerConfigParams = {
      'serverType': 'IDaas',
      'idaasConfig': idaasConfigData,
    };
    const serverConfig: ServerConfig = {
      'parameters': parameters,
    };
    return serverConfig;
  }

  /**
   * 获取LDAP协议服务器配置
   * @returns
   */
  private getLDAPServerConfig(): ServerConfig {
    const ldapConfig: LDAPConfig = {
      'authServerAddress': 'domainName',
      'authenMode': AuthModeType.SASL,
      'authenProtocol': CertifiedProtocolType.GSSAPI,
      'kdcAddress': 'kdcAddress',
      'accountIdAttributeName': 'accountId',
      'accountNameAttributeName': 'accountName',
      'encryptMode': LdapEncryptMode.LDAP,
      'ldapPort': 'portNum',
      'baseDN': 'baseDN',
    };
    if (ldapConfig['encryptMode'] !== LdapEncryptMode.LDAP) {
      ldapConfig['kdcAddress'] = '';
    }
    const parameters: ServerConfigParams = {
      'ldapConfig': ldapConfig,
    };
    const serverConfig: ServerConfig = {
      'authServerName': ldapConfig['authServerAddress'],
      'parameters': parameters,
    };
    return serverConfig;
  }

  /**
   * 获取AD协议服务器配置
   * @returns
   */
  private getADServerConfig(): ServerConfig {
    const adConfig: ADConfig = {
      'adDomain': 'domainName',
      'authenMode': AuthModeType.SASL,
    };
    const parameters: ServerConfigParams = {
      'adConfig': adConfig,
    };
    const serverConfig: ServerConfig = {
      'authServerName': 'domainName',
      'parameters': parameters,
    };
    return serverConfig;
  }

  private getServiceConfig(serverType: string): ServerConfig {
    let serverConfig: ServerConfig;
    if (serverType === ServerType.IDaaS) {
      serverConfig = this.getIDaaSServerConfig();
    } else if (serverType === ServerType.LDAP) {
      serverConfig = this.getLDAPServerConfig();
    } else {
      serverConfig = this.getADServerConfig();
    }

    return serverConfig;
  }

  // 企业账号认证
  async authenticate() {
    // 绑定域服务器
    let serverType = ServerType.AD;
    let serverConfig: ServerConfig = this.getServiceConfig(serverType);
    await osAccount.DomainServerConfigManager.addServerConfig(serverConfig);
    // 获取域服务器ID
    let servers: osAccount.DomainServerConfig[] = await osAccount.DomainServerConfigManager.getAllServerConfigs();
    let serverConfigId: string = 'serverConfigId';
    servers.forEach((server) => {
      // 过滤非目标服务器
      serverConfigId = server.id;
    });
    const enterpriseAuthInfo: spaceManager.WorkspaceDomainInfo = {
      domain: 'testDomain', // 域名
      workspaceName: 'testAccountName', // 工作空间域账号名称
      serverConfigId: serverConfigId // 工作空间所属域的服务器配置标识符，绑定域服务器后本地生成
    };
    const credential = new Uint8Array([0, 0, 0, 0, 0, 0, 0, 0]); // 员工密码的ASCII码
    try {
      const authResult: spaceManager.AuthResult = await spaceManager.authenticate(enterpriseAuthInfo, credential);
      console.info(`Succeeded in authenticating. Auth result is: ` + JSON.stringify(authResult));
    } catch (err) {
      console.error(`Failed to authenticate. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  // 获取企业应用令牌
  async getAccessToken() {
    const params: Record<string, string> = {
      'clientId': 'test1' // 业务参数，由业务方根据请求协议自定义，企业应用在域服务器的唯一标识
    };

    try {
      const result: Uint8Array = await spaceManager.getAccessToken(params); // 从域服务器获取的一次性授权码，可使用授权码与域服务器直接交互。
      console.info(`Succeeded in getting access token. Result is: ` + JSON.stringify(result));
    } catch (err) {
      console.error(`Failed to get access token. Code: ${err.code}, message: ${err.message}`);
    }
    // 处理后置逻辑
  }

  build() {
    Column() {
      Row() {
        Button('企业账号认证')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.authenticate();
          })
      }

      Row() {
        Button('获取企业应用访问令牌')
          .width(200)
          .height(50)
          .backgroundColor('#6366F1')
          .fontColor('#FFFFFF')
          .fontSize(14)
          .margin({ left: 20, bottom: 5 })
          .onClick(() => {
            this.getAccessToken();
          })
      }
    }
  }
}
```
