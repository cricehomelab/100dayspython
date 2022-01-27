# Package info https://pypi.org/project/prettytable/
from prettytable import PrettyTable
# method able to change the formatting of the table to be MS Word friendly.
from prettytable import MSWORD_FRIENDLY

# creating a prettytable object named table
table = PrettyTable()

# Changing attributes in an object through a method
table.set_style(MSWORD_FRIENDLY)


# adding field names
table.field_names = ["Pokemon Name", "Type",]
print(table)
# adding Rows.
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Bulbasaur", "Grass, Poison"])
table.add_row(["Charmander", "Fire"])

print()
print(table)
print()

table.add_column("Species", ["mouse", "Tiny Turtle", "Seed", "Lizard"])
print(table)

print(table.align)
# changing an attribute for alignment
table.align = 'l'
print(table.align)
print(table)
