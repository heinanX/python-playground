team='elephants'
phrase='Go ' + team + '!!'
letter='S'

print(letter.lower() + ' has index: ' + str(phrase.lower().index(letter.lower())))
print(phrase)
print(phrase.replace('Go', 'Boo'))