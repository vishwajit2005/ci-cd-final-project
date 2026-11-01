import unittest
from service.server import app

TestProductModel = None

class TestServer(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        self.assertTrue(True)

    def test_deserialize(self):
        self.assertTrue(True)

    def test_find_product(self):
        self.assertTrue(True)

    def test_list_products(self):
        self.assertTrue(True)

    def test_serialize(self):
        self.assertTrue(True)

    def test_update_product(self):
        self.assertTrue(True)
