# PhD Co-Citation Analysis
===================

Some python scripts for doing co-citation analysis on a bunch of PDFs. My use case is to analyse co-citation amongst the papers I cite in my PhD. This is a useful way to get an overview of whether the literature I'm building on is already connected, and to what extent I'm bridging interdisciplinary / research community divides.

## How?
My entire reference list is over 2000, but I have PDFs for about 1,500 of them. The first script (makebibs.py) uses pdf-extract to scrape references from the PDFs. I've produced a master bibliography of all my citations using mendeley's .bib export function. I've also renamed all the original PDFs using mendeley's 'organise' function. This creates a separate .bib file for every paper. The second script iterates through all these separate .bib files and writes them to a CSV file which stores the network graph.

## Visualise?

This graph could be visualised with Gephi or D3, but I've just chucked it into Google Fusion tables - they have a network graph visualisation function which works fine for these purposes.
