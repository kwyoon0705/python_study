class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale... Exhale...")


class Fish(Animal):
    def swim(self):
        print("Swiiiiim")

    def breathe(self):
        super().breathe()
        print("underwater")


nemo = Fish()

nemo.breathe()
nemo.swim()
print(nemo.num_eyes)