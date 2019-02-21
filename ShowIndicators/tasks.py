from celery import Celery

app = Celery('tasks', broker = '')

@app.task
def suma(x, y):
    return x+y

