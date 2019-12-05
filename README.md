## DISCUSSION 

This project is using **Django(2+), Django Rest Framework & Vue Js/CLI** 

The type of this application is SPA (Single Page Application) that use **Session Authentication.** combine Django Framework & Vue JS.

And also support for **Token Based Authentication** (You can using Angular/ReactJs(Native)/Vue in separate service).

### Here these sample images of this application

**Login page**
![Login Page](re_cap/login.png)

**Registration Page**
![Registration Page](re_cap/registration.png)

**Forgot Password**
![Forgot Password](re_cap/forgot-password.png)

**Forgot link already sent**
![Forgot link already sent](re_cap/email-already-sent.png)

**Form Change Password after click the link for Forgot password**
![Form Change Password](re_cap/form-reset-password-email_click.png)

**Dashboard Page**
![Dashboard Page](re_cap/dashboard.png)

**Form Ask a Question Page**
![Ask a Question Page](re_cap/ask-a-question.png)

**Answer detail Page**
![Answer Page](re_cap/answer-detail.png)

## Hot to set up the project to run on your local machine?

#### Download the code to your PC, unpack the zip and move inside the folder.

#### Create a new Python Virtual Environment:
```
python3 -m venv venv
```

#### Activate the environment and install all the Python/Django dependencies:

```
source ./venv/bin/activate
pip install -m ./requirements.txt
```

#### Apply the migrations as usual.

#### Time to install the Vue JS dependencies:
```
cd django-vue/frontend
npm install
```

#### Run Vue JS Development Server:
```
npm run serve
```

#### Run Django's development server:
```
python manage.py runserver
```

#### Open up Chrome and go to 127.0.0.1:8000 and the app is now running in development mode!