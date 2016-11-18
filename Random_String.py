#!/usr/bin/python
#ref:http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python 

import string
import random
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size)) 
    
id_generator()
id_generator(3, "6793YUIO")
