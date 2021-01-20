# Social Media page
## usage:

On terminal: run:

# create dev virtualenv
python -m virtualenv dev

# activate dev
source dev/bin/activate

# installing requirement package on dev virtual environment
python -m pip install -r requirement.txt

# run web app
python app.py

Navigate to "http://127.0.0.1:8080/" on your web-browser

All respond will be 
```json
{
    "data": "data retrived",
    "message": "messager from the sever"
}
Database:
Table `USER` : `__id__`, name, email , phoneNumber, employment, blogs
Table `BLOG` : `__it__`, tittle, content, [#like]


CRUD for User:
 ` GET /
 # Respond:message: `200 OK` on success

```json
[
    {
        "id": "unint",
        "name": "display name",
        "email": "strvar",
        "phoneNumber": "strvar",
        "employment" : "strvar",
        "blog" : "[list of unint]"
    }
]

 ` Post /
 # Respond: message:`201 CREATED` on sucess of append
 ```json
[
    {
        "id": "unint",
        "name": "display name",
        "email": "strvar",
        "phoneNumber": "strvar",
        "employment" : "strvar",
        "blog" : "[list of unint]"
    }
]

 ` GET / t_shirt/id
 # Respond: message: `404 NOT FOUND` on fail
                     `200 OK` on sucess
```json
[
    {
        "id": "unint",
        "name": "display name",
        "email": "strvar",
        "phoneNumber": "strvar",
        "employment" : "strvar",
        "blog" : "[list of unint]"
    }
]                     

 ` DELETE /t_shirt/id
 # Respond: message: `404 NOT FOUND` on fail
                     `200 OK` on sucess
```json
[
    {
        "id": "unint",
        "name": "display name",
        "email": "strvar",
        "phoneNumber": "strvar",
        "employment" : "strvar",
        "blog" : "[list of unint]"
    }
]                     

CRUD for Blog:
 ` GET /
 # Respond:message: `200 OK` on success

```json
[
    {
        "id": "unint",
        "title": "display name",
        "content": "strvar",
        "like": "list of user"
    }
]

 ` Post /
 # Respond: message:`201 CREATED` on sucess of append
 ```json
[
    {
        "id": "unint",
        "title": "display name",
        "content": "strvar",
        "like": "list of user"
    }
]

 ` GET / t_shirt/id
 # Respond: message: `404 NOT FOUND` on fail
                     `200 OK` on sucess
```json
[
    {
        "id": "unint",
        "title": "display name",
        "content": "strvar",
        "like": "list of user"
    }
]                     

 ` DELETE /t_shirt/id
 # Respond: message: `404 NOT FOUND` on fail
                     `200 OK` on sucess
```json
[
    {
        "id": "unint",
        "title": "display name",
        "content": "strvar",
        "like": "list of user"
    }
]                     