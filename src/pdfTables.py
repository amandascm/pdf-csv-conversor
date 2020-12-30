import tabula
import pandas as pd
import json
import os
import logging
logging.basicConfig(filename='info.log', filemode='w', level=logging.DEBUG)

class pdfTables():
	def __init__(self, fileName):
		#initialize attributes
		self.fileName = fileName
		configFile = open("config.json")
		self.config = json.load(configFile)
		logging.info(f"{self.fileName}: attributes were initialized")

		#find pdf tables
		self.getTablesFromFile()

		#start processment
		self.tablesProcessment()

	def getTablesFromFile(self):
		while True:
			try:
				self.fileTables = tabula.read_pdf(f"pdf/{self.fileName}", pages="all")
				logging.info(f"{self.fileName}: {len(self.fileTables)} tables were found")
				break
			except:
				logging.error(f"{self.fileName}: it was not recognized as a PDF")

	def showTablesSamples(self):
		counter = 0
		print(f"\n--------------{self.fileName} tables samples (5 last rows)--------------\n")
		for dataframe in self.fileTables:
			counter+=1
			print(f"\nTABLE {str(counter)}\n")
			print(dataframe.tail())
			print("\n\n")

	def saveTables(self):
		try:
			os.mkdir(f"table")
		except:
			logging.warning(f"{self.fileName}: table directory already exists")
		try:
			os.mkdir(f"table/{self.fileName[0:-4]}")
		except:
			logging.warning(f"{self.fileName}: table/{self.fileName[0:-4]} directory already exists")
		print(f"\n--------------{self.fileName} saving tables process--------------\n")
		print(f"\nWe found {str(len(self.fileTables))} table(s)\n")
		if self.config["saveAllTables"] is True:
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
		else:
			print("\nIf you want to save any table before applying operations on their data, type their number and the desired file name (the name cannot have any white space).\nExample:\n3 table3\nOtherwise, type 'n'\n")
			#save the desired tables in csv files (inside tables directory)
			while True:
				numbNameTable = input()
				if numbNameTable != 'n':
					listNumbName = numbNameTable.split(' ')
					if len(listNumbName) == 2:
						index = int(listNumbName[0])
						tableName = listNumbName[-1]
						if index in range(1,len(self.fileTables)+1):
							if len(self.fileTables[index-1]) > 0:
								self.fileTables[index-1].to_csv(index='False', path_or_buf=f"table/{self.fileName[0:-4]}/{tableName}.csv")
								print(f"Table {index} saved...\n")
							else:
								print(f"Table {index} is empty: not saved...\n")
						else:
							print("ERROR: You must type a valid table number")
					else:
						print("ERROR: You must type an integer number and a file name separated by a white space")
				else:
					break

	def tablesProcessment(self):
		if self.config["printSamplesOnTerminal"] is True:
			#show samples of found tables
			self.showTablesSamples()

		#check if user wants to save any table
		self.saveTables()
		
	