#!/usr/bin/env python3
import datetime

import entry
import constants
import timeutil


def start(description='', color=Color.BLUE):
    date = datetime.date.today().isoformat()
    start = timeutil.now()
    stop = None
    tags = get_tags(description, color)

    e = create(date, start, stop, color, description, tags)
    persist(e)


def get_tags(description, color):
    tags = [word[1:] for word in description.split()
            if word.startswith('#')]
    return tags + [color]
