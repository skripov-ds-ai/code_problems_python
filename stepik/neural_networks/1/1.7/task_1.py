import urllib
from urllib import request
import numpy as np

fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

# here goes your solution

data = np.array([np.array(x) for x in data])

print(data)
print("Type = ", type(data))

Y, X = np.hsplit(data, np.array([1]))

print((Y).shape)
print()
print((X).shape)

X = np.hsplit(X, np.array(np.ones(X.shape[0])).reshape(-1, 1))

print(X)