from tests.unit.base_test_unit import BaseTestUnit


class TestStoreModel(BaseTestUnit):
    """
    This class will contain unit tests for StoreModel class
    """
    def test_creating_store(self):
        """
        Test for object initialization
        """
        self.assertEqual(self.store1.name, 'test_store_1')

