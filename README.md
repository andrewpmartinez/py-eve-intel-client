Release/Master: ![Release Status](https://travis-ci.org/andrewpmartinez/py-eve-intel-client.svg?branch=master "Release/Master") Develop: ![Develop Status](https://travis-ci.org/andrewpmartinez/py-eve-intel-client.svg?branch=develop "Develop")

# Python Eve Chat Monitoring

A python application that allows EVE Chat logs to be monitored and send py-eve-chat-mon style events to a server with a secret token. Allows for configurations be via command line or through a JSON configuration file.

### Python Version Support

Python 3.3.x
Python 3.4.x

### To Install

`pip install py-eve-intel-client`

### Executables

After installation the following will be added to your Python's /Scripts/ directory:

`eve-intel.client.cmd`

`eve-intel-client.py`

`eve-intel-client.sh`

You can either navigate to that directory and execute the files, use the absolute path of the files, or add the directory to your path.
 
 
### Help

```
usage: eve-intel-client.py [-h] [--log-dir LOG_DIR] [--post-rate MS]
                           (--w WATCH_STRING | --c CONFIG_FILE)

Start an Eve intel client which will post chat events to a given URL.

The command line (--w) configuration only allows one URL to be posted to while
a configuration file (--c) allows each individual chat to post to its own URL
with its own token.

It is STRONGLY suggested that you post via HTTPS in order to keep your intel
safe and secure.

It is STRONGLY suggested that you keep your tokens safe and make them a hard to
guess string.

optional arguments:
  -h, --help         show this help message and exit
  --log-dir LOG_DIR  The absolute path to the EVE chat directory
  --post-rate MS     The rate at which chat logs are polled and chat events are
                     POSTed.

                     Value is in milli-seconds and defaults to 1000ms (1 second).
                     Lower numbers are more responsive but harder on disk IO and
                     on the target server.

                     If specified the value supplied will override any value
                     specified in the configuration file passed via --c.

  --w WATCH_STRING   A watch string which is in the format of:
                         <url>:<token>:<chats>

                         - <url>   is the URL to POST message events to. It is
                                   strongly recommended that this is HTTPS.
                         - <token> is a secret value added to HTTP POST request
                                   in the EVE-CHAT-MON header. Value MUST be
                                   header safe (i.e. printable US-ASCII). If
                                   confused stick to a-z, A-Z, 0-9.
                         - <chats> is a comma separated list of chats to watch.

                         Ex: https://example.com:a95c530a7af5d150:Alliance,Corp

  --c CONFIG_FILE    A JSON formatted configuration file:
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
```
