# 查询密钥是否存在(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-check-key-arkts_

function generateKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.generateKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data);
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}


async function generateKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  console.info(`enter promise generateKeyItem`);
  await generateKeyItem(keyAlias, huksOptions);
  console.info(`promise: generateKeyItem success`);
}


/* 2.检查密钥是否存在 */
let huksOptions: huks.HuksOptions = {
  properties: []
}


function hasKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<boolean>((resolve, reject) => {
    try {
      huks.hasKeyItem(keyAlias, huksOptions, (error, data) => {
        if (error) {
          reject(error);
        } else {
          resolve(data.valueOf());
        }
      });
    } catch (error) {
      throw (error as Error);
    }
  });
}


async function checkKeyExistence(keyAlias: string, huksOptions: huks.HuksOptions): Promise<boolean> {
  console.info(`enter promise hasKeyItem`);
  const exists = await hasKeyItem(keyAlias, huksOptions);
  console.info(`promise: hasKeyItem success, isKeyExist = ${exists}`);
  return exists;
}


async function executeCheckKey(): Promise<string> {
  try {
    /* 1.生成密钥 */
    await generateKey(keyAlias, generateHuksOptions);


    /* 2.检查密钥是否存在 */
    isKeyExist = await checkKeyExistence(keyAlias, huksOptions);


    console.info(`Key check completed, isKeyExist = ${isKeyExist}`);
    return 'Success';
  } catch (error) {
    console.error(`Key check failed: ${JSON.stringify(error)}`);
    return 'Failed';
  }
}
CheckKeyExists.ets
查询密钥是否存在
查询密钥是否存在(C/C++)
