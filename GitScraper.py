#!/usr/bin/python3

import requests
import json
import pymsteams

headers = {
    'Authorization': 'token <github auth token>',
}

with open('html_urls') as json_file:
    html_urls = json.load(json_file)

searchTerms = ['searchTerm 1', 'searchTerm 2', 'searchTerm N...']

teamsHook = pymsteams.connectorcard(<teams webhook URL>)

def notify(resp, term):
    teamsHook.text('Repo Owner: ' + resp['repository']['owner']['login'] + '   \n' + 'Repo Name: ' + resp['repository']['name'] + '   \n' + 'Search Term: ' + term + '   \n' + 'HTML URL: ' + resp['html_url'])
    #teamsHook.printme()
    teamsHook.send()

def search(searchTerms):
    for term in searchTerms:
        params = (
            ('q', term),
        )
        response = requests.get('https://api.github.com/search/code', headers=headers, params=params)
        respObj = json.loads(response.text)

        for resp in respObj['items']:
            if resp['html_url'] not in html_urls:
                html_urls.append(resp['html_url'])
                notify(resp, term)
                
        
search(searchTerms)
with open('html_urls', 'w') as outfile:
    json.dump(html_urls, outfile)
