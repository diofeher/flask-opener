# -*- coding: utf-8 -*-
import datetime
import time
import os
import six
import webbrowser
from flask import make_response, render_template


class FlaskOpener():
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.state = self.init_app(app)
        else:
            self.state = None

    def init_app(self, app):
        state = {}
        self.default_sender = app.config.get('MAIL_DEFAULT_SENDER', 'no-reply@localhost')
        # register extension with app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['mail'] = self
        return state

    def _get_filename(self):
        """Return a unique file name."""
        if self._fname is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fname = "%s-%s.html" % (timestamp, abs(id(self)))
            self._fname = os.path.join('/tmp', fname)
        return self._fname

    def send(self, message):
        # TODO: Add support for attachments
        # TODO: Add support for sent, subject, date sent, to and attachments
        context = {
            'message': message,
            'body': message.html,
        }
        content = render_template('message.html', **context)
        fp = open(self._get_filename(), 'w+')
        fp.write(content)
        fp.close()
        webbrowser.open('file://' + self._fname)
