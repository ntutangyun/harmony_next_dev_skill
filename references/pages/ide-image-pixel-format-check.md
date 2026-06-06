# @correctness/image

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-image-pixel-format-check_

const DEFAULT_IMAGE_BUFFER_SIZE: number = DEFAULT_IMAGE_WIDTH_HEIGHT * DEFAULT_IMAGE_WIDTH_HEIGHT * 4;
export class AodFailTask {
  private async setImage(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private async setImage1(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    const imageSrc = await image.createPixelMap(color, opts);
  }
  
  private setImage2() {
    // Original image size
    let width: number = 100;
    let height: number = 100;
    let buffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
    image.createPixelMap(buffer, {
      editable: false,
      pixelFormat: image.PixelMapFormat.RGBA_8888,
      size: { height: height, width: width }
    })
  }
  
}
反例
import image from '@ohos.multimedia.image';
const DEFAULT_IMAGE_WIDTH_HEIGHT: number = 600;
const DEFAULT_IMAGE_BUFFER_SIZE: number = DEFAULT_IMAGE_WIDTH_HEIGHT * DEFAULT_IMAGE_WIDTH_HEIGHT * 4;
export class AodFailTask {
  private async setImage(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    // warning
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private async setImage1(): Promise<void> {
    const color = new ArrayBuffer(DEFAULT_IMAGE_BUFFER_SIZE);
    let opts: image.InitializationOptions = {
      editable: true,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: DEFAULT_IMAGE_WIDTH_HEIGHT, width: DEFAULT_IMAGE_WIDTH_HEIGHT }
    }
    // warning
    const imageSrc = await image.createPixelMap(color, opts);
  }
  private setImage2() {
    // Original image size
    let width: number = 100;
    let height: number = 100;
    let buffer: ArrayBuffer = new ArrayBuffer(width * height * 4);
    // warning
    image.createPixelMap(buffer, {
      editable: false,
      pixelFormat: image.PixelMapFormat.RGB_565,
      size: { height: height, width: width }
    })
  }
}
规则集
plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@correctness/avsession-metadata-check
@correctness/image-interpolation-check
