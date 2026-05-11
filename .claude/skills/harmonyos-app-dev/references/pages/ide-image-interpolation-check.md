# @correctness/image

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-image-interpolation-check_

private mInterpolation: ImageInterpolation = ImageInterpolation.None;


  aboutToAppear(): void {
    this.mInterpolation = ImageInterpolation.Medium;
  }


  @Builder
  overlayIcon() {
    Image(this.icon)
      .height(this.iconSize * ADAPTIVE_SCALE)
      .width(this.iconSize * ADAPTIVE_SCALE)
      .interpolation(ImageInterpolation.Medium)
  }


  @Builder
  overlayIcon1() {
    Image(this.icon)
      .height(this.iconSize * ADAPTIVE_SCALE)
      .width(this.iconSize * ADAPTIVE_SCALE)
      .interpolation(this.mInterpolation)
  }


  build() {
    Column() {
      this.overlayIcon();
      this.overlayIcon1();
      Image($r('app.media.pause'))
        .draggable(false)
        .interpolation(ImageInterpolation.Medium)
    }
  }
}
反例
const ADAPTIVE_SCALE = 1.5;


@Component
export struct AppIcon {
  @State icon: string | PixelMap = '';
  @Prop iconSize: number = 1;
  private mInterpolation: ImageInterpolation = ImageInterpolation.Medium;


  aboutToAppear(): void {
    this.mInterpolation = ImageInterpolation.None;
  }


  @Builder
  overlayIcon() {
    Image(this.icon)
      .height(this.iconSize * ADAPTIVE_SCALE)
      .width(this.iconSize * ADAPTIVE_SCALE)
      // warning
      .interpolation(ImageInterpolation.None)
  }


  @Builder
  overlayIcon1() {
    Image(this.icon)
      .height(this.iconSize * ADAPTIVE_SCALE)
      .width(this.iconSize * ADAPTIVE_SCALE)
      // warning
      .interpolation(this.mInterpolation)
  }


  build() {
    Column() {
      this.overlayIcon();
      this.overlayIcon1();
      Image($r('app.media.pause'))
        .draggable(false)
        // warning
        .interpolation(ImageInterpolation.None)
    }
  }
}
规则集
plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@correctness/image-pixel-format-check
@correctness/listen-default-network-change
