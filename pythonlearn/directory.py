import os

print os.name
try:
    print os.uname
except BaseException,ex:
    print ex
finally:
    #print os.environ
    pass

print os.getenv('JAVA_HOME')
print os.path.abspath('./../')
