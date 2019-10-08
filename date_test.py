# python3

import datetime
import unittest

class DateTest(unittest.TestCase):
  def test_date(self):
    now = datetime.datetime.now()
    print(now)

if __name__ == '__main__':
  unittest.main()
