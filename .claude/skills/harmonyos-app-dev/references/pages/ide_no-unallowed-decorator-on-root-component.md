# @previewer/no

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-unallowed-decorator-on-root-component_

"@previewer/no-unallowed-decorator-on-root-component": "warn"
  }
}
选项

该规则无需配置额外选项。

正例
@Entry
@Component
struct LinkSampleContainer {
  @State message: string = 'Hello World';
  build() {
    Row() {
      LinkSample({message: this.message})
    }
  }
}
@Component
struct LinkSample {
  @Link message: string;
  build() {
    Row() {
      Text(this.message)
    }
  }
}
反例
@Preview
@Component
struct LinkSample {
  @Link message: string;
  build() {
    Row() {
      Text(this.message)
    }
  }
}
规则集
plugin:@previewer/recommended
plugin:@previewer/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@previewer/no-page-method-on-preview-component
一次开发多端部署规则@cross-device-app-dev
