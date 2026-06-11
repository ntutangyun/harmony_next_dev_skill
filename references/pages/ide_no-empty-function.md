# @typescript-eslint/no-empty-function

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_no-empty-function_

不允许使用空函数。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-empty-function": "error"
  }
}

选项

详情请参考@typescript-eslint/no-empty-function选项。

正例

该规则旨在消除空函数。如果函数包含注释，则不会将其视为问题。

/*eslint no-empty-function: "error"*/
function foo() {
  // do nothing.
}

const baz = () => {
  foo();
};

export class Bar {
  public meth1() {
    // do something
  }

  public meth2() {
    baz();
  }
}

反例

/*eslint no-empty-function: "error"*/
function foo() {

}

const baz = () => {

};

export class Bar {
  public meth1() {

  }

  public meth2() {

  }
}

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/no-empty-function": "error"
  }
}
```

### Code block 2

```
/*eslint no-empty-function: "error"*/
function foo() {
  // do nothing.
}

const baz = () => {
  foo();
};

export class Bar {
  public meth1() {
    // do something
  }

  public meth2() {
    baz();
  }
}
```

### Code block 3

```
/*eslint no-empty-function: "error"*/
function foo() {

}

const baz = () => {

};

export class Bar {
  public meth1() {

  }

  public meth2() {

  }
}
```

### Code block 4

```
plugin:@typescript-eslint/all
```
