# Author : Emma Chubb
# Date : 2024-06-10

# Requests lets you make a request to a webpage and print the response text. See: https://www.w3schools.com/python/module_requests.asp 
import requests
import json 
url ="https://www.gov.uk/bank-holidays.json" # this url hs UK bank holidays data in json format. 
response = requests.get(url)
data = response.json()
# this is called "pretty print" - https://www.geeksforgeeks.org/python/response-json-python-requests/ 
# print to see what data contains/looks like, comment out when not needed.
#print(json.dumps(data, indent=4, sort_keys=True))

# i only want the names of the holidays in Northern Ireland so I've used a ist comprehension.
# List comprehensions allow you to create a list by iterating over something iterable and apply optional filtering if necessary.  
# see: https://realpython.com/list-comprehension-python/  .
holidays = [event['title'] for event in data['northern-ireland']['events']]
print (holidays)

# extra step to get the holidays that only appear in northern ireland and not in the other parts of the UK.
# copy my code above except for england and scotland.

england_holidays = {event['title'] for event in data['england-and-wales']['events']}

scotland_holidays = {event['title'] for event in data['scotland']['events']}

# get the holidays that are only in northern ireland. Adapted examples of filtering from :https://www.w3schools.com/python/python_lists_comprehension.asp 
ni_only_holidays = [holiday for holiday in holidays if holiday not in england_holidays and holiday not in scotland_holidays]

print (ni_only_holidays)