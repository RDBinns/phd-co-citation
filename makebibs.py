import os, sys, glob, copy
from os import path, access, R_OK  # W_OK for write permission.
from operator import itemgetter, attrgetter
import pprint
import bibtexparser

# define the makebib function which extracts references from pdfs
def makebib(filename):
	bashCommand = "pdf-extract extract-bib --resolved_references %s" % filename
	os.system(bashCommand)

#make a list of paper names from the master bibtex file
filenames = []
with open('PhD_citations.bib') as bibtex_file:
	bibtex_str = bibtex_file.read()
	bib_database = bibtexparser.loads(bibtex_str)
	citations = (bib_database.entries)
	for citation in citations:
		cited = citation["ID"]
		print cited
		filenames.append(cited)

filenames = filter(None, filenames)
print filenames

#	extract the ids

import glob
path = "*.pdf"

matches = 0
nomatches = 0

for fname in glob.glob(path):
#	if fname splitex matches something in bib, continue, if not, discard it.
	name = os.path.splitext(fname)[0]
	print name
	print type(name)
#find rough string matches
	for filename in filenames:
#		filename = filename[:-4]
		if name[:-5] in filename:
			print "found possible match for %s in %s" % (name, filename)
			matches = matches + 1
			makebib(fname)
		else:
#			print "didn't find a match for %s" % name
			nomatches = nomatches + 1

print matches
print nomatches
