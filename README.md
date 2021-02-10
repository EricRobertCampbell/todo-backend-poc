# Django Backend POC

- To stand up the backend locally:
	From the root folder of the repo
	- Create and activate your venv
	```
	python -m venv venv
	.\venv\Scripts\activate
	```
	- Install the requirements
	```
	pip install -r .\requirements.txt
	```
	- Stand up the django server with the command
	```
	python manage.py runserver
	```

- To run tests:
	```
	python manage.py test
	```
	- There should be exactly one test, which should pass

- Before running the associated frontend tests, ensure that the database file (`db.sqlite3`) is not present, and if it is, remove it:
	- `rm db.sqlite3`
	- Then run the commands to set up and populate the database: 
	- `python manage.py migrate && python manage.py populateDb`
	- (The frontend tests rely on this data)
