import unittest
from HttpLogProcessor import HttpLogProcessor


"""
Test the number of unique IP addresses.
"""
class test_get_total_unique_ip_addresses(unittest.TestCase):
  def test_is_equal(self):
    result = HttpLogProcessor('./src/programming-task-example-data.log').get_total_unique_ip_addresses()
    assert result == 7

"""
Test the top 3 most active IP addresses.
"""
class test_get_most_active_ip_addresses(unittest.TestCase):
  def test_is_equal(self):
    result = HttpLogProcessor('./src/programming-task-example-data.log').get_most_active_ip_addresses()
    assert result == ['72.44.32.10', '50.112.00.11', '79.125.00.21' ]

"""
 Calculate the top 3 most visited URLs.
"""
class test_get_most_active_paths(unittest.TestCase):
  def test_is_equal(self):
    result = HttpLogProcessor('./src/programming-task-example-data.log').get_most_active_paths()
    assert result == ['/newsletter/', '/this/page/does/not/exist/ HTTP/1.1', '/translations/']