"""

"""
import celery
import celeryconf
import uuid



app = celery.Celery(__name__)
app.config_from_object(celeryconf)

@app.task(bind=True)
def test_task(self, x):
	return x

@app.task(bind=True)
def print_task(self, x):
	print x
	return x

@app.task(bind=True)
def add_task(self, x, y):
	return x+y

@app.task(bind=True)
def bad_task(self):
	raise RuntimeError("intentional error")


@app.task(bind=True)
def chaining_task(self, add):
	return celery.chain(add_task.s(*add), print_task.s()).apply_async()

# you can do this from a separate threads
from redbeat import RedBeatSchedulerEntry as Entry
e = Entry(
	'thingo',
	'cluster.chaining_task',
	10,
	args=([5, 6], ),
	options={'schedule_id': 'testid'},
	app=app)
e.save()
