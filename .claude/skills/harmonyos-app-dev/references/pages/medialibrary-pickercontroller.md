# 使用PickerController将编辑后的图片替换原图

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/medialibrary-pickercontroller_

-save as new:--------------------------------------------");
              let replaceUris: Array<string> = [];
              this.EditedUris.forEach((uri: string) => {
                replaceUris.push(uri);
              });
              // 将编辑后的图片uri数组通过saveTrustedPhotoAssets保存到图库中，SaveMode = SAVE_AS为另存为。
              this.pickerController.saveTrustedPhotoAssets(replaceUris, (a, b) => {
                console.log("this.pickerController.save as new, res:" + b);
              }, undefined, SaveMode.SAVE_AS);
            }).margin(10)


            Button('覆盖保存').width('25%').height('50%').margin({ top: 10 }).onClick(() => {
              console.log("----save as overwrite:--------------------------------------------");
              let replaceUris: Array<string> = [];
              this.EditedUris.forEach((uri: string) => {
                replaceUris.push(uri);
              });
              // 将编辑后的图片uri数组通过saveTrustedPhotoAssets保存到图库中，SaveMode = OVERWRITE为覆盖保存。
              this.pickerController.saveTrustedPhotoAssets(replaceUris, (a, b) => {
                console.log("this.pickerController.save override, res:" + b)
              }, undefined, SaveMode.OVERWRITE);
            }).margin(10)


            Button('Replace Url').width('25%').height('50%').margin({ top: 10 }).onClick(() => {
              // 模拟构造应用后期编辑修改后的图片uri。
              let newLocal = this.originUrl.split('.');
              let mediaType = newLocal[newLocal.length - 1];
              let editUri = newLocal[0] + "EDITED." + mediaType;
              // 将编辑后的图片uri放到全局编辑数组中。
              this.EditedUris.push(editUri);
              // 可通过该接口，将photoPicker中用户勾选的图片替换为应用后期编辑修改后的图片。
              this.pickerController.replacePhotoPickerPreview(this.originUrl, editUri, (a, b) => {
                console.log("this.pickerController.replaceUrl code" + JSON.stringify(a) + ", res:" + JSON.stringify(b))
              })
            }).margin(10)
          }.width('100%').height('10%')


          Row() {
            ForEach(this.selectedUris, (uri: string) => {
              Image(uri).height('95%').width('20%').backgroundColor(this.allBackGroundColor).onClick(() => {
              })
            }, (uri: string) => JSON.stringify(uri))
          }.width('100%').height('15%')


          PhotoPickerComponent({
            pickerOptions: this.pickerOptions,
            onSelect: (uri: string): void => this.onSelect(uri),
            onItemClicked: (itemInfo: ItemInfo, clickType: ClickType): boolean => this.onItemClicked(itemInfo,
              clickType),
            onEnterPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onEnterPhotoBrowser(photoBrowserInfo),
            onExitPhotoBrowser: (photoBrowserInfo: PhotoBrowserInfo): boolean => this.onExitPhotoBrowser(photoBrowserInfo),
            onSelectedItemsDeleted: (baseItemInfos: Array<BaseItemInfo>): void => this.onSelectedItemsDeleted(baseItemInfos),
            pickerController: this.pickerController,
          }).height('87%')
            .width('100%')
            .backgroundColor('#F1F3F5')
        }.width('100%').height('100%')
      }
    }
  }
}
使用RecentPhoto组件获取最近一张图片
使用PhotoPicker推荐图片
