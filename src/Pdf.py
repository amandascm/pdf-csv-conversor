import tabula
import pandas as pd
import json
import os
import logging
logging.basicConfig(filename='info.log', filemode='w', level=logging.DEBUG)

class Pdf:
	def __init__(self, fileName):
		#initialize attributes
		self.fileTables = []
		self.fileName = fileName
		logging.info(f"{self.fileName}: attributes were initialized")
		#find pdf tables
		self.extractTables()

	def extractTables(self):
		while True:
			try:
				self.fileTables = tabula.read_pdf(f"pdf/{self.fileName}", pages="all")
				logging.info(f"{self.fileName}: {len(self.fileTables)} tables were found")
				break
			except:
				logging.error(f"{self.fileName}: it was not possible to extract tables from file")
				break

	def showTablesSamples(self):
		counter = 0
		print(f"\n--------------{self.fileName} tables samples (5 last rows)--------------\n")
		for dataframe in self.fileTables:
			counter+=1
			print(f"\nTABLE {str(counter)}\n{dataframe.tail()}\n\n")

	def saveTables(self):
		try:
			os.mkdir(f"table")
			logging.info(f"{self.fileName}: created table directory")
		except:
			logging.warning(f"{self.fileName}: table directory already exists")
		try:
			os.mkdir(f"table/{self.fileName[0:-4]}")
			logging.info(f"{self.fileName}: created table/{self.fileName[0:-4]} directory")
		except:
			logging.warning(f"{self.fileName}: table/{self.fileName[0:-4]} directory already exists")
		print(f"\n--------------{self.fileName} saving tables process--------------\n")
		print(f"\nThere are {len(self.fileTables)} tables to be saved\n")
		counter = 0
		for table in self.fileTables:
			counter += 1
			if len(table) > 0:
				table.to_csv(path_or_buf=f"table/{self.fileName[0:-4]}/tab{counter}.csv", index='False')
				print(f"Table {counter} saved...\n")
			else:
				logging.warning(f"{self.fileName}: table {counter} is empty: not saved...\n")
				print(f"Table {counter} is empty: not saved...\n")
		logging.info(f"{self.fileName}: finished saving tables process")
