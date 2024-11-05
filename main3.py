import camelot
import csv
import pandas as pd
from common_utils import *

#calling table scope

PDF_FILE_READER = "liste-immeubles-assujettis-vente.pdf"
NEW_FORMATED_TABLE = "immeuble_new__.csv"
tables = camelot.read_pdf(PDF_FILE_READER, pages= "all",  flavor='stream')




#tables.export(NEW_FORMATED_TABLE)

print(tables[0])
# for data in tables:
#     print(data[0])


# Extraction and regrouping of various file category

"""
FILE_DOC_01 = "immeuble_new__-page-1-table-1.csv"
FILE_DOC_02 = "immeuble_new__-page-2-table-1.csv"
FILE_DOC_03 = "immeuble_new__-page-3-table-1.csv"
FILE_DOC_04 = "immeuble_new__-page-4-table-1.csv"
FILE_DOC_05 = "immeuble_new__-page-5-table-1.csv"

"""


#open first file
with open(FILE_DOC_01) as documentFile:
    immeuble_data = csv.reader(documentFile)
    print(" Some common data output")
    #print(immeuble_data)

    immeunleO1 = [ ]
    for imma1 in immeuble_data:
        if imma1 != 0:
            immeunleO1.append(imma1)
#open second file
with open(FILE_DOC_02, 'r') as documentFile02:
    immeuble_data02 = csv.reader(documentFile02)
    print(" Some common data output")

    immeunleO2 = [ ]
    for imma2 in immeuble_data02:
        if imma2 != 0:
            immeunleO2.append(imma2)
    #print(immeunleO2)


#open tkird file


with open(FILE_DOC_03, 'r') as documentFile03:
    immeuble_data03 = csv.reader(documentFile03)
    print(" Some common data output")

    immmeuble03 = [ ]
    for imma3 in immeuble_data03:
        if imma3 != 0:
            immmeuble03.append(imma3)


with open(FILE_DOC_04, 'r') as documentFile04:
    immeuble_data04 = csv.reader(documentFile04)
    print(" Some common data output")

    immmeuble04 = [ ]
    for imma4 in immeuble_data04:
        if imma4 != 0:
            immmeuble04.append(imma4)
with open(FILE_DOC_05, 'r') as documentFile05:
    immeuble_data05 = csv.reader(documentFile05)
    print(" Some common data output")

    immmeuble05 = [ ]
    for imma5 in immeuble_data05:
        if imma5 != 0:
            immmeuble05.append(imma5)


with open(FILE_DOC_06, 'r') as documentFile06:
    immeuble_data06 = csv.reader(documentFile06)
    print(" Some common data output")

    immmeuble06 = [ ]
    for imma6 in immeuble_data06:
        if imma6 != 0:
            immmeuble04.append(imma6)
with open(FILE_DOC_07, 'r') as documentFile07:
    immeuble_data07 = csv.reader(documentFile07)
    print(" Some common data output")

    immmeuble07 = [ ]
    for imma7 in immeuble_data07:
        if imma7 != 0:
            immmeuble07.append(imma7)
with open(FILE_DOC_08, 'r') as documentFile08:
    immeuble_data08 = csv.reader(documentFile08)
    print(" Some common data output")

    immmeuble08 = [ ]
    for imma8 in immeuble_data08:
        if imma8 != 0:
            immmeuble08.append(imma8)
with open(FILE_DOC_09, 'r') as documentFile09:
    immeuble_data09 = csv.reader(documentFile09)
    print(" Some common data output")

    immmeuble09 = [ ]
    for imma9 in immeuble_data09:
        if imma9 != 0:
            immmeuble09.append(imma9)
with open(FILE_DOC_010, 'r') as documentFile010:
    immeuble_data010 = csv.reader(documentFile010)
    print(" Some common data output")

    immmeuble010 = [ ]
    for imma10 in immeuble_data010:
        if imma10 != 0:
            immmeuble010.append(imma10)
with open(FILE_DOC_011, 'r') as documentFile011:
    immeuble_data011 = csv.reader(documentFile011)
    print(" Some common data output")

    immmeuble011 = [ ]
    for imma11 in immeuble_data011:
        if imma11 != 0:
            immmeuble011.append(imma11)

#-----------------------------------------------
with open(FILE_DOC_012, 'r') as documentFile012:
    immeuble_data012 = csv.reader(documentFile012)
    print(" Some common data output")

    immmeuble012 = [ ]
    for imma12 in immeuble_data012:
        if imma12 != 0:
            immmeuble012.append(imma12)
#-----------------------------------------------







# immeunleO1.append(immeunleO2)

print(" 0011 scope here +++ ")
print("\n")
print("\n")
#print(immeunleO1)
FINAL_ARRAY = [ immeunleO1, immeunleO2,
                immmeuble03, immmeuble04,
                immmeuble05, immmeuble06,
                immmeuble07, immmeuble08,
                immmeuble09, immmeuble010,immmeuble011,immmeuble012
                ]
# calling pandas for dataFrame series scope
#using list comprehension

def nesterInToNe(someNestedList):
    return [item for sublist in someNestedList for item in sublist]

final_out_put = nesterInToNe(FINAL_ARRAY)
#print the fianla result
print(" --- FINAL OUT PUT ---- RESULT -- ")
#print(len(final_out_put))




dataFrame = pd.DataFrame(data= final_out_put)
print(dataFrame)

# convert documents to csv using csv

to_csv_name_file_scope = "000000_testing.csv"


dataFrame.to_csv(to_csv_name_file_scope, index= False)













    
    




