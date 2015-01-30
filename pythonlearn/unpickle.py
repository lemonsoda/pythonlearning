try:
    import cPickle as pickle
except ImportError:
    import pickle


with open('pickle.txt','rb') as f:
    d=pickle.load(f)

print d
