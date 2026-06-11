# 无法获取到头像昵称如何解决

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-8_

确认获取authorizationCode时，调用AuthorizationWithHuaweiIDRequest接口是否传入正确的scope：'profile'。

import { authentication } from '@kit.AccountKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 获取头像昵称需要传如下scope
authRequest.scopes = ['profile'];
// 若开发者需要进行服务端开发，则需传如下permission获取authorizationCode
authRequest.permissions = ['serviceauthcode'];

确认通过AuthenticationController.executeRequest接口执行授权请求后，响应返回的Authorization Code在5分钟有效期内。

确认调用的是华为账号服务器获取头像昵称接口。

## Code blocks

### Code block 1

```
import { authentication } from '@kit.AccountKit';

// 创建授权请求，并设置参数
const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
// 获取头像昵称需要传如下scope
authRequest.scopes = ['profile'];
// 若开发者需要进行服务端开发，则需传如下permission获取authorizationCode
authRequest.permissions = ['serviceauthcode'];
```
