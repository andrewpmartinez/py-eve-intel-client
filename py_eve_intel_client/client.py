import json
import requests
import threading
from py_eve_chat_mon.monitor import Monitor


def post(url, data, token, timeout):
    requests.post(url, data, headers={Client.TOKEN_HEADER: token}, timeout=timeout)


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

    def _handler(self, chat_name, events):
        if chat_name in self.chat_configs:
            for event in events:
                config = self.chat_configs[chat_name]
                event['timestamp'] = str(event['timestamp'])

                thread = threading.Thread(target=post, args=(config['url'], json.dumps(events), config['token'], 5),
                                          kwargs={})
                thread.start()


class Chat(object):
    def __init__(self, chat_name, post_url, token):
        self.chat_name = chat_name
        self.post_url = post_url
        self.token = token
