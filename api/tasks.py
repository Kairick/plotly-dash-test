
import redis

from celery_app import celery
from utils import generate_ticker_name, generate_movement

redis_client = redis.StrictRedis(host='redis', port=6379, db=0,
                                 charset="utf-8", decode_responses=True)


@celery.task()
def create_redis_task():
    tickers = generate_ticker_name()
    for ticker in tickers:
        add_data_to_redis(ticker)


@celery.task()
def add_data_to_redis(ticker_name):
    """Добавляем изменение цены в редис"""
    redis_client.xadd(ticker_name, {'price_inc': generate_movement()})
