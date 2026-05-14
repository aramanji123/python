#############################################
# Regular expression search                 #
# pattern matching and text processing      #
# Author : Ramu                             #
# File   : 04-regex-search.py               #
# Version: 1.0                              #
#############################################



import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")