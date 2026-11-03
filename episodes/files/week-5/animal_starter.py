"""Animal class practice task: starter.

Fill in each TODO. Run this file to try your classes, and run
test_animal.py (see README.md) to check your work.
"""


class Animal:
    """A generic animal with a name, a species, a sound and an age."""

    def __init__(self, name, species, sound, age=0):
        # TODO 1: store each argument on self (self.name, self.species,
        # self.sound, self.age).
        pass

    def speak(self):
        # TODO 2: return a string like "Mittens says Meow".
        # Use return, not print.
        pass

    def have_birthday(self):
        # TODO 3: add 1 to self.age. This method returns nothing.
        pass

    def __str__(self):
        # TODO 4: return a string like "Mittens the cat (age 3)".
        pass


# TODO 5 (optional stretch): write a class Dog that inherits from Animal.
# Skip this if you are short of time; the tests for Dog are skipped until it exists.
#   - Its __init__ takes name and age=0 only, and calls
#     super().__init__(name, "dog", "Woof", age).
#   - Override speak() so it returns e.g. "Rex says Woof! Woof!".
#   - Add a new method fetch(item) returning e.g. "Rex fetches the ball".


if __name__ == "__main__":
    # TODO 6: leave the "if __name__" line as it is and put your test code
    # inside this block (Week 6 explains why it is there).
    # Create at least two Animal objects. Print each one, call speak() on
    # each, then give one a birthday and print it again.
    # If you did TODO 5, add a Dog and call fetch() on it too.
    pass
