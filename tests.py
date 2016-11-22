"""
from tabulate import tabulate

text = "We will this story with introducing ourselves.I'l go first... I am the Narrator. And you are ?"

table = [["spam",42],["eggs",451],["bacon",0]]
headers = []
print tabulate(table, headers, tablefmt="plain")
print
print tabulate(table, headers, tablefmt="simple")
print
print tabulate(table, headers, tablefmt="grid")
print
print tabulate(table, headers, tablefmt="fancy_grid")
"""

import requests

r = requests.get('https://www.winmasters.com/', )
print r.status_code
