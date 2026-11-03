"""Week 2 practice task: phone book (model solution).

Uses only Week 2 ideas: variables, input(), strings, lists, tuples,
sets, dictionaries and print().
"""

# A dictionary of lists: each key is a name, each value is a list of numbers.
contacts = {
    "Amy": ["0400 111 222"],
    "Ben": ["0400 333 444", "08 9000 1111"],
}

# Step 2: add a new contact.
name = input("New contact name: ").strip().title()
mobile = input("Mobile number: ").strip()
contacts[name] = [mobile]

# Step 3: add a second number to the same contact.
extra = input("Second number (home or work): ").strip()
contacts[name].append(extra)

# Stretch: a set keeps each number once, even if it is repeated.
# (This is done before any contact is removed, so the name still exists.)
all_numbers = set(contacts[name] + contacts["Ben"])
print(f"Different numbers for {name} and Ben: {len(all_numbers)}")

# Step 4: look up a contact. get() gives a default if the name is missing.
lookup = input("Look up which contact? ").strip().title()
numbers = contacts.get(lookup, ["not found"])
print(f"{lookup}: " + ", ".join(numbers))

# Step 5: remove a contact. pop() with a default does nothing if missing.
remove = input("Remove which contact? ").strip().title()
contacts.pop(remove, None)

# Step 6: show the phone book, with the names in alphabetical order.
names = list(contacts.keys())
names.sort()
print(f"Contacts ({len(contacts)}): " + ", ".join(names))
