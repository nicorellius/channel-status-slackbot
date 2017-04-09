"""
Start the SlackBot and handle the commands given to it.
"""

import os
from slackclient import SlackClient
import config
from utils import get_time

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(cmd, chan):
    """Receives commands directed at the bot and determines if they
       are valid commands. If so, then acts on the commands. If not,
       returns back what it needs for clarification."""

    response = "Not sure what you mean. Try the *{0}* command.".format(
        config.APPSERVER_COMMAND
    )
    
    if cmd.startswith(config.EXAMPLE_COMMAND):
        response = "Sure... write some more code then I can do that!"

    if cmd.startswith(config.APPSERVER_COMMAND):

        # somewhat arbitrary value of 10 most recent messages
        num_messages = config.NUMBER_MESSAGES
        channels_history = slack_client.api_call('channels.history',
                                                 channel=config.CHANNEL_ID,
                                                 count=num_messages)

        try:

            if channels_history.get('ok'):

                # fetch all messages from channels.history
                messages = channels_history.get('messages')

                count = 0
                temp_list = []

                while count < num_messages:

                    # get current user from messages based on count
                    user = slack_client.api_call(
                            'users.info',
                            user=messages[count]['user'])

                    # append user and corresponding message to list
                    # if the message contains a server name
                    server_list = config.SERVER_LIST

                    for server in server_list:

                        if server in messages[count]['text']:
                            temp_list.append('[{0}] {1}: {2}'.format(
                                get_time(messages[count]['ts']),
                                user['user']['name'],
                                messages[count]['text'],
                            ))

                    # make list more readable by joining line over line
                    # return_list = '\n'.join(temp_list)
                    response = '\n'.join(temp_list)

                    count += 1

                # the actual response we want, includes users and messages
                # response = '{0}'.format(return_list)

            else:
                response = 'Your API call to channels.history failed.'

        except ConnectionError:
            response = 'You have requested information about {0}.'.format(
                config.CHANNEL_NAME
            )

    slack_client.api_call("chat.postMessage", channel=chan,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """The Slack Real Time Messaging API is an events firehose.
       This parsing function returns None unless a message is
       directed at the Bot, based on its ID."""

    output_list = slack_rtm_output

    if output_list and len(output_list) > 0:
    
        for output in output_list:
    
            if output and 'text' in output and config.AT_BOT in output['text']:
    
                # return text after the @ mention, whitespace removed
                return output['text'].split(
                    config.AT_BOT
                )[1].strip().lower(), output['channel']

    return None, None


if __name__ == "__main__":

    READ_WEBSOCKET_DELAY = 1  # 1 second delay between reading from firehose

    if slack_client.rtm_connect():
        print("[{0}] Channel Status SlackBot connected and running!".format(
            get_time(int(time.time())))
        )

        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())

            if command and channel:
                handle_command(command, channel)

            time.sleep(READ_WEBSOCKET_DELAY)

    else:
        print("[{0}] Connection failed. Invalid Slack token or bot ID?".format(
            get_time(int(time.time()))
        ))
