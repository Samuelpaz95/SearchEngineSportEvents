# Search Engine for Sports Events

This is a practical work for the semantic web subject

# Start web app

## install  python libraries

requires having python installed

Linux terminal:
```bash
# inside the project folder, create a virtual enviroment
python3 -m venv myenv
# activate the virtual enviroment
source ./myenv/bin/activate
# install libraries
pip install -r requirements.txt
```
Windows cmd: 
```bash
# create a virtual enviroment
python3.exe -m venv myenv
# activate the virtual enviroment
.\myenv\Scripts\activate.bat
# install libraries
pip.exe install -r requirements.txt
```

## start the project

Only debug mode:
```bash
python manager.py runserver
```
output:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 160-612-167
```