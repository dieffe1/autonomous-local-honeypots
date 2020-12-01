#!/usr/bin/env python

import os
import argparse

parser = argparse.ArgumentParser(description="HoneyTest", epilog="Version 0.1")
parser.add_argument('-p', '--port', help='listening port', action='store', required=True)

args = parser.parse_args()

options = [ "2", "3", "2", args.port,
		"Be Careful.", "y",
		"logs_honeypot.txt", "n" ]
 
str = "\n".join(options)

os.system(("printf '%s' | ./pentbox-1.8/pentbox.rb > /dev/null" % (str)))

#print(str)

