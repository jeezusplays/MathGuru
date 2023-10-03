from AIHelper import *
import json
 
# Opening JSON file
f = open('app\\test.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
data_string = json.dumps(data)
print(data)
test = get_questions(data_string)
print(test)
print(list(test.keys()))
# print(embedding("test"))
