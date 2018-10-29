import sys
# sys.path.append('/Users/gaowanchao/workspace-python/learn')
import os
# print (os.path.abspath('..'))
print (os.path.abspath('..'))
sys.path.append(os.path.abspath('..'))

from m1 import a

def p():
    a.p()
    print ('b')

if __name__ == '__main__':
    p()