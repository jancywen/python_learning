# -*- coding: utf-8 -*-
__author__ = 'wangwenjie'
__data__ = '2018/5/25 下午1:16'
__product__ = 'PyCharm'
__filename__ = 'prototype_pattern'


from copy import copy, deepcopy


class simpleLayer():
    background = [0, 0, 0, 0]
    content = 'black'

    def getContent(self):
        return self.content

    def getBackground(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == '__main__':
    dog_layer = simpleLayer()
    dog_layer.paint('Dog')
    dog_layer.fillBackground([0, 0, 255, 0])
    print('Background:', dog_layer.getBackground())
    print('Painting: ', dog_layer.getContent())

    another_dog_layer = dog_layer.clone()
    another_dog_layer.setParent(128)
    another_dog_layer.paint('Puppy')
    print('Background:', dog_layer.getBackground())
    print('Painting:', dog_layer.getContent())
    print('Clone Background:', another_dog_layer.getBackground())
    print('Clone content:', another_dog_layer.getContent())


'''
知识点:
深拷贝浅拷贝
    浅拷贝会拷贝对象内容及其内容的引用或者子对象的引用，但不会拷贝引用的内容和子对象本身；
    而深拷贝不仅拷贝了对象和内容的引用，也会拷贝引用的内容
'''

'''
优点：
1、性能极佳，直接拷贝比在内存里直接新建实例节省不少的资源；
2、简化对象创建，同时避免了构造函数的约束，不受构造函数的限制直接复制对象，是优点，也有隐患，这一点还是需要多留意一些。
使用场景：
1、对象在修改过后，需要复制多份的场景。
2、需要优化资源的情况。
3、某些重复性的复杂工作不需要多次进行。
缺点:
1、深拷贝和浅拷贝的使用需要事先考虑周到；
2、某些编程语言中，拷贝会影响到静态变量和静态函数的使用。
'''