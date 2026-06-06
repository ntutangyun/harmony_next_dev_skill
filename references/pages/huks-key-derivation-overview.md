# 密钥派生介绍及算法规格

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-derivation-overview_

-----	--------	--------	--------
HMAC/SHA256	AES/192/256	

AES/256

HMAC/256

	12+
HMAC/SHA384	AES/256	HMAC/384	12+
HMAC/SHA512	AES/256	HMAC/512	12+
HKDF/SHA256	X25519/256	X25519/256	12+
HKDF/SHA384	X25519/256	X25519/256	12+
HKDF/SHA512	X25519/256	X25519/256	12+
密钥派生
密钥派生(ArkTS)
