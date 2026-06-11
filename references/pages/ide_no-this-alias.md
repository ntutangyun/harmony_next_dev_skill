# @typescript-eslint/no-this-alias

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-this-alias_

禁止将“this”赋值给一个变量。

该规则仅支持对.js/.ts文件进行检查。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-this-alias": "error"
  }
}

选项

详情请参考@typescript-eslint/no-this-alias选项。

正例

const time = 1000;
export class CC {
  public doWork(): void {
    console.info('work');
  }

  public init(): void {
    setTimeout(function () {
      this.doWork();
    });
  }
}

反例

// 禁止将this赋值给一个变量
const self = this;

setTimeout(function () {
  self.doWork();
});

规则集

plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-this-alias": "error"
  }
}
```

### Code block 2

```
const time = 1000;
export class CC {
  public doWork(): void {
    console.info('work');
  }

  public init(): void {
    setTimeout(function () {
      this.doWork();
    });
  }
}
```

### Code block 3

```
// 禁止将this赋值给一个变量
const self = this;

setTimeout(function () {
  self.doWork();
});
```

### Code block 4

```
plugin:@typescript-eslint/recommended
plugin:@typescript-eslint/all
```
