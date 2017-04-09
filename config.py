# Collect all configuration and settings here

import os

# Bot's ID as an environment variable. Set these to your specifics
BOT_ID = os.environ.get("BOT_ID")
AT_BOT = '<@{0}>'.format(BOT_ID)

CHANNEL_ID = os.environ.get("CHANNEL_ID")
CHANNEL_NAME = 'appservers'  # use whatever channel name you want...

EXAMPLE_COMMAND = 'do'
APPSERVER_COMMAND = 'check appservers'  # add more commands as you see fit

NUMBER_MESSAGES = 10

SERVER_LIST = [
    'merlin', 'taliesin', 'arthur', 'lancelot',
    'actin', 'datacruncher',
]
