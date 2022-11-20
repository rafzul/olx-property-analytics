import json
import ast
import re

with open('example_single_page.js','r') as f:
    fulltext = f.read()
    props = re.findall(r'(props)(.+)', fulltext)[0][1].replace(": ", "", 1)
    states = re.findall(r'(states)(.+)', fulltext)[0][1].replace(": ", "", 1)
    config = re.findall(r'(config)(.+)', fulltext)[0][1].replace(": ", "", 1)
    fulldict = dict(props=props,states=states,config=config)
    jsonfull = json.loads(fulldict)
    print(jsonfull)
    # print(type(props))
    
