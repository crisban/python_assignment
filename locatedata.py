
#########################################
## Cris Banuelos
## cris@banuelos.com
## 03/31/2017
##
## Requirements:
## Please use advanced scripting language (either Python or Ruby is
## preferred)
## Please implement a stand-alone script that does the following function:
##
## Input:
## taking an argument "root_dir" as a root directory to start traversing
## taking an argument "keyword" as a regular expression to detect a file
## contains an interested string
##
## Functionality:
## script should recursively walk the "root_dir" and detect all the files under
## that dir which contains "keywords" and count the number of files for each
## sub dir. All results should be saved in a key:value array with key being
## subdir string, and value being counts of files containing the keyword
##
## Output:
## An output array of all the data, for example {'a/b':6, 'a/b/c':7, '/a/b/c/d',0}
##
##
##  usage: python locatedata.py rootdir keyword
###########################################

import sys
import os
import glob
import fnmatch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#search through all files in given directory
def FileSearch(current, exp):
	#initialize count
	results = {}
	count = 0
	#list all files directory
	for filename in os.listdir(current):
		#check to make sure it is a file
		if os.path.isfile(filename):
			#open file, check for matches
			#with open(filename) as f:
				#ans = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
				#increment count if match found
				#if ans.find(exp) != -1:
					#count += 1
	#store count into array for given subdir
	#results[current] = count

	return results[current]



#Get root_dir and keyword
rootdir = sys.argv[1]            #input dir , cannot be "C:\root", only "root"
keyword = sys.argv[2]            #keyword - be sure to use * if needed

#init
match = []
total = 0
sub_count = 0

###########################################################################
##  Attempt 1
##
##  This only gave me a list of files and paths that contained the keyword
###########################################################################

#Recursively walk the directory that was called above, and scan the filenames
for root, subdir, files in os.walk(rootdir):
    if fnmatch.filter(files,keyword):
        sub_count = sub_count + 1               #count Subdirectory
        print sub_count
    for name in fnmatch.filter(files,keyword):  #loop through to find match
        match.append(os.path.join(root,name))   #append match array
        print os.path.join(root,name)           #print match to screen
        total = total + 1                       #match counter

print total  # total no of matches
print sub_count

#Output needs to be a dict

######################################################################
## Attempt 2
##
## Trying a different approach....not complete
#####################################################################

#Recursively walk the directory that was called above, and scan the filenames
for root, subdir, files in os.walk(rootdir):
    #Send root to function
    output[root] = FileSearch(root, keyword)

print output

#Output needs to be a dict


###################################################################
##  Plotting
###################################################################

#Plotting data
#plt.figure()
#plt.bar(subdirname,matchcount)
#plt.title('No. of Files in Directory')
#plt.ylabel('No. of Files')
#plt.xlabel('Subdirectory')
#plt.show()
#plt.savefig('plot.png')
