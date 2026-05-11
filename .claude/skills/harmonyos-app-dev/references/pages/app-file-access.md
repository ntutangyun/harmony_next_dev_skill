# 应用文件访问(ArkTS)

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-access_

在对应用文件开始访问前，开发者需要获取应用文件路径。以从UIAbilityContext获取HAP级别的文件路径为例进行说明，UIAbilityContext的获取方式请参见获取UIAbility的上下文信息。

下面介绍几种常用操作示例。

新建并读写一个文件

以下示例代码演示了如何新建一个文件并对其读写。

// pages/xxx.ets
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { buffer } from '@kit.ArkTS';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
function createFile(context: common.UIAbilityContext): void {
  let filesDir = context.filesDir;
  let file: fileIo.File | null = null;
  try {
    // 文件不存在时创建并打开文件，文件存在时打开文件
    file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    // 写入一段内容至文件
    let writeLen = fileIo.writeSync(file.fd, 'Hello world');
    console.info('The length of str is: ' + writeLen);
    // 创建一个大小为1024字节的ArrayBuffer对象，用于存储从文件中读取的数据
    let arrayBuffer = new ArrayBuffer(1024);
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: 0,
      length: arrayBuffer.byteLength
    };
    // 读取文件内容到ArrayBuffer对象中，并返回实际读取的字节数
    let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
    // 将ArrayBuffer对象转换为Buffer对象，并转换为字符串输出
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info('Succeeded in creating file, the content of file: ' + buf.toString());
  } catch (err) {
    console.error(`Failed to create file. Code: ${err.code}, message: ${err.message}`);
  } finally {
    if (file) {
      try {
        fileIo.closeSync(file);
      } catch (err) {
        console.error(`Failed to close file`);
      }
    }
  }
}
Index.ets
读取文件内容并写入到另一个文件

以下示例代码演示了如何从一个文件读写内容到另一个文件。

// pages/xxx.ets
import { fileIo, ReadOptions, WriteOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
function readWriteFile(context: common.UIAbilityContext): void {
  let srcFile: fileIo.File | null = null;
  let destFile: fileIo.File | null = null;
  try {
    let filesDir = context.filesDir;
    // 以读写的方式打开文件，文件不存在会新建文件
    srcFile = fileIo.openSync(filesDir + '/readFile.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    destFile = fileIo.openSync(filesDir + '/writeFile.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    // 创建缓冲区
    let bufSize = 4096;
    let buf = new ArrayBuffer(bufSize);
    let readOffset = 0;
    let readLength = 128;
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: readOffset,
      length: readLength
    };
    // 分次读取源文件内容并写入至目标文件
    let readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
    while (readLen > 0) {
      readOffset += readLen;
      let writeOptions: WriteOptions = {
        length: readLen
      };
      // 写入目标文件
      fileIo.writeSync(destFile.fd, buf, writeOptions);
      // 更新读取位置
      readOptions.offset = readOffset;
      readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
    }
    console.info(`Succeeded in reading and writing file.`);
  } catch (err) {
    console.error(`Failed to read and write File. Code: ${err.code}, message: ${err.message}`);
  } finally {
    try {
      if (srcFile) {
        fileIo.closeSync(srcFile);
      }
      if (destFile) {
        fileIo.closeSync(destFile);
      }
    } catch (closeErr) {
      console.error(`Failed to close file`);
    }
  }
}
Index.ets
说明

使用读写接口时，需注意可选项参数offset的设置。对于已存在且读写过的文件，文件偏移指针默认在上次读写操作的终止位置。

以流的形式读写文件

以下示例代码演示了如何使用流接口读取test.txt的文件内容并写入到destFile.txt文件中。

// pages/xxx.ets
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
async function readWriteFileWithStream(context: common.UIAbilityContext): Promise<void> {
  let filesDir = context.filesDir;
  let inputStream: fileIo.Stream | null = null;
  let outputStream: fileIo.Stream | null = null;
  try {
    // 创建并打开输入文件流
    inputStream = fileIo.createStreamSync(filesDir + '/test.txt', 'r+');
    // 创建并打开输出文件流
    outputStream = fileIo.createStreamSync(filesDir + '/destFile.txt', 'w+');
    let bufSize = 4096;
    let readSize = 0;
    let buf = new ArrayBuffer(bufSize);
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: readSize,
      length: bufSize
    };
    // 以流的形式读取源文件内容并写入到目标文件
    let readLen = await inputStream.read(buf, readOptions);
    readSize += readLen;
    while (readLen > 0) {
      const writeBuf = readLen < bufSize ? buf.slice(0, readLen) : buf;
      await outputStream.write(writeBuf);
      readOptions.offset = readSize;
      readLen = await inputStream.read(buf, readOptions);
      readSize += readLen;
    }
    console.info(`Succeeded in reading and writing file with stream.`);
  } catch (err) {
    console.error(`Failed to read and write file with stream. Code: ${err.code}, message: ${err.message}`);
  } finally {
    try {
      if (inputStream) {
        inputStream.closeSync();
      }
      if (outputStream) {
        outputStream.closeSync();
      }
    } catch (closeErr) {
      console.error(`Failed to close stream`);
    }
  }
}
Index.ets
说明

使用流接口时，需注意流的及时关闭。同时流的异步接口应严格遵循异步接口使用规范，避免同步、异步接口混用。流接口不支持并发读写。

查看文件列表

以下示例代码演示了如何查看文件列表。

import { fileIo, Filter, ListFileOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
function getListFile(context: common.UIAbilityContext): void {
  let listFileOption: ListFileOptions = {
    recursion: false,
    listNum: 0,
    filter: {
      suffix: ['.png', '.jpg', '.txt'],
      displayName: ['test*'],
      fileSizeOver: 0,
      lastModifiedAfter: new Date(0).getTime()
    }
  };
  let filesDir = context.filesDir;
  try {
    let files = fileIo.listFileSync(filesDir, listFileOption);
    for (let i = 0; i < files.length; i++) {
      console.info(`Succeeded in listing file, The name of file: ${files[i]}`);
    }
  } catch (err) {
    console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
  }
}
Index.ets
使用文件流

以下示例代码演示了如何使用文件可读流，文件可写流。

// pages/xxx.ets
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
function copyFileWithReadable(context: common.UIAbilityContext): void {
  try {
    let filesDir = context.filesDir;
    // 创建文件可读流
    const rs = fileIo.createReadStream(`${filesDir}/test.txt`);
    // 创建文件可写流
    const ws = fileIo.createWriteStream(`${filesDir}/destFile.txt`);
    // 暂停模式拷贝文件。在拷贝数据时，将原始数据暂停，然后将数据复制到另一个位置，适用于对数据完整性和一致性要求较高的场景
    rs.on('readable', () => {
      const data = rs.read();
      if (!data) {
        return;
      }
      ws.write(data);
    });


    rs.on('end', () => {
      ws.end();
      console.info(`Succeeded in copying file with read stream.`);
    });


    // 捕获异常
    rs.on('error', () => {
      rs.close();
      ws.close();
    });
  } catch (err) {
    console.error(`Failed to copy file with read stream. Code: ${err.code}, message: ${err.message}`);
  }
}
Index.ets
function copyFileWithData(context: common.UIAbilityContext): void {
  let filesDir = context.filesDir;


  try {
    // 创建文件可读流
    let rs = fileIo.createReadStream(`${filesDir}/test.txt`);
    // 创建文件可写流
    let ws = fileIo.createWriteStream(`${filesDir}/destFile.txt`);


    rs.push('Hello world');
    // 流动模式拷贝文件
    rs.on('data', (emitData) => {
      const data = emitData?.data;
      if (!data) {
        return;
      }
      ws.write(data as Uint8Array);
    });


    rs.on('end', () => {
      ws.end();
      console.info(`Succeeded in copying file with data.`);
    });


    // 捕获异常
    rs.on('error', () => {
      rs.close();
      ws.close();
    });
  } catch (err) {
    console.error(`Failed to copy file with data. Code: ${err.code}, message: ${err.message}`);
  }
}
Index.ets
使用文件哈希流

哈希流是一种数据传输和存储技术，可以将任意长度的数据转换为固定长度的哈希值来验证数据的完整性和一致性。以下代码演示了如何使用文件哈希处理接口（ohos.file.hash）来处理文件哈希流。

// pages/xxx.ets
import { fileIo } from '@kit.CoreFileKit';
import { hash } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 获取应用文件路径，请在组件内获取context
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;


function hashFileWithStream(context: common.UIAbilityContext) {
  try {
    let filesDir = context.filesDir;
    const filePath = `${filesDir}/test.txt`;
    // 创建文件可读流
    const rs = fileIo.createReadStream(filePath);
    // 创建哈希流
    const hs = hash.createHash('sha256');
    rs.on('data', (emitData) => {
      const data = emitData?.data;
      hs.update(new Uint8Array(data?.split('').map((x: string) => x.charCodeAt(0))).buffer);
    });
    rs.on('end', async () => {
      const hashResult = hs.digest();
      const fileHash = await hash.hash(filePath, 'sha256');
      console.info(`Succeeded in hashing file with stream, hash result: ${hashResult}, file hash: ${fileHash}`);
    });
  } catch (err) {
    console.error(`Failed to hash file with stream. Code: ${err.code}, message: ${err.message}`);
  }
}
Index.ets
应用文件访问与管理
应用文件访问(C/C++)

## Code blocks

### Code block 1

```
// pages/xxx.ets
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';
import { buffer } from '@kit.ArkTS';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

### Code block 2

```
function createFile(context: common.UIAbilityContext): void {
  let filesDir = context.filesDir;
  let file: fileIo.File | null = null;
  try {
    // 文件不存在时创建并打开文件，文件存在时打开文件
    file = fileIo.openSync(filesDir + '/test.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    // 写入一段内容至文件
    let writeLen = fileIo.writeSync(file.fd, 'Hello world');
    console.info('The length of str is: ' + writeLen);
    // 创建一个大小为1024字节的ArrayBuffer对象，用于存储从文件中读取的数据
    let arrayBuffer = new ArrayBuffer(1024);
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: 0,
      length: arrayBuffer.byteLength
    };
    // 读取文件内容到ArrayBuffer对象中，并返回实际读取的字节数
    let readLen = fileIo.readSync(file.fd, arrayBuffer, readOptions);
    // 将ArrayBuffer对象转换为Buffer对象，并转换为字符串输出
    let buf = buffer.from(arrayBuffer, 0, readLen);
    console.info('Succeeded in creating file, the content of file: ' + buf.toString());
  } catch (err) {
    console.error(`Failed to create file. Code: ${err.code}, message: ${err.message}`);
  } finally {
    if (file) {
      try {
        fileIo.closeSync(file);
      } catch (err) {
        console.error(`Failed to close file`);
      }
    }
  }
}
```

### Code block 3

```
// pages/xxx.ets
import { fileIo, ReadOptions, WriteOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

### Code block 4

```
function readWriteFile(context: common.UIAbilityContext): void {
  let srcFile: fileIo.File | null = null;
  let destFile: fileIo.File | null = null;
  try {
    let filesDir = context.filesDir;
    // 以读写的方式打开文件，文件不存在会新建文件
    srcFile = fileIo.openSync(filesDir + '/readFile.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    destFile = fileIo.openSync(filesDir + '/writeFile.txt', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
    // 创建缓冲区
    let bufSize = 4096;
    let buf = new ArrayBuffer(bufSize);
    let readOffset = 0;
    let readLength = 128;
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: readOffset,
      length: readLength
    };
    // 分次读取源文件内容并写入至目标文件
    let readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
    while (readLen > 0) {
      readOffset += readLen;
      let writeOptions: WriteOptions = {
        length: readLen
      };
      // 写入目标文件
      fileIo.writeSync(destFile.fd, buf, writeOptions);
      // 更新读取位置
      readOptions.offset = readOffset;
      readLen = fileIo.readSync(srcFile.fd, buf, readOptions);
    }
    console.info(`Succeeded in reading and writing file.`);
  } catch (err) {
    console.error(`Failed to read and write File. Code: ${err.code}, message: ${err.message}`);
  } finally {
    try {
      if (srcFile) {
        fileIo.closeSync(srcFile);
      }
      if (destFile) {
        fileIo.closeSync(destFile);
      }
    } catch (closeErr) {
      console.error(`Failed to close file`);
    }
  }
}
```

### Code block 5

```
// pages/xxx.ets
import { fileIo, ReadOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

### Code block 6

```
async function readWriteFileWithStream(context: common.UIAbilityContext): Promise<void> {
  let filesDir = context.filesDir;
  let inputStream: fileIo.Stream | null = null;
  let outputStream: fileIo.Stream | null = null;
  try {
    // 创建并打开输入文件流
    inputStream = fileIo.createStreamSync(filesDir + '/test.txt', 'r+');
    // 创建并打开输出文件流
    outputStream = fileIo.createStreamSync(filesDir + '/destFile.txt', 'w+');
    let bufSize = 4096;
    let readSize = 0;
    let buf = new ArrayBuffer(bufSize);
    // 设置读取的偏移量和长度，单位为Byte
    let readOptions: ReadOptions = {
      offset: readSize,
      length: bufSize
    };
    // 以流的形式读取源文件内容并写入到目标文件
    let readLen = await inputStream.read(buf, readOptions);
    readSize += readLen;
    while (readLen > 0) {
      const writeBuf = readLen < bufSize ? buf.slice(0, readLen) : buf;
      await outputStream.write(writeBuf);
      readOptions.offset = readSize;
      readLen = await inputStream.read(buf, readOptions);
      readSize += readLen;
    }
    console.info(`Succeeded in reading and writing file with stream.`);
  } catch (err) {
    console.error(`Failed to read and write file with stream. Code: ${err.code}, message: ${err.message}`);
  } finally {
    try {
      if (inputStream) {
        inputStream.closeSync();
      }
      if (outputStream) {
        outputStream.closeSync();
      }
    } catch (closeErr) {
      console.error(`Failed to close stream`);
    }
  }
}
```

### Code block 7

```
import { fileIo, Filter, ListFileOptions } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

### Code block 8

```
function getListFile(context: common.UIAbilityContext): void {
  let listFileOption: ListFileOptions = {
    recursion: false,
    listNum: 0,
    filter: {
      suffix: ['.png', '.jpg', '.txt'],
      displayName: ['test*'],
      fileSizeOver: 0,
      lastModifiedAfter: new Date(0).getTime()
    }
  };
  let filesDir = context.filesDir;
  try {
    let files = fileIo.listFileSync(filesDir, listFileOption);
    for (let i = 0; i < files.length; i++) {
      console.info(`Succeeded in listing file, The name of file: ${files[i]}`);
    }
  } catch (err) {
    console.error(`Failed to list file. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### Code block 9

```
// pages/xxx.ets
import { fileIo } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
```

### Code block 10

```
function copyFileWithReadable(context: common.UIAbilityContext): void {
  try {
    let filesDir = context.filesDir;
    // 创建文件可读流
    const rs = fileIo.createReadStream(`${filesDir}/test.txt`);
    // 创建文件可写流
    const ws = fileIo.createWriteStream(`${filesDir}/destFile.txt`);
    // 暂停模式拷贝文件。在拷贝数据时，将原始数据暂停，然后将数据复制到另一个位置，适用于对数据完整性和一致性要求较高的场景
    rs.on('readable', () => {
      const data = rs.read();
      if (!data) {
        return;
      }
      ws.write(data);
    });


    rs.on('end', () => {
      ws.end();
      console.info(`Succeeded in copying file with read stream.`);
    });


    // 捕获异常
    rs.on('error', () => {
      rs.close();
      ws.close();
    });
  } catch (err) {
    console.error(`Failed to copy file with read stream. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### Code block 11

```
function copyFileWithData(context: common.UIAbilityContext): void {
  let filesDir = context.filesDir;


  try {
    // 创建文件可读流
    let rs = fileIo.createReadStream(`${filesDir}/test.txt`);
    // 创建文件可写流
    let ws = fileIo.createWriteStream(`${filesDir}/destFile.txt`);


    rs.push('Hello world');
    // 流动模式拷贝文件
    rs.on('data', (emitData) => {
      const data = emitData?.data;
      if (!data) {
        return;
      }
      ws.write(data as Uint8Array);
    });


    rs.on('end', () => {
      ws.end();
      console.info(`Succeeded in copying file with data.`);
    });


    // 捕获异常
    rs.on('error', () => {
      rs.close();
      ws.close();
    });
  } catch (err) {
    console.error(`Failed to copy file with data. Code: ${err.code}, message: ${err.message}`);
  }
}
```

### Code block 12

```
// pages/xxx.ets
import { fileIo } from '@kit.CoreFileKit';
import { hash } from '@kit.CoreFileKit';
import { common } from '@kit.AbilityKit';


// 获取应用文件路径，请在组件内获取context
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;


```

### Code block 13

```
function hashFileWithStream(context: common.UIAbilityContext) {
  try {
    let filesDir = context.filesDir;
    const filePath = `${filesDir}/test.txt`;
    // 创建文件可读流
    const rs = fileIo.createReadStream(filePath);
    // 创建哈希流
    const hs = hash.createHash('sha256');
    rs.on('data', (emitData) => {
      const data = emitData?.data;
      hs.update(new Uint8Array(data?.split('').map((x: string) => x.charCodeAt(0))).buffer);
    });
    rs.on('end', async () => {
      const hashResult = hs.digest();
      const fileHash = await hash.hash(filePath, 'sha256');
      console.info(`Succeeded in hashing file with stream, hash result: ${hashResult}, file hash: ${fileHash}`);
    });
  } catch (err) {
    console.error(`Failed to hash file with stream. Code: ${err.code}, message: ${err.message}`);
  }
}
```
