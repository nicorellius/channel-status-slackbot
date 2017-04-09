"""
Utility module for Channel Status SlackBot.
"""

import os
import time

from slackclient import SlackClient

from config import BOT_NAME, CHANNEL_NAME


def get_time(input_time):

    return time.strftime(
        '%Y-%m-%d %H:%M:%S',
        time.localtime(float(input_time))
    )


def print_bot_id():

    bot_name = BOT_NAME

    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    api_call = slack_client.api_call("users.list")

    if api_call.get('ok'):

        # retrieve all users so we can find our bot
        users = api_call.get('members')

        for user in users:

            if 'name' in user and user.get('name') == BOT_NAME:
                print("[{0}] Bot ID for {1} is {2}".format(
                    get_time(int(time.time())),
                    user['name'],
                    user.get('id')))

    else:
        print("[{0}] Could not find bot user with the name {1}.".format(
            get_time(int(time.time())),
            bot_name
        ))


def print_channel_id():

    channel_name = CHANNEL_NAME

    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    api_call = slack_client.api_call('channels.list')

    if api_call.get('ok'):

        # retrieve all users so we can find our bot
        channels = api_call.get('channels')

        for channel in channels:

            if 'name' in channel and channel.get('name') == channel_name:
                print("[{0}] Channel ID for {1} is {2}".format(
                    get_time(int(time.time())),
                    channel['name'],
                    channel.get('id'))
                )

    else:

        print("[{0}] Could not find channel with the name {1}.".format(
            get_time(int(time.time())),
            channel_name
        ))
