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
APPSERVER_COMMAND = 'check appservers'  # Use: `@starterbot check appservers`

"""
`NUMBER_MESSAGES` should be less than the number of messages in the channel.
For example, if there are 6 messages in the channel that would be fetched 
by this bot, then the `NUMBER_MESSAGES` should not be set to be equal to 

    Traceback (most recent call last):
      File "startbot.py", line 119, in <module>
        handle_command(command, channel)
      File "startbot.py", line 52, in handle_command
        user=messages[count]['user'])
    IndexError: list index out of range
    
This is a bug that was recently fixed by fetching the number of messages in
the channels.history and then setting the value this minus one. See line
"""
NUMBER_MESSAGES = 100

# This is a list of servers we monitor on the above channel.
SERVER_LIST = [
    'merlin', 'taliesin', 'arthur', 'lancelot',
    'actin', 'datacruncher',
]
