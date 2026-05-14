#############################################
# Regular expression findall                #
# pattern matching and text processing      #
# Author : Ramu                             #
# File   : 01-regex-findall.py              #
# Version: 1.0                              #
#############################################


import re

text = " The grass is green in the field"
Pattern = r"green"

search = re.search(Pattern,text)

print(search)

if search:
   print("pattern found:",search.group())
else:
   print("pattern not found")   


   

