
'''
3.同时遍历key和value

同时遍历的方法比较多，我们一一来看：
(1)首先看方法一和方法二，其实这两种方法是差不多的，只是加不加括号的区别，这个可以根据喜好来选择。
(2)然后看方法三，方法三使用简写的方式实现了对key和value的读取，形式上更加简便

(3)再看结合zip使用的两种方法，其实方法四更像方法一和二，只是多了一个zip操作，方法五更加像方法三，也是使用了zip函数

注意：另外，我们来看下关于key，value方式和kv方式的区别，在方法四和五时，小白输出了数据的类型，
两种方式的区别就主要在于输出数据的数据类型，key，value方式输出的是值本身，数据是什么类型，结果就是什么类型，但是方法五输出的tuple类型。

'''
#------------------------------------------------------------------------------------------------

dict = {
    '小明':129,
    '小兰':148,
    '小红':89,
}


#function1

for key,value in dict.items():

    print ('key: ',key,'value: ',value)

------------------------

key:  小明 value:  129

key:  小兰 value:  148

key:  小红 value:  89

 

 

#function2

for (key,value) in dict.items():

    print ('key: ',key,'value: ',value)

------------------------

key:  小明 value:  129

key:  小兰 value:  148

key:  小红 value:  89

 

 

#function3

for kv in dict.items():

    print ('kv is : ',kv)

------------------------

kv is :  ('小明', 129)

kv is :  ('小兰', 148)

kv is :  ('小红', 89)

 

----------------------结合zip使用---------------------

#function4

for key,value in zip(dict.keys(), dict.values()):

    print ('key:',key,'value: ',value)

    print('type key:',type(key),'type value:',type(value))

------------------------

key: 小明 value:  129

type key: <class 'str'> type value: <class 'int'>

key: 小兰 value:  148

type key: <class 'str'> type value: <class 'int'>

key: 小红 value:  89

type key: <class 'str'> type value: <class 'int'>



#function5

for kv in zip(dict.keys(), dict.values()):

    print ('kv: ',kv)

    print('type:',type(kv))

------------------------

kv:  ('小明', 129)

type: <class 'tuple'>

kv:  ('小兰', 148)

type: <class 'tuple'>

kv:  ('小红', 89)

type: <class 'tuple'>


