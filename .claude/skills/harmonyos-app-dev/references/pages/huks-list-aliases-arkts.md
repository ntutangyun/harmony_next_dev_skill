# 查询密钥别名集(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-list-aliases-arkts_

let result: huks.HuksListAliasesReturnResult = await huks.listAliases(queryOptions);
    console.info(`promise: listAliases success`);
  } catch (error) {
    console.error(`promise: listAliases fail`);
    throw (error as Error);
  }
}
QueryKeyAliasSet.ets
查询密钥别名集
查询密钥别名集(C/C++)
