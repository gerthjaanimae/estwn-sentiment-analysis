#!/usr/bin/python3
from bs4 import BeautifulSoup
import codecs
from collections import defaultdict
import sys
estwn=""
estwnfile=sys.argv[2]
map={}
estwnd=defaultdict(str)
examples=defaultdict(str)
with open(sys.argv[3]) as fin:
	for line in fin:
		line=line.split("\t")
		synset=line[2].strip()
		synset="estwn-et-"+synset
		map[synset]="\t".join(line[:2])
senti=[]
with open(sys.argv[1]) as fin:
	for line in fin:
		senti.append(line)
for i in map:
	for j in senti:
		if j.startswith(map[i]):
			j=j.split("\t")
			map[i]="\t".join(j[:4])
with codecs.open(estwnfile, encoding="utf-8") as fin:
	estwn=BeautifulSoup(fin.read(), "lxml")
estwn=estwn.find_all("lexicalentry")
for lex in estwn:
	lemma=lex.find('lemma')['writtenform']
	senses=lex.find_all('sense')
	for sense in senses:
		synset=sense['synset']
		if synset in map:
			try:
				example=sense.find("example").get_text()
				examples[synset]+=";"+example	
			except:
				pass
			estwnd[synset]+=";"+lemma
			
for key in estwnd:
	#print (key)
	estwnd[key]=estwnd[key].lstrip(";")
	examples[key]=examples[key].lstrip(";")
	id=map[key]
	#print (estwnd[key])
	#print (examples[key])
	print ("%s\t%s\t%s" % (map[key], estwnd[key], examples[key]))
