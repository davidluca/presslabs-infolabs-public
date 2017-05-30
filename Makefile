run: 
	python manage.py runserver

lint:
	pep8 . --exclude='migrations'

seed:
	python manage.py seed

full-test:
	py.test -v --color=yes
