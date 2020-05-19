#!/usr/bin/env python
# -*- coding: utf-8 -*-
class PhoneBook:
    def __init__(self):
        self.numbers = {}

    def add(self, param, param1):
        self.numbers[param] = param1
    
    def lookup(self, name):
        return self.numbers[name]
    

