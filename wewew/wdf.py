# -*- coding: UTF-8 -*-
class fish:
    def __init__(self, type, name):

        self.type = type
        self.name = name

    def __str__(self):
        """
        [summary]

        Returns:
            [type]: [description]
        """
        return '鱼的类型：%s,鱼的名称：%s' % (self.type, self.name)


grassfish = fish('甲鱼', '草鱼')
print(grassfish)
print("hello world!")
print('jjj')
