import json
import requests
import configparser

from idna import encode

from ActivityClass import Activity

graph = None

def openConnection():
    config = configparser.ConfigParser()
    config.read(['config.cfg'])
    azure_settings = config['azure']


    headers = {"Content-Type: application/x-www-form-urlencoded"}
    url = "https://login.microsoftonline.com/"+azure_settings['tenantId']+"/oauth2/v2.0/token"
    print(url)
    body = "client_id="+azure_settings['clientId']
    body += "&scope=https%3A%2F%2Fgraph.microsoft.com%2F.default"
    body += "&client_secret="+azure_settings['clientSecret']
    body += "&grant_type=client_credentials"

    #response = requests.post(url,data=body)
    #if response.status_code == 200:
    #    auth_response = response.json()

    #url_calendar = "https://graph.microsoft.com/v1.0/users/Victor.Sanchez/calendar/events?$filter=startsWith(subject,'REQ')"
    #url_calendar = "https://graph.microsoft.com/v1.0/users/Victor.Sanchez@entersoluciones.com/calendarview?startdatetime=2022-06-29T00:00:00.0Z&enddatetime=2022-06-29T23:59:26.061Z"
    #headers_with_token = {"Content-type": "application/json","Authorization": "Bearer " + auth_response["access_token"]}

    #response_calendar = requests.get(url_calendar,headers=headers_with_token)
    #if response_calendar.status_code == 200:
    #    calendar_data = response_calendar.json()["value"]
    #    print("==========================================================")
    #    print(calendar_data)
    #    print("==========================================================")
    #lines = ""
    with open("response.json",encoding="utf-8") as f:
        lines = f.readlines()
    print(lines)
    strlines = '\n'.join(lines)

    body = json.loads(strlines)

    #parserResponse(calendar_data)
    parserResponse(body)

def parserResponse(body: object):
    meetings = []


    for meeting in body:
        activity = Activity(meeting)
        meetings.append(activity)
        print(activity)




openConnection()