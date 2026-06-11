# @typescript-eslint/unbound-method

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_unbound-method_

强制类作用域中的方法在预期范围内调用。

类方法作为独立变量传递时，不会保留类作用域，“this”不再指代当前类。解决方法是定义为“this: void”或者使用箭头函数。

规则配置

// code-linter.json5
{
  "rules": {
    "@typescript-eslint/unbound-method": "error"
  }
}

选项

详情请参考@typescript-eslint/unbound-method选项。

正例

class MyClass {
  public logUnbound(): void {
    this.logUnbound();
  }

  public logBound = () => {
    this.logUnbound();
  };
}

const instance = new MyClass();

// logBound will always be bound with the correct scope
const logBound = instance.logBound;
logBound();

反例

class MyClass {
  public logUnbound(): void {
    this.logUnbound();
  }

  public logBound = () => {
    this.logUnbound();
  };
}

const instance = new MyClass();

// logBound will always be bound with the correct scope
const logUnbound = instance.logUnbound;
logUnbound();

规则集

plugin:@typescript-eslint/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@typescript-eslint/unbound-method": "error"
  }
}
```

### Code block 2

```
class MyClass {
  public logUnbound(): void {
    this.logUnbound();
  }

  public logBound = () => {
    this.logUnbound();
  };
}

const instance = new MyClass();

// logBound will always be bound with the correct scope
const logBound = instance.logBound;
logBound();
```

### Code block 3

```
class MyClass {
  public logUnbound(): void {
    this.logUnbound();
  }

  public logBound = () => {
    this.logUnbound();
  };
}

const instance = new MyClass();

// logBound will always be bound with the correct scope
const logUnbound = instance.logUnbound;
logUnbound();
```

### Code block 4

```
plugin:@typescript-eslint/all
```
