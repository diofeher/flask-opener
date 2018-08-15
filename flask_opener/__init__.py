# -*- coding: utf-8 -*-
import datetime
import time
import os
import six
import webbrowser
from flask import make_response, render_template, Blueprint


class FlaskOpener():
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.state = self.init_app(app)
        else:
            self.state = None
        self.blueprint = Blueprint('flask_opener', __name__,
            static_folder='static', template_folder='templates')
        self.app.register_blueprint(self.blueprint)

    def init_app(self, app):
        state = {}
        self.default_sender = app.config.get('MAIL_DEFAULT_SENDER', 'no-reply@localhost')
        # register extension with app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['mail'] = self
        return state

    def _get_filename(self):
        """Return a unique file name."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        fname = "%s-%s.html" % (timestamp, abs(id(self)))
        return os.path.join('/tmp', fname)

    def send(self, message):
        # TODO: Add support for attachments
        # TODO: Add support for sent, subject, date sent, to and attachments
        context = {
            'message': message,
            'body': message.html,
        }
        content = render_template('flask_opener/message.html', **context)
        fname = self._get_filename()
        fp = open(fname, 'w+')
        fp.write(content)
        fp.close()
        webbrowser.open('file://' + fname)
