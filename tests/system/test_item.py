from models.item import ItemModel
from models.store import StoreModel
from models.user import UserModel
from tests.base_test import BaseTest

import json


class TestItemModel(BaseTest):
    """

    """

    def setUp(self):
        """
        This setUp method will be called after the setUp method from BaseTest class.
        If "super(TestItemModel, self).setUp()" is not present, then the setUp method
        from the BaseTest class will be overwritten!
        """
        super(TestItemModel, self).setUp()  # prevent overwriting the setUp method from BaseTest class
        with self.app() as c:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
                auth_request = c.post('/auth', data=json.dumps({
                    'username': 'test',
                    'password': '1234'
                }), headers={'Content-Type': 'application/json'})
                self.auth_header = "JWT {}".format(json.loads(auth_request.data)['access_token'])

    def test_get_item_no_auth(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test_item')

                self.assertEqual(401, resp.status_code)
                self.assertEqual({'message': 'Could not authorize. Did you include a valid Authorization header?'},
                                 json.loads(resp.data))

    def test_get_item_not_found(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test_item', headers={'Authorization': self.auth_header})

                self.assertEqual(404, resp.status_code)
                self.assertEqual({'message': 'Item not found'}, json.loads(resp.data))

    def test_get_item_auth(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                ItemModel('test_item', 10.99, 1).save_to_db()

                request = client.get('/item/test_item', headers={'Authorization': self.auth_header})

                self.assertEqual(200, request.status_code)
                self.assertEqual({'name': 'test_item',
                                  'price': 10.99
                                  },
                                 json.loads(request.data))

    def test_create_item(self):
        """

        @return:
        """
        with self.app() as c:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                """
                The data for the post request model is as in the class Item
                parser = reqparse.RequestParser()
                parser.add_argument('price',
                                    type=float,
                                    required=True,
                                    help="This field cannot be left blank!")
                parser.add_argument('store_id',
                                    type=int,
                                    required=True,
                                    help="Every item needs a store id.")
                So the data dist has two keys 'price' and 'store_id'
                """
                request = c.post('/item/test_item', data={'price': 10.99, 'store_id': 1})

                self.assertEqual(201, request.status_code)
                self.assertEqual({'name': 'test_item',
                                  'price': 10.99
                                  },
                                 json.loads(request.data))

    def test_create_duplicated_item(self):
        """

        @return:
        """
        with self.app() as c:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                ItemModel('test_item', 10.99, 1).save_to_db()
                request = c.post('/item/test_item', data={'price': 10.99, 'store_id': 1})

                self.assertEqual(400, request.status_code)
                self.assertEqual({'message': "An item with name 'test_item' already exists."},
                                 json.loads(request.data))

    def test_delete_item(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                ItemModel('test_item', 10.99, 1).save_to_db()

                request = client.delete('/item/test_item')

                self.assertEqual(200, request.status_code)
                self.assertEqual({'message': 'Item deleted'},
                                 json.loads(request.data))

    def test_put_item_update(self):
        """

        @return:
        """
        with self.app() as c:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                ItemModel('test_item', 10.99, 1).save_to_db()
                resp = c.put('/item/test_item', data={'price': 11.99, 'store_id': 1})

                self.assertEqual(200, resp.status_code)
                self.assertEqual({'name': 'test_item',
                                  'price': 11.99
                                  },
                                 json.loads(resp.data))

    def test_put_item_create(self):
        """

        @return:
        """
        with self.app() as c:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                resp = c.put('/item/test_item', data={'price': 10.99, 'store_id': 1})

                self.assertEqual(200, resp.status_code)
                self.assertEqual({'name': 'test_item',
                                  'price': 10.99
                                  },
                                 json.loads(resp.data))

    def test_item_list(self):
        """

        @return:
        """
        with self.app() as c:
            with self.app_context():
                resp = c.get('/items')

                self.assertEqual(200, resp.status_code)
                self.assertDictEqual({'items': []},
                                     json.loads(resp.data))

    def test_item_list_with_item(self):
        """

        @return:
        """
        with self.app() as c:
            with self.app_context():
                StoreModel('test_store').save_to_db()
                ItemModel('test_item', 10.99, 1).save_to_db()

                resp = c.get('/items')

                self.assertEqual(200, resp.status_code)
                self.assertDictEqual({'items': [{'name': 'test_item',
                                                 'price': 10.99}
                                                ]
                                      },
                                     json.loads(resp.data))
