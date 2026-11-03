"""Animal class practice task: model solution."""


class Animal:
    """A generic animal with a name, a species, a sound and an age."""

    def __init__(self, name, species, sound, age=0):
        self.name = name
        self.species = species
        self.sound = sound
        self.age = age

    def speak(self):
        return f"{self.name} says {self.sound}"

    def have_birthday(self):
        self.age += 1

    def __str__(self):
        return f"{self.name} the {self.species} (age {self.age})"


class Dog(Animal):
    """A dog is an animal that barks and can fetch."""

    def __init__(self, name, age=0):
        super().__init__(name, "dog", "Woof", age)

    def speak(self):
        # Overrides Animal.speak to make dogs a little more excited.
        return f"{self.name} says {self.sound}! {self.sound}!"

    def fetch(self, item):
        return f"{self.name} fetches the {item}"


if __name__ == "__main__":
    cat = Animal("Mittens", "cat", "Meow", 3)
    cow = Animal("Daisy", "cow", "Moo")
    rex = Dog("Rex", 2)

    for animal in (cat, cow, rex):
        print(animal)
        print(animal.speak())

    rex.have_birthday()
    print(rex)
    print(rex.fetch("ball"))
