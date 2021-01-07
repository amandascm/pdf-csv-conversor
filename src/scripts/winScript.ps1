#install virtualenv (python)
py -m pip install --user virtualenv

#check if virtual environment has already been created
$x = Test-Path .venv
if($x -eq $FALSE){
    python -m venv .venv
    .\.venv\Scripts\activate
    python -m pip install -r requirements.txt
    deactivate
    Write-Host "NO FOLDER WITH THIS NAME"
}
#activate virtual environment and run program
.\.venv\Scripts\activate
python main.py
deactivate