"""Это давнишнее задание, когда мы только изучили классы.
Создать класс, наследника, переопределить метод родителя и перегрузить инит."""
class Mammals:
    def __init__(self, name):
        self.name = name

    def have_backbone(self):
        print("All mammals have a backbone.")

    def feed_with_milk(self):
        print("All mammals feed their young with milk.")

rat = Mammals("Alisa")

print(rat.name)
rat.have_backbone()
rat.feed_with_milk()

class Primates(Mammals):
    def __init__(self, name, detachment = "Primates"):
        super().__init__(name)
        self.detachment = detachment
    
    def climb_trees(self):
        print("All primates can climb trees. ")

    def have_backbone(self):
        print("All primates have a backbone.")

monkey = Primates("Chichichi")

print(monkey.name)
print(monkey.detachment)

monkey.have_backbone()
monkey.climb_trees()

class Human(Primates, Mammals):
    def __init__(self, adress, job, **kwargs):
        super().__init__(**kwargs)
        self.adress = adress
        self.job = job

    def can_speak(self):
        print(f"My name is {self.name}. I live in {self.adress}. I work as a {self.job}.")

    def have_backbone(self):
        print("All humans have a backbone.")

    def feed_with_milk(self):
        print("All humans feed their young with milk.")

    def __str__(self):
        return f"I human with name: {self.name}, adress: {self.adress} and job: {self.job}."

women = Human("Minsk", "Doctor", name = "Nastya")
print(women)

print(women.detachment)
women.can_speak()
women.climb_trees()
women.have_backbone()
women.feed_with_milk()
