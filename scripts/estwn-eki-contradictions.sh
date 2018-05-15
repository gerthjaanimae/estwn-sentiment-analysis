#!/bin/bash
echo "#Sõnad, kus sentiwordnet ja eki emotsioonidetektor lähevad vastuollu."
echo "#wordnetis positiivsed, aga ekis neutraalsed."
python compare-sorted.py tugevalt-positiivsed.csv | grep 'dom neutr'
python compare-sorted.py  moodukalt-positiivsed.csv | grep 'dom neutr'
echo "#wordnetis positiivsed, aga ekis negatiivsed."
python compare-sorted.py tugevalt-positiivsed.csv | grep 'dom neg'
python compare-sorted.py moodukalt-positiivsed.csv | grep 'dom neg'
echo "#wordnetis positiivsed, aga ekis vastuolulised."
python compare-sorted.py tugevalt-positiivsed.csv | grep '\tvastuolu\t'
python compare-sorted.py moodukalt-positiivsed.csv | grep '\tvastuolu\t'
echo "#wordnetis neutraalsed, aga ekis positiivsed."
python compare-sorted.py neutraalsed.csv | grep 'dom pos'
echo "#wordnetis neutraalsed, aga ekis negatiivsed."
python compare-sorted.py neutraalsed.csv | grep 'dom neg'
echo "#wordnetis vastuolulised, aga ekis positiivsed."
python compare-sorted.py vastuolulised.csv | grep 'dom pos'
echo "#wordnetis vastuolulised, aga ekis neutraalsed."
python compare-sorted.py vastuolulised.csv | grep 'dom neutr'
echo "#wordnetis vastuolulised, aga ekis negatiivsed."
python compare-sorted.py vastuolulised.csv |grep 'dom neg'
echo "#wordnetis negatiivsed, aga ekis positiivsed."
python compare-sorted.py tugevalt-negatiivsed.csv | grep 'dom pos'
python compare-sorted.py moodukalt-negatiivsed.csv | grep 'dom pos'
echo "#wordnetis negatiivsed, aga ekis neutraalsed."
python compare-sorted.py tugevalt-negatiivsed.csv | grep 'dom neutr'
python compare-sorted.py moodukalt-negatiivsed.csv | grep 'dom neutr'
echo "#wordnetis negatiivsed, aga ekis vastuolulised."
python compare-sorted.py tugevalt-negatiivsed.csv | grep '\tvastuolu\t'
python compare-sorted.py moodukalt-negatiivsed.csv | grep '\tvastuolu\t'
echo ""
