# 基于Dockerfile部署ohpm

_Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-dockerfile_

# 修改conf/config.yaml的listen配置，不能用localhost和127.0.0.1，必须使用0.0.0.0
RUN if [ -f /opt/ohpm-repo/conf/config.yaml ]; then \
      sed -i 's/listen: [^ ]*/listen: 0.0.0.0:8088/g' /opt/ohpm-repo/conf/config.yaml; \
    fi
ENV OHPM_REPO_BIN_DIR="/opt/ohpm-repo/bin"
ENV PATH="${OHPM_REPO_BIN_DIR}:${PATH}"
# 创建用户，不允许使用root用户来运行ohpm-repo install和ohpm-repo start命令
RUN useradd -m myuser && \
    chown -R myuser:myuser /opt/ohpm-repo && \ 
    chmod -R 755 /opt/ohpm-repo
USER myuser
RUN ohpm-repo install
ENV OHPM_REPO_DEPLOY_ROOT="/home/myuser/ohpm-repo"
CMD ["ohpm-repo", "start"]

搭建私仓服务

在当前Dockerfile文件目录下，构建镜像。
docker build -t ohpm-repo .
启动服务，包括前台运行命令、后台运行命令两种形式。
# 前台运行命令
docker run -it -p 8088:8088 ohpm-repo
# 后台运行命令
docker run -d --restart=unless-stopped --name ohpm-repo -p 8088:8088 ohpm-repo
浏览器访问IP地址8088，使用私仓服务。
模板文件
添加Ability
