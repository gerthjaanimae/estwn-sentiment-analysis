#!/bin/bash
#set -o errexit
#Kontrollitakse, kas eurown moodul on juba alla laetud.
if ! [ -d eurown ]; then
echo  Giti abil eurown mooduli allalaadimine.
git clone https://gitlab.keeleressursid.ee/nemee/eurown.git
cp eurown/eurown.py eurown.py
fi
echo "Failide lahtipakkimine."
unzip -o ../required-files/archive.zip -d ../required-files/estwn/
unzip -o ../required-files/wn15-30-1.zip -d ../required-files
senti=../required-files/SentiWordNet_3.0.0_20130122.txt
pohisonastik=../required-files/Pohisonastik.csv
echo "EST-WN'i ja Sentiwordneti meelestatuse märgendite ühendamine."
./senti_estwn-map.py "$senti"
echo "Tulemus kirjutatud faili senti-estwn.csv"
echo "Tulemuste sortimine ja diagrammide joonistamine."
Rscript sort.R
echo "Paneme Estwn ja EKI sõnastiku kokku ja vaatame, kui palju sõnu on selliseid, mida Estwn-s ei ole, aga EKI-s on."
./compare-estwn-eki.py senti-estwn.csv $pohisonastik | wc -l
echo "Kontrollitakse, kui suur osa sõnadest lähevad omavahel vastuollu."
./estwn-eki-contradictions.sh > estwn-eki-contradictions.csv
echo "Vastuolud kirjutatud faili estwn-eki-contradictions.csv."
echo "Sentiwordneti ja Estwn xml faili ühendamine."
echo "Estwn xml faili allalaadimine."
wget -q https://gitlab.keeleressursid.ee/avalik/data/raw/master/estwn/estwn-et-2.0.0.beta.xml -O estwn-et-2.0.0.beta.xml
#Kuna järgmise skripti töö võtab mitu päeva aega, siis on järgmine rida välja kommenteeritud ning ülejäänud skriptide jaoks kasutatakse eelneval käivitamisel loodud väljundfaili.
#echo Estwn ja xml failis olevate sünohulkade vahelise ühendusfaili loomine.
#python map-senti-xml.py $senti map-senti-estwn-xml.csv
cp ../result-files/map-senti-xml.csv ./
echo Ühendusfaili võrdlemine esimeses etapis loodud failiga. Jäetakse välja need sünohulgad, millel juba meelestatuse märgendid olemas on.
python check-map.py senti-estwn.csv estwn-et-2.0.0.beta.xml map-senti-xml.csv > synsets-senti-xml.csv
echo "Sentiwordnetis ja xml failis olevate sünohulkade ühendamine. Väljundfailiks on senti-estwn2.csv."
python senti-estwn-xml.py $senti estwn-et-2.0.0.beta.xml synsets-senti-xml.csv > senti-estwn2.csv