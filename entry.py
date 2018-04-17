from collections import namedtuple
import uuid
import persistence
import constants

all_args = [
    'date', # e.g. "2018-04-16"
    'start', # e.g. "19:32:46.064759"
    'stop', # ^. can be None
    'color', # e.g. "red". see constants.py::Color DEFAULT BLUE
    'description', # string                        DEFAULT ''
    'tags', # array of strings                     DEFAULT []
    'uuid', # string
]
Entry = namedtuple('Entry', ' '.join(all_args))

def create(*args, **kwargs):
    # TODO validate args
    e = Entry(uuid=uuid.uuid4(), *args, **kwargs)
    # print('Created', e)  # DEBUG
    return e

def validate(e):
    for arg in all_args:
        assert arg in dir(e), 'Entry {} is invalid: No "{}" field'.format(e.uuid, arg)

def persist(e):
    # print('Persisting', e)  # DEBUG
    validate(e)
    persistence.write_entry(e)

    # # DEBUG:
    # print('Writing: ({} - {}) [{}] {}'.format(e.start, e.stop, e.color, e.description))

def get():
    pass

# TODO when mutating an entry, if start time or description changes you need to make sure to write to the old name (or delete the old name). prob best to sidestep this by never mutating exc to add a stop time
# JUST KIDDING NOT USING DESC AS FILENAME
