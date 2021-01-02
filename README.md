# pdf to csv conversor

This project aims to convert a set of pdf files to csv (if one of them has more than one table: multiple csv files will be generated). You can run this project on linux or windows.

## Dependencies

- [Python](https://www.python.org/downloads/)
- [Java](https://www.java.com/pt-BR/download/manual.jsp)

## Execution

### Windows
- Clone or download the repository
- Open a PowerShell in the **src** directory of the project
- Make sure your system is configured to allow script execution
- Run the command:
	```
	 .\winScript.ps1
	```

### Linux
- Clone or download the repository
- Open a terminal in the **src** directory of the project
- Run the commands:
	```
	 chmod +x script.sh
	```
	``` 
	./script.sh
	```
The first execution will prepare a virtual environment and create the **src/pdf** directory : where you must include your pdf files and reexecute the project.
All tables will be at the **src/table** directory inside a specific folder which name corresponds to the name of the document that contained them.