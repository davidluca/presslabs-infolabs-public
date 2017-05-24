run: 
	python manage.py runserver

pep:
	pep8 --first infolabs

seed:
	python manage.py seed
