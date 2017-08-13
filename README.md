# testdatagen

### Django web app to generate test data

#### Usage
i) Clone the repo  
ii) Change to testdatagen directory (top-level one containing manage.py and README.md)  
iii) Install requirements: pip install -r requirements.txt  (Not required if you already have Django, Faker and Gunicorn)  
iv) Run the django server: gunicorn testdatagen.wsgi --log-file -  
v) Navigate to (http://localhost:8000/json) and follow the steps

#### Supported Formats
- JSON
- CSV

#### Demo
Try it out [here](https://testdatagen.herokuapp.com/json/) for JSON and [here](https://testdatagen.herokuapp.com/csv/) for CSV  
(*The demo app supports generation of up to 50 rows and 5 fields*)
