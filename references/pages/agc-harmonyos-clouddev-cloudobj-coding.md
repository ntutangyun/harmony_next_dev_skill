# 开发云对象

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-cloudobj-coding_

云对象创建完成后，您便可以直接在云对象中编写需要实现的方法。例如，通过云对象实现add与subtract两个方法。

export class MyCloudObject {
    add(num1: number, num2: number) {
        return { result: num1 + num2 };
    }
    subtract(num1: number, num2: number) {
        return { result: num1 - num2 };
    }
}

注意

云对象是无状态性的。云对象部署至云侧后，每一次调用都可能是不同的后台节点，因此在云对象上定义类成员变量是无意义的。从一个Method中对一个类成员属性赋值，然后期望从另一个Method去获取类成员属性，这样的做法是错误的。

云对象无需编写构造函数。云侧在收到对云对象的某一个函数的请求时，会调用云对象的默认的无参构造函数。

云对象方法的输入是从JSON反序列化而来，只能是string、number或者Object，不支持Date、Uint8Array等类型。如果在编写云对象代码的过程中需要传递Date或Uint8Array，建议通过定义成number或者数组，在Method内通过显式地调用Date或Uint8Array的构造函数来达到目的。

云对象的方法的输出当前不支持单个number返回。

云对象的方法的输入、输出可以使用自定义对象，不能使用第三方依赖定义的对象或类型。注意，并不是云对象不能有第三方依赖，而是云对象的输入和输出不能有第三方依赖，否则在"Generator Invoke Interface"阶段，将会因为找不到依赖而失败，根本原因是，端侧代码运行在HarmonyOS支持方舟运行时，而云侧运行在Node.js中，二者的依赖管理不同。

说明

右击“package.json”文件，选择“Run 'npm install'”菜单，也可以实现依赖包安装。

所有安装的依赖包都会存储在当前云对象的“node_modules”目录下。

## Code blocks

### Code block 1

```
export class MyCloudObject {
    add(num1: number, num2: number) {
        return { result: num1 + num2 };
    }
    subtract(num1: number, num2: number) {
        return { result: num1 - num2 };
    }
}
```
