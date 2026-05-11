# 如何主动通过手势缩放变焦比

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-faq-14_

hilog.error(0x0001, TAG, `Failed to getZoom. Code: ${err.code}, message: ${err?.message}`);
    }
    return zoom;
  }


  /**
   * 设置变焦比。
   * @param {number} zoomRatio - 要设置的变焦比。
   */
  setZoom(zoomRatio: number): void {
    try {
      customScan.setZoom(zoomRatio);
      hilog.info(0x0001, TAG, `setZoom end, zoomRatio: ${zoomRatio}`);
    } catch (err) {
      hilog.error(0x0001, TAG, `Failed to setZoom. Code: ${err.code}, message: ${err?.message}`);
    }
  }


  /**
   * 处理捏合手势的开始事件，记录初始变焦比。
   */
  pinchGestureStart(): void {
    this.baseZoom = this.getZoom();
    this.zoomRatio = this.baseZoom;
    hilog.info(0x0001, TAG, `pinchGestureStart. baseZoom: ${this.baseZoom}`);
  }


  /**
   * 处理捏合手势的更新事件，根据手势缩放比例更新当前变焦比。
   * @param {number} scale - 当前捏合手势的缩放比例。
   */
  public pinchGestureUpdate(scale: number): void {
    hilog.info(0x0001, TAG, `pinchGestureUpdate. scale: ${scale}`);
    let tmpZoom: number = scale * this.baseZoom;
    if (scale > 1) {
      if (tmpZoom <= MAX_ZOOM_RATIO) {
        this.updateZoom(tmpZoom);
      }
    } else {
      if (tmpZoom < MIN_ZOOM_RATIO) {
        tmpZoom = MIN_ZOOM_RATIO;
      }
      this.updateZoom(tmpZoom);
    }
  }


  /**
   * 更新当前变焦比，如果变化大于阈值0.01则进行设置。
   * @param {number} tmpZoom - 临时计算的变焦比。
   */
  public updateZoom(tmpZoom: number): void {
    if (Math.abs(tmpZoom - this.zoomRatio) > 0.01) {
      hilog.info(0x0001, TAG, `updateZoom. tmpZoom: ${tmpZoom}`);
      this.zoomRatio = tmpZoom;
      this.setZoom(this.zoomRatio);
    }
  }
}
H5场景如何接入扫码
自定义界面扫码如何实现扫码框
