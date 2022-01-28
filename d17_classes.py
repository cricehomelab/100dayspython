# create a class
class User:
    # using a constructor can be an easier way of handling attribute creation.
    # this allows us to specify what happens when an object is being constructed.
    # this allows us to specify values.
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # This allows us to initialize/create starting values for our attributes.
        # This is called everytime you create an object from this class.

        # a value that will always start at a certain number.
        self.followers = 0
        self.following = 0
    #          methods ALWAYS have "self" paramenter
    def follow(self, user):
        user.followers += 1
        self.following += 1


# another class example.
class Car:
    # __init__ initializes the class and sets the attributes you want set after the 'self' declaration.
    def __init__(self, seats):
        # setting the value of seats to be the variable passed in called 'seats'
        self.seats = seats
    # methods are what your class does.


    def enter_race_mode(self):
        self.seats = 2



# create an object
#user_1 = User()

# One way to add attributes to an object
#user_1.id = "001"
#user_1.username = "charlie"
# this is the better way.
user_1 = User("001", "charlie")
user_2 = User("002", "renee")

print(user_1.id)
print(user_1.username)
# this will show at 0 as default.
print(f"{user_1.username} has {user_1.followers} followers. ")

# after creating a function to "follow someone we can see the data changes for both objects.
user_2.follow(user_1)

print(f"{user_1.username} has {user_1.followers} followers. ")
print(f"{user_1.username} is following {user_1.following} people.")

print(f"{user_2.username} has {user_2.followers} followers. ")
print(f"{user_2.username} is following {user_2.following} people.")

# repeating this again to show that this can happen both ways.
user_1.follow(user_2)

print(f"{user_1.username} has {user_1.followers} followers. ")
print(f"{user_1.username} is following {user_1.following} people.")

print(f"{user_2.username} has {user_2.followers} followers. ")
print(f"{user_2.username} is following {user_2.following} people.")

# creating attributes for every object you make from scratch can be a lot of work.
# it can also be error-prone.
#user_2 = User()
#user_2.id = "002"
#user_2.username = "renee"

user_2 = User("002", "renee")

vroom = Car(4)
print(f"The car has {vroom.seats} seats")
# calling a method called "enter_race_mode"
vroom.enter_race_mode()
print(f"Car was modded for race mode and has {vroom.seats}")

