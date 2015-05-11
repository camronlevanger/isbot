import pprint
import requests
from yelp import *
from phabricator import Phabricator

phab = Phabricator()
phab.update_interfaces()
phab.user.whoami()

crontable = []
outputs = []
phab_listener_started = False

pp = pprint.PrettyPrinter(indent=4)


def startPhab():
    phab_listener_started = True
    diffs = phab.differential.query(
        arcanistProjects=['PowerStandings'],
        status='status-open'
    )

    #pp.pprint(diffs)
    print diffs[0]['uri']


def getUnreviewedDiffs():
    diffs = phab.differential.query(
        arcanistProjects=['PowerStandings'],
        status='status-open'
    )

    messages = []
    count = 0

    for diff in diffs:
        message = diff['title'] + " " + diff['uri']
        messages.append(message)
        count = count + 1

    return count, messages


def process_message(data):

    if not phab_listener_started:
        startPhab()

    isbot = '<@U04F3NB5M>'
    # print data

    # send a direct message to isbot with a command
    if data.get('text') and isbot in data.get('text'):
        if 'tableflip' in data['text']:
            tableflip = requests.get('http://tableflipper.com/json')
            tableflip = tableflip.json()
            # print tableflip
            outputs.append([data['channel'], tableflip['gif']])

        elif 'lunch' in data['text']:
            food = query_api('lunch', 'Provo, UT')
            # print food
            outputs.append(
                [data['channel'],
                    "<@" + data['user'] + "> How about " + food['name']
                    + "? " + food['location']['address'][0] + " "
                    + food['location']['city'] + " " + food['mobile_url']]
            )

            outputs.append(
                [data['channel'],
                    "It has a " + str(food['rating'])
                    + " star rating...here is what people are saying:"]
            )

            outputs.append([data['channel'], food['reviews'][0]['excerpt']])
            outputs.append([data['channel'], food['image_url']])

        elif 'dinner' in data['text']:
            food = query_api('dinner', 'Provo, UT')
            outputs.append(
                [data['channel'],
                    "<@" + data['user'] + "> How about " + food['name']
                    + "? " + food['location']['address'][0] + " "
                    + food['location']['city'] + " " + food['mobile_url']]
            )

            outputs.append(
                [data['channel'],
                    "It has a " + str(food['rating'])
                    + " star rating...here is what people are saying:"]
            )

            outputs.append([data['channel'], food['reviews'][0]['excerpt']])
            outputs.append([data['channel'], food['image_url']])

        elif 'diffs' in data['text'] and 'need' in data['text'] and 'review' in data['text']:
            count, diffs = getUnreviewedDiffs()

            if count > 1:
                outputs.append([data['channel'], 'Yes, ' + str(count) + ' diffs are waiting for review in the PowerStandings repo...'])
                for message in diffs:
                    outputs.append([data['channel'], message])
            else:
                outputs.append([data['channel'], 'Perhaps, but all of the diffs for PowerStandings currently have at least one review.'])

        else:
            outputs.append([data['channel'], "Sorry, I do not understand"])
            outputs.append(
                [data['channel'],
                    "Commands I know: tableflip, lunch, dinner"]
            )

    if data.get('text') and data.get('text') == isbot:
        outputs.append([data['channel'], "Commands I know: tableflip, lunch, dinner"])
