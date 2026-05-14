#############################################
# Regular expression replace                #
# pattern matching and text processing      #
# Author : Ramu                             #
# File   : 03-regex-replace.py              #
# Version: 1.0                              #
#############################################

import re

text = " The roses are white"

pattern = r"white"

replacement = "red"

new_text = re.sub(pattern,replacement,text)

print("new text :",new_text)

