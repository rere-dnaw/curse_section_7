"""
This file will contain integration tests
"""

from models.item import ItemModel
from models.store import StoreModel
from tests.integration.base_test_integration import BaseTestIntegration


class ItemTest(BaseTestIntegration):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db()  # only needed if connecting to 'sqlite:///data.db'
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        """
        This method will test if the relationship
        between store and item is correct.
        """

        with self.app_context():
            store = StoreModel('test_store_1')
            item = ItemModel('Eye', '300', '1')

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store_1')