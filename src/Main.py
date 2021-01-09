import PdfRepository as pdfRepository
import Pdf as pdf
import os
import logging
logging.basicConfig(filename='info.log', filemode='w', level=logging.DEBUG)

def main():
    try:
        os.mkdir(f"pdf")
    except:
        logging.warning(f"Main: pdf directory already exists")
    root = os.path.join('pdf')
    pdfRepo = pdfRepository.PdfRepository()
    for directory, subdir_list, file_list in os.walk(root):
        for name in file_list:
            pdfRepo.addPdf(pdf.Pdf(name))
        pdfRepo.showAndSaveTables()

if __name__ == "__main__":
    main()