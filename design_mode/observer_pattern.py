# -*- coding: utf-8 -*-
__author__ = 'wangwenjie'
__data__ = '2018/5/28 下午1:39'
__product__ = 'PyCharm'
__filename__ = 'observer_pattern'


# 观察者模式


class Observer:
    def update(self):
        pass


class AlarmSensor(Observer):
    def update(self, action):
        print('Alarm Got: %s' % action)
        self.runAlarm()

    def runAlarm(self):
        print('Alarm Ring...')


class WaterSprinker(Observer):
    def update(self, action):
        print('Sprinker Got: %s' % action)
        self.runSprinker()

    def runSprinker(self):
        print('Spray Water...')


class EmergencyDialor(Observer):
    def update(self, action):
        print('Dialer Got: %s' % action)
        self.runDialer()

    def runDialer(self):
        print('Dial 119...')


class Observed:
    observers = []
    action = ''

    def addObserver(self, observer):
        self.observers.append(observer)

    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)


class smokeSensor(Observed):
    def setAction(self, action):
        self.action = action

    def isFire(self):
        return True


if __name__ == '__main__':
    alarm = AlarmSensor()
    sprinker = WaterSprinker()
    dialer = EmergencyDialor()

    smoke_sensor = smokeSensor()
    smoke_sensor.addObserver(alarm)
    smoke_sensor.addObserver(sprinker)
    smoke_sensor.addObserver(dialer)

    if smoke_sensor.isFire():
        smoke_sensor.setAction('On Fire!')
        smoke_sensor.notifyAll()



'''
定义:
    定义对象间一种一对多的依赖关系, 使得当该对象状态改变时,所有依赖于它的对象都会得到通知,并被自动更新.
'''

'''
三、观察者模式的优点和应用场景
优点：
1、观察者与被观察者之间是抽象耦合的；
2、可以将许多符合单一职责原则的模块进行触发，也可以很方便地实现广播。
应用场景：
1、消息交换场景。如上述说到的消息队列等；
2、多级触发场景。比如支持中断模式的场景中，一个中断即会引发一连串反应，就可以使用观察者模式。

四、观察者模式的缺点
1、观察者模式可能会带来整体系统效率的浪费；
2、如果被观察者之间有依赖关系，其逻辑关系的梳理需要费些心思。
'''