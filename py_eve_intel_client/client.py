import json
import requests
from py_eve_chat_mon.monitor import Monitor
from .exception import InvalidChatConfig

class Client(object):
    TOKEN_HEADER = "EVE-CHAT-MON"

    def __init__(self, chat_configs, log_dir, post_rate=1000):
        self.post_rate = post_rate
        self.log_dir = log_dir
        self.chat_configs = {}

        for chat_name, chat_config in chat_configs.items():
            self.chat_configs[chat_name] = chat_config

        self.monitor = None

    def start(self):
        if not self.monitor:
            self.monitor = Monitor(self.chat_configs.keys(), self.log_dir, self._handler, self.post_rate)

        self.monitor.start()

    def stop(self):
        self.monitor.stop()

    def _handler(self, chat_name, event):
        if chat_name in self.chat_configs:
            config = self.chat_configs[chat_name]
            print("Posting to url: %s".format(config.url))
            print("Token: %s".format(config.token))
            print("Body: %s".format(json.dumps(event)))

            requests.post(config.url, json.dumps(event), headers={Client.TOKEN_HEADER: config.token}, timeout=5)


    def add_chat(self, chat_config):
        if not chat_config:
            raise InvalidChatConfig()

        self.chat[chat_config.chat_name] = chat_config

class Chat(object):
    def __init__(self, chat_name, post_url, token):
        self.chat_name = chat_name
        self.post_url = post_url
        self.token = token
