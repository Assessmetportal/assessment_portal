# Assessment portal

## Deploying heroku

```sh
$ heroku git:remote -a assessmentportal300
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku ps:scale web=1
$ git push heroku main
```

## Configuration

Configuration located in `envs/.env`, for examples see `envs/.env.ci`

## Installing on a local machine

This project requires python3.8 and .

Install requirements:

```sh
$ pip install pipenv
$ pipenv shell
$ pipenv install
```

```sh
$ python ./manage.py migrate
$ python ./manage.py createsuperuser
```

Development servers:

```bash
# run django dev server
$ python ./manage.py runserver
```

## Linting

```sh
$ flake8
$ isort .
```

## Docker

### Containers management

#### Formatted output

```shell
$ docker ps -a --format "{{.ID}}: {{.Image}} {{.Names}} {{.Size}}"
```

### Building

```bash
$ docker-compose -f local.yml up
```

or

```bash
$ docker-compose -f local.yml build ...
```

if u wanna rebuild specific container.

#### psql shell

```bash
$ docker-compose -f local.yml run --rm postgres psql -d database -U user -W password
```

#### Migrations

```bash
$ docker-compose -f local.yml run --rm -w /src/ web python manage.py makemigrations 
$ docker-compose -f local.yml run --rm -w /src/ web python manage.py migrate
```

#### Check migrations

```shell
$ docker-compose -f local.yml run --rm -w /src/ web python manage.py makemigrations --check --dry-run
```
