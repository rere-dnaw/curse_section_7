from models.item import ItemModel
from tests.base_test import BaseTest
from models.store import StoreModel
import json


class TestStore(BaseTest):
    """

    """
    def test_create_store(self):
        """

        @return:
        """

        with self.app() as client:
            with self.app_context():

                response = client.post('/store/store_test')

                self.assertIsNotNone(StoreModel.find_by_name('store_test'))
                self.assertEqual(response.status_code, 201)
                self.assertDictEqual({'name': 'store_test',
                                      'items': [],
                                      },
                                     json.loads(response.data))

    def test_duplicate_store(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                response = client.post('/store/store_test')
                response = client.post('/store/store_test')

                self.assertEqual(400, response.status_code)
                self.assertEqual({'message': "A store with name 'store_test' already exists."},
                                 json.loads(response.data))

    def test_delete_store(self):
        """
        should I make a test for delete store
        when store not found?
        @return:
        """

        with self.app() as client:
            with self.app_context():
                client.post('/store/store_test')

                resp = client.delete('/store/store_test')

                self.assertIsNone(StoreModel.find_by_name('store_test'))

                self.assertEqual(200,resp.status_code)
                self.assertEqual({'message': 'Store deleted'}, json.loads(resp.data))

    def test_find_store(self):
        """

        @return:
        """

        with self.app() as client:
            with self.app_context():

                client.post('store/test_store')
                store = client.get('store/test_store')

                self.assertEqual(200, store.status_code)
                self.assertEqual({'name': 'test_store',
                                  'items': []},
                                 json.loads(store.data))

    def test_store_not_found(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                # client.post('store/test_store')
                store = client.get('store/test_store')

                self.assertEqual(404, store.status_code)
                self.assertEqual({'message': 'Store not found'},
                                 json.loads(store.data))

    def test_store_found_with_items(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                client.post('store/test_store')

                ItemModel('test_item', 10.99, 1).save_to_db()

                store = client.get('store/test_store')

                self.assertEqual(200, store.status_code)
                self.assertDictEqual({'name': 'test_store',
                                      'items': [{'name': 'test_item',
                                                 'price': 10.99,
                                                 }]
                                      },
                                     json.loads(store.data))



    def test_store_list(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                store_list = client.get('/stores')

                self.assertEqual(200, store_list.status_code)
                self.assertDictEqual({'stores': []}, json.loads(store_list.data))

    def test_store_list_with_items(self):
        """

        @return:
        """

        with self.app() as client:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                ItemModel('test_item', 10.99, 1).save_to_db()

                store_list = client.get('/stores')

                self.assertEqual(200, store_list.status_code)
                self.assertDictEqual({'stores': [{'name': 'test_store',
                                                  'items': [{'name': 'test_item',
                                                             'price': 10.99,
                                                             }]}]}, json.loads(store_list.data))


