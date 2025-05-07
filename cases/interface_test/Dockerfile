# 使用 Python 3.9 作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/ &&  \
    pip config set install.trusted-host mirrors.aliyun.com &&  \
    pip install -r requirements.txt

# 复制项目文件
COPY . .

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 设置容器启动命令
CMD ["sleep","infinity"]
