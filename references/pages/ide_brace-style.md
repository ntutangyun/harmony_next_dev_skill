# @typescript-eslint/brace-style

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_brace-style_

对代码块强制执行一致的括号样式。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/brace-style": "error"
  }
}

选项

详情请参考@typescript-eslint/brace-style选项。

正例

function foo(): boolean {
  return true;
}

class C {
  static {
    foo();
  }

  public meth() {
    foo();
  }
}

export { C };

反例

function foo(): boolean
{
  return true;
}

class C {
  static
  {
    foo();
  }

  public meth()
  {
    foo();
  }
}

export { C };

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/brace-style": "error"
  }
}
```

### Code block 2

```
function foo(): boolean {
  return true;
}

class C {
  static {
    foo();
  }

  public meth() {
    foo();
  }
}

export { C };
```

### Code block 3

```
function foo(): boolean
{
  return true;
}

class C {
  static
  {
    foo();
  }

  public meth()
  {
    foo();
  }
}

export { C };
```

### Code block 4

```
plugin:@typescript-eslint/all
```
