#!/usr/bin/python3
import csv
import eurown
import sys
#Funktsioon, mis võtab välja read kindla sõnaliigiga senti-wordnetist
def getSenti(pos):
	senti={}
	sentifile=sys.argv[1]
	with open (sentifile) as fin:
		sentirows=csv.reader(fin, delimiter="\t")
		for row in sentirows:
			if "#" not in row[0] and row[0]==pos:
				senti[row[1]]=row
	return senti
def getMapping(mappingfile):
	mapping={}
	with open (mappingfile) as fin:
		rows=csv.reader(fin, delimiter=" ")
		for row in rows:
			mapping[row[0]]=row[1]
	return mapping

#Dictid, mis sisaldavad sentiwordnetist saadud ridu. Võti on offset.
sAdj=getSenti("a")
sAdv=getSenti("r")
sNoun=getSenti("n")
sVerb=getSenti("v")

#Dictid, kus hoitakse mappingu infot. Võti on vana versiooni identifikaator, väärtus on uue oma.
mAdj=getMapping("../required-files/wn15-30-1.adj")
mAdv=getMapping("../required-files/wn15-30-1.adv")
mNoun=getMapping("../required-files/wn15-30-1.noun")
mVerb=getMapping("../required-files/wn15-30-1.verb")

#Funktsioon, mis teeb sünohulga identifikaatori kaheksakohaliseks.
def convertOffset(off):
	if len(off)==8:
		return off
	else:
		return convertOffset(str(0)+off)
lex=eurown.read_file("../required-files/estwn/kb73-utf8.norm")
fout=open("senti-estwn.csv", "w")
#Kirjutame tabeli päise
fout.write("sonaliik\tidentifikaator\tpos_skoor\tneg_skoor\tsonad\tnaited\n")
def convertEst(pos, senti, map):

	for synset in lex:
		for i in synset.eq_links:
			offset=i.target_concept.wordnet_offset
			if offset==None:
				continue
			offset=convertOffset(offset)
		if synset.pos==pos:
			try:
				row = senti[map[offset]]
			except KeyError:
				#print (offset)
				continue
			fout.write("\t".join(row[:-2])+"\t")
			literals=[]
			glosses=[]
			for l in synset.variants:
				literals.append(l.literal)
				if l.gloss !=None:
					glosses.append(l.gloss)
			fout.write(";".join(literals)+"\t")
			fout.write(";".join(glosses)+"\n")

convertEst("a", sAdj, mAdj)
convertEst("b", sAdv, mAdv)
convertEst("n", sNoun, mNoun)
convertEst("v", sVerb, mVerb)