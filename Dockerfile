FROM python:3

MAINTAINER sangjing@leinao.ai

ARG GIT_PROJECT_PATH=/data/project
ARG TIME=5

ENV GIT_PROJECT_PATH $GIT_PROJECT_PATH
ENV TIME ${TIME}

RUN python -m pip install --upgrade pip

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY logConfig.py ./
COPY loggingConfig.yaml ./
COPY auto_push_to_github.py ./

CMD [ "python", "./auto_push_to_github.py ${GIT_PROJECT_PATH} ${TIME}" ]