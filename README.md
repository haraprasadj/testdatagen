# testdatagen

### Django web app to generate test data

#### Usage
i) Clone the repo  
ii) Change to testdatagen directory (top-level one containing manage.py and README.md)  
iii) Install requirements: pip install -r requirements.txt  (Not required if you already have Django, Faker and Gunicorn)
iv) Run the django server: gunicorn testdatagen.wsgi --log-file -  
v) Navigate to (http://localhost:8000/json) and follow the steps

#### Note: Support available only for JSON format now

#### Demo
Try it out [here](https://testdatagen.herokuapp.com/json/)  
The demo app supporting 100 rows and 5 fields at the most
