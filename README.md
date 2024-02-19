# Python-celery-redis

### Description of the Repository:
This Repository is used to create celery jobs with cron schedule with redis as a broker.

### GitFlow

#### Celery Beat:
Celery Beat is a scheduler that enables you to schedule periodic tasks (also known as "cron jobs") within your Celery application. It's responsible for sending messages to the Celery worker processes at specified intervals, triggering the execution of tasks according to the defined schedule. Celery Beat can be configured to use various schedulers, including the default scheduler based on the schedule attribute of the task, or more advanced schedulers like the celery.beat.DatabaseScheduler

#### Celery Worker:
Celery Beat is a scheduler that enables you to schedule periodic tasks (also known as "cron jobs") within your Celery application. It's responsible for sending messages to the Celery worker processes at specified intervals, triggering the execution of tasks according to the defined schedule. Celery Beat can be configured to use various schedulers, including the default scheduler based on the schedule attribute of the task, or more advanced schedulers like the celery.beat.DatabaseScheduler

1. Open two terminals parallely to launch beat and worker.
2. Install requirements:
```bash
celery==5.3.5
redis==4.1.4
```
3. In first terminal:
```bash
 celery -A tasks worker --loglevel=info 
```
4. In second terminal:
```bash
 celery -A tasks beat --loglevel=info
```