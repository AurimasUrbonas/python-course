people = [
  {"name": "Harry", "house": "Griffindor"},
  {"name": "Draco", "house": "Slytherin"},
  {"name": "Bob", "house": "Griffindor"},
]

people.sort(key=lambda person: person["name"])

print(people)