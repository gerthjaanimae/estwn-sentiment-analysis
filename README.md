# estwn-sentiment-analysis
The repository containing scripts for my master thesis and other files related to them.
The electronic version of the master thesis can be found at 
# Structure of the repository
The repository contains following files and directories:
* scripts - scripts for the master thesis. For reproducing the results of the practical part of the thesis, run "all-steps.sh".
* result-files
** senti-estwn.csv - Contains Estonian wordnet synsets with sentiment scores derived from Sentiwordnet 3.0.
** senti-estwn2.csv - Contains additional Estonian Wordnet synsets with sentiment scores. (See the master thesis for more information).
** map-senti-xml.csv - Mappings between Princeton Wordnet 3.0 synsets and and the latest Estonian Wordnet (in XML-format).
** estwn-eki-comparison.csv - Comparison between Wordnet and Emotsioonidetektor, created by EKI.
** estwn-eki-contradictions.csv - Contains words which have conflicting sentiment values between Wordnet and Emotsioonidetektor.
* required-files - Files required for running the scripts which cannot be downloaded automatically or which are no longer available.
** archive.zip- Older version of Estwn required for running the script. Can be downloaded from
**Pohisonastik.csv - Basic dictionary for EKI emotsioonidetektor. Received from Hille Pajupuu.
** SentiWordNet_3.0.0_20130122.txt - Sentiwordnet file. Can be downloaded from
** wn15-30-1.zip and wn30-15-1.zip - mapping files between Wordnet version 1.5 and 3.0.
