#!/usr/bin/python
# -*- coding: UTF-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from logConfig import logger
from git import Repo
import time
import datetime
import os
import sys

interval = sys.argv[2]

def startCronTask(task,**interval_config):
    # 定义全局变量scheduler，用于控制定时任务的启动和停止
    global scheduler
    scheduler = BlockingScheduler()
    scheduler.add_listener(CronTask_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler._logger = logger
    logger.info('==================================== 新的日志分段 ==============================================')
    scheduler.add_job(func=task, trigger='interval', **interval_config, id='push_to_github')
    logger.info('当前所有定时任务job1：%s', scheduler.get_jobs())
    logger.info('定时任务调度器状态1：%s', scheduler.state)

    scheduler.start()

#移除单独的定时任务
def stopCronTask(job_id):
    logger.info('当前所有定时任务job3：%s',scheduler.get_jobs())
    #移除单个job
    scheduler.remove_job(job_id)
    logger.info('当前所有定时任务job：%s',scheduler.get_jobs())


def CronTask_listener(event):
    if event.exception:
        logger.info ('状态异常')
    else:
        logger.info ('状态健康')

def cronTask():
    logger.info("启动定时任务，间隔 {} 分钟".format(interval))

    # 创建版本库对象
    repo = Repo('sys.argv[1]')
    repo.commit('-m', '自动上传至GitHub')
    # 获取远程仓库
    remote = repo.remote()
    # 推送本地修改到远程仓库
    remote.push()

def main():
    startCronTask(cronTask,minutes=interval)

if __name__ == '__main__':
    main()