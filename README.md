# eml_sentense_extractor
Extracts sentenses from eml files (e-mails).


Use:
find ../email | grep eml | python extract_sentences.py  > email.txt

Tested with python 3.6

Requires:
langdetect nltk
