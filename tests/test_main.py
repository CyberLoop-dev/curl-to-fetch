import unittest
from main import parse_curl,to_fetch
class Tests(unittest.TestCase):
 def test_get_header(self):
  r=parse_curl('curl -H "Accept: application/json" https://example.test/items')
  self.assertEqual(r["method"],"GET"); self.assertEqual(r["headers"]["Accept"],"application/json")
 def test_post(self):
  r=parse_curl('curl -d "name=Ada" https://example.test/users')
  self.assertEqual(r["method"],"POST"); self.assertEqual(r["body"],"name=Ada")
 def test_explicit_method(self):
  self.assertIn('"PATCH"',to_fetch(parse_curl("curl -X PATCH https://example.test/a")))
 def test_unknown_flag(self):
  with self.assertRaises(ValueError): parse_curl("curl --unknown https://example.test")
if __name__=="__main__": unittest.main()
