import os
import subprocess
import sys


class NotImplementedException(Exception):
    pass

def list2cmdline(args):
    return subprocess.list2cmdline(args)

def fail_if(condition, msg, end='\n'):
    if condition:
        fail(msg, end=end)

def fail(msg, end='\n'):
    print(msg, file=sys.stderr, end=end)
    exit(1)

def get_install_dir():
    return os.path.dirname(os.path.abspath(__file__))
