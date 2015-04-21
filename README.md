# isbot
ISDC Slack Chat Bot

Designed to run as a plugin of python-rtmbot https://github.com/camronlevanger/python-rtmbot.

####Additional functionality is welcomed in the form of a github pull request!

##Current Functionality/Commands
+ lunch - @isbot: where should I go to lunch? - Searches yelp for highly rated places to eat in the area.
+ tableflip - @isbot: tableflip - fetches a random awesome tableflipper.com GIF

##Install
Once you have python-rtmbot up and running:

`cd /path/to/rtmbot/plugins`

`git clone git@github.com:camronlevanger/isbot.git`

`pip install -r requirements.txt`


You will also need to set some environment variables in order to use the Yelp integration. Add the following to your .bash_profile or .zshrc (or whatever it is you prefer):

```# Yelp API authentication information
 export YELP_CONSUMER_KEY=5mS4Kybbj_FCmpMpib1mgA
 export YELP_CONSUMER_SECRET=vO1241dzVOu6IYPQdTl2jYvdfd4
 export YELP_TOKEN=XZa_sIFpyZcn0ynXVtgv3wCLSuhaxNNx
 export YELP_TOKEN_SECRET=tvubnzdXZDun-ospypixsIy4Jwc```

 Once you have completed the install, restart python-rtmbot. isbot should be now connected to Slack.
