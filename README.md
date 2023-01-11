# Photo Manager

## Configuration
Configuration located in `envs/.env`, for examples see `envs/.env.ci`

## Installing on a local machine
This project requires python3.9

Install requirements:


```sh
$ python ./backend/manage.py migrate
$ python ./backend/manage.py createsuperuser
```

Development servers:

```bash
# run django dev server
$ python ./backend_api/manage.py runserver
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

### Management

Basic usage of compose file:

#### psql shell

```bash
$ docker-compose -f local.yml run --rm postgres psql -d database -U user -W password
```

#### Migrations

```bash
$ docker-compose -f local.yml run --rm -w /src/backend web python manage.py makemigrations 
$ docker-compose -f local.yml run --rm -w /src/backend web python manage.py migrate
```

#### Check migrations

```shell
$ docker-compose -f local.yml run --rm -w /src/backend web python manage.py makemigrations --check --dry-run
```
