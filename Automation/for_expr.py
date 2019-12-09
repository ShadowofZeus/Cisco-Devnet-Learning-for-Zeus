#!/usr/bin/env python

from jinja2 import Environment, FileSystemLoader
import os

persons = [
    {'name': 'Andrej', 'age': 34},
    {'name': 'Mark', 'age': 17},
    {'name': 'Thomas', 'age': 44},
    {'name': 'Lucy', 'age': 14},
    {'name': 'Robert', 'age': 23},
    {'name': 'Dragomir', 'age': 54}
]

templateLoader = FileSystemLoader(searchpath="/")
templateEnv = Environment(loader=templateLoader)
TEMPLATE_FILE = os.path.join(os.path.dirname(__file__), 'cisco-sample.j2')
template = templateEnv.get_template(TEMPLATE_FILE)

print(template)
