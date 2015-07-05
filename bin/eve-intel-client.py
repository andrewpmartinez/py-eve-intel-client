import time
import json
import argparse
from py_eve_intel_client.client import Client

parser = argparse.ArgumentParser(description="""Start an Eve intel client which will post chat events to a given URL.

The command line (--w) configuration only allows one URL to be posted to while
a configuration file (--c) allows each individual chat to post to its own URL
with its own token.

It is STRONGLY suggested that you post via HTTPS in order to keep your intel
safe and secure.

It is STRONGLY suggested that you keep your tokens safe and make them a hard to
guess string.

""", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--log-dir", type=str, required=False, dest="log_dir",
                    help="The absolute path to the EVE chat directory")
parser.add_argument("--post-rate", metavar="MS", type=int, required=False, dest="post_rate",
                    help="""The rate at which chat logs are polled and chat events are
POSTed.

Value is in seconds and defaults to 1 second.
Lower numbers are more responsive but harder on disk IO and
on the target server.

If specified the value supplied will override any value
specified in the configuration file passed via --c.

""")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--w', type=str, metavar="WATCH_STRING", dest="watch_string",
                   help="""A watch string which is in the format of:
    <url>:<token>:<chats>

    - <url>   is the URL to POST message events to. It is
              strongly recommended that this is HTTPS.
    - <token> is a secret value added to HTTP POST request
              in the EVE-CHAT-MON header. Value MUST be
              header safe (i.e. printable US-ASCII). If
              confused stick to a-z, A-Z, 0-9.
    - <chats> is a comma separated list of chats to watch.

    Ex: https://example.com:a95c530a7af5d150:Alliance,Corp

""")
group.add_argument('--c', type=argparse.FileType('r'), metavar="CONFIG_FILE", dest="config_file",
                   help="""A JSON formatted configuration file:
{
    "postRate": 1000,
    "chats": {
        "Alliance": {
            "url": "https://example.com/alliance",
            "token": "a6928b9c624683fbbb40266c1f19382b"
        },
        "Corp": {
            "url": "https://example.com/corp",
            "token": "1de7fdf5119097846de6b2d210f911ea"
        }
    }

}

""")

def merge_file_configs(cmd_args, file_config):
    args = cmd_args.copy()
    args['chat_configs'] = file_config['chats']

    if not args['post_rate']:
        args['post_rate'] = config['postRate']

    if not args['log_dir']:
        args['log_dir'] = config['logDir']

    return args

if __name__ == "__main__":
    args = vars(parser.parse_args())

    if args['config_file']:
        config = json.load(args['config_file'])
        args = merge_file_configs(args, config)
    else:
        args['chat_configs'] = [] #TODO: parse from command line watch string

    client = Client(args['chat_configs'], args['log_dir'], post_rate=args['post_rate'])
    client.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client.stop()

    exit()
