# 扫码授权登录

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-authorize-by-qrcode_

场景介绍

对于在缺乏便捷触控界面或输入受限的设备上登录应用的场景，推荐使用扫码授权登录方式接入Account Kit。用户使用已登录华为账号的设备（例如：Phone、Tablet等）扫描应用二维码并完成授权后，应用即可获取用户标识UnionID/OpenID等信息，实现扫码授权登录。

业务流程

扫码授权登录的整体接入流程如下：

[h2]步骤说明

展示二维码阶段（序号1-5）

用户选择华为账号扫码授权方式登录，应用调用华为账号服务器获取二维码信息。

应用根据华为账号服务器返回的二维码信息生成二维码图片。

等待用户扫码授权登录阶段（序号6-9）

应用将获取到的设备码传给应用服务端，应用服务端使用设备码轮询扫码授权登录-获取用户级凭证接口。

针对轮询扫码授权登录-获取用户级凭证接口响应的结果，应用请自行进行处理。

用户扫码授权登录阶段（序号10-21）

用户使用已登录华为账号的设备（例如：Phone、Tablet等）扫描应用二维码并完成授权。此时应用服务端轮询扫码授权登录-获取用户级凭证接口获取到Access Token，再使用Access Token调用获取用户信息接口获取用户UnionID、OpenID等信息。

应用服务端将业务登录凭证SessionId、UnionID/OpenID传给应用，应用获取到UnionID/OpenID可用于判断华为账号是否登录。

应用对用户标识UnionID/OpenID、业务登录凭证SessionId信息进行安全认证后完成扫码授权登录。

接口说明

扫码授权登录流程涉及关键接口如下所示：

接口名称	描述
获取二维码信息接口	应用通过调用该接口获取二维码信息。
扫码授权登录-获取用户级凭证接口	通过轮询该接口，获取用户级凭证。
获取用户信息接口	在获取到用户级凭证后，通过该接口获取用户UnionID/OpenID等信息。

开发步骤

[h2]获取二维码信息

应用调用华为账号的获取二维码信息接口获取二维码信息。

请求消息示例

请通过POST方式调用，示例如下：

POST /oauth2/v3/device/code HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

client_id=<client_id>&scope=openid profile

响应消息示例

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "create_time": 1569813512,
    "device_code": "AgEAAN7qd*****U0TvQ",
    "expire_in": 1800,
    "interval": 3,
    "scan_expire_in": 120,
    "user_code": "ABCDEFGH",
    "verification_url": "https://oauth-login1.cloud.huawei.com/oauth2/v3/device"
}

请求参数、响应参数及错误码等信息详见获取二维码信息接口。

[h2]生成二维码

应用根据响应中的verification_url和user_code生成二维码并展示。

二维码URL内容如下

https://oauth-login1.cloud.huawei.com/oauth2/v3/device?user_code=<user_code>

应用可以通过QRCode来生成二维码并在应用内展示，等待用户扫码。

说明

获取二维码信息接口返回的user_code存在有效期（以接口响应结果中的scan_expire_in字段实际值为准），如果用户未在此时间内扫码，需要重新调用获取二维码信息接口生成新的二维码。

[h2]轮询获取用户级凭证

应用服务端轮询调用扫码授权登录-获取用户级凭证接口（轮询间隔时间可参考获取二维码信息接口响应结果中的interval字段值），直到轮询次数超过限制、设备码超过有效期或成功获取Access Token为止。

请求消息示例

请通过POST方式调用，示例如下：

POST /oauth2/v3/token HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

grant_type=device_code&code=<device_code>&client_id=<client_id>&client_secret=<client_secret>

响应消息示例

用户未扫码时

HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "sub_error": 20411,
    "error_description": "user code not scan",
    "error": 1101
}

用户已扫码并完成授权时

HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "access_token": "DgEAAN7qd*****U0TvQ/eXpE4x+gvhoYh5/UuzL",
    "refresh_token": "DgECAL++vCn******NQ/UOL8+wm0jJi+o4NI793H",
    "expires_in": 3600,
    "id_token": "eyJraW*****ifQ.eyJhdF9oYX*****Q2fQ.TT05lFYe*****vDwb_Gj1ccR59yyB2Ig",
    "scope": "openid profile",
    "token_type": "Bearer",
    "open_id": "AQAxrBzThFv*****lv9tV_4rMCc"
}

请求参数、响应参数及错误码等信息详见扫码授权登录-获取用户级凭证接口。

说明

获取二维码信息接口返回的device_code存在有效期（以接口响应结果中的expire_in字段实际值为准），超时后需要重新调用获取二维码信息接口生成新的二维码。

应用服务端在轮询扫码授权登录-获取用户级凭证接口时，同一个设备码轮询次数不得超过获取二维码信息接口响应结果中的expire_in/interval的值，轮询超过限制后请求会被拒绝，需要重新调用获取二维码信息接口生成新的二维码。

[h2]用户扫码授权登录

用户使用已登录华为账号的设备（例如：Phone、Tablet等）扫描应用的二维码，弹出授权页面，显示应用名称、图标及申请的权限列表，用户点击允许后完成授权流程。

在用户完成授权后，此时应用服务端轮询扫码授权登录-获取用户级凭证接口获取到Access Token，再使用Access Token调用获取用户信息接口获取用户UnionID、OpenID等信息。

应用服务端将业务登录凭证SessionId、UnionID/OpenID传给应用，应用获取到UnionID/OpenID可用于判断华为账号是否登录。

应用对用户标识UnionID/OpenID、业务登录凭证SessionId信息进行安全认证后完成扫码授权登录。

说明

若Access Token过期，可以使用Refresh Token调用刷新用户级凭证获取新的Access Token。

## Code blocks

### Code block 1

```
POST /oauth2/v3/device/code HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

client_id=<client_id>&scope=openid profile
```

### Code block 2

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "create_time": 1569813512,
    "device_code": "AgEAAN7qd*****U0TvQ",
    "expire_in": 1800,
    "interval": 3,
    "scan_expire_in": 120,
    "user_code": "ABCDEFGH",
    "verification_url": "https://oauth-login1.cloud.huawei.com/oauth2/v3/device"
}
```

### Code block 3

```
https://oauth-login1.cloud.huawei.com/oauth2/v3/device?user_code=<user_code>
```

### Code block 4

```
POST /oauth2/v3/token HTTP/1.1
Host: oauth-login.cloud.huawei.com
Content-Type: application/x-www-form-urlencoded

grant_type=device_code&code=<device_code>&client_id=<client_id>&client_secret=<client_secret>
```

### Code block 5

```
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "sub_error": 20411,
    "error_description": "user code not scan",
    "error": 1101
}
```

### Code block 6

```
HTTP/1.1 200 OK
Content-Type: application/json;charset=utf-8

{
    "access_token": "DgEAAN7qd*****U0TvQ/eXpE4x+gvhoYh5/UuzL",
    "refresh_token": "DgECAL++vCn******NQ/UOL8+wm0jJi+o4NI793H",
    "expires_in": 3600,
    "id_token": "eyJraW*****ifQ.eyJhdF9oYX*****Q2fQ.TT05lFYe*****vDwb_Gj1ccR59yyB2Ig",
    "scope": "openid profile",
    "token_type": "Bearer",
    "open_id": "AQAxrBzThFv*****lv9tV_4rMCc"
}
```
