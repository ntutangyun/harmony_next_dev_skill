# 用户相册资源使用指导

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoaccesshelper-useralbum-guidelines_

文档中使用到photoAccessHelper的地方默认为使用开发准备中获取的对象，如未添加此段代码报photoAccessHelper未定义的错误请自行添加。

为了保证应用的运行效率，大部分photoAccessHelper的接口调用都是异步的。以下异步调用的API示例均采用Promise函数，更多方式可以查阅模块描述。

如无特别说明，文档中涉及的待获取资源均视为已预置，并且数据库中存在相应数据。如果按照示例代码执行后获取资源为空，请确认文件是否已预置，以及数据库中是否存在该文件的数据。

获取用户相册

通过PhotoAccessHelper.getAlbums接口获取用户相册。

前提条件

获取相册管理模块photoAccessHelper实例。
申请相册管理模块功能相关权限'ohos.permission.READ_IMAGEVIDEO'。

下面以获取一个相册名为'albumName'的用户相册为例。

开发步骤

建立检索条件，用于获取用户相册。
调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
调用FetchResult.getFirstObject接口获取第一个用户相册。
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';


// ...


async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
  predicates.equalTo(albumName, 'test');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };


  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
        photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    fetchResult.close();
    // ...
  } catch (err) {
    console.error('getAlbums failed with err: ' + err);
    // ...
  }
}
GetUserAlbumAbility.ets
重命名用户相册

重命名用户相册时，修改的是相册的Album.albumName属性。

调用MediaAlbumChangeRequest.setAlbumName重命名用户相册后再通过PhotoAccessHelper.applyChanges更新到数据库中完成修改。

在重命名用户相册之前，需要先获取相册对象，可以通过FetchResult中的接口获取对应位置的用户相册。

重命名相册时，相册名的参数规格为：

相册名字符串长度为1~255。

不允许出现的非法英文字符，包括：

. \ / : * ? " ' ` < > | { } [ ]

英文字符大小写不敏感。
相册名不允许重名。

前提条件

获取相册管理模块photoAccessHelper实例。
申请相册管理模块功能相关权限'ohos.permission.READ_IMAGEVIDEO'和'ohos.permission.WRITE_IMAGEVIDEO'。

下面以将一个相册名为'albumName'的用户相册重命名为例。

开发步骤

建立检索条件，用于获取用户相册。
调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
调用FetchResult.getFirstObject接口获取第一个用户相册。
调用MediaAlbumChangeRequest.setAlbumName接口设置新的相册名。
调用PhotoAccessHelper.applyChanges接口将修改的相册属性更新到数据库中完成修改。
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';


// ...


async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
  predicates.equalTo(albumName, 'test');
  let fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: predicates
  };


  try {
    let fetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
        photoAccessHelper.AlbumSubtype.USER_GENERIC, fetchOptions);
    let album: photoAccessHelper.Album = await fetchResult.getFirstObject();
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest =
      new photoAccessHelper.MediaAlbumChangeRequest(album);
    let newAlbumName: string = 'newAlbumName';
    albumChangeRequest.setAlbumName(newAlbumName);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('setAlbumName successfully, new albumName: ' + album.albumName);
    fetchResult.close();
    // ...
  } catch (err) {
    console.error('setAlbumName failed with err: ' + err);
    // ...
  }
}
RenameUserAlbumAbility.ets
添加图片和视频到用户相册中

先获取用户相册对象和需要添加到用户相册中的图片或视频的对象数组，然后调用MediaAlbumChangeRequest.addAssets和PhotoAccessHelper.applyChanges接口往用户相册中添加图片或视频。

前提条件

获取相册管理模块photoAccessHelper实例。
申请相册管理模块功能相关权限'ohos.permission.READ_IMAGEVIDEO'和'ohos.permission.WRITE_IMAGEVIDEO'。

下面以将往相册名为'albumName'的用户相册中添加一张图片为例。

开发步骤

建立相册检索条件，用于获取用户相册。
建立图片检索条件，用于获取图片。
调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
调用FetchResult.getFirstObject接口获取第一个用户相册。
调用PhotoAccessHelper.getAssets接口获取图片资源。
调用FetchResult.getFirstObject接口获取第一张图片。
调用MediaAlbumChangeRequest.addAssets接口往用户相册中添加图片。
调用PhotoAccessHelper.applyChanges接口提交相册变更请求。
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
// ...


async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
  albumPredicates.equalTo(albumName, 'test');
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: albumPredicates
  };


  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };


  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
        photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    let photoFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.PhotoAsset> =
      await phAccessHelper.getAssets(photoFetchOptions);
    let photoAsset: photoAccessHelper.PhotoAsset = await photoFetchResult.getFirstObject();
    console.info('getAssets successfully, albumName: ' + photoAsset.displayName);
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest =
      new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.addAssets([photoAsset]);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('succeed to add ' + photoAsset.displayName + ' to ' + album.albumName);
    albumFetchResult.close();
    photoFetchResult.close();
    return true;
  } catch (err) {
    console.error('addAssets failed with err: ' + err);
    return false;
  }
}
AddMediaToUserAlbumAbility.ets
获取用户相册中的图片和视频

先获取用户相册对象，然后调用Album.getAssets接口获取用户相册中的图片资源。

前提条件

获取相册管理模块photoAccessHelper实例。
申请相册管理模块功能相关权限'ohos.permission.READ_IMAGEVIDEO'和'ohos.permission.WRITE_IMAGEVIDEO'。

下面以获取相册名为'albumName'的用户相册中的一张图片为例。

开发步骤

建立相册检索条件，用于获取用户相册。
建立图片检索条件，用于获取图片。
调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
调用FetchResult.getFirstObject接口获取第一个用户相册。
调用Album.getAssets接口获取用户相册中的图片资源。
调用FetchResult.getFirstObject接口获取第一张图片。
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';


// ...


async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
  albumPredicates.equalTo(albumName, 'test');
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: albumPredicates
  };


  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };


  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
        photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    let photoFetchResult = await album.getAssets(photoFetchOptions);
    let photoAsset = await photoFetchResult.getFirstObject();
    console.info('album getAssets successfully, albumName: ' + photoAsset.displayName);
    albumFetchResult.close();
    photoFetchResult.close();
    // ...
  } catch (err) {
    console.error('album getAssets failed with err: ' + err);
    // ...
  }
}
GetMediaFromUserAlbumAbility.ets
从用户相册中移除图片和视频

先获取用户相册对象，然后调用Album.getAssets接口获取用户相册中的资源。

选择其中要移除的资源，然后调用MediaAlbumChangeRequest.removeAssets和PhotoAccessHelper.applyChanges接口移除。

前提条件

获取相册管理模块photoAccessHelper实例。
申请相册管理模块功能相关权限'ohos.permission.READ_IMAGEVIDEO'和'ohos.permission.WRITE_IMAGEVIDEO'。

下面以从相册名为'albumName'的用户相册中移除一张图片为例。

开发步骤

建立相册检索条件，用于获取用户相册。
建立图片检索条件，用于获取图片。
调用PhotoAccessHelper.getAlbums接口获取用户相册资源。
调用FetchResult.getFirstObject接口获取第一个用户相册。
调用Album.getAssets接口获取图片资源。
调用FetchResult.getFirstObject接口获取第一张图片。
调用MediaAlbumChangeRequest.removeAssets接口从用户相册中移除图片。
调用PhotoAccessHelper.applyChanges接口提交相册变更请求。
import { dataSharePredicates } from '@kit.ArkData';
import { photoAccessHelper } from '@kit.MediaLibraryKit';


// ...


async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  let albumPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let albumName: photoAccessHelper.AlbumKeys = photoAccessHelper.AlbumKeys.ALBUM_NAME;
  albumPredicates.equalTo(albumName, 'test');
  let albumFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: albumPredicates
  };


  let photoPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
  let photoFetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [],
    predicates: photoPredicates
  };


  try {
    let albumFetchResult: photoAccessHelper.FetchResult<photoAccessHelper.Album> =
      await phAccessHelper.getAlbums(photoAccessHelper.AlbumType.USER,
        photoAccessHelper.AlbumSubtype.USER_GENERIC, albumFetchOptions);
    let album: photoAccessHelper.Album = await albumFetchResult.getFirstObject();
    if (album === undefined) {
      console.error('album is undefined');
      albumFetchResult.close();
      return false;
    }
    console.info('getAlbums successfully, albumName: ' + album.albumName);
    let photoFetchResult = await album.getAssets(photoFetchOptions);
    let photoAsset = await photoFetchResult.getFirstObject();
    if (photoAsset === undefined) {
      console.error('photoAsset is undefined');
      photoFetchResult.close();
      return false;
    }
    console.info('album getAssets successfully, albumName: ' + photoAsset.displayName);
    let albumChangeRequest: photoAccessHelper.MediaAlbumChangeRequest =
      new photoAccessHelper.MediaAlbumChangeRequest(album);
    albumChangeRequest.removeAssets([photoAsset]);
    await phAccessHelper.applyChanges(albumChangeRequest);
    console.info('succeed to remove ' + photoAsset.displayName + ' from ' + album.albumName);
    albumFetchResult.close();
    photoFetchResult.close();
    return true;
  } catch (err) {
    console.error('removeAssets failed with err: ' + err);
    return false;
  }
}
RemoveMediaFromUserAlbumAbility.ets
媒体资源使用指导
系统相册资源使用指导
