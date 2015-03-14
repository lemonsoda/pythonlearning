try:
    import cPickle as pickle
except ImportError:
    import pickle

d={'name':'Bob','age':20,'score':88}
with open('pickle.txt','w') as f:
    pickle.dump(d,f)

print d


    
