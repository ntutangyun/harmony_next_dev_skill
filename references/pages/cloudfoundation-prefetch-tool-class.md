# 预加载工具类

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-prefetch-tool-class_

在“entry/src/main/ets/common”目录下新增GlobalContext.ets和PreferenceUtil.ets。

GlobalContext

全局上下文类，提供全局上下文句柄的初始化和获取功能。参考示例如下：

import { common } from '@kit.AbilityKit';

export class GlobalContext {
  private static context: common.UIAbilityContext;

  public static initContext(context: common.UIAbilityContext): void {
    GlobalContext.context = context;
  }

  public static getContext(): common.UIAbilityContext {
    return GlobalContext.context;
  }
}

PreferenceUtil

首选项工具类，提供数据读取和存储功能。参考示例如下：

import { preferences } from '@kit.ArkData';
import { Context } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = 'PreferenceUtil';
const DEFAULT_STORE_NAME: string = 'prefetchDefaultStore';

export class PreferenceUtil {
  private static cachedPreferences: Map<string, preferences.Preferences> = new Map();

  private constructor() {
  }

  public static async getValue(context: Context, storeName: string,
    key: string): Promise<preferences.ValueType | null> {
    try {
      let store = await PreferenceUtil.getStore(context, storeName);
      PreferenceUtil.updateStoreCache(storeName, store);
      const result = await store.get(key, '');
      return result;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `getValue from ${storeName} error, key:${key}, err:${err.message}`);
      return null;
    }
  }

  public static getValueSync(context: Context, storeName: string, key: string): preferences.ValueType | null {
    try {
      let store = PreferenceUtil.getStoreSync(context, storeName);
      PreferenceUtil.updateStoreCache(storeName, store);
      const result = store.getSync(key, '');
      return result;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `getValueSync from ${storeName} error, key:${key}, err:${err.message}`);
      return null;
    }
  }

  public static async setValue(context: Context, storeName: string, key: string,
    value: preferences.ValueType): Promise<void> {
    try {
      let store = await PreferenceUtil.getStore(context, storeName);
      PreferenceUtil.updateStoreCache(storeName, store);
      await store.put(key, value);
      await store.flush();
    } catch (err) {
      hilog.error(DOMAIN, TAG, `putValue from ${storeName} error, key:${key}, err:${err.message}`);
    }
  }


  private static async getStore(context: Context, storeName: string): Promise<preferences.Preferences> {
    let actualStoreName = !storeName ? DEFAULT_STORE_NAME : storeName;
    let store = PreferenceUtil.cachedPreferences.get(actualStoreName);
    if (store) {
      return store;
    }
    hilog.info(DOMAIN, TAG, `there is no cached store:${actualStoreName}, begin to get one`);
    try {
      return preferences.getPreferences(context, actualStoreName);
    } catch (error) {
      hilog.error(DOMAIN, TAG, `Failed to get preferences: ${error}`);
      throw new Error(`Failed to get preferences: ${error}`);
    }
  }

  private static getStoreSync(context: Context, storeName: string): preferences.Preferences {
    let actualStoreName = !storeName ? DEFAULT_STORE_NAME : storeName;
    let store = PreferenceUtil.cachedPreferences.get(actualStoreName);
    if (store) {
      return store;
    }
    hilog.info(DOMAIN, TAG, `getStoreSync there is no cached store:${actualStoreName}, begin to get one`);
    try {
      return preferences.getPreferencesSync(context, { name: actualStoreName });
    } catch (error) {
      hilog.error(DOMAIN, TAG, `Failed to get preferences sync: ${error}`);
      throw new Error(`Failed to get preferences sync: ${error}`);
    }
  }

  private static updateStoreCache(storeName: string, store: preferences.Preferences): void {
    if (!PreferenceUtil.cachedPreferences.has(storeName)) {
      PreferenceUtil.cachedPreferences.set(storeName, store);
    }
  }
}

## Code blocks

### Code block 1

```
import { common } from '@kit.AbilityKit';

export class GlobalContext {
  private static context: common.UIAbilityContext;

  public static initContext(context: common.UIAbilityContext): void {
    GlobalContext.context = context;
  }

  public static getContext(): common.UIAbilityContext {
    return GlobalContext.context;
  }
}
```

### Code block 2

```
import { preferences } from '@kit.ArkData';
import { Context } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = 'PreferenceUtil';
const DEFAULT_STORE_NAME: string = 'prefetchDefaultStore';

export class PreferenceUtil {
  private static cachedPreferences: Map<string, preferences.Preferences> = new Map();

  private constructor() {
  }

  public static async getValue(context: Context, storeName: string,
    key: string): Promise<preferences.ValueType | null> {
    try {
      let store = await PreferenceUtil.getStore(context, storeName);
      PreferenceUtil.updateStoreCache(storeName, store);
      const result = await store.get(key, '');
      return result;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `getValue from ${storeName} error, key:${key}, err:${err.message}`);
      return null;
    }
  }

  public static getValueSync(context: Context, storeName: string, key: string): preferences.ValueType | null {
    try {
      let store = PreferenceUtil.getStoreSync(context, storeName);
      PreferenceUtil.updateStoreCache(storeName, store);
      const result = store.getSync(key, '');
      return result;
    } catch (err) {
      hilog.error(DOMAIN, TAG,
        `getValueSync from ${storeName} error, key:${key}, err:${err.message}`);
      return null;
    }
  }

  public static async setValue(context: Context, storeName: string, key: string,
    value: preferences.ValueType): Promise<void> {
    try {
      let store = await PreferenceUtil.getStore(context, storeName);
      PreferenceUtil.updateStoreCache(storeName, store);
      await store.put(key, value);
      await store.flush();
    } catch (err) {
      hilog.error(DOMAIN, TAG, `putValue from ${storeName} error, key:${key}, err:${err.message}`);
    }
  }


  private static async getStore(context: Context, storeName: string): Promise<preferences.Preferences> {
    let actualStoreName = !storeName ? DEFAULT_STORE_NAME : storeName;
    let store = PreferenceUtil.cachedPreferences.get(actualStoreName);
    if (store) {
      return store;
    }
    hilog.info(DOMAIN, TAG, `there is no cached store:${actualStoreName}, begin to get one`);
    try {
      return preferences.getPreferences(context, actualStoreName);
    } catch (error) {
      hilog.error(DOMAIN, TAG, `Failed to get preferences: ${error}`);
      throw new Error(`Failed to get preferences: ${error}`);
    }
  }

  private static getStoreSync(context: Context, storeName: string): preferences.Preferences {
    let actualStoreName = !storeName ? DEFAULT_STORE_NAME : storeName;
    let store = PreferenceUtil.cachedPreferences.get(actualStoreName);
    if (store) {
      return store;
    }
    hilog.info(DOMAIN, TAG, `getStoreSync there is no cached store:${actualStoreName}, begin to get one`);
    try {
      return preferences.getPreferencesSync(context, { name: actualStoreName });
    } catch (error) {
      hilog.error(DOMAIN, TAG, `Failed to get preferences sync: ${error}`);
      throw new Error(`Failed to get preferences sync: ${error}`);
    }
  }

  private static updateStoreCache(storeName: string, store: preferences.Preferences): void {
    if (!PreferenceUtil.cachedPreferences.has(storeName)) {
      PreferenceUtil.cachedPreferences.set(storeName, store);
    }
  }
}
```
