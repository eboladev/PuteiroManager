#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from app.Controllers.Clients_Controller import *

def main():
	c = Clients_Controller()
	c.listAll()
	#c.listOne(2)

if __name__ == '__main__':
	main()
