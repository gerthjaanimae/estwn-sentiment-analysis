#!/usr/bin/python3
import sys
import csv
import codecs

fout=codecs.open("estwn-eki-comparison.csv", "w"	, encoding="utf-8")

senti=[]
sentifile=sys.argv[1]
with open (sentifile) as fin:
	sentirows=csv.reader(fin, delimiter="\t")
	for row in sentirows:
		if "#" not in row[0]:
			senti.append(row)

sonastik=[]
file=sys.argv[2]
with open (file) as fin:
	rows=csv.reader(fin, delimiter=",")
	for row in rows:
		sonastik.append(row)
	

sonastik.pop(0)
for row in sonastik:
	sona=row[0]
	#Muutuja, mis näitab, kas sõna on wordnetis olemas.
	olemas=False
	for i in senti:
		sonad=i[4].split(";")
		for j in sonad:
			if j==sona:
				fout.write(sona+"\t"+row[1]+"\t"+i[4]+";"+i[2]+"\t"+i[3]+"\n")
				olemas=True
	if olemas==False:
		print (sona)
fout.close()
