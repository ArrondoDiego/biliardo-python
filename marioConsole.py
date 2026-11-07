'''
   Console i/o for Python 2/3
'''
import sys
import math
from math import *
import random
from random import *
import string
from string import *
from copy import *

BR = '\n'
br = '\n'

def ex(x):                          #   exhibit
    if isinstance(x,int) or isinstance(x,float):
        z='num {'+str(x)+'}'
    elif isinstance(x,str):
        z='str {'+x+'}'
    elif isinstance(x,bool):
        z='bool {'+x+'}'
    elif isinstance(x,tuple):
        z='tuple {'+x+'}'
    elif isinstance(x,list):
        z='list {'+x+'}'
    return z
'''
    a,b,c = gets(int,str,float)
'''
def gets(*types):
    try:
        x = tuple([types[i](val) for i,val in enumerate(input().split(' '))])
    except:
        print('input error')
        x = tuple(None for i in range(len(types)))
    return x

def tryIt(*args):                   #   output
    if len(args) == 0:
        n = 1
    else:
        try:
            n = int(args[0])
        except:
            n = 1
    return n
def lf(*args):                      #   line feed at will
    n = tryIt(*args)
    for i in range(n):
        sys.stdout.write('\n')
def LF(*args):                      #   line feed at will
    lf(*args)
def write(*args):                   #   print w/out newline
    for x in args:
        sys.stdout.write(str(x))
        sys.stdout.write(' ')
def writeln(*args):                 #   print w/ newline
    write(*args)
    lf()
def out(*args):                     #   print w/out newline, w/out blank
    for x in args:
        sys.stdout.write(str(x))
def outln(*args):                   #   print w/ newline, w/out blank
    out(*args)
    lf()
def version():
    return sys.version_info.major
def read(msg='input:',typ=int):     #   input for ONE VARIABLE
    if not isinstance(msg,str):
        msg = 'input:'
    msg = ' '.join(msg.strip().split()) + ' '
    if sys.version_info.major==3:
        x = input(msg)              #   string input for Python 3
    else:
        x = raw_input(msg)          #   string input for Python 2
    if typ==int or typ==float:      #   numeric input
        try:
            i = x.split()[0]        #   discard after first blank
            sign = 1
            if i[0]=='-':
                sign=-1             #   negative? store sign
                i = i[1:]
            while i.count('.') > 1: #   there will be only one (point)
                f = i.rfind('.')
                i = i[:f]+i[f+1:]
            if typ==int and '.' in i:
                i = i[:i.find('.')]
            z = ''
            for x in i:
                if '0'<=x<='9' or x=='.':
                    z+= x
            i = float(z)            #   "z" is a purged string
            if typ==int:
                i = int(i)
            x = typ(i) * sign
        except:
            x = typ(0)              #   float('nan')
    return x
def readInt(msg='integer: '):
    return read(msg,int)
def readFloat(msg='float: '):
    return read(msg,float)
def readStr(msg='string:'):
    return read(msg,str)
def readint(msg='integer: '):
    return read(msg,int)
def readfloat(msg='float: '):
    return read(msg,float)
def readstr(msg='string:'):
    return read(msg,str)

'''
a = read('test float')
while a!=-1:
    print(a)
    a = read('test float')
'''
