# ArkTS language: decorators, state management, builders

Source pages:
- arkts-get-started, arkts-basic-syntax-overview, arkts-decorator-overview
- arkts-declarative-ui-description, arkts-state-management, arkts-state-management-overview
- arkts-state, arkts-prop, arkts-link, arkts-provide-and-consume, arkts-observed-and-objectlink
- arkts-localstorage, arkts-appstorage, arkts-environment, arkts-persiststorage
- arkts-watch, arkts-builder, arkts-builderparam, arkts-extend
- arkts-rendering-control-overview, arkts-rendering-control-ifelse, arkts-rendering-control-foreach, arkts-rendering-control-lazyforeach

## What ArkTS is

ArkTS is **TypeScript + UI decorators + a stricter type system**. You write `.ets` files (not `.ts`), they compile via the ArkCompiler to bytecode (`.abc`) and run in the ArkTS runtime. Highlights:

- Standard TS syntax (let/const, classes, generics, async/await, modules).
- Stricter than TS: no `any` in many places, structural-typing rules are tightened, restricted `Object` usage.
- UI is **declarative** via `@Component` structs and a `build()` method.
- State is wired with **decorators** that the compiler/runtime use to observe writes and re-render.

The page anatomy:

```typescript
@Entry                                  // Mark this as a routable page (only one @Entry per file)
@Component                              // Mark as a custom component
struct MyPage {                         // 'struct' is the ArkTS keyword for a component
  @State counter: number = 0;           // mutable state — writes re-render UI

  build() {                             // mandatory; describes the UI tree
    Column() {                          // Container components take a trailing arrow block of children
      Text(`Count: ${this.counter}`)
        .fontSize(20)                   // Attribute methods chain on the component
      Button('Add')
        .onClick(() => { this.counter++; })  // Event methods chain too
    }
  }
}
```

## Decorator cheat sheet

| Decorator | What it does | Where |
|---|---|---|
| `@Entry` | Marks the component as the page's entry; needed to be addressable via routing. **Exactly one per file.** | Component decl |
| `@Component` | Declares a custom component (a `struct`). | Component decl |
| `@Reusable` | Marks a custom component as reuse-eligible (recycling, like RecyclerView). | Component decl |
| `@State` | Local mutable state. Writes trigger re-render of the component. | Member var |
| `@Prop` | Read-only copy of a parent's value. Updates **only when parent re-renders** (one-way down). | Member var |
| `@Link` | Two-way bound to a parent's `@State`/`@Link`/etc. Use the `$var` sugar at the call site. | Member var |
| `@Provide` / `@Consume` | Cross-level binding (skip intermediate components). Consume reads, both write. | Member var |
| `@ObjectLink` / `@Observed` | Track changes inside nested objects. `@Observed` on the class, `@ObjectLink` on the var. | Class / member var |
| `@StorageLink` / `@StorageProp` | Two-way / one-way binding to `AppStorage`. | Member var |
| `@LocalStorageLink` / `@LocalStorageProp` | Two-way / one-way binding to a scoped `LocalStorage`. | Member var |
| `@Watch('handler')` | Calls `handler` when the decorated value changes. | After another state decorator |
| `@Builder` | Reusable UI snippet (a method that returns UI). | Method |
| `@BuilderParam` | Accepts a `@Builder` from a parent — like a UI prop. | Member |
| `@Extend(Component)` / `@Styles` | Reusable attribute groups. `@Extend` is per-component-type; `@Styles` is generic. | Function |
| `@Require` | Marks a member as required for initialization from parent. | Member var |
| `@Track` | Restricts which class properties trigger UI updates (perf). | Member var |
| `@Concurrent` | Marks a function as runnable on a TaskPool/Worker (V1). | Function |
| `@Sendable` | Class can cross thread boundaries (Worker/TaskPool). | Class |
| (V2) `@ObservedV2`, `@Trace`, `@ComponentV2`, `@Local`, `@Param`, `@Event`, `@Provider`, `@Consumer`, `@Monitor`, `@Once` | V2 state management — more granular, less magic. | Various |

**V1 vs V2**: V2 (introduced for newer apps) decouples observation from the framework's heuristics. If the user is starting fresh and targets API 12+ with appropriate releases, V2 (`@ObservedV2 + @Trace`) is cleaner; otherwise stay on V1 (`@Observed + @ObjectLink`).

## State decorator semantics in plain English

- `@State foo: T` lives **in the component**. Reassign (`this.foo = x`) and changes to direct fields (`this.foo.bar = 1` for objects) trigger re-render. Array/object **internal mutations like `arr.push()`** only re-render if the variable was reassigned, or if elements are `@Observed`. Supports primitive types, classes, Date (API 10+), Map/Set/null/undefined (API 11+). Must be initialized locally.

- `@Prop foo: T` — child reads a one-way snapshot. Modifying it locally is permitted but the next parent re-render overwrites it. Pass with `foo: this.parentFoo`.

- `@Link foo: T` — child shares the parent's storage. Pass with `foo: $parentFoo` (the `$` sugar gives you the writable handle). Both sides can write.

- `@Provide` / `@Consume` — `@Provide`d on an ancestor, `@Consume`d on any descendant (matched by variable name or alias). Use to skip prop drilling through intermediate components.

- `@Observed class X {}` + `@ObjectLink foo: X` — enables observing **nested property** writes. The bare `@State` of a class can observe top-level reassignment and one-level property writes; deeper writes need `@Observed`.

- `LocalStorage` — page-scope key/value store. Bound at entry time:
  ```typescript
  const ls = new LocalStorage({ count: 0 });
  // Then:
  @Entry(ls)
  @Component
  struct Page {
    @LocalStorageLink('count') count: number = 0;   // two-way
    @LocalStorageProp('count') readonly readCount: number = 0;  // one-way
    build() { /* ... */ }
  }
  ```

- `AppStorage` — singleton across the app. Set: `AppStorage.setOrCreate('key', value)`. Bind in any component via `@StorageLink('key') foo: T = default;` (two-way) or `@StorageProp` (one-way). Pair with `PersistentStorage.persistProp('key', default)` to write through to disk.

- `Environment` — read-only system info exposed through AppStorage: `Environment.envProp('languageCode', 'en');`, then `@StorageProp('languageCode') lang: string = 'en';`.

## Triggers that DON'T re-render

These trip people up:

- Mutating nested objects without `@Observed`. Wrap nested types: `@Observed class Item {...}` and inject via `@ObjectLink`.
- Array methods like `.sort()` in-place — assign the result back (`this.list = [...this.list]`) or use `@Observed` on items.
- Adding/removing keys from a plain `Object` — frameworks observe known keys only. Use `Map` (API 11+) or replace the whole object.
- Mutating without an `@State`/`@Prop`/`@Link` wrapper at all — re-renders only happen on observed writes.

## Builders, ExtendCommands, Styles

`@Builder` is a reusable UI snippet that returns nothing but emits components:

```typescript
@Builder
function PillButton(label: string, onTap: () => void) {
  Button(label)
    .type(ButtonType.Capsule)
    .height(40)
    .onClick(onTap);
}

@Entry @Component
struct Page {
  build() {
    Column() {
      PillButton('Save', () => {});
      PillButton('Cancel', () => {});
    }
  }
}
```

`@BuilderParam` lets a parent pass a Builder into a child (like a slot/render prop):

```typescript
@Component
struct Container {
  @BuilderParam content: () => void = noop;
  build() { Column() { this.content() } }
}

@Builder function noop() {}

@Entry @Component
struct Page {
  build() {
    Container({ content: () => { Text('I am injected') } });
  }
}
```

`@Extend(Component)` packages attribute calls for one specific component type:

```typescript
@Extend(Text) function headline(size: number) {
  .fontSize(size).fontWeight(FontWeight.Bold)
}

// usage: Text('Title').headline(24)
```

`@Styles` packages attributes that apply to **any** component (generic styles).

## Rendering control

In `build()`, use these constructs (do not call them outside `build`):

- `if (cond) { ... } else { ... }` — conditional rendering. Whole subtree mounts/unmounts.
- `ForEach(arr, (item, index) => { ... }, keyGenerator?)` — render a list. Provide a stable `keyGenerator` for diff stability:
  ```typescript
  ForEach(this.items,
    (item: Item) => { ItemView({ item }) },
    (item: Item) => item.id        // key generator
  )
  ```
- `LazyForEach(dataSource, (item) => {...}, keyGen)` — render only on-demand for large lists. Backed by an `IDataSource` instance you implement (manages listeners + `getData(index)` + `totalCount()`).
- `Repeat(arr).each((item, index) => {...}).key(...).template(...)` — V2-style repeat that supports template polymorphism.

## Code style guidelines (when generating)

- Each page is a separate `.ets` file in `entry/src/main/ets/pages/` and registered in `main_pages.json`.
- Import SDK from `@kit.*` packages (e.g. `@kit.AbilityKit`, `@kit.ArkUI`, `@kit.BasicServicesKit`, `@kit.NetworkKit`, `@kit.MediaKit`). The older `@ohos.*` form still works but is being phased out.
- Avoid `any` and `Object` types — use specific interfaces.
- Components named `PascalCase struct`. Methods and state vars are `camelCase`. Module names lowercase with hyphen.

## Beyond this page

- For state-management edge cases (V2 decorators, Map/Set observation): visit the source pages listed at top.
- For ArkUI components and layouts: `references/03-arkui-ui.md`.
