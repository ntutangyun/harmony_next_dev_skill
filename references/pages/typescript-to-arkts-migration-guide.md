# 从TypeScript到ArkTS的适配规则

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typescript-to-arkts-migration-guide_

ArkTS规范约束了TypeScript（简称TS）中影响开发正确性或增加运行时开销的特性。本文罗列了ArkTS中限制的TS特性，并提供重构代码的建议。ArkTS保留了TS大部分语法特性，未在本文中约束的TS特性，ArkTS完全支持。例如，ArkTS支持自定义装饰器，语法与TS一致。按本文约束进行代码重构后，代码仍为合法有效的TS代码。

示例

包含关键字var的原始TypeScript代码：

function addTen(x: number): number {
  var ten = 10;
  return x + ten;
}
Sample.ts

重构后的代码：

function addTen(x: number): number {
  let ten = 10;
  return x + ten;
}
Index.ets

级别

约束分为两个级别：错误、警告。

错误：必须要遵从的约束。如果不遵从该约束，将会导致程序编译失败。
警告：推荐遵从的约束。尽管现在违反该约束不会影响编译流程，但是在将来，违反该约束可能会导致程序编译失败。

不支持的特性

目前，不支持的特性主要包括：

与降低运行时性能的动态类型相关的特性。
需要编译器额外支持从而导致项目构建时间增加的特性。

根据开发者的反馈和实际场景的数据，未来将逐步减少不支持的特性。

概述

本节罗列了ArkTS不支持或部分支持的TypeScript特性。完整的列表以及详细的代码示例和重构建议，请参考约束说明。更多案例请参考适配指导案例。

强制使用静态类型

静态类型是ArkTS的重要特性之一。当程序使用静态类型时，所有类型在编译时已知，这有助于开发者理解代码中的数据结构。编译器可以提前验证代码的正确性，减少运行时的类型检查，从而提升性能。

基于上述考虑，ArkTS中禁止使用any类型。

示例

// 不支持：
let res: any = some_api_function('hello', 'world');
// 支持：
class CallResult {
  public succeeded(): boolean {
    return false;
  }
  public errorMessage(): string {
    return '123';
  }
}
function some_api_function(param1: string, param2: string): CallResult {
  return new CallResult();
}


let res: CallResult = some_api_function('hello', 'world');
if (!res.succeeded()) {
  console.info('Call failed: ' + res.errorMessage());
}

any类型在TypeScript中并不常见，仅约1%的TypeScript代码库使用。代码检查工具（例如ESLint）也制定了一系列规则来禁止使用any。因此，虽然禁止any将导致代码重构，但重构量很小，有助于整体性能提升。

ArkTS语法适配背景
适配指导案例
