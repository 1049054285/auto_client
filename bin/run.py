import requests
import os
os.environ['AUTO_CLIENT_SETTINGS'] = 'conf.settings'

from src.plugins import PluginManager

if __name__ == '__main__':
    obj = PluginManager()
    server_dict = obj.exec_plugin()
    print(server_dict)




