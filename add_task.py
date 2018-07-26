"""

"""
import cluster
from redbeat import RedBeatSchedulerEntry as Entry


entry = Entry('thingo', 'cluster.add_task', 10, args=(5, 10), app=cluster.app)
entry.save()
print entry.key, "->", entry.interval