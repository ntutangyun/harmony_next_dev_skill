# 添加图片区域

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-image_

添加图片区域通常用image组件来实现，使用的方法和text组件类似。

图片资源建议放在js\default\common目录下，common目录需自行创建，详细的目录结构见目录结构。代码示例如下：

<!-- xxx.hml -->
<image class="img" src="{{middleImage}}"></image>

/* xxx.css */
.img {
  margin-top: 30px;
  margin-bottom: 30px;
  height: 385px;
}

// xxx.js
export default {
  data: {
    middleImage: '/common/ice.png',
  },
}

## Code blocks

### Code block 1

```
<!-- xxx.hml -->
<image class="img" src="{{middleImage}}"></image>
```

### Code block 2

```
/* xxx.css */
.img {
  margin-top: 30px;
  margin-bottom: 30px;
  height: 385px;
}
```

### Code block 3

```
// xxx.js
export default {
  data: {
    middleImage: '/common/ice.png',
  },
}
```
