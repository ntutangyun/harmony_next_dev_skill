# (可选）一键生成Model Class

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-modelclass_

云数据库支持从端侧或者云侧云函数（含云对象）访问云数据库，代码涉及调用云数据库时，需引入对应云数据库对象类型的Model Class。当前支持为对象类型一键生成Server Model与Client Model，供您在端侧及云侧云函数（含云对象）开发时引用。

生成Server Model

指定目录下生成对应对象类型的Server Model文件，后续您便可以在代码中方便地引用该Server Model 。

"dependencies": {
  "@hw-agconnect/cloud-server": "latest"
}

import { cloud } from '@hw-agconnect/cloud-server';
import { Post } from './Post'; // Post是Server Model

// Demo是Post对象类型使用的存储区名
const collection = cloud.database({ zoneName: 'Demo' }).collection(Post);

// IdGenerator云对象，实现了对Post对象类型的查询和更新
export class IdGenerator {
  query() {
    return collection.query().get();
  }

  upsert(posts: Post[]) {
    return new Promise((resolve, reject) => {
      collection.upsert(posts.map(post => Post.parseFrom(post)))
        .then(result => resolve({ result }))
        .catch(err => reject(err))
    });
  }
}

注意

如果定义的云数据库表字段中包含ByteArray或Date类型的字段，在插入或者更新云数据库时需要使用Server Model的parseFrom方法将入参转化成API识别的类型，例如上述示例中的Post.parseFrom方法。

生成Client Model

指定目录下生成对应对象类型的Client Model文件，后续您便可以在端侧代码中方便地引用该Client Model，具体可参考端云一体化工程初始化代码中的Client Model示例（“ets/pages/CloudDb/Post.ts”）在CloudDb.ets以及DbInset.ets中的引用。

## Code blocks

### Code block 1

```
"dependencies": {
  "@hw-agconnect/cloud-server": "latest"
}
```

### Code block 2

```
import { cloud } from '@hw-agconnect/cloud-server';
import { Post } from './Post'; // Post是Server Model

// Demo是Post对象类型使用的存储区名
const collection = cloud.database({ zoneName: 'Demo' }).collection(Post);

// IdGenerator云对象，实现了对Post对象类型的查询和更新
export class IdGenerator {
  query() {
    return collection.query().get();
  }

  upsert(posts: Post[]) {
    return new Promise((resolve, reject) => {
      collection.upsert(posts.map(post => Post.parseFrom(post)))
        .then(result => resolve({ result }))
        .catch(err => reject(err))
    });
  }
}
```
