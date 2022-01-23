"""

Procedural programming is what we have been doing up until this point. The coffee machine project really illustrates
how the code logic can start to feel like spaghetti after a while.
Object-Oriented Programming (OOP) helps to address this.
    - The idea is to further break down complex problems with goals like
        - enabling collaboration
        - additional abstraction of complex ideas
        - reusing code that's useful for more than one thing (possibly for other projects)
If you run a restaurant:
    - receptionist - reserves seats for guests
    - wait staff - takes and brings customers their order
    - cook staff - cooks the food
    - cleaning - cleans the table after the customer has left.
    - manager - helps prioritize issues for staff.
If you only have one staff member in a restaurant you cannot care for all the needs and service many guests at the
same time. If you have a large restaurants you need more than one person doing a job at the same time.

In programming if you have a large program or a program that needs to be used by multiple people at the same time you
need to have different parts of code do things at the same time you need to be able to break the code down so that
different pieces can be doing different things simultaneously.

Implementing OOP:
OOP creates objects they are attempting to model a real world object similar to the restaurant, have an object that
waits table, an object that seats guests, an object that prepares food, and an object that cleans up after a guest has
left.

What does a waiter/waitress do? (VERY basic)
    - variables a waiter needs:
        - is_holding_plate  = True # whether the waiter is holding a plate or not
        - table_held = ["1-1", "2-2",] # what tables the server is responsible for maintaining.
    - things a server needs to do:
        - def take_order(table, order): # take an order from a specific table to the chef.
        - def take_payment(amount) # takes money from a customer to the restaurant for the food provided.
The things a waiter needs to do are ATTRIBUTEs.
Attributes are things that an object needs to keep track of.
The things a server needs to do are METHODs.
Method is a function that an object can do.

Going back to the restaurant idea once we know what a waiter's objects are and what their methods are we can "clone"
another waiter that has an identical skill set. (IE one waiter named Jim and one waiter named Jeniffer).

The archetype of "waiter" is called a class
The "objects" doing the work are like "Jim" and "Jeniffer" who are both waiters.
a Class is a blueprint that creates an object.

Constructing Objects:
    Objects are stored in variables.
    car = CarBlueprint()
    This is way of defining an object.
    Class names are in PascalCase where the first letter of the first letter in a word is capitalized. This helps to
    differentiate the class from otherthings like a_function or a_variable which the words are separated by an "_"


"""