from celery import Celery


celery = Celery(
    'worker',
    broker='redis://redis',
    include=['tasks']
)

celery.conf.beat_schedule = {
    'create_redis_task': {
        'task': 'tasks.create_redis_task',
        'schedule': 1.0,
    },
}




