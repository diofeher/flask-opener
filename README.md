Flask Opener
=============

Simple extension inspired by [letter_opener](https://github.com/ryanb/letter_opener/) and [django_naomi](https://github.com/edwinlunando/django-naomi/)to be used with Flask.


Installation
============
Put this in your configuration code:

```
from flask import Flask
from flask_opener import FlaskOpener

app = Flask(__name__)
mail = FlaskOpener(app)
```

The interface used by FlaskOpener is the same as [Flask-Mail](https://pythonhosted.org/Flask-Mail/).


Configuration
==============

To be done