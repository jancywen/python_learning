# -*- coding: utf-8 -*-
__author__ = 'wangwenjie'
__data__ = '2018/5/25 上午10:09'
__product__ = 'PyCharm'
__filename__ = 'builder_pattern'


# 建造者模式

class Burger():
    name = ''
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


class cheeseBurger(Burger):
    def __init__(self):
        self.name = 'cheese burger'
        self.price = 10.0


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = 'spicy chicken burger'
        self.price = 15.0


class Snack():
    name = ''
    price = 0.0
    type = 'SNACK'

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = 'chips'
        self.price = 0.0


class chickenWings(Snack):
    def __init__(self):
        self.name = 'chicken wings'
        self.price = 12.0


class Beverage():
    name = ''
    price = 0.0
    type = 'BEVERAGE'

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


class order():
    burger = ''
    snack = ''
    beverage = ''

    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print('Burger: %s' % self.burger.getName())
        print('Snack: %s' % self.snack.getName())
        print('Beverage: %s' % self.beverage.getName())


class orderBuilder():
    bBurger = ''
    bSnack = ''
    bBeverage = ''

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return order(self)


# 用以安排已有模块的构造步骤
class orderDirector():
    order_builder = ""

    def __init__(self, order_builder):
        self.order_builder = order_builder

    def createOrder(self, burger, snack, beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()


if __name__ == '__main__':
    order_builder = orderBuilder()
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())
    order_1 = order_builder.build()
    order_1.show()



'''
定义:
    将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
'''

'''
优点：
1、封装性好，用户可以不知道对象的内部构造和细节，就可以直接建造对象；
2、系统扩展容易；
3、建造者模式易于使用，非常灵活。在构造性的场景中很容易实现“流水线”；
4、便于控制细节。

使用场景：
1、目标对象由组件构成的场景中，很适合建造者模式。
例如，在一款赛车游戏中，车辆生成时，需要根据级别、环境等，选择轮胎、悬挂、骨架等部件，构造一辆“赛车”；
2、在具体的场景中，对象内部接口需要根据不同的参数而调用顺序有所不同时，可以使用建造者模式。
例如：一个植物养殖器系统，对于某些不同的植物，浇水、施加肥料的顺序要求可能会不同，
因而可以在Director中维护一个类似于队列的结构，在实例化时作为参数代入到具体建造者中。

缺点:
1、“加工工艺”对用户不透明。（封装的两面性）
'''