#############################################
# Regular expression match                  #
# pattern matching and text processing      #
# Author : Ramu                             #
# File   : 02-regex-match.py                #
# Version: 1.0                              #
#############################################

import re

text  = "The dog is white"
pattern = r"The"

match = re.match(pattern,text)

if match:
    print("match found:",match.group())
else:
    print("No match")    


   

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")