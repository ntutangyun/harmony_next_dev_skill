# @previewer/mandatory

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_value-for-local-initialization_

"@previewer/mandatory-default-value-for-local-initialization": "warn"
  }
}
选项

该规则无需配置额外选项。

正例
@Builder
function MyBuilderFunction(): void {
}


@Entry
@Component
struct Index {
  messageA?: string;
  message: string = 'Hello World';
  @Provide messageB: string = 'messageB';
  @StorageLink('varA') varA: number = 2;
  @StorageProp('languageCode') lang: string = 'en';
  @LocalStorageLink('PropA') storageLink1: number = 1;
  @LocalStorageProp('PropB') storageLink2: number = 2;
  @BuilderParam myBuilder: () => void = MyBuilderFunction;


  build() {
    Row() {
      Column() {
        Text(this.message)
        this.myBuilder()
      }
    }
  }
}
反例
@Entry
@Component
struct Index {
  @BuilderParam myBuilder: () => void;


  build() {
    Row() {
      Column() {
        Text('Hello World')
        this.myBuilder()
      }
    }
  }
}
规则集
plugin:@previewer/recommended
plugin:@previewer/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

预览规则@previewer
@previewer/no-page-method-on-preview-component
