"""
This file will contain a class which will set up
an attributes for the unit1 test
"""

from unittest import TestCase
from models.item import ItemModel
# this is needed for SQLalchemy for creating a store object
from models.store import StoreModel


class BaseTestUnit(TestCase):
    """
    This class will setup a testing class
    """
    def setUp(self):
        """
        This class is called before every test.
        """
        self.item1 = ItemModel('Head', 1000.99, 1)
        self.store1 = StoreModel('test_store_1')
