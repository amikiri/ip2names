#! /usr/bin/env python3

''' 
ip2names.py - version and date see below
Author : Micheal Beatty - mike at mwbeatty.org

Should probably use options so user can specify whether or not
they are using an input file. Maybe for a future release.
'''
import os
import sys
import socket


def gethostname(x, y):
	# This works for the most part but breaks when hostname not found
	for i in input_file:
	    i = i.strip()	#removes the newline character
	    #This is necessary to account for situations 
	    #where hostname is not found
	    try:
	        name_info = socket.gethostbyaddr(i)
	        output_file.write(' '.join(str(s) for s in name_info) + "\n")
	    except socket.herror as err:
	        output_file.write(i + ' ' + str(err) + '\n')
	        continue	



def main():
	''' gets input and output file and passes them to the 
	function that will resolve the ip address'''

	input_file = open(sys.argv[1], "r")
	output_file = open(sys.argv[2], 'a')
	gethostname(input_file, output_file)
	output_file.close()


if __name__ == "__main__":
	main()