import unittest
from app.main import app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add(self):
        response = self.app.get("/add?a=2&b=3")
        data = response.get_json()
        self.assertEqual(data["result"], 5)

if __name__ == '__main__':
    unittest.main()
