"""
Collect all configuration and settings here.
"""

import os

# Bot's ID as an environment variable. Set these to your specifics.
# Bot ID for starterbot is U4W8M9KU4
BOT_ID = os.environ.get("BOT_ID")
BOT_NAME = 'starterbot'

AT_BOT = '<@{0}>'.format(BOT_ID)

# Channel ID for appservers is C4UEFK337
CHANNEL_ID = os.environ.get("CHANNEL_ID")
CHANNEL_NAME = 'appservers'

# Add more commands as you see fit.
EXAMPLE_COMMAND = 'do'
APPSERVER_COMMAND = 'check appservers'

# Increasing this above the number of members throws an error.
NUMBER_MESSAGES = 10

# This is a list of servers we monitor on the above channel.
SERVER_LIST = [
    'merlin', 'taliesin', 'arthur', 'lancelot',
    'actin', 'datacruncher',
]
