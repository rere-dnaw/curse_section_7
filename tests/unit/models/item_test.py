from tests.unit.base_test_unit import BaseTestUnit


class ItemTest(BaseTestUnit):
    def test_create_item(self):

        self.assertEqual(self.item1.name, 'Head',
                         "The name of the item after creation does not equal the constructor argument.")
        self.assertEqual(self.item1.price, 1000.99,
                         "The price of the item after creation does not equal the constructor argument.")

        self.assertEqual(self.item1.store_id, 1)
        self.assertIsNone(self.item1.store)

    def test_item_json(self):
        expected = {
            'name': 'Head',
            'price': 1000.99
        }
        self.assertEqual(
            self.item1.json(),
            expected,
            "The JSON export of the item is incorrect. Received {}, expected {}.".format(self.item1.json(), expected))


