import pdfTables as pdf
import os

try:
	os.mkdir(f"pdf")
except:
	print(f"\nWARNING: pdf directory already exists\n")
root = os.path.join('pdf')
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        pdfFile = pdf.pdfTables(name)