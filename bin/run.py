import os
import sys
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
os.environ['AUTO_CLIENT_SETTINGS'] = 'conf.settings'

from src.plugins import PluginManager

if __name__ == '__main__':
    obj = PluginManager('10.0.0.12')
    server_dict = obj.exec_plugin()
    print(server_dict)




