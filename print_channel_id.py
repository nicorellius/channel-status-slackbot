import os

from slackclient import SlackClient

# Channel ID for appservers is C4UEFK337
CHANNEL_NAME = 'appservers'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


if __name__ == '__main__':
    
    api_call = slack_client.api_call('channels.list')
    
    if api_call.get('ok'):
        
        # retrieve all users so we can find our bot
        channels = api_call.get('channels')
        
        for channel in channels:
            
            if 'name' in channel and channel.get('name') == CHANNEL_NAME:

                print("Channel ID for {0} is {1}".format(
                      channel['name'], channel.get('id')))
    
    else:
        
        print("could not find channel with the name " + CHANNEL_NAME)
