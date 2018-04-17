#!/usr/bin/env python3
import json

def get_event():
    path = './example-event.json'
    with open(path) as f:
        return json.load(f)

print(get_event())
