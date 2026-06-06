# 规则变更说明

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codelinter-rules-change_

@correctness/v1-state-object-member-used-in-function-parameter-check
6.0.2.636

新增规则

@correctness/redundant-dependency-check
@cross-device-app-dev/immersive-effect-check
6.0.1.246

新增规则

@compatibility/api-compatibility-check
6.0.0.848

新增规则

@security/no-unsafe-kdf
@security/no-unsafe-sm4
@security/no-unsafe-sm2-key
@security/no-unsafe-sm2-cipher
@security/no-unsafe-ecdh
@security/no-unsafe-huks
6.0.0.828

新增规则

@performance/no-use-any-import
@performance/avoid-overusing-custom-component-check
@performance/bad-deep-clone-check
@performance/reasonable-audio-use-check
@performance/reasonable-sensor-use-check
@performance/reasonable-gps-use-check
@performance/reuse-date-instances-check
@performance/crypto-replacement-check
@performance/monitor-invisible-area-in-image-animation
@performance/datashare-query-unrelease-check
@performance/dark-color-mode-check
@performance/update-state-var-between-animatetos-check
@performance/tabs-on-change-check
@performance/nested-post-frame-callback-check
@cross-device-app-dev/window-size-change-listener-check
6.0.0.418

新增规则

@performance/web-on-active-check
@performance/gif-hardware-decoding-check
@cross-device-app-dev/one-multi-breakpoint-check

变更规则

@typescript-eslint/explicit-function-return-type规则新增额外选项allowArkTS（默认为false），配置为true时，支持对.ets文件进行检查。

5.1.0.828

新增规则

@performance/web-cache-mode-check
@correctness/audio-interrupt-check
@correctness/audio-pause-or-mute-check
@correctness/avsession-metadata-check
@correctness/avsession-buttons-check
@correctness/image-interpolation-check
@correctness/image-pixel-format-check
@performance/hp-ffrt-no-use-std

变更规则

@performance/hp-arkui-use-taskpool-for-web-request所属规则集由recommended改为all。
5.0.7.100

新增规则

@performance/foreach-index-check
@performance/js-code-cache-by-precompile-check
@performance/js-code-cache-by-interception-check
@performance/init-list-component
@correctness/listen-default-network-change
@correctness/listen-multi-network-concurrent
@security/no-unsafe-3des

变更规则

@performance/high-frequency-log-check增加检测高频函数onWillScroll。
@typescript-eslint/prefer-readonly-parameter-types和@typescript-eslint/no-magic-numbers中，规则的默认告警级别由error改为warn。
@typescript-eslint/lines-between-class-members默认检查规则从成员变量之间必须有空行分隔，变更为成员变量和成员变量之间不需要有空行分隔。
@security/no-unsafe-hash新增对@ohos/crypto-js包中不安全Hash算法检查。
@security/no-unsafe-mac新增对@ohos/crypto-js包中不安全Mac算法检查。
5.0.5.200

变更规则

@performance/hp-arkui-avoid-empty-callback所属规则集由recommended改为all。
@performance/hp-arkui-use-word-break-to-replace-zero-width-space所属规则集由recommended改为all。
@performance/hp-arkui-remove-redundant-nest-container所属规则集由recommended改为all。
@performance/hp-arkui-remove-container-without-property所属规则集由recommended改为all。
@performance/sparse-array-check所属规则集由recommended改为all。
@performance/number-init-check所属规则集由recommended改为all。
@performance/typed-array-check所属规则集由recommended改为all。
5.0.3.800

新增规则

@performance/hp-arkui-reduce-pangesture-distance
@performance/hp-arkui-suggest-use-get-anonymousid-async
@performance/multiple-associations-state-var-check
@performance/constant-property-referencing-check-in-loops
@performance/foreach-args-check

变更规则

@security/specified-interface-call-chain-check新增对命名空间namespace、类型别名type、接口interface、枚举enum和结构体struct的支持。namespace字段配置类型从字符串变更为数组。
@performance/high-frequency-log-check默认告警等级从suggestion变更为warn，该规则新增至all规则集中。
@performance/number-init-check默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
@performance/start-window-icon-check默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
@performance/sparse-array-check默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
@performance/typed-array-check默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
@performance/waterflow-data-preload-check该规则新增至recommended规则集中。
@performance/hp-arkts-no-use-any-export-current告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkts-no-use-any-export-other，该规则新增至recommended规则集中。
@performance/hp-arkui-avoid-empty-callback告警级别由warn改为suggestion。
@performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse，该规则新增至recommended规则集中。
@performance/hp-arkui-image-async-load所属规则集由recommend改为all。
@performance/hp-arkui-load-on-demand告警级别由suggestion改为warn。
@performance/hp-arkui-no-stringify-in-lazyforeach-key-generator告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkui-remove-container-without-property告警级别由warn改为suggestion。
@performance/hp-arkui-remove-redundant-nest-container告警级别由warn改为suggestion。
@performance/hp-arkui-replace-nested-reusable-component-by-builder告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkui-suggest-cache-avplayer告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component告警级别由suggestion改为warn, 该规则新增至recommended规则集中。
@performance/hp-arkui-suggest-use-effectkit-blur，该规则新增至recommended规则集中。
@performance/hp-arkui-use-grid-layout-options告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkui-use-local-var-to-replace-state-var告警级别由suggestion改为warn。
@performance/hp-arkui-use-onAnimationStart-for-swiper-preload告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkui-use-reusable-component告警级别由suggestion改为warn。
@performance/hp-arkui-use-row-column-to-replace-flex，所属规则集由recommended改为all。
@performance/hp-arkui-use-scale-to-replace-attr-animateto告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkui-use-taskpool-for-web-request告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkui-use-transition-to-replace-animateto告警级别由suggestion改为warn，该规则新增至recommended规则集中。
@performance/hp-arkui-use-word-break-to-replace-zero-width-space该规则新增至recommended规则集中。
@performance/hp-arkui-set-cache-count-for-lazyforeach-grid告警级别由warn改为suggestion。

下线规则

@performance/hp-arkui-wrap-waterflow-if-else-footer
5.0.3.600

新增规则

@performance/hp-arkui-wrap-waterflow-if-else-footer
@performance/hp-arkui-remove-unchanged-state-var
@performance/hp-arkts-no-use-any-export-current
@performance/hp-arkts-no-use-any-export-other
@performance/hp-arkui-suggest-cache-avplayer
@performance/hp-arkui-suggest-use-effectkit-blur
@performance/lottie-animation-destroy-check
@performance/timezone-interface-check

变更规则

以下规则的部分场景，在5.0.3.600之前的版本检查执行Codelinter检查时不报错，升级至DevEco Studio 5.0.3.600版本后执行Codelinter检查将报错。

@typescript-eslint/no-unnecessary-condition
// 场景一：支持逻辑表达式的检查
interface GeneratedTypeLiteralInterface {}
declare let foo: GeneratedTypeLiteralInterface;
foo ??= 1; // 升级前不报错，升级后报错
// 场景二：链式表达式中可以推断为非空的场景下，不需要增加判空
interface GeneratedTypeLiteralInterface {
  bar: () => number;
}
type Foo = GeneratedTypeLiteralInterface | null;
declare const foo: Foo;
foo?.bar()?.toExponential(); // 升级前不报错，升级后报错
@typescript-eslint/promise-function-async
// 函数返回值没有显式定义类型，并且返回值可能为Promise的场景下，函数需要定义为async
function promiseInUnionWithoutExplicitReturnType(p: boolean) { // 升级前不报错，升级后报错
  return p ? Promise.resolve(5) : 5;
}
@typescript-eslint/member-ordering
// 配置了optionalityOrder选项，并且类属性中不包含可选变量的场景下，规则中配置的order选项在历史版本中失效了
// 规则配置为"@typescript-eslint/member-ordering": ["error", {"default": {"memberTypes": 'never', "order": 'natural-case-insensitive', "optionalityOrder": 'required-first',}}]
class X {
  b: string = '';
  a: string = ''; // 升级前不报错，升级后报错
}
@typescript-eslint/naming-convention
// 支持检查interface中的typeMethod
// 规则配置为："@typescript-eslint/naming-convention": ["error", {selector: 'typeMethod', format: ['PascalCase']}]
interface SOME_INTERFACE {
  someMethod: () => void; // 升级前不报错，升级后报错
  some_property: string;
}
@typescript-eslint/ban-types
// 支持检查extend、implements后的类型
// 规则配置为："@typescript-eslint/ban-types": ["error",{"types": {"Bar": {"message": ""}}}]
interface Bar {}
interface Baz {}
interface Foo extends Bar, Baz {} // 升级前不报错，升级后报错
@typescript-eslint/no-floating-promises
// 场景一：.finally()被认为是没有有效处理Promise中可能发生的异常
Promise.reject().finally(() => {}) // 升级前不报错，升级后报错
// 场景二：.then()中的第二个参数如果是undefined或者null，被认为是没有有效处理Promise中可能发生的异常
Promise.resolve().then(() => {}, undefined); // 升级前不报错，升级后报错
Promise.resolve().then(() => {}, null); // 升级前不报错，升级后报错
@typescript-eslint/no-inferrable-types
// 支持检查构造函数中的参数类型
class Foo {
  constructor(param: boolean = true) {} // 升级前不报错，升级后报错
}
@typescript-eslint/prefer-readonly
interface GeneratedObjectLiteralInterface {
  prop?: string
}


class Test {
  // 支持检查私有属性
  #testObj: GeneratedObjectLiteralInterface = {}; // 升级前不报错，升级后报错


  public test(): void {
    this.#testObj?.prop;
  }
}

5.0.3.500

新增规则

@security/no-unsafe-dh-key
@security/no-unsafe-dsa-key
@security/no-unsafe-rsa-key
@performance/hp-arkui-use-attributeUpdater-control-refresh-scope
@performance/hp-arkui-use-id-in-get-resource-sync-api
@performance/hp-arkui-use-transition-to-replace-animateto
@performance/hp-arkui-remove-redundant-state-var
@performance/hp-arkui-use-taskpool-for-web-request
@security/specified-interface-call-chain-check
@hw-stylistic/file-naming-convention

变更规则

@performance/high-frequency-log-check所属规则集由all变更为recommended。

下线规则

@performance/object-creation-check
@performance/hp-arkui-limit-refresh-scope
@performance/lazyforeach-args-check
Code Linter代码检查规则
recommended推荐规则清单
