import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#调试模式开关(DEBUG)
TEST = False

# 配置信息采集插件
PLUGIN_ITEMS = {
    "nic": "src.plugins.nic.Nic",
    "disk": "src.plugins.disk.Disk",
    "basic": "src.plugins.basic.Basic",
    "board": "src.plugins.board.Board",
    "memory": "src.plugins.memory.Memory",
}

# 服务端API
API = 'http://127.0.0.1:8000/api/server'

# 客户端采集模式 agent,ssh,salt
MODE = 'salt'

#SSH模式 配置项
SSH_USER = 'root'
SSH_PWD = '123456'
SSH_PORT = 22