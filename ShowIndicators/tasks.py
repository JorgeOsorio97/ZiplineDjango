from celery import Celery

app = Celery('tasks', broker = 'sqs://AKIAIXPPXFTW77RSDS7A:FGXzxmBI3dMiE3Em1cTWgnBJyhXol49VgFGV8TOF@')

@app.task
def suma(x, y):
    return x+y

