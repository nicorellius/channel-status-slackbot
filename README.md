# channel-status-slackbot
A Slack Bot for monitoring the status of channels

To set up, you will need to do several things:

1. Clone this repository
1. Make a virtual environment for this project
1. Install requirements
1. Log in to [slack.com]() and create your API token. Then set the environment variable: `export SLACK_BOT_TOKEN=xxx`
1. Run the `python utils.py`. This will print out your bot ID and channel ID
1. Set these environment variables: `export BOT_ID=xxx`, `export CHANNEL_ID=xxx`
1. Tweak the `startbot.py` to meet your needs
1. Run `python startbot.py`
1. In the Slack channel you've configured, run the command to get your list: `@starterbot check appservers`
