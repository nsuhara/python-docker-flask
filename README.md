# feedback-api

## api

| service     | method                 | example               |
| :---------- | :--------------------- | :-------------------- |
| healthcheck | get                    | /feedback/healthcheck |
| api         | get, post, put, delete | /feedback/api         |

## api sample

| service  | method | example                                      |
| :------- | :----- | :------------------------------------------- |
| read all | get    | [link](app/feedback/client/get_read_all.py)  |
| read one | get    | [link](app/feedback/client/get_read_one.py)  |
| upsert   | post   | [link](app/feedback/client/post_upsert.py)   |
| update   | put    | [link](app/feedback/client/put_update.py)    |
| delete   | delete | [link](app/feedback/client/delete_delete.py) |

## app sample

| service  | method | example                                                                                                                           |
| :------- | :----- | :-------------------------------------------------------------------------------------------------------------------------------- |
| app form | get    | /feedback/api?process=front_end&request=app_form&secret_key=M7XvWE9fSFg3                                                          |
|          |        | /feedback/api?process=front_end&request=app_form&secret_key=M7XvWE9fSFg3&url=sample-url&service=sample-service&title=sample-title |

## setup environment

```command_line.sh
source config/{environment}
```

## check code

```command_line.sh
python -B -m pylint --rcfile=.pylintrc -f parseable `find app -name "*.py" -not -path "app/tests"`
```

## unit test

```command_line.sh
python -B -m unittest discover tests
```

## launch docker

```command_line.sh
Dockerfiles/docker_compose_up.sh
```

## launch flask

```command_line.sh
brew services start postgresql
source config/{environment}
flask db init
flask db migrate
flask db upgrade
flask run
```

## migrate error

```command_line.sh
# ERROR [root] Error: Can't locate revision identified by {id}
flask db revision --rev-id {id}
```

## connect to local rds

```command_line.sh
psql -h localhost -p 5432 -d {database} -U {user}
```

## commit without updating

```command_line.sh
git commit --allow-empty -m "empty commit"
git push origin {branch}
```
