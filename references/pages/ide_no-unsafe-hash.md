# @security/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unsafe-hash_

import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA256');


//正例2
/**
 * 下载crypto-js依赖：ohpm install @ohos/crypto-js
 */
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA256('Message').toString();
反例
//反例1.1
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('MD5');


//反例1.2
import cryptoFramework from '@ohos.security.cryptoFramework';
cryptoFramework.createMd('SHA1');


//反例2.1
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.MD5('Message').toString();


//反例2.2
import { CryptoJS } from '@ohos/crypto-js';
CryptoJS.SHA1('Message').toString();
规则集
plugin:@security/recommended
plugin:@security/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@security/no-unsafe-ecdsa
@security/no-unsafe-mac
