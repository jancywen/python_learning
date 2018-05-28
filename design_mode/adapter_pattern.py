# -*- coding: utf-8 -*-
__author__ = 'wangwenjie'
__data__ = '2018/5/28 上午10:49'
__product__ = 'PyCharm'
__filename__ = 'adapter_pattern'


# 适配器模式 adapter pattern

class ACpnStaff:
    name = ''
    id = ''
    phone = ''

    def __init__(self, id):
        self.id = id

    def getName(self):
        print('A protocol getName method...id: %s' % self.id)
        return self.name

    def setName(self, name):
        print('A protocol setName methond...id: %s' % self.id)
        self.name = name

    def getPhone(self):
        print('A protocol getPhone method...id: %s' % self.id)
        return self.phone

    def setPhone(self, phone):
        print('A protocol setPhone method...id: %s' % self.id)
        self.phone = phone

class BCpnStaff:
    name = ''
    id = ''
    telephone = ''

    def __init__(self, id):
        self.id = id

    def get_name(self):
        print('B protocol get_name method...id: %s' % self.id)
        return self.name

    def set_name(self, name):
        print('B protocol set_name method...id: %s' % self.id)
        self.name = name

    def get_telephone(self):
        print('B protocol get_telephone method...id: %s' % self.id)
        return self.telephone

    def set_telephone(self, telephone):
        print('B protocol set_telephone method...id: %s' % self.id)
        self.telephone = telephone


class CpnStaffAdapter:
    b_cpn = ''

    def __init__(self, id):
        self.b_cpn = BCpnStaff(id)

    def getName(self):
        return self.b_cpn.get_name()

    def setName(self, name):
        return self.b_cpn.set_name(name)

    def getPhone(self):
        return self.b_cpn.get_telephone()

    def setPhone(self, phone):
        return self.b_cpn.set_telephone(phone)


if __name__ == '__main__':
    acpn_staff = ACpnStaff('123')
    acpn_staff.setName('X_A')
    acpn_staff.setPhone('1234567890')
    print('A Staff Name: %s' % acpn_staff.getName())
    print('A Staff Phone: %s' % acpn_staff.getPhone())

    bcpn_staff = CpnStaffAdapter('456')
    bcpn_staff.setName('Y_B')
    bcpn_staff.setPhone('0987654321')
    print('B Staff Name: %s' % bcpn_staff.getName())
    print('B Staff Phone: %s' % bcpn_staff.getPhone())



'''
定义: 
    将一个类的接口变换成客户端期待的另一个接口, 从而使原本因为接口不匹配而无法在一起工作的两个类能够在一起工作
adapter_pattern 与 decorator_pattern 区别
    前者将另一个对象进行'伪装'; 后者给一个对象增加了一些额外的职责
'''

'''
优点：
1、适配器模式可以让两个接口不同，甚至关系不大的两个类一起运行；
2、提高了类的复用度，经过“伪装”的类，可以充当新的角色；
3、适配器可以灵活“拆卸”。
应用场景：
1、不修改现有接口，同时也要使该接口适用或兼容新场景业务中，适合使用适配器模式。
缺点:
1、适配器模式与原配接口相比，毕竟增加了一层调用关系，所以，在设计系统时，不要使用适配器模式。
'''