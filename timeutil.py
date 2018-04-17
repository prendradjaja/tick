import datetime


def now():
    return datetime.datetime.now().time()

def to_filename_component(t):
    hours = str(t.hour).rjust(2, '0')
    mins = str(t.minute).rjust(2, '0')
    secs = str(t.second).rjust(2, '0')
    return '{}-{}-{}'.format(hours, mins, secs)

def serialize(t):
    return t.isoformat()

def deserialize(timestring):
    # https://stackoverflow.com/a/10198149
    return datetime.datetime.strptime(timestring, "%H:%M:%S.%f").time()
