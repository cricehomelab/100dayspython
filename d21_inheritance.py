
# Animal is a class that can be inherited.
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale exhale")


# Fish is inheriting animal as a class because it is a an animal.
class Fish(Animal):
    def __init__(self):
        super().__init__()

    # the breathe method is modified so that the fish can breathe underwater.
    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    # the swim method is added since fish is an animal that swims. 
    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
