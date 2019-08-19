FROM python:3.7-alpine

# 基于node镜像 ，如果基于刚才的镜像则 FROM ryzebo/docker-nodejs-test:0.1


MAINTAINER yuswift <bjliyu@foxmail.com>
# 作者信息

RUN mkdir -p /app/AutoBeijingEntry
#RUN mkdir /app && cd /app && git clone git@github.com:yuswift/AutoBeijingEntry.git

WORKDIR /app/AutoBeijingEntry

COPY /Users/swift/job/py_repo/AutoBeijingEntry/main.py .

COPY /Users/swift/job/py_repo/AutoBeijingEntry/config.yaml .

# 设定初始目录

RUN pip3 install -r requirements.txt

CMD ["python3","main.py"]
