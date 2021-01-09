import json
import Pdf as pdf
import logging
logging.basicConfig(filename='info.log', filemode='w', level=logging.DEBUG)

class PdfRepository:
	def __init__(self):
		configFile = open("config.json")
		self.config = json.load(configFile)
		self.pdfList = []

	def addPdf(self, obj):
		if isinstance(obj, pdf.Pdf):
			self.pdfList.append(obj)
			logging.info(f"PdfRepository: {obj.fileName} added to repository")
		else:
			logging.error(f"PdfRepository: cannot add {type(obj)} to repository")


	def removePdf(self, obj):
		repoSize = len(self.pdfList)
		self.pdfList = filter(lambda p:p.fileName != obj.fileName, self.pdfList)
		if len(self.pdfList) < repoSize:
			logging.info(f"PdfRepository: {obj.fileName} successfully removed")
		else:
			logging.error(f"PdfRepository: {obj.fileName} could not be removed")

	def showAndSaveTables(self):
		for p in self.pdfList:
			if self.config["printSamplesOnTerminal"] is True:
				p.showTablesSamples()
			p.saveTables()
		logging.info(f"PdfRepository: all existing tables in repository's files were saved")