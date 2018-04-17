"""
Importing this module will create (if nonexistent):
- db/
"""

import json
import os
import re
import shutil
import uuid

from misc import NotImplementedException, fail_if, get_install_dir
import constants
import timeutil
import entry


class _UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return json.JSONEncoder.default(self, obj)

class _Persistence:
    def __init__(self, branch_name=None):
        self._db_dir = os.path.join(get_install_dir(), constants.DB_DIR)
        self._ensure_dir_exists(self._db_dir)

    # def get_file(self, version, name):
    #     return os.path.join(self.get_version_dir(version), name)
    #
    # def make_file(self, version, name, contents=None):
    #     """
    #     If the file exists already, this raises an exception.
    #     """
    #     path = self.get_file(version, name)
    #     os.mknod(path)
    #     if contents is not None:
    #         with open(path, 'w') as f:
    #             f.write(contents)
    #     return path
    #
    # def read_file(self, version, name, default=''):
    #     path = self.get_file(version, name)
    #     try:
    #         with open(path, 'r') as f:
    #             return f.read()
    #     except FileNotFoundError:
    #         return default

    def write_entry(self, e):
        time = timeutil.deserialize(e.start)  # TODO should Entries themselves be automatically (de)serialized
        time = timeutil.to_filename_component(time)
        description = e.description[:10]
        description = re.sub(r'[^A-Za-z]', '-', description)
        description = description.lower()
        my_uuid = e.uuid

        date_dir = os.path.join(self._db_dir, e.date)
        self._ensure_dir_exists(date_dir)

        filename = '{}--{}--{}'.format(time, description, my_uuid)
        path = os.path.join(date_dir, filename)
        obj = {
            'data': e,
            'schema': entry.all_args
        }
        with open(path, 'w') as f:
            f.write(json.dumps(obj, cls=_UUIDEncoder))

    def _ensure_dir_exists(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

_persistence = _Persistence()

def write_entry(e):
    _persistence.write_entry(e)
