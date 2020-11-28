#!/usr/bin/env python3

import re
import requests
import os.path

from dataclasses import dataclass

@dataclass
class Visit:
    id: str
    name: str

def createOutputDir():
    dir = 'gpx'
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return dir

def getCookie():
    cookie_file = 'cookie.txt'
    if not os.path.isfile(cookie_file):
        print("Missing " + cookie_file)
        exit(1)

    with open('cookie.txt', 'r') as file:
        cookie = file.read().strip()
    if len(cookie) <= 20:
        print("Invalid cookie in " + cookie_file)
        exit(2)
    
    return cookie

def getVisitList():
    headers = {
        'Cache-Control': 'max-age=0',
        'Cookie': cookie
    }
    response = requests.get(url, headers=headers)
    response_text = response.text
    start = response_text.find('<select name="selected_visit">')
    end = response_text.find('</select>', start)
    response_text = response_text[start:end]

    pattern = re.compile(r'<option value="(\d+)">([^<]+)</option>')
    visit_list = []
    for (visit_id, visit_name) in re.findall(pattern, response_text):
        visit_list.append(Visit(id=visit_id, name=visit_name))
    return visit_list

def processVisits(visit_list):
    headers = {
        'Cache-Control': 'max-age=0',
        'Cookie': cookie,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    for visit in visit_list:
        response = requests.post(url, data='selected_visit=' + visit.id, headers=headers)
        response_text = response.text
        if response_text.find('<gpx ') >= 0 and response_text.find('</gpx>') >= 0:
            with open(output_dir + '/' + visit.name + '.gpx', 'w') as file:
                file.write(response.text)
            print("Downloaded GPX file for visit " + visit.name)
        else:
            print("Failed to download GPX file for visit " + visit.name)

url = 'http://snow.traceup.com/settings/gpx'

output_dir = createOutputDir()
cookie = getCookie()

visit_list = getVisitList()
if not visit_list:
    print("Unable to load any visits, please check that you're using the correct cookie.")
    exit(3)
processVisits(visit_list)
