def fun1(test1,test2,test3,test4):
    print 'in fun1:'
    print 'test1 is'
    print test1
    print 'test2 is'
    print test2
    print 'test3 is'
    print test3
    print 'test4 is'
    print test4
    return

def fun2(*test):
    print 'in fun2:'
    print 'test is'
    print test
    return

def fun3(**test):
    print 'in fun3:'
    print 'test is'
    print test
    return

mytuple=(1,2,3,4)
mylist=[5,6,7,8]
mydict={'test1':'value1','test2':'value2','test3':'value3','test4':'value4'}

fun1(1,2,3,4)
fun1(*mytuple)

fun2(1,2,3,4)
fun2(*mytuple)

fun1(test1='value1',test2='value2',test3='value3',test4='value4')
fun1(**mydict)

fun3(test1='value1',test2='value2',test3='value3',test4='value4')
fun3(**mydict)
