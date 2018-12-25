#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging
import logging.config
import yaml

def load_yaml_config(config_path):
    with open(config_path, "r") as f:
        data = yaml.load(f)
    return data

def setup_logging():
    configuration_path = "loggingConfig.yaml"
    logging_configuration = load_yaml_config(configuration_path)
    logging.config.dictConfig(logging_configuration)

# 创建一个logger
logger = logging.getLogger(__name__)

setup_logging()

if __name__ == '__main__':
    # 记录一条日志
    logger.info('test')
