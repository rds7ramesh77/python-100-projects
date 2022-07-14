#Python program for Story Generator

""" For this we use Random Module"""

import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 23th oct']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat','a dog']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker','Ram','Shyam']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England','Nepal','USA','Portugal']
went = ['cinema', 'university','seminar', 'school', 'laundry','library']
happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
