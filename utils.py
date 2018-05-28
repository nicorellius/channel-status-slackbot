"""
Utility module for Channel Status SlackBot.
"""

import os
import time

from slackclient import SlackClient

import config


def _get_time(input_time):

    return time.strftime(
        '%Y-%m-%d %H:%M:%S',
        time.localtime(float(input_time))
    )


def _print_bot_id():

    bot_name = config.BOT_NAME

    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    call = slack_client.api_call("users.list")

    if call.get('ok'):

        # retrieve all users so we can find our bot
        users = call.get('members')

        for user in users:

            if 'name' in user and user.get('name') == config.BOT_NAME:
                print("[{0}] Bot ID for {1} is {2}".format(
                    _get_time(int(time.time())),
                    user['name'],
                    user.get('id')))

    else:
        print("[{0}] Could not find bot user with the name {1}.".format(
            _get_time(int(time.time())),
            bot_name
        ))


def _print_channel_id():

    channel_name = config.CHANNEL_NAME

    slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

    call = slack_client.api_call('channels.list')

    if call.get('ok'):

        # retrieve all users so we can find our bot
        channels = call.get('channels')

        for channel in channels:

            if 'name' in channel and channel.get('name') == channel_name:
                print("[{0}] Channel ID for {1} is {2}".format(
                    _get_time(int(time.time())),
                    channel['name'],
                    channel.get('id'))
                )

    else:

        print("[{0}] Could not find channel with the name {1}.".format(
            _get_time(int(time.time())),
            channel_name
        ))


if __name__ == "__main__":

    _print_bot_id()
    _print_channel_id()
