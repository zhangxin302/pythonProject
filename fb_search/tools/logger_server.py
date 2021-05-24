"""
日志系统
"""
import os

from loguru import logger


LOG_DIR = os.path.expanduser(os.path.dirname(os.path.dirname(__file__)))
# LOG_FILE = os.path.join(LOG_DIR, "log_{time}.log")
LOG_FILE = os.path.join(LOG_DIR, "log_facebook_main.log")
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

logger.add(LOG_FILE, rotation="100MB", retention=1, encoding='utf-8')