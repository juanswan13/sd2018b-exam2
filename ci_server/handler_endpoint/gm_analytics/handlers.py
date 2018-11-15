import os
import logging
import requests
import json
from flask import request

def repository_merged():
    logging.debug('Event Received')
    post_json_data = request.get_data()
    string = str(post_json_data, 'utf-8')
    jsonFile = json.loads(string)
    pull_id = jsonFile["pull_request"]["head"]["sha"]
    url = 'https://raw.githubusercontent.com/juanswan13/sd2018b-exam2/' + pull_id + '/images.json'
    response = requests.get(url)
    packages_json = json.loads(response.content)
    

    logging.debug(text)
    result = {'command_return': 'Funciona'}
    return result
