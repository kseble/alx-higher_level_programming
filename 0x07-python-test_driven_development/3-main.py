#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "white")
say_my_name("Job")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
