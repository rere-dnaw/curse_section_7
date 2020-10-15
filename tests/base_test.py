"""
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    @classmethod
    def setUpClass(cls):
        """
        If error "AssertionError: A setup function was called after the first request was handled."
        occurs, this is because the app is passed to SClAlchemy db.init(app). This happened when the app
        debugging mode is set to TRUE(in debugging mode flask is checking much more things).
        To make it go away the debugging needs to be set to false and PROPAGATE_EXCEPTIONS needs to be
        set to TRUE.
        """
        app.config['PROPAGATE_EXCEPTIONS'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():

            db.init_app(app)
            db.create_all()

    def setUp(self):
        # Make sure database exists
        with app.app_context():
            db.create_all()
        # Get a test client
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
