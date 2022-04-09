# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:53:16 2022

@author: brmzn
"""

import glassdoor_scrapper as gs
import pandas as pd

path = "C:/Users/brmzn/Downloads/Compressed/chromedriver_win32_3/chromedriver.exe"

df = gs.get_jobs("data scientist", 15, False, path, 15)

df