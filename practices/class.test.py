#!/usr/bin/env python3
class Testing(object):
    def method2(self,s):
        print(f'{s} is printing out');

    def method1(self):
        self.method2(object)


a = Testing()
a.method1()
a.method2("i am foobar")
