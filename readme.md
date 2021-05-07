## Introduction
Web scraping programme
Extract all category id in the Harmonized Tariff Schedule of the United States from 1994 to 2009
output format: csv
url: https://usitc.gov/tata/hts/archive/index.htm

## Run
1. run download_pdf.py to get all trade data pdf
2. run pdf_to_csv_data.py to get the csv data


## Logic
1. Regular pattern of pdf address

for loop 1994-2009
for loop chapter 01-99(special situation 991-995,991-997)

https://www.usitc.gov/tata/hts/archive/9600/960c14.pdf
https://www.usitc.gov/tata/hts/archive/0000/000c01.pdf
https://www.usitc.gov/tata/hts/archive/0100/0100c01.pdf
https://www.usitc.gov/publications/docs/tata/hts/bychapter/0500c01.pdf
https://www.usitc.gov/tata/hts/archive/9400/940c991.pdf
https://www.usitc.gov/tata/hts/archive/0100/0100c99.pdf

2. Data in pdf

use pdfplumber to transform pdf to text

use regular expression to get id
