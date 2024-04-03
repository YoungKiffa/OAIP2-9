class door():
    def __init__(self, color, height, weight, length):
        self.color = color
        self.height = height
        self.weight = weight
        self.length = length
        self.poloz = False
    def start(self):
        self.poloz = True
        print('Дверь открыта')

    def stop(self):
        self.poloz = False
        print('Дверь закрыта')
        

tree = door('brown', 129, 18, 437)
tree.start()
tree.stop()



class MyClass():
    def __init__(self):
        self.__my_attr = 3

    def set_my_attr(self, val):
        self.__my_attr = val

    def get_my_attr(self):
        return self.__my_attr


obj1 = MyClass()
print(obj1.get_my_attr())
obj1.set_my_attr(7)
print(obj1.get_my_attr())
