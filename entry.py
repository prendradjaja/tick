from collections import namedtuple
import uuid
import persistence

all_args = [
    'date', # e.g. "2018-04-16"
    'start', # e.g. "19:32:46.064759"
    'stop', # ^. can be None
    'color', # e.g. "red". see constants.py::Color
    'description', # string
    'tags', # array of strings
    'uuid', # string
]
Entry = namedtuple('Entry', ' '.join(all_args))

def create(*args):
    # TODO validate args
    return Entry(uuid=uuid.uuid4(), *args)

def validate(e):
    for arg in all_args:
        assert arg in dir(e), 'Entry {} is invalid: No "{}" field'.format(uuid, arg)

def persist(e):
    validate(e)
    persistence.write_entry(e)

# TODO when mutating an entry, if start time or description changes you need to make sure to write to the old name (or delete the old name). prob best to sidestep this by never mutating exc to add a stop time
