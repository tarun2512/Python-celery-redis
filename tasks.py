import os
import platform
from datetime import datetime

import redis
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

if platform.system().lower() == "windows":
    os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")

celery = Celery(__name__)
celery.conf.broker_url = celery.conf.result_backend = "redis://admin:iLensDevRedis@****:6379/5"
# Celery configuration
celery.conf.beat_schedule = {
    # Executes every minute
    "periodic_task-every-minute": {"task": "periodic_task_1", "schedule": crontab(minute="*/2")},
    "periodic_task-every-hour": {"task": "periodic_task_2", "schedule": crontab(minute="*/5")},
}

celery.conf.timezone = "UTC"


@celery.task(name="periodic_task_1")
def periodic_task_1():
    redis_url = "redis://admin:iLensDevRedis@****:6379/"
    redis_conn = redis.from_url(redis_url, db=int(6), decode_responses=True)
    key = "example_key"
    value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    redis_conn.set(key, value)
    print("Hi! from periodic_task")
    logger.info("Hello! from periodic task")


@celery.task(name="periodic_task_2")
def periodic_task_2():
    redis_url = "redis://admin:iLensDevRedis@******:6379/"
    redis_conn = redis.from_url(redis_url, db=int(14), decode_responses=True)
    key = "example_key"
    value = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    redis_conn.set(key, value)
    print("Hi! from periodic_task")
    logger.info("Hello! from periodic task")
