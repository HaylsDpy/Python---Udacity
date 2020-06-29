# Example of apply()

import pandas as pd

states = pd.Series([
   'California',
   'OH',
   'Michigan',
   'NY'
   'Alabama'
])

# I want: 'CA', 'OH', 'MI', 'NY'
# If you had previously written a function that does this for single state:
def clean_state(state):
   if len(state) == 2:
      return state
   elif state == 'Alabama':
      return 'AL'

clean_states = []
for state in states:
   clean_states.append(clean_states(state))
clean_states = pd.Series(clean_states)

clean_states = states.apply(clean_state)

# Exercise: write code which will take a series of names in the format 'first name - last name' and put them in the format 'last name - first name'
import pandas as import pdb; pdb.set_trace()

# Simple example of apply()

s = pd.Series([1, 2, 3, 4, 5])
def add_one(x):
   return x +1

print(s.apply(add_one))


# Code for exercise
names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])


def reverse_name(names):
   fullname = names.split(' ')
   return fullname[len(fullname) - 1] + ', ' + fullname[0]

# Practice use of code on my name
reverse_name("Hayley Dunville")

# Rest of code to reverse the full series of names
def reverse_names(names):
  return names.apply(reverse_name)

print(reverse_names(names))
