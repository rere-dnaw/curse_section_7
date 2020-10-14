from tests.base_test import BaseTest
from models.user import UserModel


class TestUserModel(BaseTest):
    """
    This class will contain the integration tests for
    UserModel class
    """
    def test_crud(self):
        """
        Integration test for saving and removing from db
        """

        with self.app_context():
            user = UserModel('Lea', 'lea123')

            self.assertIsNone(UserModel.find_by_username('Lea'))
            self.assertIsNone(UserModel.find_user_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username('Lea'))
            self.assertIsNotNone(UserModel.find_user_by_id(1))

            user.delete_from_db()

            self.assertIsNone(UserModel.find_by_username('Lea'))
            self.assertIsNone(UserModel.find_user_by_id(1))
