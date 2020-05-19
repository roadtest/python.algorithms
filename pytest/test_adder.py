# test_adder.py
#from proj.adder import adder
from proj.adder import adder
import unittest

class TestAdder(unittest.TestCase):
    def test_simple(self):
        res = adder(2, 3)
        self.assertEquals(res, 5)
