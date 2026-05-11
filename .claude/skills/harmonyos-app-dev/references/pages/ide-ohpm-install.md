# ohpm install

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-install_

default                   // <targetName>默认为default
|   |   dependencyMap.json5   // 记录在特定target语境下的各模块依赖配置文件路径
|   +---module1               // 在特定target语境下某模块的依赖配置文件的存储目录，与原模块根目录同名
|   |       oh-package.json5  // 在特定target语境下某模块依赖配置文件
|   +---module2
|   |       oh-package.json5
|   |   oh-package.json5      // 在特定target语境下生成的工程级依赖配置文件

dependencyMap.json5内容示例：

{
  targetName: "default",
  rootDependency: "./oh-package.json5",
  dependencyMap: {
       "module1": "./module1/oh-package.json5",
       "module2": "./module2/oh-package.json5"
  }
}

ohpm install指定target_path时依赖配置优先级说明：

1、<target_path>/dependencyMap.json5中rootDependency配置的oh-package.json5的优先级高于<project_root>/oh-package.json5。

2、.ohpmrc中projectPackageJson指定的项目级配置文件中overrides、overrideDependencyMap配置优先级同时高于<target_path>/dependencyMap.json5中rootDependency配置的oh-package.json5中对应配置 和 <project_root>/oh-package.json5中对应配置。

3、<target_path>/moduleName/oh-package.json5的优先级高于overrideDependencyMap中的依赖配置文件。

4、overrides中的依赖版本优先级高于<target_path>/moduleName/oh-package.json5中对应的依赖版本。

注意

仅当<target_path>/dependencyMap.json5中targetName的值不为空且不等于'default'时，<project_root>/moduleName目录下生成的lock文件名才会变更为：oh-package-targetName-lock.json5。

ohpm init
ohpm list
