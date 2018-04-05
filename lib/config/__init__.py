from . import global_settings
import os
import importlib

class Settings(object):
    def __init__(self):
        for item in dir(global_settings):
           if item.isupper():
               k = item
               v = getattr(global_settings, k)
               setattr(self, k, v)

        settings_path = os.environ.get('AUTO_CLIENT_SETTINGS')
        settings_module = importlib.import_module(settings_path)
        for item in dir(settings_module):
           if item.isupper():
               k = item
               v = getattr(settings_module, k)
               setattr(self, k, v)


settings = Settings()