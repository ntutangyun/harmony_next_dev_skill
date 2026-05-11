# 异常堆栈解析原理

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle_

-----------------------key----------------------------------  :  -----------value----------*/
originalmethodname: originalmethodstartline: originalmethodendline :  obfuscatedmethodname
originalmethodname 表示原始的方法名称。
[:originalmethodstartline:originalmethodendline] 表示原始的方法起始行数与结束行数，左右都是闭区间。
obfuscatedmethodname 表示混淆后的方法名称。
MemberMethodCache：该字段对应的值为该文件下的成员方法名混淆前后的映射关系。

开启属性混淆时，成员方法映射关系的格式如下：

/*--------------------------key---------------------------------  :  -----------value----------*/
originalmethodname:originalmethodstartline:originalmethodendline  :  obfuscatedmethodname

未开启属性混淆时，成员方法映射关系的格式如下：

/*--------------------------key-------------------------------------  :  -----------value----------*/
originalmethodname : originalmethodstartline : originalmethodendline  :  originalmethodname
originalmethodname 表示原始的成员方法名称。
[:originalmethodstartline :originalmethodendline] 表示原始的成员方法起始行数与结束行数，左右都是闭区间。
obfuscatedmethodname 表示混淆后的成员方法名称。
PropertyCache：该字段对应的值为全局所有属性名混淆前后的映射关系，只有在开启属性混淆时才会有值。

属性名映射关系格式如下：

/*--------key-------  :  -----------value----------*/ 
originalpropertyname  :  obfuscatedmethodname
originalpropertyname 表示原始的属性名称。
obfuscatedmethodname 表示混淆后的属性名称。
代码混淆解析

异常堆栈如下：

Pid:58348
Uid:20020156
Reason:RangeError
Error name:RangeError
Error message:The number cannot be converted to a BigInt because it is not an integer
Stacktrace:
Cannot get SourceMap info, dump raw stack:
    at g2 (home|home|1.0.0|src/main/ets/pages/a.ts:6:6)
    at getVersion (home|home|1.0.0|src/main/ets/pages/a.ts:2:2)
    at anonymous (home|home|1.0.0|src/main/ets/pages/Index.ts:61:61)

经过sourceMap映射转码堆栈如下：
at g2 (home/src/main/ets/pages/tool.ts:7:27)
at getVersion (home/src/main/ets/pages/tool.ts:2:30)
at anonymous (home/src/main/ets/pages/Index.ets:23:40)

a.ts通过sourceMap还原为tool.ts。

"home|home|1.0.0|src/main/ets/pages/a.ts": {
    "version": 3,
    "file": "tool.ts",
    "sources": [
      "home/src/main/ets/pages/tool.ts"
    ],
    "names": [],
    "mappings": "AAAA,MAAM,CAAC,OAAO,UAAU,UAAU,IAAI,MAAM;IAC1C,IAAI,KAAM,IAAiB,CAAA;IAC3B,UAAW;AACb,CAAC;AAED,eAA2B,MAAM;IAC/B,IAAI,GAAG,GAAG,MAAM,CAAC,MAAM,CAAC,CAAA;IACxB,OAAO,GAAG,CAAC;AACb,CAAC",
    "sourceRoot": "",
    "entry-package-info": "home|1.0.0"
  }
函数级文件名映射。

查看混淆映射表：$ProjectPath\$ModuleName\build\$product\cache\default\default@CompileArkTS\esmodule\release\obfuscation\nameCache.json

"home/src/main/ets/pages/tool.ts": {
    "IdentifierCache": {
      "getVersion#res": "h2",
      "#testObfuscation:6:9": "g2"
    },
    "MemberMethodCache": {},
    "obfName": "home/src/main/ets/pages/a.ts"
  }

该字段的IdentifierCache与MemberMethodCache中保存了方法名混淆前后的映射关系，对应格式为："源码方法名:该方法起始行号:该方法结束行号":"混淆后方法名"。

源码方法名中的"源码方法名"代表上下级关系，故匹配后可以通过"#"保留最后名称。

第一条堆栈混淆后的方法名为"g2"，若存在多个"g2"则需要通过行号范围过滤，故利用上述字段对该方法名进行还原：

通过key(home/src/main/ets/pages/tool.ts)查找到映射表。
在上述字段中找出所有混淆后方法名为"g2"的条目，该条目为：
"#testObfuscation:6:9": "g2"
找到行号范围包含步骤一中还原后行号的条目，步骤一中得到的行号为7包含在6-9之内，因此可以得到源码对应方法名为"#testObfuscation"，经过字符串处理结果为"testObfuscation"。
at testObfuscation (home/src/main/ets/pages/tool.ts:7:27)
at getVersion (home/src/main/ets/pages/tool.ts:2:30)
at anonymous (home/src/main/ets/pages/Index.ets:23:40)

堆栈轨迹分析
使用ASan检测内存错误
