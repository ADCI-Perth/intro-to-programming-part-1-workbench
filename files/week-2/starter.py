"""Week 2 practice task: phone book (starter).

Use only what you have learnt so far: variables, input(), strings,
lists, tuples, sets, dictionaries and print().
Do not use if, for, while or def. You will meet them in Week 3.
"""

# A dictionary of lists: each key is a name, each value is a list of numbers.
contacts = {
    "Amy": ["0400 111 222"],
    "Ben": ["0400 333 444", "08 9000 1111"],
}

# Step 2: add a new contact.
# TODO: ask for a name with input(). Tidy it with .strip() and .title().
# TODO: ask for a mobile number with input().
# TODO: add the name to contacts, with a list holding the mobile number.

# Step 3: add a second number to the same contact.
# TODO: ask for a second number with input().
# TODO: use .append() to add it to that contact's list.

# Stretch (optional): print how many different numbers the new contact
# and Ben have together, using a set. Do this before Step 5.
# TODO: all_numbers = set(contacts[name] + contacts["Ben"])
# TODO: print  Different numbers for <name> and Ben: <count>

# Step 4: look up a contact.
# TODO: ask "Look up which contact? " and tidy the answer.
# TODO: use contacts.get(name, ["not found"]) to fetch the list of numbers.
# TODO: print one line like  Ben: 0400 333 444, 08 9000 1111
#       (hint: ", ".join(numbers) turns a list into one string)

# Step 5: remove a contact.
# TODO: ask "Remove which contact? " and tidy the answer.
# TODO: use contacts.pop(name, None) to remove it.

# Step 6: show the phone book in alphabetical order.
# TODO: make a list of the names with list(contacts.keys()).
# TODO: sort the list with .sort().
# TODO: print one line like  Contacts (3): Amy, Ben, Cara
#       (hint: len(contacts) gives the count)
