from util import getch
import persistence
import entry
import constants
import timeutil

import uuid
import datetime


def main():
    while True:
        char = getch()
        if char == '\x03':
            break
        print(char)
        if char == ' ':
            start_or_stop()
        elif char == 'c':
            color()
        elif char == 'd':
            description()
        elif char == ' ':
            stop()
        elif char == 'e':
            stop_with_manual_end()
        elif char == 'r':
            resume_previous()
        elif char == 'm':
            manual_entry()
        else:
            print('Invalid command.')

def start_or_stop():
    prev = persistence.get_newest_entry_today_if_any()
    if not prev:
        start()
    elif prev:
        if prev.stop is not None:
            start()
        else:
            stop()

def start():
    e = entry.create(
        date = datetime.date.today().isoformat(),
        start = timeutil.serialize(timeutil.now()),
        stop = None,
        color = constants.Color.BLUE,
        description = '',
        tags = [],
    )
    # print('Trying to persist', e)  # DEBUG
    entry.persist(e)

def stop():
    prev = _get_prev_if_exists_and_unstopped()
    if not prev:
        return
    if prev.stop is not None:
        print('FATAL: Trying to stop an already-stopped event.')
        return
    modified = prev._replace(stop = timeutil.serialize(timeutil.now()))
    entry.persist(modified)

def _get_prev_if_exists_and_unstopped():
    prev = persistence.get_newest_entry_today_if_any()
    if not prev:
        print('FATAL: No previous entry.')
        return
    if prev.stop is not None:
        print('FATAL: Previous entry is stopped!')
        return  # TODO should you be able to?
    # prev exists and has not been stopped
    return prev

def color():
    color = input('> ')
    if color not in constants.ALL_COLORS:
        print('FATAL: Invalid color.')
        return  # TODO loop instead
    prev = _get_prev_if_exists_and_unstopped()
    if not prev:
        return
    modified = prev._replace(color = color)
    entry.persist(modified)

def description():
    description = input('> ')
    prev = _get_prev_if_exists_and_unstopped()
    if not prev:
        return
    modified = prev._replace(description = description)
    entry.persist(modified)

def stop_with_manual_end():
    print('WARNING: Parsing is not yet implemented')  # TODO
    stop = 'HUMAN-' + input('> ')
    prev = _get_prev_if_exists_and_unstopped()
    if not prev:
        return

def resume_previous():
    prev = persistence.get_newest_entry_today_if_any()
    if not prev:
        print('FATAL: No previous entry.')
        return
    if prev.stop is None:
        print('Previous entry is still going!')
        print('No action taken.')
        return  # TODO should you be able to?
    # prev entry is stopped and therefore continuable
    modified = (prev
        ._replace(start = timeutil.now())
        ._replace(stop = None)
        ._replace(uuid = uuid.uuid4())
    )

def manual_entry():
    prev = persistence.get_newest_entry_today_if_any()
    if prev and prev.stop is None:
        print('WARNING: Previous entry is not stopped.')
    start = 'HUMAN-' + input('start> ')
    stop = 'HUMAN-' + input('stop> ')
    color = input('color? ') or constants.Color.BLUE
    if color not in constants.ALL_COLORS:
        print('FATAL: Invalid color.')
        return  # TODO loop instead
    description = input('description?' )
    e = entry.create(
        date = datetime.date.today().isoformat(),
        start = start,
        stop = stop,
        color = color,
        description = description,
        tags = [],  # TODO
    )
    entry.persist(e)

if __name__ == '__main__':
    main()
