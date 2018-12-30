from django.test import TestCase
import os
from django.views.generic import TemplateView
TemplateView()
# Create your tests here.
#print(os.path.abspath("static/upload/aryan.jpg"))

class aryan:
    @classmethod
    def a(cls):
        return "hello class"

class my_decorator(object):

    def __init__(self, f=None,name=None):
        print("inside my_decorator.__init__()")
        #f() # Prove that function definition has completed
        self.f=f
    def __call__(self,a,b):
       print("inside my_decorator.__call__()")
       self.f(a,b)



#@my_decorator(name="aryan")
def aFunction(a,b):
    print("inside aFunction()")
    print(a,b)

print("Finished decorating aFunction()")

aFunction("hero","aryan")
print("------------------------")

class check:
    def simple(self, func=None, takes_context=None, name=None):
        def f():
            print("before func")
            func()
        return f

c=check()
@c.simple
def aa():
    print("aaa")
aa()
"""class a:
  def __init__(self):
      print("constructer")

  def __call__(self ):
      print("callable...")

b=a()"""

print("========================")
def decorator(arg1, arg2):

    def real_decorator(function):

        def wrapper(args):
            print("Congratulations.  You decorated a function that does something with ",args)
            function(args)
        return wrapper

    return real_decorator


@decorator("arg1", "arg2")
def print_args(args):

        print("arg")
print_args("hello")