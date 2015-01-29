import os
import sys

word = 'my'

files=[x for x in os.listdir('.') if not os.path.isdir(x) and x.index(word)>0]
dirs=[x for x in os.listdir('.') if os.path.isdir(x)]

print files
