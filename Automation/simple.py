#!/usr/bin/env python

from jinja2 import Template

name = 'Simba'
age = 28

tm = Template("My name is {{ name }} and I am {{ age }}")
msg = tm.render(name=name, age=age)

print(msg)
