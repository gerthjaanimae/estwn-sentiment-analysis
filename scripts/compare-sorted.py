import csv
import codecs
import sys

senti=[]
sentifile=sys.argv[1]
with open (sentifile) as fin:
	sentirows=csv.reader(fin, delimiter="\t")
	for row in sentirows:
		senti.append(row)

sonastik=[]
file="../required-files/Pohisonastik.csv"
with open (file) as fin:
	rows=csv.reader(fin, delimiter=",")
	for row in rows:
		sonastik.append(row)
	
#eemaldame päised
sonastik.pop(0)
senti.pop(0)

print("sonaliik\tidentifikaator\tpos_skoor\tneg_skoor\teki_skoor\tsonad\tnaited")
for i in senti:
	detskoor=""
	#print (i)
	try:
		sonad=i[4].split(";")
		for sona in sonad:
			for rida in sonastik:
				if sona==rida[0]:
					#print(sona, rida[0], "#")
					detskoor=rida[1]
		line=i[:4]+[detskoor]+i[4:]
		line="\t".join(line)
	except:
		print(i)
		line="\t".join(i)
	print(line)
	
	
