"""Tests for the Animal practice task.

While you work, change MODULE_NAME to "animal_starter" to test your own code.
Change it back to "animal_solution" to test the model solution.
"""

import importlib

import pytest

MODULE_NAME = "animal_solution"

animal = importlib.import_module(MODULE_NAME)
Animal = animal.Animal
Dog = getattr(animal, "Dog", None)  # Dog is an optional stretch step
needs_dog = pytest.mark.skipif(Dog is None, reason="Dog is an optional stretch step")


def test_animal_attributes():
    cat = Animal("Mittens", "cat", "Meow", 3)
    assert cat.name == "Mittens"
    assert cat.species == "cat"
    assert cat.sound == "Meow"
    assert cat.age == 3


def test_age_defaults_to_zero():
    assert Animal("Daisy", "cow", "Moo").age == 0


def test_speak():
    assert Animal("Mittens", "cat", "Meow").speak() == "Mittens says Meow"


def test_str():
    assert str(Animal("Mittens", "cat", "Meow", 3)) == "Mittens the cat (age 3)"


def test_instances_are_independent():
    a = Animal("A", "cat", "Meow", 1)
    b = Animal("B", "cow", "Moo", 5)
    a.have_birthday()
    assert a.age == 2
    assert b.age == 5
    assert a is not b


def test_have_birthday_returns_nothing():
    a = Animal("A", "cat", "Meow")
    assert a.have_birthday() is None
    assert a.age == 1


@needs_dog
def test_dog_is_an_animal():
    rex = Dog("Rex", 2)
    assert isinstance(rex, Animal)
    assert rex.species == "dog"
    assert rex.sound == "Woof"
    assert rex.age == 2


@needs_dog
def test_dog_age_defaults_to_zero():
    assert Dog("Rex").age == 0


@needs_dog
def test_dog_overrides_speak():
    assert Dog("Rex").speak() == "Rex says Woof! Woof!"


@needs_dog
def test_dog_fetch():
    assert Dog("Rex").fetch("ball") == "Rex fetches the ball"


@needs_dog
def test_dog_inherits_methods():
    rex = Dog("Rex", 2)
    rex.have_birthday()
    assert rex.age == 3
    assert str(rex) == "Rex the dog (age 3)"
