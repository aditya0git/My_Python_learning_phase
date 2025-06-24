# This script merges all valid PDF files in the current directory into a single file named merged_pdf.pdf.
# It skips invalid or corrupted PDFs and prints a message for each one. 

from pypdf import PdfWriter
from os import listdir

AllFiles = listdir()
AllPdfFiles = list(filter(lambda x : x.endswith(".pdf") or x.endswith(".PDF"), AllFiles))
j = len(AllPdfFiles)

new_file = PdfWriter()

k = 0
if j == 0 :
    print("There's no PDF in the current directory.")
else :
    for i in AllPdfFiles :
        try :
            new_file.append(i)
        except Exception :
            print(f"{i} is an invalid PDF")
        else :
            k += 1

if k != 0 :
    new_file.write("merged_pdf.pdf")
    print(f"\nThe {"valid " if k != j else ""}PDFs in the current directory has been merged to \"merged_pdf.pdf\".")
else :
    print(f"\nThere's no valid PDF in the currect directory.")
    
new_file.close()
