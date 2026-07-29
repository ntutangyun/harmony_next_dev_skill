# @compatibility/deprecate-api-check

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deprecate-api-check_

在开发中避免使用废弃的API接口。

规则配置

// code-linter.json5
{
  "rules": {
    "@compatibility/deprecate-api-check": "suggestion"
  }
}

选项

该规则无需配置额外选项。

正例

import media from '@ohos.multimedia.media';

function nonDeprecatedApi(): void {
  media.createAVPlayer().then((avPlayer) => {
    avPlayer.on('stateChange', () => {});
    avPlayer.play();
  });
}

反例

import { media } from '@kit.MediaKit';

function deprecatedApi(): void {
  let audioPlayer: media.AudioPlayer = media.createAudioPlayer ();
  audioPlayer.src = 'https://example.com/audio.mp3';
  audioPlayer.play ();
  audioPlayer.release ();
}

规则集

plugin:@compatibility/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

## Code blocks

### Code block 1

```
// code-linter.json5
{
  "rules": {
    "@compatibility/deprecate-api-check": "suggestion"
  }
}
```

### Code block 2

```
import media from '@ohos.multimedia.media';

function nonDeprecatedApi(): void {
  media.createAVPlayer().then((avPlayer) => {
    avPlayer.on('stateChange', () => {});
    avPlayer.play();
  });
}
```

### Code block 3

```
import { media } from '@kit.MediaKit';

function deprecatedApi(): void {
  let audioPlayer: media.AudioPlayer = media.createAudioPlayer ();
  audioPlayer.src = 'https://example.com/audio.mp3';
  audioPlayer.play ();
  audioPlayer.release ();
}
```

### Code block 4

```
plugin:@compatibility/all
```
