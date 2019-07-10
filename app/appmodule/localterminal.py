#!/usr/bin/env python
import os
from platform import uname
class LocalTerminal(object):
	"""docstring for LocalTerminal"""
	def __init__(self):
		super(LocalTerminal, self).__init__()
		if uname()[0] == "Linux":
			os.system("xfce4-terminal")
		elif uname()[0] == "Windows":
			os.system("start cmd")
		else:
			print("error")
