#############################################
# Regular expression split                  #
# pattern matching and text processing      #
# Author : Ramu                             #
# File   : 05-regex-split.py                #
# Version: 1.0                              #
#############################################

import re

text = "c,c++,java,python"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)