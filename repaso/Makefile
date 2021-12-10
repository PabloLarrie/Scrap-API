up:
	docker-compose up

migrate:
	docker-compose run repaso python3 manage.py migrate

migrations:
	docker-compose run repaso python3 manage.py makemigrations

shell:
	docker-compose run repaso python3 manage.py shell_plus

loadfilms:
	docker-compose run repaso python3 manage.py loaddata Scrapp/results

chown:
	sudo chown `whoami` -R .

#
#down:
#	docker-compose down
#
#dest:
#	docker exec -it hsdecker_postgres_1 bash
#
#test:
#	${DOCKER_HSDECKER} pytest -c pytest.ini
#
#pip-compile:
#	${DOCKER_HSDECKER} pip-compile requirements.in > requirements.txt
#
#
#freeze_dependencies: pip-compile chown
#
#run:
#	${DOCKER_HSDECKER} python manage.py runserver
#
#build:
#	docker-compose build
#
#loadcards:
#	${DOCKER_HSDECKER} python manage.py loaddata cards/fixtures/*
#
#loaddecks:
#	${DOCKER_HSDECKER} python manage.py loaddata decks/fixtures/*
#
#loadgroups:
#	${DOCKER_HSDECKER} python manage.py setup_user_permissions
#
#loadusers:
#	${DOCKER_HSDECKER} python manage.py setup_user_creation
#
#loadprofiles:
#	${DOCKER_HSDECKER} python manage.py loaddata users/fixtures/*
#
#installfrontend:
#	${DOCKER_FRONTEND} npm install
#
#installvuestrap:
#	${DOCKER_FRONTEND} npm install vue bootstrap bootstrap-vue
#
#addvuestrap:
#	${DOCKER_FRONTEND} vue add bootstrap-vue
#
#installrouter:
#	${DOCKER_FRONTEND} npm install vue-router
#
#vuestrap: installvuestrap addvuestrap
#
#build_and_setup: build migrate loadgroups loadusers loadcards loaddecks loadprofiles installfrontend
#
#setup: migrate loadgroups loadusers loadcards loaddecks loadprofiles installfrontend