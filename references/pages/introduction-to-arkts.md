# ArkTS语言介绍

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts_

ArkTS是一种设计用于构建高性能应用的编程语言。它在继承TypeScript语法的基础上进行了优化，以提供更高的性能和开发效率。

许多编程语言在设计之初未考虑移动设备，导致应用运行缓慢、低效且功耗大。随着移动设备在日常生活中越来越普遍，针对移动环境的编程语言优化需求日益增加。ArkTS专为解决这些问题而设计，聚焦提高运行效率。

TypeScript是在JavaScript基础上通过添加类型定义扩展而来的，ArkTS则是TypeScript的进一步扩展。TypeScript提供了一种更结构化的JavaScript编码方法，深受开发者喜爱。ArkTS保持了TypeScript的大部分语法，旨在为现有的TypeScript开发者提供高度兼容的体验，帮助移动开发者快速上手。

ArkTS的一大特性是它专注于低运行时开销。ArkTS对TypeScript的动态类型特性施加了更严格的限制，以减少运行时开销，提高执行效率。通过取消动态类型特性，ArkTS代码能更有效地被运行前编译和优化，从而实现更快的应用启动和更低的功耗。

ArkTS语言设计中考虑了与TypeScript和JavaScript的互通性。许多移动应用开发者希望重用TypeScript和JavaScript代码及库，因此ArkTS提供与TypeScript和JavaScript的无缝互通，使开发者可以轻松集成TypeScript和JavaScript代码到应用中，充分利用现有代码和库进行ArkTS开发。

本教程将指导开发者了解ArkTS的核心功能、语法和最佳实践，助力开发者使用ArkTS高效构建高性能的移动应用。

如需详细了解ArkTS语言，请参阅ArkTS具体指南和DevEco Studio。

基本知识
声明

ArkTS通过声明引入变量、常量、类型和函数。

变量声明

使用关键字let声明的变量可以在程序执行期间具有不同的值。

let hi: string = 'hello';
hi = 'hello, world';

常量声明

使用关键字const声明的常量为只读类型，只能被赋值一次。

const hello: string = 'hello';

对常量重新赋值会造成编译时错误。

自动类型推断

如果变量或常量的声明包含初始值，开发者无需显式指定类型，因为ArkTS规范已列举了所有允许自动推断类型的场景。

以下示例中，两条声明语句都是有效的，两个变量都是string类型：

let hi1: string = 'hello';
let hi2 = 'hello, world';

导入HarmonyOS SDK的开放能力

HarmonyOS SDK提供的开放能力（接口）也需要在导入声明后使用。可直接导入接口模块来使用该模块内的所有接口能力，例如：

import UIAbility from '@ohos.app.ability.UIAbility';

从HarmonyOS NEXT Developer Preview 1版本开始引入Kit概念。SDK对同一个Kit下的接口模块进行了封装，开发者在示例代码中可通过导入Kit的方式来使用Kit所包含的接口能力。其中，Kit封装的接口模块可查看SDK目录下Kit子目录中各Kit的定义。在代码开发中，推荐通过导入Kit方式使用开放能力。

通过导入Kit方式使用开放能力有三种方式：

方式一：导入Kit下单个模块的接口能力。例如：

import { UIAbility } from '@kit.AbilityKit';

方式二：导入Kit下多个模块的接口能力。例如：

import { UIAbility, Ability, Context } from '@kit.AbilityKit';

方式三：导入Kit包含的所有模块的接口能力。例如：

import * as module from '@kit.AbilityKit';

其中，“module”为别名，可自定义，然后通过该名称调用模块的接口。

说明

方式三可能会导入过多无需使用的模块，导致编译后的HAP包太大，占用过多资源，请谨慎使用。

初识ArkTS语言
ArkTS编程规范
