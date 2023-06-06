## Requirements

- Python 3.x
- Flask

## Installation

#Create and activate a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


#Usage
flask run      
#or 
python app.py


#1. As a JSON REST API with endpoints GET /personal, GET /experience, GET /education  you can access :
#Web 
http://127.0.0.1:5000/personal
http://127.0.0.1:5000/experience
http://127.0.0.1:5000/education

#Or comand line 
curl http://127.0.0.1:5000/personal
curl http://127.0.0.1:5000/experience
curl http://127.0.0.1:5000/education

#As a Flask CLI command that prints the data to the console
#comand line 
flask print_cv