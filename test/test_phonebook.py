#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add('Bob', "12345")
        number = phonebook.lookup("Bob")
        self.assertEqual("12345", number)
