#!/usr/bin/python3
import csv
import requests
import json
import time
from bs4 import BeautifulSoup
import codecs
import sys
senti=[]
sentifile=sys.argv[1]
out=""
try:
	with open(sys.argv[2]) as fin:
		out=fin.read()
except:
	pass
#Loend, kus hoitakse juba kontrollitud ridu - juhuks kui skript peaks vahepeal kokku jooksma.
checked=""
try:
	with open("checked.txt") as fin:
		checked=fin.read()
except:
	pass

with open (sentifile) as fin:
	sentirows=csv.reader(fin, delimiter="\t")
	for row in sentirows:
		if "#" not in row[0]:
			senti.append(row)

#senti=senti[20:40]
count=0
for row in senti:
	id=row[1].lstrip("0")+"-"+row[0]
	#print (id)
	if row[0]+"\t"+row[1] in out or id in checked:
		continue
	with open ("checked.txt", "a") as fout:
		fout.write(id+"\n")
	
	time.sleep(6)
	try:
		x=requests.get("http://estwn-test.keeleressursid.ee/api/v1/extrel/?lexid=9&system=ILI-3.0&reltype=eq_synonym&label="+id)
	except:
		time.sleep(500)
		x=requests.get("http://estwn-test.keeleressursid.ee/api/v1/extrel/?lexid=9&system=ILI-3.0&reltype=eq_synonym&label="+id)
	x=json.loads(x.text)['results']
	if len(x)==0:
		count+=1
		continue
	x=x[0]
	time.sleep(6)
	try:
		y=requests.get("http://estwn-test.keeleressursid.ee/api/v1/synset/"+str(x['synset']))
	except:
		time.sleep(500)
		y=requests.get("http://estwn-test.keeleressursid.ee/api/v1/synset/"+str(x['synset']))
	#print (y.text)
	y=json.loads(y.text)
	label=y['label']
	line="\t".join([row[0], row[1], label])+"\n"
	with open (sys.argv[2], "a") as fout:
		fout.write(line)
fout.close()
print (count)