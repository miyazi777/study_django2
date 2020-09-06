from django.test import TestCase, Client

# Create your tests here.
class BlogTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('/')
        self.assertEqual(200, res.status_code)

    def test_index_fail_access(self):
        res = self.c.get('/unknown')
        self.assertEqual(404, res.status_code)


