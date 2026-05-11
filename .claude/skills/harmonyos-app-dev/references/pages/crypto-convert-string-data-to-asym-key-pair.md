# 指定PEM格式字符串数据转换非对称密钥对(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-convert-string-data-to-asym-key-pair_

--BEGIN RSA PRIVATE KEY-----\n' +
    'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n' +
    'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n' +
    'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n' +
    'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n' +
    'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n' +
    '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n' +
    'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n' +
    'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n' +
    'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n' +
    'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n' +
    'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n' +
    'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n' +
    'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n' +
    '-----END RSA PRIVATE KEY-----\n';
let publicPkcs1Str1024: string =
  '-----BEGIN RSA PUBLIC KEY-----\n' +
    'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n' +
    'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n' +
    'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n' +
    '-----END RSA PUBLIC KEY-----\n';


async function testPkcs1ToPkcs8ByPromise() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  let keyPair = await asyKeyGenerator.convertPemKey(publicPkcs1Str1024, priKeyPkcs1Str1024);
  let priPemKey = keyPair.priKey;
  let pubPemKey = keyPair.pubKey;
  let priString = priPemKey.getEncodedPem('PKCS8');
  let pubString = pubPemKey.getEncodedPem('X509');
  console.info('[promise]TestPkcs1ToPkcs8ByPromise priString output: ' + priString);
  console.info('[promise]TestPkcs1ToPkcs8ByPromise pubString output: ' + pubString);
}
Promise.ets

同步返回结果（调用方法convertPemKeySync）：

import { cryptoFramework } from '@kit.CryptoArchitectureKit';


let priKeyPkcs1Str1024: string =
  '-----BEGIN RSA PRIVATE KEY-----\n' +
    'MIICXQIBAAKBgQCwIN3mr21+N96ToxnVnaS+xyK9cNRAHiHGgrbjHw6RAj3V+l+W\n' +
    'Y68IhIe3DudVlzE9oMjeOQwkMkq//HCxNlIlFR6O6pa0mrXSwPRE7YKG97CeKk2g\n' +
    'YOS8YEh8toAvm7xKbiLkXuuMlxrjP2j/mb5iI/UASFSPZiQ/IyxDr0AQaQIDAQAB\n' +
    'AoGAEvBFzBNa+7J4PXnRQlYEK/tvsd0bBZX33ceacMubHl6WVZbphltLq+fMTBPP\n' +
    'LjXmtpC+aJ7Lvmyl+wTi/TsxE9vxW5JnbuRT48rnZ/Xwq0eozDeEeIBRrpsr7Rvr\n' +
    '7ctrgzr4m4yMHq9aDgpxj8IR7oHkfwnmWr0wM3FuiVlj650CQQDineeNZ1hUTkj4\n' +
    'D3O+iCi3mxEVEeJrpqrmSFolRMb+iozrIRKuJlgcOs+Gqi2fHfOTTL7LkpYe8SVg\n' +
    'e3JxUdVLAkEAxvcZXk+byMFoetrnlcMR13VHUpoVeoV9qkv6CAWLlbMdgf7uKmgp\n' +
    'a1Yp3QPDNQQqkPvrqtfR19JWZ4uy1qREmwJALTU3BjyBoH/liqb6fh4HkWk75Som\n' +
    'MzeSjFIOubSYxhq5tgZpBZjcpvUMhV7Zrw54kwASZ+YcUJvmyvKViAm9NQJBAKF7\n' +
    'DyXSKrem8Ws0m1ybM7HQx5As6l3EVhePDmDQT1eyRbKp+xaD74nkJpnwYdB3jyyY\n' +
    'qc7A1tj5J5NmeEFolR0CQQCn76Xp8HCjGgLHw9vg7YyIL28y/XyfFyaZAzzK+Yia\n' +
    'akNwQ6NeGtXSsuGCcyyfpacHp9xy8qXQNKSkw03/5vDO\n' +
    '-----END RSA PRIVATE KEY-----\n';
let publicPkcs1Str1024: string =
  '-----BEGIN RSA PUBLIC KEY-----\n' +
    'MIGJAoGBALAg3eavbX433pOjGdWdpL7HIr1w1EAeIcaCtuMfDpECPdX6X5ZjrwiE\n' +
    'h7cO51WXMT2gyN45DCQySr/8cLE2UiUVHo7qlrSatdLA9ETtgob3sJ4qTaBg5Lxg\n' +
    'SHy2gC+bvEpuIuRe64yXGuM/aP+ZvmIj9QBIVI9mJD8jLEOvQBBpAgMBAAE=\n' +
    '-----END RSA PUBLIC KEY-----\n';


function testPkcs1ToPkcs8BySync() {
  let asyKeyGenerator = cryptoFramework.createAsyKeyGenerator('RSA1024');
  try {
    let keyPairData = asyKeyGenerator.convertPemKeySync(publicPkcs1Str1024, priKeyPkcs1Str1024);
    if (keyPairData != null) {
      console.info('[Sync]: convert pem key pair result: success.');
    } else {
      console.error('[Sync]: convert pem key pair result: fail.');
    }
    let priPemKey = keyPairData.priKey;
    let pubPemKey = keyPairData.pubKey;
    let priString = priPemKey.getEncodedPem('PKCS8');
    let pubString = pubPemKey.getEncodedPem('X509');
    console.info('[Sync]TestPkcs1ToPkcs8BySync priString output: ' + priString);
    console.info('[Sync]TestPkcs1ToPkcs8BySync pubString output: ' + pubString);
  } catch (e) {
    console.error(`Sync failed: errCode: ${e.code}, message: ${e.message}`);
  }
}
Sync.ets
使用ECC压缩/非压缩点格式转换(C/C++)
指定PEM格式字符串数据转换非对称密钥对(C/C++)
