"""
全局设置
"""
from redis import StrictRedis, ConnectionPool

EPR_TIME = 7  # 抓取贴子的过期时间

REDIS = StrictRedis(connection_pool=ConnectionPool(host="127.0.0.1", port=6379,db=0))
