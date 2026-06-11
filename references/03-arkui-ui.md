# ArkUI: layouts, components, navigation, animation

Source pages:
- arkui-overview, arkts-layout-development-overview
- arkts-layout-development-create-list, arkts-layout-development-create-grid, arkts-layout-development-stack-layout
- arkts-common-components-button, arkts-common-components-text-display, arkts-common-components-text-input
- arkts-graphics-display, arkts-navigation-tabs
- arkts-navigation-introduction, arkts-navigation-navigation, arkts-set-navigation-routing, arkts-router-to-navigation
- arkts-use-animation, arkts-animation, arkts-animation-attribute
- arkts-interaction-development-guide-overview

## Layouts — pick by purpose

| Layout | When to reach for it |
|---|---|
| **Column / Row** (linear) | Vertical / horizontal stack of children. Default first choice. |
| **Stack** | Children overlap (z-stack). Useful for floating elements, panel-over-content. |
| **Flex** | Like linear, but children stretch/compress via `flexGrow` / `flexShrink`. Use when you need ratio-based fill. |
| **RelativeContainer** | 2D anchor-based positioning — pin child A to right-edge of child B, etc. Use when nesting linear layouts gets too deep. |
| **GridRow / GridCol** (栅格) | Responsive grid spanning multiple device sizes. Use when same content needs different layouts per device. |
| **List / Grid / WaterFlow** | Vertically scrolling collections. |
| **Tabs** | In-page section switching with a tab bar. |
| **Swiper** | Carousel / paged horizontal scroller. |
| **Scroll** | Plain scrollable container (1D). |
| **DynamicLayout** (API 24+) | Switch layout algorithm at runtime, preserving child state. Use for responsive landscape/portrait. |

Container components take children inside a trailing `() { }` block:

```typescript
Column({ space: 8 }) {                  // optional params
  Text('A')
  Text('B')
}
.width('100%')                          // chainable attributes apply to the container
.padding(16)
.alignItems(HorizontalAlign.Start)
```

### Sizing & box model

Every component has 4 nested regions: **margin → border → content area → content**. Set with:
- `.width(<num | '<n>%' | '<n>vp'>)` / `.height(...)`
- `.margin({ top, bottom, left, right })`, `.padding(...)`, `.border(...)`
- `.alignContent(...)` / `.alignItems(...)` — alignment of children inside the container.

Units: numbers are `vp` (virtual pixels). Strings can be `'<n>%'`, `'<n>vp'`, `'<n>px'`, `'<n>fp'` (font px), `'<n>lpx'` (logical px). Prefer `vp` and percentages for cross-device behaviour.

### Filling / stretching / hiding

- `flexGrow` / `flexShrink` — children of Flex grow/shrink with the container.
- `layoutWeight(n)` — child claims `n / total-weight` of remaining space (linear containers).
- `aspectRatio(width/height)` — preserve a ratio while scaling.
- `displayPriority(n)` — hide low-priority siblings when the container shrinks.

### Absolute & relative positioning

- `position({ x, y })` — absolute, doesn't affect siblings' layout.
- `offset({ x, y })` — relative, doesn't reflow either.

## Lists & grids

`List` is the workhorse for vertical scroll:

```typescript
List({ space: 8 }) {
  ForEach(this.items, (item: Item) => {
    ListItem() {
      Row() {
        Text(item.title).fontSize(16)
      }
    }
  }, (item: Item) => item.id)
}
.divider({ strokeWidth: 1, color: '#eee' })
.onScrollIndex((first, last) => { /* ... */ })
```

For very long lists, swap `ForEach` → `LazyForEach` + an `IDataSource` implementation; this lazily mounts items in the viewport only and reuses them as you scroll.

`Grid` uses `columnsTemplate`/`rowsTemplate`:

```typescript
Grid() {
  ForEach(this.cells, (c: Cell) => {
    GridItem() { Image(c.url).width('100%').aspectRatio(1) }
  }, (c: Cell) => c.id)
}
.columnsTemplate('1fr 1fr 1fr')       // 3-column grid like CSS grid
.columnsGap(8).rowsGap(8)
```

`WaterFlow` is the Pinterest-style staggered grid.

## Common components

| Component | Typical use |
|---|---|
| `Text` | Plain text. Compose with `Span` for inline formatting. |
| `Span` | Inline run inside a Text. |
| `TextInput` / `TextArea` | Single-line / multi-line text entry. |
| `Search` | Search-styled input with icon. |
| `RichEditor` | Rich text editor with mixed inline content. |
| `Button` | Action button. `.type(ButtonType.Capsule | Normal | Circle)`. |
| `Toggle` | Toggleable switch / checkbox / button. |
| `Slider`, `Rating` | Numeric inputs. |
| `Radio`, `Checkbox` | Selection. |
| `Image` | Image. Source via `$r('app.media.icon')`, file URL, or PixelMap. |
| `Video` | Video playback (uses Media Kit underneath). |
| `WebView` from `@ohos.web.webview` | Embedded web content. |
| `SymbolGlyph`, `SymbolSpan` | Vector icon symbols. |
| `XComponent` | Native rendering surface (NDK, Canvas, GPU). |
| `Canvas` | 2D drawing API. |

### Pattern: text + input

```typescript
Column({ space: 16 }) {
  Text('Username').fontSize(14).fontColor('#666')
  TextInput({ placeholder: 'enter…', text: this.username })
    .type(InputType.Normal)
    .onChange((value: string) => { this.username = value })
    .height(48).width('100%')
}
.padding(16)
```

## Navigation between pages

Two systems coexist; **prefer `Navigation`** for new code.

### Navigation (recommended)

`Navigation` is the modern stateful router. It owns a stack and renders `NavDestination` children. Define a `NavPathStack` and `NavDestination`s:

```typescript
@Entry @Component
struct Root {
  @State pathStack: NavPathStack = new NavPathStack();

  build() {
    Navigation(this.pathStack) {
      // Home content
      Column() {
        Button('Go to detail')
          .onClick(() => { this.pathStack.pushPath({ name: 'Detail', param: { id: 42 } }) })
      }
    }
    .title('Home')
    .navDestination(this.navMap)        // resolver Builder
  }

  @Builder
  navMap(name: string, param: object) {
    if (name === 'Detail') {
      DetailPage({ id: (param as { id: number }).id })
    }
  }
}
```

For lazier registration, declare a **router_map.json** at `entry/src/main/resources/base/profile/router_map.json`, point `module.json5 → "routerMap": "$profile:router_map"`, and let the framework resolve `pushPath({ name: 'Detail' })` to a file:

```json
{
  "routerMap": [
    {
      "name": "Detail",
      "pageSourceFile": "src/main/ets/pages/Detail.ets",
      "buildFunction": "DetailBuilder",
      "data": { "description": "Detail page" }
    }
  ]
}
```

Stack ops: `pushPath`, `pushPathByName`, `pop`, `popToName`, `clear`, `replacePath`, `removeByName`. Read parameters in destinations via the stack.

### Legacy router (still works)

```typescript
const router = this.getUIContext().getRouter();
router.pushUrl({ url: 'pages/Second', params: { id: 42 } });
router.back();
router.replaceUrl({ url: 'pages/Login' });
router.getParams() as { id: number };
```

When migrating from `router` to `Navigation`: every former `pages/Foo` URL becomes a Navigation destination. Page state inside a NavDestination survives stack pushes/pops, so refactor with care.

## Tabs

```typescript
@Entry @Component
struct Page {
  @State index: number = 0;
  private controller: TabsController = new TabsController();

  build() {
    Tabs({ barPosition: BarPosition.Start, index: this.index, controller: this.controller }) {
      TabContent() { /* home tab */ }
        .tabBar('Home')
      TabContent() { /* profile tab */ }
        .tabBar('Profile')
    }
    .onChange((index: number) => { this.index = index })
  }
}
```

## Animation

Three patterns:

1. **Attribute animation** — wrap an attribute change in `animateTo`:
   ```typescript
   animateTo({ duration: 300, curve: Curve.Ease }, () => {
     this.offsetX = 100;       // any animatable attr you change in here will animate
   });
   ```

2. **Animation on a specific component**:
   ```typescript
   Text('Hi').opacity(this.opacity)
     .animation({ duration: 300, curve: Curve.Linear })   // every change of any animatable attr animates
   ```

3. **Transitions** — `pageTransition`, `transition` modifier, `NavDestination` transitions, `Geometry transitions` (shared element).

Plus `keyframeAnimation`, `springMotion`, and physics-based curves.

## Gestures & touch

Bind directly:

```typescript
Text('Tap')
  .onClick((e: ClickEvent) => { /* tap */ })
  .gesture(
    LongPressGesture({ repeat: false })
      .onAction(() => { /* long-press */ })
  )
```

For complex pipelines combine `PriorityGesture`, `ParallelGesture`, `GestureGroup`.

## Customising components

- `@Reusable` declared on a `@Component` lets `LazyForEach` recycle it; implement `aboutToReuse(params)` to receive new bindings.
- `@Component({ freezeWhenInactive: true })` (V2) freezes off-screen subtrees.
- `@Watch` triggers callbacks on state writes.
- `@Builder` and `@BuilderParam` (see `references/02-arkts-language.md`) compose UI snippets.

## Building ArkUI from C/C++ (ArkUI-NDK)

When you need to construct the UI tree from native code (`ArkUI_NodeHandle` via `arkui/native_node.h`), the C-API now mirrors most of the declarative surface. Recently expanded native-side guides (see `references/pages/<slug>.md`):

- Layout: `ndk-layout-container` (使用布局组件), `ndk-common-attribute-layout` (设置通用布局属性).
- Collections: `arkts-list-and-grid-ndk` (使用列表与网格).
- Containers & nav: `ndk-swiper` (Swiper 滑块视图), `ndk-navigation-query` (导航类组件).
- Components: `ndk-use-text-component` (Text), `ndk-build-form-components` (表单组件), `arkts-build-media-ndk` (媒体展示).
- Events/input: `ndk-add-component-events` (添加事件监听), `ndk-add-event-response` (添加事件响应), `ndk-bind-input-events` (绑定基础输入事件).

Mount native nodes inside ArkUI through an `XComponent`'s `NodeContent`. See also the NDK overview in `references/10-kits-catalog.md`.

## Beyond this page

For graphics (Canvas, Image processing, ArkGraphics2D/3D, XComponent, GPU/WebGL): `references/10-kits-catalog.md`.
For window management, status bar, splash screen: `references/04-ability-and-lifecycle.md`.
