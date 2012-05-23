#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

def main(args):
	import Bootstrap as app
	global app
	app = app.Bootstrap(args)
	app.exec_()

if __name__ == "__main__":
	main(sys.argv)
