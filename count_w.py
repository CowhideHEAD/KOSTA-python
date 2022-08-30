count={'a':0,'i':0,'o':0,'u':0,'e':0}
a='''The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

alist=list(a)


for i in range(len(alist)):
     if alist[i]=='a':
             count['a']=count['a']+1
     if alist[i]=='i':
             count['i']=count['i']+1
     if alist[i]=='o':
             count['o']=count['o']+1
     if alist[i]=='u':
             count['u']=count['o']+1
     if alist[i]=='e':
            count['e']=count['e']+1

print(count.items())
