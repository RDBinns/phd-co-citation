"""put all phd pdfs in a folder
rename all files in bibtex format - authorSurname_year
optional: write a bash / python script which iterates through every pdf and cleans up the titles - removing co-authors (anything between ',' and _)
write a bash / python script which iterates through every pdf in the folder "pdf-extract extract-bib --resolved_references %s.pdf"
write a script which reads each .bib file, writes into a csv file two columns - the paper name (filename but remove '.pdf' and the citation name)
upload to google fusion tables."""

import os, sys, glob, copy
from os import path, access, R_OK  # W_OK for write permission.
from operator import itemgetter, attrgetter
import pprint
import bibtexparser

# we have a .bib file for every pdf. we need to add these to a CSV file (which will be our rudimentary network graph data store).

def addbib(bibfile):
	with open('%s.bib' % bibfile) as bibtex_file:
		bibtex_str = bibtex_file.read()
		bib_database = bibtexparser.loads(bibtex_str)
		citations = (bib_database.entries)
		print citations
		for citation in citations:
				citer = bibfile
				cited = citation["ID"] # minus the last four characters?
				entry = "%s," % bibfile + "%s" % cited + "\n"
				with open("archive6.csv", "a") as archive:
					archive.write(entry)
				print "archived entry %s" % entry

#column headings
with open("archive6.csv", "a") as archive:
	archive.write("Paper, Citation\n")

import glob
path = "*.bib"
for fname in glob.glob(path):
	bibfile = os.path.splitext(fname)[0]
	print bibfile
	addbib(bibfile)
