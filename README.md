# Django Backend POC

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
