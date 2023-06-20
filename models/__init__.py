#!/usr/bin/python3
"""
Module instantiates object
of FileStorage or DBStorage.
"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorag()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
