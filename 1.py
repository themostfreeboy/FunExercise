# -*- coding: cp936 -*-
def myfun1(*test1):
    print 'test1 is'
    print test1
    return

def myfun2(**test2):
    print 'test2 is'
    print test2
    return

def myfun3(test3,*test4):
    print 'test3 is'
    print test3
    print'test4 is'
    print test4
    return

def myfun4(test5,test6,test7,test8):
    print 'test5 is'
    print test5
    print'test6 is'
    print test6
    print 'test7 is'
    print test7
    print'test8 is'
    print test8
    return

def myfun5(key1='mytest9',key2='mytest10'):
#def myfun5(key1,key2):
    print 'test9 is'
    print key1
    print'test10 is'
    print key2
    return

def myfun6(*test11,**test12):
    print 'test11 is'
    print test11
    print'test12 is'
    print test12
    return

def myfun7(test13,test14='test14',test15='test15',*test16,**test17):
    print 'test13 is'
    print test13
    print'test14 is'
    print test14
    print 'test15 is'
    print test15
    print'test16 is'
    print test16
    print'test17 is'
    print test17
    return

mytuple=(1,2,3,4)
mylist=[5,6,7,8]
mydict={'key1':'value1','key2':'value2'}

myfun1(*mytuple)#有* 有*
myfun1(1,2,3,4)#有* 无*
myfun2(**mydict)#有** 有**
myfun2(key1='value1',key2='value2')#有** 无**
myfun3(*mytuple)
myfun4(*mytuple)#无* 有*
myfun5(**mydict)#无** 有**
myfun6(1,2,3,4,{'key5':'value5','key6':'value6'})
myfun6(1,2,3,4,**{'key5':'value5','key6':'value6'})
myfun7(1,2,3,4,key5='value5',key6='value6')
