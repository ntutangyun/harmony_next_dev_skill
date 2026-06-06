# 管理群组关键资产(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/asset-js-group-access-control_

let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
  let str = textDecoder.decodeToString(arr, { stream: false });
  return str;
}
query_group_plaintext.ets
新增群组关键资产

在群组中新增密码为demo_pwd、别名为demo_alias、附属信息为demo_label的关键资产。

let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
attr.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label'));
attr.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
try {
  asset.add(attr).then(() => {
    console.info(`Succeeded in adding Asset to the group.`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to add Asset to the group. Code is ${err.code}, message is ${err.message}`);
    // ...
  })
} catch (error) {
  let err = error as BusinessError;
  console.error(`Failed to add Asset to the group. Code is ${err?.code}, message is ${err?.message}`);
  // ...
}
add_group.ets
删除群组关键资产

在群组中删除别名为demo_alias的关键资产。

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias')); // 此处指定别名删除单条群组关键资产，也可不指定别名删除多条群组关键资产。
query.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
try {
  asset.remove(query).then(() => {
    console.info(`Succeeded in removing Asset from the group.`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to remove Asset from the group. Code is ${err.code}, message is ${err.message}`);
    // ...
  });
} catch (err) {
  console.error(`Failed to remove Asset from the group. Code is ${err?.code}, message is ${err?.message}`);
  // ...
}
remove_group.ets
更新群组关键资产

在群组中更新别名为demo_alias的关键资产，明文更新为demo_pwd_new，附属属性更新为demo_label_new。

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias'));
query.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo_pwd_new'));
attrsToUpdate.set(asset.Tag.DATA_LABEL_NORMAL_1, stringToArray('demo_label_new'));
try {
  asset.update(query, attrsToUpdate).then(() => {
    console.info(`Succeeded in updating Asset in the group.`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to update Asset in the group. Code is ${err.code}, message is ${err.message}`);
    // ...
  });
} catch (err) {
  console.error(`Failed to update Asset in the group. Code is ${err?.code}, message is ${err?.message}`);
  // ...
}
update_group.ets
查询单条群组关键资产明文

在群组中查询别名为demo_alias的关键资产明文。

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias')); // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ALL); // 此处表示需要返回群组关键资产的所有信息，即属性+明文。
query.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
try {
  asset.query(query).then((res: Array<asset.AssetMap>) => {
    for (let i = 0; i < res.length; i++) {
      // 解析secret。
      let secret: Uint8Array = res[i].get(asset.Tag.SECRET) as Uint8Array;
      // 将Uint8Array转换为string类型。
      let secretStr: string = arrayToString(secret);
    }
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to query Asset plaintext from the group. Code is ${err.code}, message is ${err.message}`);
    // ...
  });
} catch (err) {
  console.error(`Failed to query Asset plaintext from the group. Code is ${err?.code}, message is ${err?.message}`);
  // ...
}
query_group_plaintext.ets
查询单条群组关键资产属性

在群组中查询别名为demo_alias的关键资产属性。

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo_alias')); // 指定了群组关键资产别名，最多查询到一条满足条件的群组关键资产。
query.set(asset.Tag.RETURN_TYPE, asset.ReturnType.ATTRIBUTES); // 此处表示仅返回群组关键资产属性，不包含群组关键资产明文。
query.set(asset.Tag.GROUP_ID, stringToArray('demo_group_id'));
try {
  asset.query(query).then((res: Array<asset.AssetMap>) => {
    for (let i = 0; i < res.length; i++) {
      // 解析属性。
      let accessibility: number = res[i].get(asset.Tag.ACCESSIBILITY) as number;
      console.info(`Succeeded in getting accessibility, which is: ${accessibility}.`);
    }
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to query Asset attribute from the group. Code is ${err.code}, message is ${err.message}`);
    // ...
  });
} catch (err) {
  console.error(`Failed to query Asset attribute from the group. Code is ${err?.code}, message is ${err?.message}`);
  // ...
}
query_group_attr.ets
查询需要用户认证的关键资产(ArkTS)
同步（备份恢复）关键资产(ArkTS)
