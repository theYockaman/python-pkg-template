# Package Name
> Description of Package and ability built into the application. 


## VENV
### Create a VENV
```
python -m venv venv
```
### Activate a VENV

#### MACOS / Linux
```
source venv/bin/activate
```


#### Windows
```
# Command Prompt (cmd.exe)
venv\Scripts\activate.bat

# Powershell
.\venv\Scripts\Activate.ps1
```




## Build the Package 
```
# Install build tool if not installed
pip install --upgrade build 

# Build source and wheel distributions 
python -m build
```

### Add Requirements Built in the VENV
```
pip freeze > requirements.txt
```


## Install Package
```
pip install git+https://github.com/yourusername/my_package.git
```