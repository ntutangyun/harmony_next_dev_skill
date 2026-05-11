# 密钥删除(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-delete-key-arkts_

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
  try {
    await generateKeyItem(keyAlias, huksOptions);
    console.info(`promise: generateKeyItem success`);
  } catch (error) {
    console.error(`promise: generateKeyItem failed, ${JSON.stringify(error)}`);
  }
}


/* 2.删除密钥 */
let deleteHuksOptions: huks.HuksOptions = {
  properties: []
}


function deleteKeyItem(keyAlias: string, huksOptions: huks.HuksOptions) {
  return new Promise<void>((resolve, reject) => {
    try {
      huks.deleteKeyItem(keyAlias, huksOptions, (error, data) => {
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


async function deleteKey(keyAlias: string, huksOptions: huks.HuksOptions): Promise<void> {
  console.info(`enter promise deleteKeyItem`);
  try {
    await deleteKeyItem(keyAlias, huksOptions);
    console.info(`promise: deleteKeyItem success`);
  } catch (error) {
    console.error(`promise: deleteKeyItem failed, ${JSON.stringify(error)}`);
  }
}


async function executeKeyLifecycle(): Promise<string> {
  try {
    /* 1.生成密钥 */
    console.info('start generateKey...');
    await generateKey(keyAlias, generateHuksOptions);
    console.info('end generateKey...');


    /* 2.删除密钥 */
    console.info('start deleteKey...');
    await deleteKey(keyAlias, deleteHuksOptions);
    console.info('end deleteKey...');


    console.info('Key lifecycle completed successfully');
    return 'Success';
  } catch (error) {
    console.error(`Key lifecycle failed: ${JSON.stringify(error)}`);
    return 'Failed';
  }
}
KeyDeletion.ets
密钥删除
密钥删除(C/C++)
