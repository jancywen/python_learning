# -*- coding: utf-8 -*-
__author__ = 'wangwenjie'
__data__ = '2018/5/24 下午3:40'
__product__ = 'PyCharm'
__filename__ = 'singleton_pattern'


'''单例模式'''

import threading
import time


# 这里使用方法__new__来实现单例模式
# 抽象单例
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        print('Singleton init')


'''
知识点：

继承自object的新式类才有__new__

__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供

__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例

__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值

若__new__没有正确返回当前类cls的实例，那__init__是不会被调用的，即使是父类的实例也不行
'''


# 总线
class Bus(Singleton):
    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        time.sleep(3)
        print("Sending Signal Data...", data)
        self.lock.release()


# 线程对象，为更加说明单例的含义，这里将Bus对象实例化写在了run里
class VisitEntity(threading.Thread):
    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)


if __name__ == "__main__":

    for i in range(3):
        print("Entity %d begin to run..." % i)
        my_entity = VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()
        my_entity.run()


'''
    知识点:
    start() 启用新线程
    run() 在当前线程
'''

'''
定义:
    保证某一个类只有一个实例，而且在全局只有一个访问点.
'''

'''
单例模式的优点：
1、由于单例模式要求在全局内只有一个实例，因而可以节省比较多的内存空间；
2、全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用；
3、单例可长驻内存，减少系统开销。
单例模式的应用举例：
1、生成全局惟一的序列号；
2、访问全局复用的惟一资源，如磁盘、总线等；
3、单个对象占用的资源过多，如数据库等；
4、系统全局统一管理，如Windows下的Task Manager；
5、网站计数器。

单例模式的缺点
1、单例模式的扩展是比较困难的；
2、赋于了单例以太多的职责，某种程度上违反单一职责原则（六大原则后面会讲到）;
3、单例模式是并发协作软件模块中需要最先完成的，因而其不利于测试；
4、单例模式在某种情况下会导致“资源瓶颈”。
'''