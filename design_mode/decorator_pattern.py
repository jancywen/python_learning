# -*- coding: utf-8 -*-
__author__ = 'wangwenjie'
__data__ = '2018/5/28 上午9:24'
__product__ = 'PyCharm'
__filename__ = 'decorator_pattern'

# 装饰器模式 decorator pattern

class LogManager():
    @staticmethod
    def log(func):
        def wrapper(*args):
            print('Visit func %s', func.__name__)
            return func(*args)
        return wrapper

class Beverage():
    name = ''
    price = 0.0
    type = 'BEVERAGE'

    @LogManager.log
    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = 'coke'
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = 'milk'
        self.price = 5.0

class drinkDecorator():
    def getName(self):
        pass

    def getPrice(self):
        pass


class iceDecorator(drinkDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + '+ice'

    def getPrice(self):
        return self.beverage.getPrice() + 0.3


class sugerDecorator(drinkDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + '+suger'

    def getPrice(self):
        return self.beverage.getPrice() + 0.5


if __name__ == '__main__':
    coke_cola = coke()
    print('Name: %s' % coke_cola.getName())
    print('Price: %s' % coke_cola.getPrice())

    ice_coke = iceDecorator(coke_cola)
    print('Name: %s' % ice_coke.getName())
    print('Price: %s' % ice_coke.getPrice())


'''
定义:
    动态的给对象添加一些额外的职责
和Proxy Pattern 的区别:
    装饰器模式是代理模式的一种特殊情况,decorator_pattern侧重对主题类功能的加强或减弱; proxy_pattern侧重对主题类过程的控制
    
AOP Aspect Oriented Programming 面向切面编程
    如果几个或者更多个逻辑过程中,有重复的操作行为, 就可以将这些行为提取出来(即形成切面), 进行统一管理和维护
    
OOP Object Oriented Programming 面向对象编程
'''

'''
三、装饰器模式的优点和应用场景
优点：
1、装饰器模式是继承方式的一个替代方案，可以轻量级的扩展被装饰对象的功能；
2、Python的装饰器模式是实现AOP的一种方式，便于相同操作位于不同调用位置的统一管理。
应用场景：
1、需要扩展、增强或者减弱一个类的功能，如本例。

四、装饰器模式的缺点
1、多层装饰器的调试和维护有比较大的困难。

'''