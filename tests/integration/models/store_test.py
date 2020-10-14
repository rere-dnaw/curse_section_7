from tests.integration.base_test_integration import BaseTestIntegration
from models.store import StoreModel
from models.item import ItemModel


class TestStoreModel(BaseTestIntegration):
    """
    This class will contain integration tests for class "StoreModel"
    """
    def test_create_store_list_empty(self):
        """
        This will test if created store has an empty items list
        """
        store = StoreModel('test_store_1')

        self.assertLessEqual(store.items.all(), [],
                             "The store items list must to be empty!")

    def test_json(self):
        """
        This method will test the json file format
        """
        store = StoreModel('test_store_1')

        expected = {
            'name': 'test_store_1',
            'items': [],
        }

        self.assertDictEqual(self.store1.json(), expected)

    def test_json_with_item(self):
        """
        This method will test the json file format
        """

        with self.app_context():
            store = StoreModel('test_store_1')
            item = ItemModel('Head', 99.9, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'name': 'test_store_1',
                'items': [{'name': 'Head',
                           'price': 99.9,
                           }],
            }

            self.assertDictEqual(store.json(), expected)

    def test_crud(self):
        """
        This will test adding and removing Store object into db
        """

        with self.app_context():
            store = StoreModel('test_store_1')

            self.assertIsNone(StoreModel.find_by_name('test_store_1'))

            store.save_to_db()
            self.assertIsNotNone(StoreModel.find_by_name('test_store_1'))

            store.delete_from_db()
            self.assertIsNone(StoreModel.find_by_name('test_store_1'))

    def test_store_relationship(self):
        """
        This method will test the relationship between
        Store and Item objects
        """
        with self.app_context():
            store = StoreModel('test_store_1')
            item = ItemModel('Head', 99.9, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'Head')

