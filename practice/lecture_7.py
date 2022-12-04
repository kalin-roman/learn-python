import os, sys

from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from lesson_six.Lesson_6_sorts import  bubble_sort

a = [5,31,5,64,32,4,56,]
bubble_sort(a)
print(a,__name__)