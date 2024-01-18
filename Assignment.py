#책에 있는 예제 205쪽 8.10까지
#8.1
e2f={'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f)
#8.2
print(e2f['dog'])
print(e2f.get('dog'))
#8.3
word1, word2, word3=list(e2f.items())
word1=list(word1)
word2=list(word2)
word3=list(word3)
word1.reverse()
word2.reverse()
word3.reverse()
f2e={word1[0]:word1[1], word2[0]:word2[1], word3[0]:word3[1]}
print(f2e)
# f2e = {key: value for value, key in e2f.items()}
# print(f2e)
#8.4
e2f_value=list(e2f.values())
idx=e2f_value.index('chien')
e2f_key=list(e2f.keys())
print(e2f_key[idx])
#8.5
print(e2f.keys())
#8.6
element ={'cats':'Henry','octopi':'Grumpy','emus':'Lucy'}
life={'animals': element, 'plants':{},'other': {}}#참조한다는게 무슨 뜻인겨
print(life)
#8.7
print(life.keys())
#8.8
keys=list(life.keys())
print(keys[0])
print(life[keys[0]].keys())
#8.9
print(life[keys[0]].values())
#8.10
squares={i: i*i for i in range(10)}
#squares={i: pow(i,2) for i in range(10)}
#squares={i: i**2 for i in range(10)}

print(squares)
# 8.11
odd={i for i in range(10) if i % 2 != 0}
print(odd,type(odd))
# 8.12
# generator comprehension은 list comprehencion과 비슷하지만 ()를 쓴다.
string='Got'
for i in string:
    print(i)
for i in range(10):
    print(i)
# 8.13
key=("optimist","pessimist","troll")
value=('The glass is half full', "The glass is half empty", "How did you get a glass?")
kvdict={}
for key, value in zip(key, value):
    temp={key:value}
    kvdict.update(temp)
print(kvdict,type(kvdict))
# 8.14
titles=['Creature of Habit', 'Crewel Fate']
plots=['Anun turns into a mon ster', 'A haunted yarn shop']
kvdict={}
for key, value in zip(titles, plots):
    temp = {key: value}
    kvdict.update(temp)
print(kvdict, type(kvdict))
'''
# 8.13
key = ("optimist", "pessimist", "troll")
value = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
kvdict = dict(zip(key, value))
print(kvdict, type(kvdict))

# 8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['Anun turns into a monster', 'A haunted yarn shop']
kvdict = dict(zip(titles, plots))
print(kvdict, type(kvdict))
'''