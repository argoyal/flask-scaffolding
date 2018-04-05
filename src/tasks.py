from celery import shared_task


@shared_task
def test_task():
    print("Hello celery tasks are enabled")
