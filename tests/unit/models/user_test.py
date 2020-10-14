from tests.unit.base_test_unit import BaseTestUnit


class TestUserModel(BaseTestUnit):
    """
    This class will contain the unit tests for user model
    """
    def test_user_init(self):
        """
        Init test
        """
        self.assertEqual(self.user1.user_name, 'Ben')
        self.assertEqual(self.user1.user_password, 'big')
