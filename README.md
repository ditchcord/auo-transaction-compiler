# auo-transaction-compiler

### Automatically organize all TartanConnect accounting records into categories

## Obtaining TartanConnect accounting records
1. Rename the file to something easy to type like **record1** or whatever
2.

## Quick Start
1. Install Python 3.10 or newer
2. Clone the repository to your device
3. Move your record .csv to the **private** folder (so that git pushes won't expose ppl's data)
3. Open main.py
4. Type the path of the file eg. private/record5
4. A new folder with the current date & time will be created in the private folder with bunch of CSVs

## The output .csv's
- **gift.csv** and **agency.csv** show all records for their respective accounts since the beginning of time (like 2019)
- every other file is a list of items matching a category found within the gift or agency account
- there are **8** spending categories and **3** revenue categories. Revenue categories start with **REVENUE--**
- There won't be a file for any given account category if the program didn't find any items fitting into that category.

## Why are there expenses in some revenue categories
- Some categories like JFC and donations include expenses related to funding corrections or refunds and admin fees
- It's just easier to treat those kinds of expenses as subtractions from the revenue
- Otherwise, it might be a categorization mistake

## Troubleshooting
If items are being put into the wrong category, go to the **change2ndColumnToCategory** function definition and add or reorganize the dictionaries.

Email wellsjason543 at gmail dot com for issues or questions

#

Copyright (c) 2025 Jason H. Wells

MOST RIGHTS RESERVED - DISTRIBUTION PROHIBITED

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to use, modify, or merge the Software on 
their personal computer. The following rights are reserved: To 
publish, distribute, sublicense, and/or sell copies of the 
Software or modified versions of the Software, including 
anything merged with the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE.