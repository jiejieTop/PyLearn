class Cat :

    def __init__(self,new_name):
        self.name = new_name;

    def eat(self):
        print("%s爱吃鱼"%self.name)

    def drink(self):
        print("%s要喝水"%self.name)


tom = Cat('Tom')


tom.eat()
tom.drink()

tom1 = Cat('Tom1')


tom1.eat()
tom1.drink()
