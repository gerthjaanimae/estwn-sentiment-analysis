import sys
with open(sys.argv[2]) as fin:
	estwn=fin.read()
with open(sys.argv[1]) as fin:
	vana=fin.read()
with open(sys.argv[3]) as fin:
	for line in fin:
		synset=line.split("\t")[:2]
		new=line.split("\t")[2]
		new=new.strip()
		synset="\t".join(synset)
		if synset not in vana and new in estwn:
			print (line.strip())
			#print (new)
