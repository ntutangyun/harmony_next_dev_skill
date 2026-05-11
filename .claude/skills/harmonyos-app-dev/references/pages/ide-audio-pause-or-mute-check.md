# @correctness/audio

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-audio-pause-or-mute-check_

player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
          console.info('Succeeded');
        });
        player.on('audioOutputDeviceChangeWithInfo', ()=>{
          console.error(`createAVPlayer audioOutputDeviceChangeWithInfo`);
        });
        console.info('Succeeded in creating AVPlayer.');
      } else {
        console.error(`Failed to create AVPlayer, error message:${error.message}`);
      }
    });
    audio.createAudioRenderer(audioRendererOptions,(err, audioRenderer: audio.AudioRenderer) => {
      if (err) {
        console.error(`AudioRenderer Created: Error: ${err}`);
      } else {
        audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
          console.info('Succeeded');
        });
        audioRenderer.on('outputDeviceChangeWithInfo', ()=>{
          console.error(`createAudioRenderer outputDeviceChangeWithInfo`);
        })
        console.info('AudioRenderer Created: Success: SUCCESS');
      }
    });
  }
}
反例
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
let audioStreamInfo1: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_44100,
  channels: audio.AudioChannel.CHANNEL_1,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION,
  rendererFlags: 0
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo1,
  rendererInfo: audioRendererInfo
};
function demoCallBack() {
  // warning line
  media.createAVPlayer((error: BusinessError, player: media.AVPlayer) => {
    if (player != null) {
      player.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
        console.info('Succeeded');
      });
      console.info('Succeeded in creating AVPlayer.');
    } else {
      console.error(`Failed to create AVPlayer, error message:${error.message}`);
    }
  });
  // warning line
  audio.createAudioRenderer(audioRendererOptions,(err, audioRenderer: audio.AudioRenderer) => {
    if (err) {
      console.error(`AudioRenderer Created: Error: ${err}`);
    } else {
      audioRenderer.on('audioInterrupt', (interruptEvent: audio.InterruptEvent)=>{
        console.info('Succeeded');
      });
      console.info('AudioRenderer Created.');
    }
  });
}
规则集
plugin:@correctness/all

Code Linter代码检查规则的配置指导请参考Code Linter代码检查。

@correctness/audio-interrupt-check
@correctness/avsession-metadata-check
