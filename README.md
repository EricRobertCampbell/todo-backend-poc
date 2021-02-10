#Django Backend POC

- To run tests:
```
python manage.py test
```
	- There should be exactly one test, which should pass

- Before running the associated fronted tests, run
```
python manage.py migrate && python manage.py populateDb
```
(The frontend tests rely on this data)
