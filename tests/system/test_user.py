from tests.base_test import BaseTest
from models.user import UserModel
import json


class UserTest(BaseTest):
    """
    This class will contain a system tests
    for the UserModel object
    """

    def test_register_user(self):
        """
        Test for user registration.
        """

        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'Luk',
                                                          'password': 'Luk123',
                                                          })

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('Luk'))

                self.assertDictEqual(json.loads(response.data),
                                     {'message': 'User was created successfully.'},
                                     )

    def test_register_and_login(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'Luk',
                                                          'password': 'Luk123',
                                                          })
                auth_response = client.post('/auth',
                                            data=json.dumps({'username': 'Luk',
                                                             'password': 'Luk123',
                                                             }),
                                            headers={'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_register_duplicate_user(self):
        """

        @return:
        """
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={'username': 'Luk',
                                                          'password': 'Luk123',
                                                          })
                response = client.post('/register', data={'username': 'Luk',
                                                          'password': 'Luk123',
                                                          })

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual(json.loads(response.data), {'message': 'The user name exist in db'})
