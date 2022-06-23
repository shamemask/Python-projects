#!/usr/bin/env python
import os
try:
    import readline
except:
    import pyreadline
    
from pprint import pprint

from flask import *
from app import *

os.environ['PYTHONINSPECT'] = 'True'